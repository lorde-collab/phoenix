#!/usr/bin/env python3
"""
Utilities for all of phoenix

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

import argparse
import glob
import os
import io
import sys
import shlex
import subprocess
import datetime

from phoenix import __version__
from phoenix.constants import (
    SUB_UPDATE_INTERVAL, SUBSTEP_TYPES, MEMLIM_DEFAULT)

def now():
    """ Simple method to get current datetime """
    return datetime.datetime.now()


def get_args(argv):
    """ Get arguments
    Args:
        argv (list): List of strings from commandline.
    Returns:
        args (Namespace): Argparse object.
    """

    parser = argparse.ArgumentParser(prog="phoenix")
    subparser = parser.add_subparsers(help="Actions")
    parser.add_argument("-v", "--version", action="version",
                        version="phoenix {}".format(__version__))

    ###########
    ### Sub ###
    ###########
    sub = subparser.add_parser("sub", help="Submit a phoenix batch")
    sub.add_argument("-P", "--project", type=str)
    sub.add_argument("-J", "--jobname", type=str)
    sub.add_argument("-a", "--app", type=str)
    sub.add_argument("-q", "--queue", type=str)
    sub.add_argument("-n", "--ncores", type=int, default=1)
    sub.add_argument("-M", "--memlim", type=int, default=MEMLIM_DEFAULT)
    sub.add_argument("-K", "--hang", action="store_true")
    sub.add_argument("-k", "--killall", action="store_true")
    sub.add_argument("-s", "--system", type=str, default="")
    sub.add_argument("-S", "--split_cutoff", type=int, default=4000)
    sub.add_argument("-o", "--stdout", type=str, required=True)
    sub.add_argument("-e", "--stderr", type=str, required=True)
    sub.add_argument("-i", "--input", dest="cmdfile", type=str, required=True)
    sub.add_argument("-u", "--update_interval", type=int,
                     default=SUB_UPDATE_INTERVAL)

    ############
    ### Step ###
    ############
    step = subparser.add_parser("step", help="Complete a phoenix step")
    step.add_argument("-d", "--directory", type=str, required=True)
    step.add_argument("-s", "--step", type=int, required=True)
    step.add_argument("-f", "--force_qc", action="store_true")

    ###########
    ### Run ###
    ###########
    run = subparser.add_parser("run", help="Run a phoenix pipeline")
    run.add_argument("-d", "--directory", type=str, required=True)
    run.add_argument("-s", "--step", type=int)
    run.add_argument("-f", "--force_qc", action="store_true")
    run.add_argument("-e", "--email_list", nargs="+")

    args = parser.parse_args(argv)

    return args

def isint(intstr):
    """ Checks if a string is an integer.
    Args:
        intstr (str): A string
    Returns: bool
    """

    try:
        int(intstr)
        return True
    except ValueError:
        return False

def get_phoenix_scripts(phoenix_directory):
    """ Get a list of phoenix scripts in a directory.
    Args:
        phoenix_directory (str): Path to a phoenix directory.
    Returns:
        phoenix_scripts (list): List of phoenix scripts.
    """
    assert os.path.isdir(phoenix_directory)
    phoenix_directory = os.path.realpath(phoenix_directory)
    phoenix_scripts = glob.glob(os.path.join(phoenix_directory, "??_?_*_*.sh"))
    return phoenix_scripts

def get_phoenix_steps(phoenix_directory):
    """ Get a dict of phoenix steps.
    Args:
        phoenix_directory (str): Path to a phoenix directory.
    Returns:
        phoenix_scripts (list): List of phoenix scripts.
    """
    phoenix_steps = {}
    phoenix_scripts = get_phoenix_scripts(phoenix_directory)
    for phoenix_script in phoenix_scripts:
        pieces = os.path.basename(phoenix_script.split('.')[0]).split('_')
        assert isint(pieces[0])
        assert isint(pieces[1])
        step = int(pieces[0])
        substep = int(pieces[1])
        substep_name = pieces[2]
        step_name = pieces[3]
        assert SUBSTEP_TYPES[substep] == substep_name
        if step in phoenix_steps:
            assert phoenix_steps[step] == step_name
        else:
            phoenix_steps[step] = step_name
    return phoenix_steps

def run_shell_command(command_string, shell=False, stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE):
    """ Executes a command and returns stdout, stderr, return_code.
    Args:
        command_string: Command to be executed
        shell (bool): Whether or not to use shell
        stdout (?): Where to redirect stdout for subprocess.run
        stderr (?): Where to redirect stderr for subprocess.run
    Returns:
        stdout_str (str): stdout of command as a single string.
        stderr_str (str): stderr of command as a single string.
        return_code (int): integer return code of command.
    """

    # Needed for running 'coverage' with buffering on - if we run with
    # buffering then sys.stdout turns into a StringIO class and can't
    # be passed to subprocess.run
    if not isinstance(stdout, io.TextIOWrapper):
        stdout = subprocess.PIPE
    if not isinstance(stderr, io.TextIOWrapper):
        stderr = subprocess.PIPE

    command = shlex.split(command_string)
    if shell:
        command = command_string
    try:
        proc = subprocess.run(command, stdout=stdout, stderr=stderr,
                              shell=shell)
    except FileNotFoundError:
        stdout = ""
        stderr = "Command '%s' not found"%(command[0])
        return_code = 127
        return (stdout, stderr, return_code)

    stdout_str = ""
    stderr_str = ""
    if proc.stdout:
        stdout_str = proc.stdout.decode('utf-8')
    if proc.stderr:
        stderr_str = proc.stderr.decode('utf-8')
    return_code = proc.returncode

    return (stdout_str, stderr_str, return_code)

def run_shell_command_wrapper(cmds_and_io):
    """ Wrapper to 'run_shell_command' to be used with multiprocessing.Pool
    Args:
        cmds_and_io (list):
            - cmds (list): Commands to run.
            - outfiles (list): STDOUT for each command.
            - errfiles (list): STDOUT for each command.
    Returns: None
    """

    cmd = cmds_and_io[0]
    outfile = cmds_and_io[1]
    errfile = cmds_and_io[2]

    fout = open(str(outfile), "w")
    ferr = open(str(errfile), "w")

    # NOTE: Obviously shell injection could be a concern here. However,
    # we need to allow for compound ('&&') commands to be entered in the
    # cmds file so need to execute each command 'as-is'
    (stdout, stderr, return_code) = run_shell_command(cmd, shell=True)

    print(stdout, file=fout)
    print(stderr, file=ferr)

    fout.close()
    ferr.close()
