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

        self.flag_params = {
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
        for (flag, keys) in self.flag_params.items():
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

        self._funkeys = {
            "user": ("User <", ">"),
            "queue": ("Queue <", ">"),
            "project": ("Project <", ">"),
            "status": ("Status <", ">"),
            "resreq": ("Requested Resources <", ">")
        }

    def from_bjobs(self, joblines):
        """ Fill in information about the job from LSF bjobs output
        Args:
            joblines (list): List of lines from LSF 'bjobs -al' output.
        Returns: None
        """

        year = datetime.datetime.now().year

        for line in joblines:
            if 'Job <' in line:
                self.jobid = int(line.split('Job <')[1].split('[')[0])
                self.jobindex = int(line.split('Job <')[1].split('[')[1]\
                                                          .split(']')[0])
            for (fun, key) in self._funkeys.items():
                if key[0] in line:
                    val = line.split(key[0])[1].split(key[1])[0]
                    setattr(self, fun, val)

    def __str__(self):
        rstring = "Job {}".format(self.jobid)
        if self.jobindex:
            rstring += "[{}]\n".format(self.jobindex)
        else:
            rstring += "\n"
        for fun in sorted(list(self._funkeys.keys())):
            val = getattr(self, fun)
            rstring += "{}: {}\n".format(fun, val)

        return rstring

    @property
    def resreq(self):
        return self.__resreq
    @resreq.setter
    def resreq(self, resreq):
        self.__resreq = resreq

