#!/usr/bin/env python3
"""
Initialization

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

from phoenix.batch_systems.AbstractBatchSystem import AbstractBatchSystem
from phoenix.batch_systems.AbstractBatchSystem import AbstractJob
from phoenix.batch_systems.LSFBatchSystem import LSFBatchSystem as LSF
from phoenix.batch_systems.LSFBatchSystem import LSFJob
from phoenix.batch_systems.SGEBatchSystem import SGEBatchSystem as SGE
from phoenix.batch_systems.LocalBatchSystem import LocalBatchSystem as Local
