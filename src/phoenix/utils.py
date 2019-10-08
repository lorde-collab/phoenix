#!/usr/bin/env python3
""" Utilities for all of phoenix """

import argparse

from phoenix import __version__
from phoenix.constants import SUB_UPDATE_INTERVAL

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
    sub.add_argument("-M", "--memlim", type=int)
    sub.add_argument("-K", "--hang", action="store_true")
    sub.add_argument("-s", "--system", type=str, default="local")
    sub.add_argument("-o", "--stdout", type=str, required=True)
    sub.add_argument("-e", "--stderr", type=str, required=True)
    sub.add_argument("-i", "--input", type=str, required=True)
    sub.add_argument("-u", "--update_interval", type=int,
                     default=SUB_UPDATE_INTERVAL)

    ############
    ### Step ###
    ############
    step = subparser.add_parser("step", help="Complete a phoenix step")
    step.add_argument("-d", "--directory", type=str, required=True)
    step.add_argument("-s", "--step", type=int, required=True)

    ###########
    ### Run ###
    ###########
    run = subparser.add_parser("run", help="Run a phoenix pipeline")
    run.add_argument("-d", "--directory", type=str, required=True)
    run.add_argument("-s", "--step", type=int)
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

        
