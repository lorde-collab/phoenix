#!/usr/bin/env python3
"""
Constants for phoenix

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

SUB_UPDATE_INTERVAL = 3
MEMLIM_DEFAULT = 2513
SUBSTEP_TYPES = {
    1: 'qc',
    2: 'hook',
    3: 'local',
    4: 'createcmdfile',
    5: 'submit'
}
SPLIT_CUTOFF = 4000
