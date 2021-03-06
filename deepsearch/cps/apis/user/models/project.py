# coding: utf-8

"""
    User Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.user.configuration import Configuration


class Project(object):
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
        'date': 'str',
        'name': 'str',
        'proj_key': 'str',
        'role': 'UserType'
    }

    attribute_map = {
        'date': 'date',
        'name': 'name',
        'proj_key': 'proj_key',
        'role': 'role'
    }

    def __init__(self, date=None, name=None, proj_key=None, role=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._name = None
        self._proj_key = None
        self._role = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if name is not None:
            self.name = name
        if proj_key is not None:
            self.proj_key = proj_key
        if role is not None:
            self.role = role

    @property
    def date(self):
        """Gets the date of this Project.  # noqa: E501


        :return: The date of this Project.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Project.


        :param date: The date of this Project.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def proj_key(self):
        """Gets the proj_key of this Project.  # noqa: E501


        :return: The proj_key of this Project.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this Project.


        :param proj_key: The proj_key of this Project.  # noqa: E501
        :type: str
        """

        self._proj_key = proj_key

    @property
    def role(self):
        """Gets the role of this Project.  # noqa: E501


        :return: The role of this Project.  # noqa: E501
        :rtype: UserType
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Project.


        :param role: The role of this Project.  # noqa: E501
        :type: UserType
        """

        self._role = role

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
