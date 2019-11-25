#!/usr/bin/env python3
""" Main phoenix entry point """

import sys

from phoenix import utils, core
from phoenix.batch_systems.batch_utils import detect_scheduler

def main():
    """ Main routine """
    args = utils.get_args(sys.argv[1:])
    action = sys.argv[1]

    if action == "sub":
        if not args.system:
            args.system = detect_scheduler()
        core.phoenix_sub(args)
    elif action == "step":
        core.phoenix_step(args.directory, args.step, args.force)
    elif action == "run":
        core.phoenix_run(args.directory, args.step, args.email_list)
    else:
        sys.exit("ERROR: Unknown action '{}'".format(action))

main()
