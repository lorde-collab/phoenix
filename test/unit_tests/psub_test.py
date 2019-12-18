#!/usr/bin/env python3
""" A suite for testing utilities """

import unittest
import glob
import os
import io
import sys
import tempfile
import shutil

import phoenix.psub as psub
import phoenix.utils as utils
from phoenix.batch_systems import batch_utils

class Main(unittest.TestCase):
    """ Test main functionality """
    def setUp(self):
        self.datadir = os.path.realpath("data")
        self.this_dir = os.getcwd()
        self.tmpdirname = tempfile.mkdtemp()
        os.chdir(self.tmpdirname)
        self.sleeper_cmd = ("sub -o out.%J.%I.txt -e out.%J.%I.txt "
                            "-i {}/data/cmdfiles/sleeper.sh".format(
                            self.this_dir).split())

    def tearDown(self):
        os.chdir(self.this_dir)
        shutil.rmtree(self.tmpdirname)

    def test_get_scheduler(self):
        for named_scheduler in ['local', 'LSF']:
            scheduler = psub.get_scheduler(named_scheduler)
            self.assertEqual(scheduler.system.lower(), named_scheduler.lower())

        for no_support in ["SGE", "slurm", "PBS"]:
            scheduler = psub.get_scheduler(no_support)
            self.assertIsNone(scheduler)

    @unittest.expectedFailure
    def test_bad_scheduler(self):
        sched = psub.get_scheduler("foo")

    def test_submit_array(self):
        argv = self.sleeper_cmd
        args = utils.get_args(argv)
        arrays = psub.submit_array(args)
        self.assertTrue(len(arrays) == 1)

    def test_empty_jobs_dict(self):
        jobs = {}
        self.assertFalse(psub.job_array_unfinished(jobs))

    def test_pending_jobs_dict(self):
        scheduler_name = batch_utils.detect_scheduler()
        scheduler = psub.get_scheduler(scheduler_name)
        argv = self.sleeper_cmd
        args = utils.get_args(argv)
        arrays = psub.submit_array(args)
        jobs = scheduler.jobs_from_arrays(arrays)
        self.assertTrue(psub.job_array_unfinished(jobs))

    def test_running_jobs_dict(self):
        pass

    def test_done_jobs_dict(self):
        pass

    def test_exit_jobs_dict(self):
        pass

    def test_track_and_resub_sleeper(self):
        scheduler_name = batch_utils.detect_scheduler()
        scheduler = psub.get_scheduler(scheduler_name)
        argv = self.sleeper_cmd
        args = utils.get_args(argv)
        arrays = psub.submit_array(args)
        failed_indices = psub.track_and_resub(args, arrays)
        self.assertEqual(failed_indices, [])
