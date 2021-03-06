# coding: utf-8

"""
    Corpus Processing Service (CPS) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.public.configuration import Configuration


class SystemCeleryTasksFailureFailures(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'logs': 'dict(str, object)',
        'meta': 'dict(str, object)',
        'task_id': 'str',
        'worker_name': 'str'
    }

    attribute_map = {
        'logs': 'logs',
        'meta': 'meta',
        'task_id': 'task_id',
        'worker_name': 'worker_name'
    }

    def __init__(self, logs=None, meta=None, task_id=None, worker_name=None, local_vars_configuration=None):  # noqa: E501
        """SystemCeleryTasksFailureFailures - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._logs = None
        self._meta = None
        self._task_id = None
        self._worker_name = None
        self.discriminator = None

        if logs is not None:
            self.logs = logs
        if meta is not None:
            self.meta = meta
        if task_id is not None:
            self.task_id = task_id
        if worker_name is not None:
            self.worker_name = worker_name

    @property
    def logs(self):
        """Gets the logs of this SystemCeleryTasksFailureFailures.  # noqa: E501


        :return: The logs of this SystemCeleryTasksFailureFailures.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this SystemCeleryTasksFailureFailures.


        :param logs: The logs of this SystemCeleryTasksFailureFailures.  # noqa: E501
        :type: dict(str, object)
        """

        self._logs = logs

    @property
    def meta(self):
        """Gets the meta of this SystemCeleryTasksFailureFailures.  # noqa: E501


        :return: The meta of this SystemCeleryTasksFailureFailures.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this SystemCeleryTasksFailureFailures.


        :param meta: The meta of this SystemCeleryTasksFailureFailures.  # noqa: E501
        :type: dict(str, object)
        """

        self._meta = meta

    @property
    def task_id(self):
        """Gets the task_id of this SystemCeleryTasksFailureFailures.  # noqa: E501


        :return: The task_id of this SystemCeleryTasksFailureFailures.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this SystemCeleryTasksFailureFailures.


        :param task_id: The task_id of this SystemCeleryTasksFailureFailures.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def worker_name(self):
        """Gets the worker_name of this SystemCeleryTasksFailureFailures.  # noqa: E501


        :return: The worker_name of this SystemCeleryTasksFailureFailures.  # noqa: E501
        :rtype: str
        """
        return self._worker_name

    @worker_name.setter
    def worker_name(self, worker_name):
        """Sets the worker_name of this SystemCeleryTasksFailureFailures.


        :param worker_name: The worker_name of this SystemCeleryTasksFailureFailures.  # noqa: E501
        :type: str
        """

        self._worker_name = worker_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SystemCeleryTasksFailureFailures):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemCeleryTasksFailureFailures):
            return True

        return self.to_dict() != other.to_dict()
