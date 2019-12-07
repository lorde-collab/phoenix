#!/usr/bin/env python
"""
Template for an Abstract batch system and job

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

from phoenix.constants import SPLIT_CUTOFF

class AbstractBatchSystem:
    """ Generic job type """
    def __init__(self, system):
        self._system = system
        self._split_cutoff = SPLIT_CUTOFF

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


    def sub_array_for_cmdfile(self, args):
        """ Submits one or more arrays for commands in a commandfile
        Args:
            args (Namespace): Argparse namespace.
        Returns:
            array_ids (list): List of job array ids.
        """
        raise NotImplementedError()

class AbstractJob:
    """ Generic job type """
    def __init__(self):
        """ init """
        self.__jobid = None
        self.__jobindex = None
        self.__queue = None
        self.__user = None
        self.__project = None

        # By default we don't know if it exited or not.
        self.__exit_reason = "?"
        self.__exit_code = "?"
        self.__status = "?"

    def __str__(self):
        """ str() representation """
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
        """
        Whether or not this job should be considered finished (not recoverable)
        """
        raise NotImplementedError()

    @property
    def exit_reason(self):
        """ Why the job exited (getter) """
        if self.exit_success or self.exit_failure:
            return self.__exit_reason
        return None
    @exit_reason.setter
    def exit_reason(self, exit_reason):
        """ Why the job exited (setter) """
        self.__exit_reason = exit_reason

    ###############################################
    ### Common parlance for all scheduler types ###
    ###############################################
    @property
    def pending(self):
        """ Whether or not this job is pending """
        raise NotImplementedError()
    @property
    def running(self):
        """ Whether or not this job is running """
        raise NotImplementedError()
    @property
    def exit_success(self):
        """ Whether or not this job has exited with success """
        raise NotImplementedError()
    @property
    def exit_failure(self):
        """ Whether or not this job has exited with failure """
        raise NotImplementedError()

    #######################################################################
    ### Generic Job properties directly accessible via queueing systems ###
    #######################################################################
    @property
    def jobid(self):
        """ Job id (getter) """
        return self.__jobid
    @jobid.setter
    def jobid(self, jobid):
        """ Job id (setter) """
        self.__jobid = jobid

    @property
    def jobindex(self):
        """ Job index (getter) """
        return self.__jobindex
    @jobindex.setter
    def jobindex(self, jobindex):
        """ Job index (setter) """
        self.__jobindex = jobindex

    @property
    def queue(self):
        """ Queue that the job was submitted to (getter) """
        return self.__queue
    @queue.setter
    def queue(self, queue):
        """ Queue that the job was submitted to (setter) """
        self.__queue = queue

    @property
    def user(self):
        """ User the job was submitted by (getter) """
        return self.__user
    @user.setter
    def user(self, user):
        """ User the job was submitted by (setter) """
        self.__user = user

    @property
    def project(self):
        """ Project the job was submitted under (getter) """
        return self.__project
    @project.setter
    def project(self, project):
        """ Project the job was submitted under (setter) """
        self.__project = project

    @property
    def status(self):
        """ Job status (getter) """
        return self.__status
    @status.setter
    def status(self, status):
        """ Job status (setter) """
        self.__status = status

    @property
    def exit_code(self):
        """ Job exit code (getter) """
        if self.exit_success or self.exit_failure:
            return self.__exit_code
        return None
    @exit_code.setter
    def exit_code(self, exit_code):
        """ Job exit code (setter) """
        self.__exit_code = exit_code
