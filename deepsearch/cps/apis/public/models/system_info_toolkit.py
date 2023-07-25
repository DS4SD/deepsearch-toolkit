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


class SystemInfoToolkit(object):
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
        'cli_command': 'str',
        'host': 'str',
        'name': 'str',
        'required_version': 'str',
        'verify_ssl': 'bool'
    }

    attribute_map = {
        'cli_command': 'cli_command',
        'host': 'host',
        'name': 'name',
        'required_version': 'required_version',
        'verify_ssl': 'verify_ssl'
    }

    def __init__(self, cli_command=None, host=None, name=None, required_version=None, verify_ssl=None, local_vars_configuration=None):  # noqa: E501
        """SystemInfoToolkit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cli_command = None
        self._host = None
        self._name = None
        self._required_version = None
        self._verify_ssl = None
        self.discriminator = None

        if cli_command is not None:
            self.cli_command = cli_command
        if host is not None:
            self.host = host
        if name is not None:
            self.name = name
        self.required_version = required_version
        if verify_ssl is not None:
            self.verify_ssl = verify_ssl

    @property
    def cli_command(self):
        """Gets the cli_command of this SystemInfoToolkit.  # noqa: E501


        :return: The cli_command of this SystemInfoToolkit.  # noqa: E501
        :rtype: str
        """
        return self._cli_command

    @cli_command.setter
    def cli_command(self, cli_command):
        """Sets the cli_command of this SystemInfoToolkit.


        :param cli_command: The cli_command of this SystemInfoToolkit.  # noqa: E501
        :type: str
        """

        self._cli_command = cli_command

    @property
    def host(self):
        """Gets the host of this SystemInfoToolkit.  # noqa: E501


        :return: The host of this SystemInfoToolkit.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SystemInfoToolkit.


        :param host: The host of this SystemInfoToolkit.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def name(self):
        """Gets the name of this SystemInfoToolkit.  # noqa: E501


        :return: The name of this SystemInfoToolkit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInfoToolkit.


        :param name: The name of this SystemInfoToolkit.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required_version(self):
        """Gets the required_version of this SystemInfoToolkit.  # noqa: E501


        :return: The required_version of this SystemInfoToolkit.  # noqa: E501
        :rtype: str
        """
        return self._required_version

    @required_version.setter
    def required_version(self, required_version):
        """Sets the required_version of this SystemInfoToolkit.


        :param required_version: The required_version of this SystemInfoToolkit.  # noqa: E501
        :type: str
        """

        self._required_version = required_version

    @property
    def verify_ssl(self):
        """Gets the verify_ssl of this SystemInfoToolkit.  # noqa: E501


        :return: The verify_ssl of this SystemInfoToolkit.  # noqa: E501
        :rtype: bool
        """
        return self._verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, verify_ssl):
        """Sets the verify_ssl of this SystemInfoToolkit.


        :param verify_ssl: The verify_ssl of this SystemInfoToolkit.  # noqa: E501
        :type: bool
        """

        self._verify_ssl = verify_ssl

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
        if not isinstance(other, SystemInfoToolkit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemInfoToolkit):
            return True

        return self.to_dict() != other.to_dict()
