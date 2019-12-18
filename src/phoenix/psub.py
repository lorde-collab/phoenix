#!/usr/bin/env python3
"""
Phoenix 'sub' specific logic

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
import time

from phoenix import batch_systems
from phoenix.batch_systems import batch_utils
from phoenix import utils

def get_scheduler(scheduler_name):
    """ Return the appropriate BatchSystem object
    Args:
        scheduler_name (str): Name of the scheduler.
    Returns:
        scheduler (?): Scheduler specific class from BatchSystem.
    """

    if scheduler_name in ['local', 'Local']:
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
    system = args.system
    if not system:
        system = batch_utils.detect_scheduler()

    scheduler = get_scheduler(system)
    job_arrays = scheduler.sub_array_for_cmdfile(args)

    return job_arrays

def job_array_unfinished(jobs):
    """ Check the status of 'jobs' dictionary and decide if the array is
        finished or not.
    Args:
        jobs (dict): Job dictionary with key [jobid, jobindex]
    Returns: bool
    """
    for jobid in jobs:
        job = jobs[jobid]
        if not job.finished:
            return True
    return False

def track_and_resub(args, job_arrays):
    """ Track job arrays and resubmit any individual elements which fail
    Args:
        job_arrays (list): List of integers.
    Returns:
        failed_indices (list): List of jobids which failed.
    """

    print("job arrays: ", job_arrays)

    system = args.system
    if not system:
        system = batch_utils.detect_scheduler()

    scheduler = get_scheduler(system)
    jobs = scheduler.jobs_from_arrays(job_arrays)

    sys.stdout.flush()
    failed_indices = []

    # Loop until all jobs are finished, or a single job has failed and the
    # killall option is specified.
    checked_once = False
    while job_array_unfinished(jobs) or not checked_once:
        checked_once = True
        sys.stdout.flush()

        tjobs = scheduler.jobs_from_arrays(job_arrays)
        #for (k, tjob) in tjobs.items():
        #    print(k, tjob)
        sys.stdout.flush()
        npend = 0
        nrequeued = 0
        nrun = 0
        ndone = 0
        nfailed = 0
        for jkey in jobs:
            job = jobs[jkey]
            if job.exit_success:
                # Job has already finished previously. Check next job.
                ndone += 1
                continue
            elif job.exit_failure:
                # Job has already failed previously. Check next job.
                nfailed += 1
                continue

            tjob = tjobs[jkey]

            # Update 'jobs' dict
            jobs[jkey] = tjob
            job = tjob

            # If we have made it this far then the last time we checked the
            # job was not in DONE or EXIT state.
            if job.pending:
                npend += 1
            elif job.running:
                nrun += 1
            elif job.exit_success:
                ndone += 1
            elif job.exit_failure:
                # Job exited since the last time we checked ... deal with it
                print("[WARN] {} job {}[{}] has exited with code {}".format(
                    utils.now(), job.jobid, job.jobindex, job.exit_code))
                print("       Failure reason: {}".format(job.exit_reason))
                if job.recover():
                    nrequeued += 1
                else:
                    nfailed += 1

                # TODO: Log this in failed_indicies
            else:
                print("[WARN] {} job {}[{}] has unknown status {}".format(
                    utils.now(), job.jobid, job.jobindex, job.status))

        print("[UPDATE] {0:s} nPEND nRUN nDONE nREQUEUE nFAIL = {1:5d} "\
              "{2:5d} {3:5d} {4:5d} {5:5d}".format(
                  utils.now().strftime("%Y-%m-%d %H:%M:%S"), npend, nrun,
                  ndone, nrequeued, nfailed))

        sys.stdout.flush()
        #print("job_array_unfinished ...")
        #sys.stdout.flush()
        #print(job_array_unfinished(jobs))
        #sys.stdout.flush()
        #print(":)")
        #sys.stdout.flush()
        time.sleep(args.update_interval)

    #print("Returning")
    #sys.stdout.flush()
    return failed_indices
