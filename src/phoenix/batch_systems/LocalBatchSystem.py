#!/usr/bin/env python3
"""
Module for running phoenix without any queueing system (local) while still
Treating it as a batch system.

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
from multiprocessing import Pool

from phoenix.batch_systems import AbstractBatchSystem
from phoenix import utils


#pylint: disable=abstract-method
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
