# coding: utf-8

"""
    Knowledge-Graph Create API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.kg.create.configuration import Configuration


class SparseMatrixWithNamesOrHashes(object):
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
        'i': 'list[str]',
        'j': 'list[str]',
        'w': 'list[float]'
    }

    attribute_map = {
        'i': 'I',
        'j': 'J',
        'w': 'W'
    }

    def __init__(self, i=None, j=None, w=None, local_vars_configuration=None):  # noqa: E501
        """SparseMatrixWithNamesOrHashes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._i = None
        self._j = None
        self._w = None
        self.discriminator = None

        self.i = i
        self.j = j
        if w is not None:
            self.w = w

    @property
    def i(self):
        """Gets the i of this SparseMatrixWithNamesOrHashes.  # noqa: E501


        :return: The i of this SparseMatrixWithNamesOrHashes.  # noqa: E501
        :rtype: list[str]
        """
        return self._i

    @i.setter
    def i(self, i):
        """Sets the i of this SparseMatrixWithNamesOrHashes.


        :param i: The i of this SparseMatrixWithNamesOrHashes.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and i is None:  # noqa: E501
            raise ValueError("Invalid value for `i`, must not be `None`")  # noqa: E501

        self._i = i

    @property
    def j(self):
        """Gets the j of this SparseMatrixWithNamesOrHashes.  # noqa: E501


        :return: The j of this SparseMatrixWithNamesOrHashes.  # noqa: E501
        :rtype: list[str]
        """
        return self._j

    @j.setter
    def j(self, j):
        """Sets the j of this SparseMatrixWithNamesOrHashes.


        :param j: The j of this SparseMatrixWithNamesOrHashes.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and j is None:  # noqa: E501
            raise ValueError("Invalid value for `j`, must not be `None`")  # noqa: E501

        self._j = j

    @property
    def w(self):
        """Gets the w of this SparseMatrixWithNamesOrHashes.  # noqa: E501


        :return: The w of this SparseMatrixWithNamesOrHashes.  # noqa: E501
        :rtype: list[float]
        """
        return self._w

    @w.setter
    def w(self, w):
        """Sets the w of this SparseMatrixWithNamesOrHashes.


        :param w: The w of this SparseMatrixWithNamesOrHashes.  # noqa: E501
        :type: list[float]
        """

        self._w = w

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
        if not isinstance(other, SparseMatrixWithNamesOrHashes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SparseMatrixWithNamesOrHashes):
            return True

        return self.to_dict() != other.to_dict()
