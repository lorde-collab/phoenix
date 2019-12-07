#!/usr/bin/env python3
"""
Main phoenix entry point

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

import sys
import os

from phoenix import utils, core
from phoenix.batch_systems.batch_utils import detect_scheduler

def main():
    """ Main routine """
    args = utils.get_args(sys.argv[1:])
    action = sys.argv[1]

    if action == "sub":
        if not args.system:
            args.system = detect_scheduler()
        if not args.jobname:
            args.jobname = os.path.basename(args.cmdfile)
        core.phoenix_sub(args)
    elif action == "step":
        core.phoenix_step(args.directory, args.step, args.force_qc)
    elif action == "run":
        core.phoenix_run(args.directory, args.step, args.email_list)
    else:
        sys.exit("ERROR: Unknown action '{}'".format(action))

main()
