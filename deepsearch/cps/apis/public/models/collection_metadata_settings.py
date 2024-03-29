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


class CollectionMetadataSettings(object):
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
        'description': 'str',
        'display_name': 'str',
        'licence': 'str',
        'source': 'str',
        'version': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'licence': 'licence',
        'source': 'source',
        'version': 'version'
    }

    def __init__(self, description=None, display_name=None, licence=None, source=None, version=None, local_vars_configuration=None):  # noqa: E501
        """CollectionMetadataSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._display_name = None
        self._licence = None
        self._source = None
        self._version = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if licence is not None:
            self.licence = licence
        if source is not None:
            self.source = source
        if version is not None:
            self.version = version

    @property
    def description(self):
        """Gets the description of this CollectionMetadataSettings.  # noqa: E501


        :return: The description of this CollectionMetadataSettings.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CollectionMetadataSettings.


        :param description: The description of this CollectionMetadataSettings.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this CollectionMetadataSettings.  # noqa: E501


        :return: The display_name of this CollectionMetadataSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CollectionMetadataSettings.


        :param display_name: The display_name of this CollectionMetadataSettings.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def licence(self):
        """Gets the licence of this CollectionMetadataSettings.  # noqa: E501


        :return: The licence of this CollectionMetadataSettings.  # noqa: E501
        :rtype: str
        """
        return self._licence

    @licence.setter
    def licence(self, licence):
        """Sets the licence of this CollectionMetadataSettings.


        :param licence: The licence of this CollectionMetadataSettings.  # noqa: E501
        :type: str
        """

        self._licence = licence

    @property
    def source(self):
        """Gets the source of this CollectionMetadataSettings.  # noqa: E501


        :return: The source of this CollectionMetadataSettings.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CollectionMetadataSettings.


        :param source: The source of this CollectionMetadataSettings.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def version(self):
        """Gets the version of this CollectionMetadataSettings.  # noqa: E501


        :return: The version of this CollectionMetadataSettings.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CollectionMetadataSettings.


        :param version: The version of this CollectionMetadataSettings.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, CollectionMetadataSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollectionMetadataSettings):
            return True

        return self.to_dict() != other.to_dict()
