#!/usr/bin/env python3
""" Main phoenix entry point """

import sys

from phoenix import utils

def main():
    """ Main routine """
    args = utils.get_args(sys.argv[1:])
    action = sys.argv[1]

    if action == "sub":
        core.sub(args)
    elif action == "step":
        core.step(args)
    elif action == "run":
        core.run(args)
    else:
        sys.exit("ERROR: Unknown action '{}'".format(action))

main()
