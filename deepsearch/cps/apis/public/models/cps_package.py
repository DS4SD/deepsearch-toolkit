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


class CpsPackage(object):
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
        'dependencies': 'list[str]',
        'description': 'str',
        'name': 'str',
        'package_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'dependencies': 'dependencies',
        'description': 'description',
        'name': 'name',
        'package_id': 'package_id',
        'type': 'type'
    }

    def __init__(self, dependencies=None, description=None, name=None, package_id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """CpsPackage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dependencies = None
        self._description = None
        self._name = None
        self._package_id = None
        self._type = None
        self.discriminator = None

        self.dependencies = dependencies
        self.description = description
        self.name = name
        self.package_id = package_id
        self.type = type

    @property
    def dependencies(self):
        """Gets the dependencies of this CpsPackage.  # noqa: E501


        :return: The dependencies of this CpsPackage.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this CpsPackage.


        :param dependencies: The dependencies of this CpsPackage.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and dependencies is None:  # noqa: E501
            raise ValueError("Invalid value for `dependencies`, must not be `None`")  # noqa: E501

        self._dependencies = dependencies

    @property
    def description(self):
        """Gets the description of this CpsPackage.  # noqa: E501


        :return: The description of this CpsPackage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CpsPackage.


        :param description: The description of this CpsPackage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this CpsPackage.  # noqa: E501


        :return: The name of this CpsPackage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CpsPackage.


        :param name: The name of this CpsPackage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def package_id(self):
        """Gets the package_id of this CpsPackage.  # noqa: E501


        :return: The package_id of this CpsPackage.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this CpsPackage.


        :param package_id: The package_id of this CpsPackage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and package_id is None:  # noqa: E501
            raise ValueError("Invalid value for `package_id`, must not be `None`")  # noqa: E501

        self._package_id = package_id

    @property
    def type(self):
        """Gets the type of this CpsPackage.  # noqa: E501


        :return: The type of this CpsPackage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CpsPackage.


        :param type: The type of this CpsPackage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["model", "dictionary", "knowledge_graph", "data_catalog", "data_flow", "bundle"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, CpsPackage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CpsPackage):
            return True

        return self.to_dict() != other.to_dict()
