#!/usr/bin/env python3
""" A suite for testing utilities """

import unittest
import glob
import os
import sys
import tempfile
import shutil

from phoenix.batch_systems import LSF, SGE, LSFJob
from phoenix.batch_systems import batch_utils
import phoenix.utils as utils

class LSFSchedulerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not batch_utils.detect_scheduler() == "LSF":
            raise unittest.SkipTest("Skipping LSF tests")

    def setUp(self):
        self.datadir = os.path.realpath("data")
        self.this_dir = os.getcwd()
        self.tmpdirname = tempfile.mkdtemp()
        os.chdir(self.tmpdirname)
        print("cwd: ", os.getcwd())

    def tearDown(self):
        os.chdir(self.this_dir)
        shutil.rmtree(self.tmpdirname)

    def test_create_simple(self):
        lsf = LSF()
        self.assertEqual(lsf._system, "LSF")

    def test_sub_array_for_cmdfile(self):
        lsf = LSF()
        cmdfile = self.datadir + "/cmdfiles/sleeper.sh"
        argv = ['sub', '-P', 'project', '-q', 'normal', '-K',
                '-M', '500', '-o', 'tmp/out.%J.%I.txt', '-e',
                'tmp/err.%J.%I.txt', '-i', cmdfile]

        args = utils.get_args(argv)

        array_ids = lsf.sub_array_for_cmdfile(args)
        self.assertTrue(isinstance(array_ids, list))
        self.assertEqual(len(array_ids), 1)
        for array_id in array_ids:
            self.assertTrue(utils.isint(array_id))

    def test_sub_array_for_cmdfile_split(self):
        lsf = LSF()
        cmdfile = self.datadir + "/cmdfiles/sleeper.sh"
        argv = ['sub', '-P', 'project', '-q', 'normal', '-K',
                '-M', '500', '-o', 'tmp/out.%J.%I.txt', '-e',
                'tmp/err.%J.%I.txt', '-S', '3', '-i', cmdfile]

        args = utils.get_args(argv)

        array_ids = lsf.sub_array_for_cmdfile(args)
        self.assertTrue(isinstance(array_ids, list))
        self.assertEqual(len(array_ids), 2)
        for array_id in array_ids:
            self.assertTrue(utils.isint(array_id))

    def test_jobs_from_arrays(self):
        lsf = LSF()
        cmdfile = self.datadir + "/cmdfiles/sleeper.sh"
        argv = ['sub', '-P', 'project', '-q', 'normal', '-K',
                '-M', '500', '-o', 'tmp/out.%J.%I.txt', '-e',
                'tmp/err.%J.%I.txt', '-S', '3', '-i', cmdfile]

        args = utils.get_args(argv)

        array_ids = lsf.sub_array_for_cmdfile(args)
        jobs = lsf.jobs_from_arrays(array_ids)
        self.assertEqual(len(jobs), 4)

class LSFJobTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not batch_utils.detect_scheduler() == "LSF":
            raise unittest.SkipTest("Skipping LSF tests")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_simple(self):
        job = LSFJob()

    def test_finished(self):
        job = LSFJob()
        self.assertFalse(job.finished)

class SGETest(unittest.TestCase):
    def setUpClass():
        if not batch_utils.detect_scheduler() == "SGE":
            raise unittest.SkipTest("Skipping SGE tests")
    def test_create_simple(self):
        scheduler = LSF()
        self.assertEqual(scheduler._system, "SGE")
