# coding: utf-8

"""
    Knowledge-Graph Query API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.kg.query.configuration import Configuration


class Node(object):
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
        'name': 'str',
        'hash': 'str',
        'synonyms': 'list[str]',
        'categories': 'list[str]',
        'database': 'object'
    }

    attribute_map = {
        'name': 'name',
        'hash': 'hash',
        'synonyms': 'synonyms',
        'categories': 'categories',
        'database': 'database'
    }

    def __init__(self, name=None, hash=None, synonyms=None, categories=None, database=None, local_vars_configuration=None):  # noqa: E501
        """Node - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._hash = None
        self._synonyms = None
        self._categories = None
        self._database = None
        self.discriminator = None

        self.name = name
        if hash is not None:
            self.hash = hash
        if synonyms is not None:
            self.synonyms = synonyms
        if categories is not None:
            self.categories = categories
        if database is not None:
            self.database = database

    @property
    def name(self):
        """Gets the name of this Node.  # noqa: E501


        :return: The name of this Node.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Node.


        :param name: The name of this Node.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def hash(self):
        """Gets the hash of this Node.  # noqa: E501


        :return: The hash of this Node.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Node.


        :param hash: The hash of this Node.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def synonyms(self):
        """Gets the synonyms of this Node.  # noqa: E501


        :return: The synonyms of this Node.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this Node.


        :param synonyms: The synonyms of this Node.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def categories(self):
        """Gets the categories of this Node.  # noqa: E501


        :return: The categories of this Node.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Node.


        :param categories: The categories of this Node.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def database(self):
        """Gets the database of this Node.  # noqa: E501


        :return: The database of this Node.  # noqa: E501
        :rtype: object
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this Node.


        :param database: The database of this Node.  # noqa: E501
        :type: object
        """

        self._database = database

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
        if not isinstance(other, Node):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Node):
            return True

        return self.to_dict() != other.to_dict()
