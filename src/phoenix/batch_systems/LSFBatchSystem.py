#!/usr/bin/env python3

import tempfile
import os
import sys
from phoenix import utils
from phoenix.batch_systems import AbstractBatchSystem

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
        while jid_end < nlines:
            jid_beg = jid_end + 1
            jid_end += split_cutoff - 1
            if jid_end > nlines:
                jid_end = nlines
            cmd = self._get_bsub_command(argsd, jid_beg, jid_end)
            print(cmd)
            (stdout, stderr, return_code) = utils.run_shell_command(cmd)

    def jobs_from_arrays(job_arrays):
        """ Creates a set of Jobs from the verbose output of the arrays.
        Args:
            array_ids (list): List of Job array ids.
        Returns:
            jobs (dict): Dictionary of Job objects.
        """





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


