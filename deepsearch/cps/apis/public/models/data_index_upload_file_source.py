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


class DataIndexUploadFileSource(object):
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
        'file_url': 'str',
        'scratch_files_id': 'list[str]'
    }

    attribute_map = {
        'file_url': 'file_url',
        'scratch_files_id': 'scratch_files_id'
    }

    def __init__(self, file_url=None, scratch_files_id=None, local_vars_configuration=None):  # noqa: E501
        """DataIndexUploadFileSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_url = None
        self._scratch_files_id = None
        self.discriminator = None

        if file_url is not None:
            self.file_url = file_url
        if scratch_files_id is not None:
            self.scratch_files_id = scratch_files_id

    @property
    def file_url(self):
        """Gets the file_url of this DataIndexUploadFileSource.  # noqa: E501

        File URL to be converted and uploaded to the data index  # noqa: E501

        :return: The file_url of this DataIndexUploadFileSource.  # noqa: E501
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this DataIndexUploadFileSource.

        File URL to be converted and uploaded to the data index  # noqa: E501

        :param file_url: The file_url of this DataIndexUploadFileSource.  # noqa: E501
        :type: str
        """

        self._file_url = file_url

    @property
    def scratch_files_id(self):
        """Gets the scratch_files_id of this DataIndexUploadFileSource.  # noqa: E501

        List of CCS's scratch files id to be converted and uploaded to the data index  # noqa: E501

        :return: The scratch_files_id of this DataIndexUploadFileSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._scratch_files_id

    @scratch_files_id.setter
    def scratch_files_id(self, scratch_files_id):
        """Sets the scratch_files_id of this DataIndexUploadFileSource.

        List of CCS's scratch files id to be converted and uploaded to the data index  # noqa: E501

        :param scratch_files_id: The scratch_files_id of this DataIndexUploadFileSource.  # noqa: E501
        :type: list[str]
        """

        self._scratch_files_id = scratch_files_id

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
        if not isinstance(other, DataIndexUploadFileSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataIndexUploadFileSource):
            return True

        return self.to_dict() != other.to_dict()
