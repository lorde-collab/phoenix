#!/usr/bin/env python3

from phoenix.batch_systems import AbstractBatchSystem

class LocalBatchSystem(AbstractBatchSystem):
    """ Local Batch System class """
    def __init__(self):
        print("Hello from Local!")

    def sub_array_for_cmdfile(self, cmdfile, **kwargs):
        """ Submits one or more arrays for commands in a commandfile
        Args:
            cmdfile (str): Path to a command file.
        Returns:
            array_ids (list): List of job array ids.
        """

        # TODO:
        # 1) Grab 'ncores' from kwargs
        # 2) Go through and background up to 'ncores' commands
        # 3) Return the pids as an array here



