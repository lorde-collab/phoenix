#!/usr/bin/env python3
""" Phoenix 'sub' specific logic """

def get_scheduler(scheduler_name):
    """ Return the appropriate BatchSystem object
    Args:
        scheduler_name (str): Name of the scheduler.
    Returns:
        scheduler (?): Scheduler specific class from BatchSystem.
    """

    if scheduler_name in ['local']:
        scheduler = BatchSystem.LocalBatchSystem
    elif scheduler_name in ['lsf', 'LSF']:
        scheduler = BatchSystem.LSFBatchSystem
    elif scheduler_name in ['sge', 'SGE']:
        scheduler = BatchSystem.SGEBatchSystem
    elif scheduler_name in ['slurm']:
        scheduler = BatchSystem.SlurmBatchSystem
    elif scheduler_name in ['PBS']:
        scheduler = BatchSystem.PBSBatchSystem
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
    job_arrays = scheduler.sub_array_for_cmdfile(args.input)

    return job_arrays

def track_and_resub(job_arrays):
    """ Track job arrays and resubmit any individual element which fails
    Args:
        job_arrays (list): List of integers.
    Returns:
        failed_index (int): Index of array(s) which failed or None.
    """

    return None

