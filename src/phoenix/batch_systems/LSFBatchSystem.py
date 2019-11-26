#!/usr/bin/env python3

import tempfile
from phoenix.batch_systems import AbstractBatchSystem

class LSFBatchSystem(AbstractBatchSystem):
    """ LSF Batch System class """
    def __init__(self):
        print("Hello from LSF!")
        super(LSFBatchSystem, self).__init__('LSF')

    def sub_array_for_cmdfile(self, args):
        """ Submits one or more arrays for commands in a commandfile
        Args:
            args (Namespace): Argparse Namespace
                - split_cutoff
        Returns:
            array_ids (list): List of job array ids.
        """

        print("args:", args)
        argsd = args.__dict__

        split_cutoff = argsd.get('split_cutoff', self._split_cutoff)
        queue = argsd.get('queue', None)
        app = argsd.get('app', None)
        mem_lim = argsd.get('mem_res')
        jobname = argsd.get('jobname')
        project = argsd.get('project')
        outfile = argsd.get('stdout')
        errfile = argsd.get('stderr')


