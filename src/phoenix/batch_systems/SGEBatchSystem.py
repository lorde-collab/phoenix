#!/usr/bin/env python3

import tempfile
import os
import sys
import datetime
from phoenix import utils
from phoenix.batch_systems import AbstractBatchSystem, AbstractJob

class SGEBatchSystem(AbstractBatchSystem):
    """ SGE Batch System class """
    def __init__(self):
        super(SGEBatchSystem, self).__init__('SGE')

class SGEJob(AbstractJob):
    """ SGE Job """
    def __init__(self):
        super(SGEJob, self).__init__('SGE')
