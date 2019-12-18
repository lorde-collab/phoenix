#!/usr/bin/env python3
""" A suite for testing utilities """

import unittest
import glob
import os
import io
import sys

import phoenix.psub as psub

class Main(unittest.TestCase):
    """ Test main functionality """
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

