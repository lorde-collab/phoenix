#!/usr/bin/env python3
"""
Utilities used for batch_systems module

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

from phoenix import utils

def detect_scheduler():
    """ Detect what (if any) scheduler is available.
    Args:
        None
    Returns:
        scheduler (str): The scheduler detected on the system.
    """
    # Check for LSF
    (stdout, stderr, return_code) = utils.run_shell_command("lsid")
    if return_code == 0 and "LSF" in stdout:
        return "LSF"

    return "local"
