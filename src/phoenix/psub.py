#!/usr/bin/env python3
""" Phoenix 'sub' specific logic """
import sys

from phoenix import batch_systems

def get_scheduler(scheduler_name):
    """ Return the appropriate BatchSystem object
    Args:
        scheduler_name (str): Name of the scheduler.
    Returns:
        scheduler (?): Scheduler specific class from BatchSystem.
    """

    if scheduler_name in ['local']:
        scheduler = batch_systems.Local()
    elif scheduler_name in ['lsf', 'LSF']:
        scheduler = batch_systems.LSF()
    elif scheduler_name in ['sge', 'SGE']:
        scheduler = None
    elif scheduler_name in ['slurm']:
        scheduler = None
    elif scheduler_name in ['PBS']:
        scheduler = None
    else:
        sys.exit("ERROR: Batch system '{}' is not yet supported"
                 "".format(scheduler_name))

    return scheduler


def submit_array(args):
    """ Submit one (or more) job arrays from a script
    Args:
        args (Namespace): Argparse object which has the following fields:
            - project
            - jobname
            ... list here ... 
    Returns:
        job_arrays (list): List of integers relating to job arrays.
    """
    job_arrays = []
    print("Submitting job arrays from input file")

    scheduler = get_scheduler(args.system)
    job_arrays = scheduler.sub_array_for_cmdfile(args)

    return job_arrays

def track_and_resub(job_arrays):
    """ Track job arrays and resubmit any individual elements which fail
    Args:
        job_arrays (list): List of integers.
    Returns:
        failed_indices (list): List of jobids which failed.
    """

    print("job arrays: ", job_arrays)

    jobs = jobs_from_arrays(job_arrays)

    sys.exit(1)

    return []

