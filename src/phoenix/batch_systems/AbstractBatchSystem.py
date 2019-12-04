#!/usr/bin/env python

class AbstractBatchSystem:
    """ Generic job type """
    def __init__(self, system):
        self._system = system
        self._split_cutoff = 4000

    def check_job_state(self, job_id):
        """ Checks on the status of a single job
        Args:
            jobid (int): Job id of the job.
        Returns:
            state (str): State of the job (Pend, Run, Done, Fail).
        """
        raise NotImplementedError()

    def verbose_array_state(self, array_id):
        """ Checks the state of the array with verbosity.
        Args:
            array_id (int): Job array id.
        Returns:
            stdout (str): stdout of check.
            stderr (str): stderr of check.
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

    def __str__(self):
        raise NotImplementedError()

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
