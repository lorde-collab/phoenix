#!/usr/bin/env python

from phoenix.constants import SPLIT_CUTOFF

class AbstractBatchSystem:
    """ Generic job type """
    def __init__(self, system):
        self._system = system
        self._split_cutoff = SPLIT_CUTOFF

        self.__fail_exit_reasons = []

    # If the job failed due to these reasons, consider it unrecoverable
    @property
    def fail_exit_reasons(self):
        raise NotImplementedError()

    def check_job_state(self, job_id):
        """ Checks on the status of a single job
        Args:
            jobid (int): Job id of the job.
        Returns:
            state (str): State of the job (Pend, Run, Done, Fail).
        """
        raise NotImplementedError()

    def jobs_from_arrays(self, array_ids):
        """ Creates a set of Jobs from the verbose output of the arrays.
        Args:
            array_ids (list): List of Job array id.
        Returns:
            jobs (dict): Dictionary of Job objects.
        """
        raise NotImplementedError()

    def jobs_from_array(self, array_id):
        """ Creates a set of Jobs from the verbose output of the arrays.
        Args:
            array_ids (int): Array id.
        Returns:
            jobs (dict): Dictionary of Job objects.
        """
        raise NotImplementedError()


    def sub_array_for_cmdfile(self, cmdfile, **kwargs):
        """ Submits one or more arrays for commands in a commandfile
        Args:
            cmdfile (str): Path to a command file.
        Returns:
            array_ids (list): List of job array ids.
        """
        raise NotImplementedError()

class AbstractJob:
    """ Generic job type """
    def __init__(self, system):
        self.__jobid = None
        self.__jobindex = None
        self.__queue = None
        self.__user = None

        # By default we don't know if it exited or not.
        self.__exit_reason = "?"
        self.__exit_code = "?"
        self.__status = "?"

    def __str__(self):
        raise NotImplementedError()

    def recover(self):
        """ Attempt to recover the job.
        Args: None
        Returns:
            bool: Whether or not the job was recovered.
        """
        raise NotImplementedError()

    # Whether or not this job should be considered finished (not recoverable)
    @property
    def finished(self):
        raise NotImplementedError()

    # Why the job exited
    @property
    def exit_reason(self):
        if self.exit_success or self.exit_failure:
            return self.__exit_reason
        else:
            return None
    @exit_reason.setter
    def exit_reason(self, exit_reason):
        self.__exit_reason = exit_reason

    ###############################################
    ### Common parlance for all scheduler types ###
    ###############################################
    @property
    def pending(self):
        raise NotImplementedError()
    @property
    def running(self):
        raise NotImplementedError()
    @property
    def exit_success(self):
        raise NotImplementedError()
    @property
    def exit_failure(self):
        raise NotImplementedError()

    #######################################################################
    ### Generic Job properties directly accessible via queueing systems ###
    #######################################################################
    @property
    def jobid(self):
        return self.__jobid
    @jobid.setter
    def jobid(self, jobid):
        self.__jobid = jobid

    @property
    def jobindex(self):
        return self.__jobindex
    @jobindex.setter
    def jobindex(self, jobindex):
        self.__jobindex = jobindex

    @property
    def queue(self):
        return self.__queue
    @queue.setter
    def queue(self, queue):
        self.__queue = queue

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def project(self):
        return self.__project
    @project.setter
    def project(self, project):
        self.__project = project

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def exit_code(self):
        if self.exit_success or self.exit_failure:
            return self.__exit_code
        else:
            return None
    @exit_code.setter
    def exit_code(self, exit_code):
        self.__exit_code = exit_code

