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


class ProjectFlavourTotalKgs(object):
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
        'flavour_name': 'str',
        'proj_key': 'str',
        'total_kgs': 'int'
    }

    attribute_map = {
        'flavour_name': 'flavour_name',
        'proj_key': 'proj_key',
        'total_kgs': 'total_kgs'
    }

    def __init__(self, flavour_name=None, proj_key=None, total_kgs=None, local_vars_configuration=None):  # noqa: E501
        """ProjectFlavourTotalKgs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._flavour_name = None
        self._proj_key = None
        self._total_kgs = None
        self.discriminator = None

        self.flavour_name = flavour_name
        self.proj_key = proj_key
        self.total_kgs = total_kgs

    @property
    def flavour_name(self):
        """Gets the flavour_name of this ProjectFlavourTotalKgs.  # noqa: E501


        :return: The flavour_name of this ProjectFlavourTotalKgs.  # noqa: E501
        :rtype: str
        """
        return self._flavour_name

    @flavour_name.setter
    def flavour_name(self, flavour_name):
        """Sets the flavour_name of this ProjectFlavourTotalKgs.


        :param flavour_name: The flavour_name of this ProjectFlavourTotalKgs.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and flavour_name is None:  # noqa: E501
            raise ValueError("Invalid value for `flavour_name`, must not be `None`")  # noqa: E501

        self._flavour_name = flavour_name

    @property
    def proj_key(self):
        """Gets the proj_key of this ProjectFlavourTotalKgs.  # noqa: E501


        :return: The proj_key of this ProjectFlavourTotalKgs.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this ProjectFlavourTotalKgs.


        :param proj_key: The proj_key of this ProjectFlavourTotalKgs.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and proj_key is None:  # noqa: E501
            raise ValueError("Invalid value for `proj_key`, must not be `None`")  # noqa: E501

        self._proj_key = proj_key

    @property
    def total_kgs(self):
        """Gets the total_kgs of this ProjectFlavourTotalKgs.  # noqa: E501


        :return: The total_kgs of this ProjectFlavourTotalKgs.  # noqa: E501
        :rtype: int
        """
        return self._total_kgs

    @total_kgs.setter
    def total_kgs(self, total_kgs):
        """Sets the total_kgs of this ProjectFlavourTotalKgs.


        :param total_kgs: The total_kgs of this ProjectFlavourTotalKgs.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_kgs is None:  # noqa: E501
            raise ValueError("Invalid value for `total_kgs`, must not be `None`")  # noqa: E501

        self._total_kgs = total_kgs

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
        if not isinstance(other, ProjectFlavourTotalKgs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectFlavourTotalKgs):
            return True

        return self.to_dict() != other.to_dict()
