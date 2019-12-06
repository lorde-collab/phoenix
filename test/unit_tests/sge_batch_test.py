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

class SGETest(unittest.TestCase):
    def setUpClass():
        if not batch_utils.detect_scheduler() == "SGE":
            raise unittest.SkipTest("Skipping SGE tests")
    def test_create_simple(self):
        scheduler = LSF()
        self.assertEqual(scheduler._system, "SGE")
