#!/usr/bin/env python3
""" A suite for testing utilities """

import unittest
import glob
import os
import sys
import tempfile
import shutil

from phoenix.batch_systems import AbstractBatchSystem, AbstractJob
import phoenix.utils as utils

class AbstractSchedulerTest(unittest.TestCase):
    def test_not_implemented_errors(self):
        sched = AbstractBatchSystem('')
        # Call all functions which take only a single input and should
        # raise a NotImplementedError
        for method in ['jobs_from_arrays', 'jobs_from_array',
            'sub_array_for_cmdfile']:
            fun = getattr(sched, method)
            with self.assertRaises(NotImplementedError):
                fun(None)

class AbstractJobTest(unittest.TestCase):
    def test_not_implemeneted_errors(self):
        job = AbstractJob()

        # Call all functions which are properties
        for method in ['finished', 'pending', 'running', 'exit_reason',
                       'exit_success', 'exit_failure', 'exit_success']:
            with self.assertRaises(NotImplementedError):
                getattr(job, method)

        # Call all functions which take no values
        for method in ['recover']:
            fun = getattr(job, method)
            with self.assertRaises(NotImplementedError):
                fun()

        with self.assertRaises(NotImplementedError):
            foo = str(job)


    def test_unset_properties(self):
        job = AbstractJob()

        # these should give 'None' without being set
        for fun in ['jobid', 'jobindex', 'queue', 'user', 'project']:
            prop = getattr(job, fun)
            self.assertIsNone(prop)

        # these should give '?' without being set
        for fun in ['status']:
            prop = getattr(job, fun)
            self.assertEqual(prop, '?')

    def test_set_properties(self):
        job = AbstractJob()

        for fun in ['jobid', 'jobindex', 'queue', 'user', 'project', 'status']:
            setattr(job, fun, fun)
            prop = getattr(job, fun)
            self.assertEqual(prop, fun)



