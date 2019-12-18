#!/usr/bin/env python3
"""
Module for the LSF batch system

+--------------------------------------------------------------------------+
| Copyright 2019 St. Jude Children's Research Hospital                     |
|                                                                          |
| Licensed under a modified version of the Apache License, Version 2.0     |
| (the "License") for academic research use only; you may not use this     |
| file except in compliance with the License. To inquire about commercial  |
| use, please contact the St. Jude Office of Technology Licensing at       |
| scott.elmer@stjude.org.                                                  |
|                                                                          |
| Unless required by applicable law or agreed to in writing, software      |
| distributed under the License is distributed on an "AS IS" BASIS,        |
| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. |
| See the License for the specific language governing permissions and      |
| limitations under the License.                                           |
+--------------------------------------------------------------------------+
"""

import os
import sys
from phoenix import utils
from phoenix.batch_systems import AbstractBatchSystem, AbstractJob

class LSFBatchSystem(AbstractBatchSystem):
    """ LSF Batch System class """
    def __init__(self):
        super(LSFBatchSystem, self).__init__('LSF')

        self.__flag_params = {
            '-P': ['project'],
            '-J': ['jobname'],
            '-oo': ['stdout'],
            '-eo': ['stderr'],
            '-app': ['app'],
            '-q': ['queue]'],
            '-n': ['ncores']
        }

    def sub_array_for_cmdfile(self, args):
        """ Submits one or more arrays for commands in a commandfile
        Args:
            args (Namespace): Argparse Namespace
                - split_cutoff
        Returns:
            array_ids (list): List of job array ids.
        """
        argsd = args.__dict__
        array_ids = []

        for eo_file in [args.stdout, args.stderr]:
            logdir = os.path.dirname(eo_file)
            if logdir:
                os.makedirs(logdir, exist_ok=True)

        # Create commands for each bsub array needed
        split_cutoff = argsd.get('split_cutoff', self._split_cutoff)
        nlines = open(args.cmdfile).read().count('\n')
        jid_beg = 1
        jid_end = split_cutoff
        if nlines < split_cutoff:
            jid_end = nlines
        cmd = self._get_bsub_command(argsd, jid_beg, jid_end)
        (stdout, stderr, return_code) = utils.run_shell_command(cmd)
        if return_code != 0:
            print("ERROR: Unable to submit LSF job. Bsub command: {}"\
                  .format(cmd), file=sys.stderr)
            sys.exit(return_code)
        # NOTE: ST Jude specific LSF output:
        # "Job <JOBID> is submitted to queue <QUEUE>"
        array_ids.append(stdout.split('<')[1].split('>')[0])
        while jid_end < nlines:
            jid_beg = jid_end + 1
            jid_end += split_cutoff - 1
            if jid_end > nlines:
                jid_end = nlines
            cmd = self._get_bsub_command(argsd, jid_beg, jid_end)
            (stdout, stderr, return_code) = utils.run_shell_command(cmd)
            array_ids.append(stdout.split('<')[1].split('>')[0])

        return array_ids

    def jobs_from_arrays(self, array_ids):
        """ Creates a set of Jobs from the verbose output of the arrays.
        Args:
            array_ids (list): List of Job array ids.
        Returns:
            jobs (dict): Dictionary of Job objects.
        """

        jobs = {}

        for array_id in array_ids:
            jobs.update(self.jobs_from_array(array_id))

        return jobs

    def jobs_from_array(self, array_id):
        """ Creates a set of Jobs from the verbose output of the arrays.
        Args:
            array_id (int): Array id.
        Returns:
            jobs (dict): Dictionary of Job objects.
        """
        cmd = "bjobs -al {}".format(array_id)
        (stdout, stderr, return_code) = utils.run_shell_command(cmd)
        outlines = stdout.replace("\n                     ", "").splitlines()

        jobs = {}

        joblines = []
        for line in outlines:
            if '---' in line:
                job = LSFJob()
                job.from_bjobs(joblines)
                jobs[(job.jobid, job.jobindex)] = job
                joblines = []
            else:
                joblines.append(line)
        job = LSFJob()
        job.from_bjobs(joblines)
        jobs[(job.jobid, job.jobindex)] = job

        return jobs

    def _get_bsub_command(self, argsd, jid_beg, jid_end):
        """ Get the bsub command needed to submit the job array
        Args:
            argsd (dict): Argparse Namespace turned to dict
            jid_beg (int): Beginning job array id.
            jid_end (int): Ending job array id.
        Returns:
            cmd (str): 'bsub' LSF command.
        """

        cmd = "bsub"
        for (flag, keys) in self.__flag_params.items():
            for key in keys:
                if key == 'jobname':
                    jobname = argsd.get('key')
                    if not jobname:
                        jobname = os.path.basename(argsd['cmdfile'])
                    cmd += " -J %s[%i-%i]"%(jobname, jid_beg, jid_end)
                elif argsd.get(key):
                    cmd += " {} {}".format(flag, argsd.get(key))

        # NOTE: SJ specific: divide the memory limit by number of cores and
        # specify this as the -R resource requirements for memory
        memres = int(float(argsd['memlim'])/float(argsd['ncores']))
        cmd += ' -R "span[hosts=1]" -R "rusage[mem={}]"'.format(memres)
        cmd += ' "sub_line_from_file_lsf.sh {}"'.format(argsd['cmdfile'])

        return cmd

class LSFJob(AbstractJob):
    """ LSF Job """
    def __init__(self):
        super(LSFJob, self).__init__()

        self.__resreq = None
        self.__joblines = []

        self._keyfuns = {
            ("User <", ">"): "user",
            ("Queue <", ">"): "queue",
            ("Project <", ">"): "project",
            ("Status <", ">"): "status",
            ("Requested Resources <", ">"): "resreq",
            ("Exited with exit code ", "."): "exit_code",
            ("Exited by LSF signal ", "."): "exit_code",
            ("Completed <exit>; ", ":"): "exit_reason"
        }

        self.__run_pend_statuses = ['RUN', 'PEND']
        self.__recoverable_reasons = ["TERM_MEMLIMIT"]

    def recover(self):
        """ Attempt to recover the job.
        Args: None
        Returns:
            bool: Whether or not the job was recovered.
        """
        assert self.exit_failure, "ERROR: Trying to recover an unfailed job"

        if self.exit_reason == "?":
            return False
        elif self.exit_reason not in self.__recoverable_reasons:
            print("Cannot recover job which failed due to {}"\
                  .format(self.exit_reason))
            return False
        elif self.exit_reason == "TERM_MEMLIMIT":
            print("Working to recover job failed due to memory limit")
            print("TODO!")
            sys.exit(1)

        print("WARNING: End of 'recover' function reached.")
        return None

    @property
    def finished(self):
        # TODO: Should this move to AbstractJob?
        if self.status in self.__run_pend_statuses:
            # Running or pending ... NOT finished
            return False
        elif self.status == 'EXIT' and \
            self.exit_reason in self.__recoverable_reasons:
            # Failed but recoverable ... NOT finished
            return False
        elif self.status in ["EXIT", "DONE"]:
            # Succeeded or failed without ability to recover ... Finished
            return True

        print("Unknown case for LSF job. Status is {}".format(self.status))
        for jobline in self.__joblines:
            print("JOBLINE: {}".format(jobline))
        return False

    @property
    def pending(self):
        return self.status == "PEND"
    @property
    def running(self):
        return self.status == "RUN"
    @property
    def exit_success(self):
        return self.status == "DONE"
    @property
    def exit_failure(self):
        return self.status == "EXIT"

    def from_bjobs(self, joblines):
        """ Fill in information about the job from LSF bjobs output
        Args:
            joblines (list): List of lines from LSF 'bjobs -al' output.
        Returns: None
        """
        self.__joblines = joblines

        for line in self.__joblines:
            if 'Job <' in line:
                self.jobid = int(line.split('Job <')[1].split('[')[0])
                self.jobindex = int(line.split('Job <')[1].split('[')[1]\
                                                          .split(']')[0])
            for (key, fun) in self._keyfuns.items():
                if key[0] in line:
                    val = line.split(key[0])[1].split(key[1])[0]
                    setattr(self, fun, val)

    def __str__(self):
        """ Return job object as string """
        rstring = ""
        #for jobline in self.__joblines:
        #    rstring += jobline+"\n"
        rstring += "Job {}".format(self.jobid)
        if self.jobindex:
            rstring += "[{}]\n".format(self.jobindex)
        else:
            rstring += "\n"
        funs = []
        for key in sorted(list(self._keyfuns.keys())):
            fun = self._keyfuns[key]
            funs.append(fun)

        for fun in sorted(list(set(funs))):
            val = getattr(self, fun)
            rstring += "{}: {}\n".format(fun, val)

        return rstring

    @property
    def resreq(self):
        """ Resource requirements (getter) """
        return self.__resreq
    @resreq.setter
    def resreq(self, resreq):
        """ Resource requirements (setter) """
        self.__resreq = resreq
