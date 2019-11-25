#!/usr/bin/env python3

from phoenix import utils

def detect_scheduler():
    """ Detect what (if any) scheduler is available.
    Args:
        None
    Returns:
        scheduler (str): The scheduler detected on the system.
    """
    # Check for LSF
    (stdout, stderr, return_code) = utils.run_shell_command("lsid")
    if return_code == 0 and "LSF" in stdout:
        return "LSF"

    return "local"
