#!/usr/bin/env python3
""" A suite for testing utilities """

import unittest
import glob
import os

import phoenix.utils as utils

class Utilities(unittest.TestCase):
    """ Test simple utility functions """
    def test_simple_shell_command(self):
        """ Tests functionality of a shell command """
        (stdout, stderr, return_code) = \
            utils.run_shell_command("echo foo")

        self.assertIsInstance(stdout, str)
        self.assertIsInstance(stderr, str)
        self.assertIsInstance(return_code, int)

        self.assertEqual(stdout, 'foo\n')
        self.assertEqual(stderr, '') 
        self.assertEqual(return_code, 0)

    def test_command_not_found(self):
        """ Tests functionality of a shell command """
        (stdout, stderr, return_code) = utils.run_shell_command("blah")

        self.assertIsInstance(stdout, str)
        self.assertIsInstance(stderr, str)
        self.assertIsInstance(return_code, int)

        self.assertEqual(return_code, 127)

    def test_isint(self):
        """ Test the isint function """

        self.assertEqual(utils.isint('3'), True)
        self.assertEqual(utils.isint('d'), False)
        self.assertEqual(utils.isint('3.1'), False)
        self.assertEqual(utils.isint(''), False)

    def test_get_phoenix_scripts(self):
        phoenix_dir = "data/phoenix_dirs/RNA_mapping"
        phoenix_scripts = utils.get_phoenix_scripts(phoenix_dir)
        scripts = glob.glob(os.path.realpath(phoenix_dir) + "/??_?_*_*.sh")
        self.assertEqual(phoenix_scripts, scripts)

    def test_get_phoenix_steps(self):
        phoenix_dir = "data/phoenix_dirs/RNA_mapping"
        steps = utils.get_phoenix_steps(phoenix_dir)
        self.assertEqual(steps, {0: 'fastq', 1: 'mapping', 2: 'resolve',
            3: 'finishalign', 4: 'SAMExtractUnmapped', 5: 'FASTA',
            6: 'splitFASTA', 7: 'batchSim4', 8: 'merge', 9: 'globalNames',
            10: 'extractRefine', 11: 'finish', 12: 'finalQC', 13: 'end'})

class Argparser(unittest.TestCase):
    """ Test argparse options """
    def test_ok_sub(self):
        argv = ['sub', '-P', 'project', '-q', 'normal', '-n', '5', '-K',
                '-s', 'LSF', '-o', 'out.%J.%I.txt', '-e', 'err.%J.%I.txt',
                '-i', 'cmds.sh']

        args = utils.get_args(argv)
        self.assertEqual(args.project, 'project')
        self.assertEqual(args.queue, 'normal')
        self.assertEqual(args.ncores, 5)
        self.assertTrue(args.hang)
        self.assertEqual(args.system, 'LSF')
        self.assertEqual(args.stdout, 'out.%J.%I.txt')
        self.assertEqual(args.stderr, 'err.%J.%I.txt')
        self.assertEqual(args.input, 'cmds.sh')

    def test_ok_step(self):
        argv = ['step', '-d', '/path/to/dir', '-s', '001']

        args = utils.get_args(argv)
        self.assertEqual(args.directory, '/path/to/dir')
        self.assertEqual(args.step, 1)
        self.assertEqual(args.force_qc, False)

    def test_ok_run(self):
        argv = ['run', '-d', '/path/to/dir']

        args = utils.get_args(argv)
        self.assertEqual(args.directory, '/path/to/dir')
        self.assertEqual(args.force_qc, False)
        self.assertEqual(args.email_list, None)
