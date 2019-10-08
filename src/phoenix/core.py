#!/usr/bin/env python3
""" Core routines """

import glob
import os
import datetime

from phoenix.constants import SUBSTEP_TYPES
from phoenix import utils

def phoenix_run(directory, starting_step=None, email_list=None):
    """ Run a phoenix pipeline.
    Args:
        directory (str): Directory to find scripts in.
        step (int): Optional step to start on.
        email_list (list): Optional list of emails to use.
    Returns: None
    """

    # Argument QC
    assert os.path.isdir(directory)
    directory = os.path.realpath(directory)
    if starting_step:
        assert isinstance(starting_step, int)
    if email_list:
        assert isinstance(email_list, list)

    # Create a dict of steps and validate each step / substep
    steps = {}
    phoenix_scripts = glob.glob(os.path.join(directory, "??_?_*_*.sh"))
    for phoenix_script in phoenix_scripts:
        pieces = os.path.basename(phoenix_script.split('.')[0]).split('_')
        assert utils.isint(pieces[0])
        assert utils.isint(pieces[1])
        step = int(pieces[0])
        substep = int(pieces[1])
        substep_name = pieces[2]
        step_name = pieces[3]
        assert SUBSTEP_TYPES[substep] == substep_name
        if step in steps:
            assert steps[step] == step_name
        else:
            steps[step] = step_name
    if not steps:
        sys.exit("ERROR: No phoenix steps detected. This is unlikely to be a "
                 "phoenix directory.")

    # Run each step
    print("[RUNNER] Total number of steps: {}".format(len(steps)))
    print("[RUNNER] Date: ", datetime.datetime.now())
    for step in steps:
        if starting_step and starting_step > step:
            print("[RUNNER]: Skipping step {}".format(step))
            continue

        print("phoenix_step(", directory, step, ")")

        # TODO: 
        # If exit code != 0
        #     1) email the email list
        #     2) 




