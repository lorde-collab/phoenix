#!/usr/bin/env python3
"""
Module for the SGE batch system

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
