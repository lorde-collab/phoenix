#!/usr/bin/env python3
""" Main phoenix entry point """

import sys

from phoenix import utils, core

def main():
    """ Main routine """
    args = utils.get_args(sys.argv[1:])
    action = sys.argv[1]

    if action == "sub":
        core.phoenix_sub(args)
    elif action == "step":
        core.phoenix_step(args.directory, args.step)
    elif action == "run":
        core.phoenix_run(args.directory, args.step, args.email_list)
    else:
        sys.exit("ERROR: Unknown action '{}'".format(action))

main()
