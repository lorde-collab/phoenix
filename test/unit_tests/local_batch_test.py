#!/usr/bin/env python3
""" A suite for testing utilities """

import unittest
import glob
import os
import sys
import tempfile
import shutil

from phoenix.batch_systems import Local
from phoenix.batch_systems import batch_utils
import phoenix.utils as utils

class LocalSchedulerTest(unittest.TestCase):
    def setUp(self):
        self.datadir = os.path.realpath("data")
        self.this_dir = os.getcwd()
        self.tmpdirname = tempfile.mkdtemp()
        os.chdir(self.tmpdirname)

    def tearDown(self):
        os.chdir(self.this_dir)
        shutil.rmtree(self.tmpdirname)

    def test_create_simple(self):
        sched = Local()
        self.assertEqual(sched._system, "Local")

    def test_sub_array_for_cmdfile(self):
        sched = Local()
        cmdfile = self.datadir + "/cmdfiles/sleeper.sh"
        argv = ['sub', '-P', 'project', '-q', 'normal', '-K',
                '-M', '500', '-o', 'tmp/out.%J.%I.txt', '-e',
                'tmp/err.%J.%I.txt', '-i', cmdfile]

        args = utils.get_args(argv)

        array_ids = sched.sub_array_for_cmdfile(args)
        self.assertTrue(isinstance(array_ids, list))
        self.assertEqual(len(array_ids), 1)
