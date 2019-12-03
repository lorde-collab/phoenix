#!/usr/bin/env python3
""" A suite for testing utilities """

import unittest
import glob
import os
import sys

import phoenix.core as core

class Run(unittest.TestCase):
    """ Test 'Run' specific functionality """
    @unittest.expectedFailure
    def test_run_nodir(self):
        not_a_dir = "/path/to/blah"
        core.phoenix_run(not_a_dir)

    @unittest.expectedFailure
    def test_not_a_phoenix_dir(self):
        directory = "data/phoenix_dirs/yp1tkNml-pre"
        core.phoenix_run(directory)
    
    @unittest.expectedFailure
    def test_bad_starting_step(self):
        directory = "data/phoenix_dirs/yp1tkNml"
        core.phoenix_run(directory, starting_step="foo")

    @unittest.expectedFailure
    def test_bad_email_list(self):
        directory = "data/phoenix_dirs/yp1tkNml"
        core.phoenix_run(directory, email_list="jrobert.michael@stjude.org")

    @unittest.expectedFailure
    def test_fail_run_strongarm(self):
        directory = "data/phoenix_dirs/yp1tkNml"
        core.phoenix_run(directory)

    @unittest.expectedFailure
    def test_fail_run_qc(self):
        directory = "data/phoenix_dirs/simple_example"
        os.remove(directory + "/*.tmp")
        os.remove(directory + "/*.out")
        os.remove(directory + "/*.err")
        core.phoenix_run(directory, starting_step=1)

    def test_successful_run(self):
        directory = "data/phoenix_dirs/simple_example"
        core.phoenix_run(directory)

    def test_successful_run_force_qc(self):
        directory = "data/phoenix_dirs/qc_fail_example"
        core.phoenix_run(directory, starting_step=1, force_qc=True)

class Step(unittest.TestCase):
    """ Test 'Run' specific functionality """
    @unittest.expectedFailure
    def test_run_nodir(self):
        not_a_dir = "/path/to/blah"
        core.phoenix_step(not_a_dir, 1)

    @unittest.expectedFailure
    def test_not_a_phoenix_dir(self):
        directory = "data/phoenix_dirs/yp1tkNml-pre"
        core.phoenix_step(directory, 1)

    def test_fail_step(self):
        directory = "data/phoenix_dirs/yp1tkNml/workspace"
        return_code = core.phoenix_step(directory, 1)
        self.assertEqual(return_code, 1)

    def test_simple_step(self):
        directory = "data/phoenix_dirs/simple_example"
        return_code = core.phoenix_step(directory, 0)
        self.assertEqual(return_code, 0)

    def test_simple_step_outfiles(self):
        directory = "data/phoenix_dirs/simple_example"
        return_code = core.phoenix_step(directory, 0,
            outfile=directory+"/STEP-00.out",
            errfile=directory+"/STEP-00.err")
        self.assertEqual(return_code, 0)
