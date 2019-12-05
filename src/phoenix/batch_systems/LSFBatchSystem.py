#!/usr/bin/env python3

import tempfile
import os
import sys
import datetime
from phoenix import utils
from phoenix.batch_systems import AbstractBatchSystem, AbstractJob

class LSFBatchSystem(AbstractBatchSystem):
    """ LSF Batch System class """
    def __init__(self):
        print("Hello from LSF!")
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

        print("args:", args)
        for eo_file in [args.stdout, args.stderr]:
            logdir = os.path.dirname(eo_file)
            os.makedirs(logdir, exist_ok=True)

        # Create commands for each bsub array needed
        split_cutoff = argsd.get('split_cutoff', self._split_cutoff)
        nlines = open(args.cmdfile).read().count('\n')
        jid_beg = 1
        jid_end = split_cutoff
        if nlines < split_cutoff:
            jid_end = nlines
        cmd = self._get_bsub_command(argsd, jid_beg, jid_end)
        print(cmd)
        (stdout, stderr, return_code) = utils.run_shell_command(cmd)
        # NOTE: ST Jude specific LSF output:
        # "Job <JOBID> is submitted to queue <QUEUE>"
        array_ids.append(stdout.split('<')[1].split('>')[0])
        while jid_end < nlines:
            jid_beg = jid_end + 1
            jid_end += split_cutoff - 1
            if jid_end > nlines:
                jid_end = nlines
            cmd = self._get_bsub_command(argsd, jid_beg, jid_end)
            print(cmd)
            (stdout, stderr, return_code) = utils.run_shell_command(cmd)
            array_ids.append(stdout.split('<')[1].split('>')[0])

        return array_ids

    def jobs_from_arrays(self, job_arrays):
        """ Creates a set of Jobs from the verbose output of the arrays.
        Args:
            array_ids (list): List of Job array ids.
        Returns:
            jobs (dict): Dictionary of Job objects.
        """

        jobs = {}

        for job_array in job_arrays:
            jobs.update(self.jobs_from_array(job_array))

        return jobs

    def jobs_from_array(self, job_array):
        """ Creates a set of Jobs from the verbose output of the arrays.
        Args:
            array_ids (int): Array id.
        Returns:
            jobs (dict): Dictionary of Job objects.
        """
        cmd = "bjobs -al {}".format(job_array)
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
        super(LSFJob, self).__init__('LSF')

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
            sys.exit(1)

    @property
    def finished(self):
        if self.status in self.__run_pend_statuses:
            # Running or pending ... NOT finished
            return False
        elif self.status == 'EXIT' and \
            self.exit_reason in self.__recoverable_reasons:
            # Failed but recoverable ... NOT finished
            return False

        # Status not in RUN or PEND, and it is recoverable ... finished
        return True

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

        year = datetime.datetime.now().year

        for line in self.__joblines:
            '''
            if 'loadSched' not in line and 'loadStop' not in line and line and not '          ' in line:
                print(line)
            '''
            if 'Job <' in line:
                self.jobid = int(line.split('Job <')[1].split('[')[0])
                self.jobindex = int(line.split('Job <')[1].split('[')[1]\
                                                          .split(']')[0])
            for (key, fun) in self._keyfuns.items():
                if key[0] in line:
                    val = line.split(key[0])[1].split(key[1])[0]
                    setattr(self, fun, val)

    def __str__(self):
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
        return self.__resreq
    @resreq.setter
    def resreq(self, resreq):
        self.__resreq = resreq

