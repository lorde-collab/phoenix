#!/usr/bin/env python3
""" Module for the SGE batch system """

from phoenix.batch_systems import AbstractBatchSystem, AbstractJob

#pylint: disable=abstract-method
class SGEBatchSystem(AbstractBatchSystem):
    """ SGE Batch System class """
    def __init__(self):
        """ init """
        super(SGEBatchSystem, self).__init__('SGE')

class SGEJob(AbstractJob):
    """ SGE Job """
    def __init__(self):
        """ init """
        super(SGEJob, self).__init__('SGE')
