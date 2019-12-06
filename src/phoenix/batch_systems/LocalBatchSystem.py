#!/usr/bin/env python3

import os
import sys

from phoenix.batch_systems import AbstractBatchSystem
from multiprocessing import Pool
from phoenix import utils


class LocalBatchSystem(AbstractBatchSystem):
    """ Local Batch System class """
    def __init__(self):
        super(LocalBatchSystem, self).__init__('Local')

    def sub_array_for_cmdfile(self, args):
        """ Submits one or more arrays for commands in a commandfile
        Args:
            cmdfile (str): Path to a command file.
        Returns:
            (list): [multiprocessing.pool.MapResult]: The multiprocessing
                object in list form.
        """

        pid = os.getpid()
        pid_str = "%i"%(pid)

        for eo_file in [args.stdout, args.stderr]:
            logdir = os.path.dirname(eo_file)
            if logdir:
                os.makedirs(logdir, exist_ok=True)

        # For local we ignore split cutoff. Any reason to use this?
        cmds = open(args.cmdfile).read().splitlines()
        outfiles = []
        errfiles = []
        wrapper_args = []
        for icmd, cmd in enumerate(cmds):
            icmd_str = "%i"%(icmd)
            outfile = args.stdout.replace("%J", pid_str).replace("%I", icmd_str)
            errfile = args.stderr.replace("%J", pid_str).replace("%I", icmd_str)
            wrapper_args.append([cmd, outfile, errfile])

        pool = Pool(processes=args.ncores)
        mpres = pool.map_async(utils.run_shell_command_wrapper, wrapper_args)

        return [mpres]



