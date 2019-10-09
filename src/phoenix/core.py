#!/usr/bin/env python3
""" Core routines """

import os
import sys
import datetime
import glob

from phoenix import utils, psub

def phoenix_run(directory, starting_step=None, force_qc=False, email_list=None):
    """ Run a phoenix pipeline.
    Args:
        directory (str): Directory to find scripts in.
        starting_step (int): Optional step to start on.
        force_qc (bool): Whether or not to force past QC issues
        email_list (list): Optional list of emails to use.
    Returns: None
    """

    # Argument QC
    assert os.path.isdir(directory)
    if starting_step:
        assert isinstance(starting_step, int)
    if email_list:
        assert isinstance(email_list, list)
    directory = os.path.realpath(directory)

    # Create a dict of steps and validate each step / substep
    steps = utils.get_phoenix_steps(directory)
    if not steps:
        sys.exit("ERROR: No phoenix steps detected. This is unlikely to be a "
                 "phoenix directory.")

    # Run each step
    print("[RUNNER] Total number of steps: {}".format(len(steps)))
    print("[RUNNER] Date: ", datetime.datetime.now())
    for step in steps:
        print("[RUNNER] {} Starting step {} / {}: {}".format(
            datetime.datetime.now(), step, len(steps), steps[step]))
        if starting_step and starting_step > step:
            print("[RUNNER]: Skipping step {}".format(step))
            continue

        outfile = directory + "/STEP-%02i.out"%(step)
        errfile = directory + "/STEP-%02i.err"%(step)

        return_code = phoenix_step(directory, step, outfile, errfile, force_qc)
        if return_code != 0:
            if email_list:
                print("TODO: Send an email to the email list!")

            print("[RUNNER] ERROR: Phoenix step exited with code "\
                  "{}".format(return_code))
            sys.exit(return_code)
        else:
            print("[RUNNER] {} Finished step {} / {}: {}".format(
                datetime.datetime.now(), step, len(steps), steps[step]))

def phoenix_step(directory, step, outfile=None, errfile=None, force_qc=False):
    """ Run a single phoenix step.
    Args:
        directory (str): Directory to find scripts in.
        starting_step (int): Optional step to start on.
        outfile (str): Filename for stdout.
        errfile (str): Filename for stderr.
        force_qc (bool): Whether or not to force past QC issues
    Returns: (int): Return code
    """
    original_dir = os.getcwd()

    assert os.path.isdir(directory)
    directory = os.path.realpath(directory)

    fout = sys.stdout
    if outfile:
        fout = open(outfile, 'w')
    ferr = sys.stderr
    if errfile:
        ferr = open(errfile, 'w')

    steps = utils.get_phoenix_steps(directory)
    assert steps
    step_name = steps[step]

    print("[STEP {}] Running the following substeps:".format(step), file=fout)

    all_phoenix_scripts = utils.get_phoenix_scripts(directory)
    base_regex = "%02i"%(step)+"_?_*_*.sh"
    phoenix_scripts = glob.glob(os.path.join(directory, base_regex))
    substeps = []

    # Get a list of all substeps to be processed (in order)
    for phoenix_script in sorted(phoenix_scripts):
        assert phoenix_script in all_phoenix_scripts
        substep_script = os.path.basename(phoenix_script)
        pieces = substep_script.split('.sh')[0].split('_')
        substeps.append((step, int(pieces[1]), pieces[3], pieces[2],
                         phoenix_script))
        if len(substeps) > 1:
            assert substeps[-1][0] > substeps[-2][0] \
                   or substeps[-1][1] > substeps[-2][1]

    # Print out the substeps to be processed
    for substep in substeps:
        print("[STEP {}.{}] {}.{}".format(substep[0], substep[1], substep[2],
                                          substep[3]), file=fout)

    # Process the substeps
    for substep in substeps:
        stat = "[STEP {}.{}]".format(substep[0], substep[1])
        step_name = substep[2]
        substep_name = substep[3]
        if substep_name == "qc" and force_qc:
            print("{} SKIP qc".format(stat))
            continue
        phoenix_script = substep[4]
        print("", file=fout)
        print("{} STEP {}.{}".format(stat, step_name, substep_name), file=fout)
        print("{} Date: ".format(stat), datetime.datetime.now(), file=fout)
        print("{} Running script {}".format(stat, phoenix_script), file=fout)

        os.chdir(directory)
        (stdout, stderr, return_code) = utils.run_shell_command(phoenix_script)
        os.chdir(original_dir)
        print(stdout, file=fout)
        print(stderr, file=ferr)
        if return_code != 0:
            print("{} Substep FAILURE".format(stat), file=fout)
            return return_code

        print("{} Done running {}".format(stat, phoenix_script), file=fout)
        print("{} Date: ".format(stat), datetime.datetime.now(), file=fout)
        print("{} Substep successful!".format(stat), file=fout)

    print("", file=fout)
    print("[STEP {}] Step successful!".format(step), file=fout)

    if outfile:
        fout.close()
    if errfile:
        ferr.close()

    return 0

def phoenix_sub(args):
    """ Submit and track phoenix jobs """
    job_arrays = psub.submit_array(args)
    failed_idx = psub.track_and_resub(job_arrays)
