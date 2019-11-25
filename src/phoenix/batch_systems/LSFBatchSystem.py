#!/usr/bin/env python3

import tempfile

class LSFBatchSystem:
    """ LSF Batch System class """
    def __init__(self):
        print("Hello from LSF!")

    def sub_array_for_cmdfile(self, cmdfile, **kwargs):
        """ Submits one or more arrays for commands in a commandfile
        Args:
            cmdfile (str): Path to a command file.
        Returns:
            array_ids (list): List of job array ids.
        """

        split_cutoff = kwargs.pop('split_cutoff', self.__split_cutoff)
        queue = kwargs.pop('queue', None)
        app = kwargs.pop('app', None)
        mb_res = kwargs.pop('mem_res')
        jobname = kwargs.pop('jobname')
        project = kwargs.pop('project')
        outfile = kwargs.pop('outfile')
        errfile = kwargs.pop('errfile')
        overwrite_eo = kwargs.pop('overwrite_eo', False)


