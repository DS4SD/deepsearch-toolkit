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


class ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions(object):
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
        'match_mode': 'str',
        'redirect_keys_to_s3': 'list[str]'
    }

    attribute_map = {
        'match_mode': 'match_mode',
        'redirect_keys_to_s3': 'redirect_keys_to_s3'
    }

    def __init__(self, match_mode='document_hash', redirect_keys_to_s3=None, local_vars_configuration=None):  # noqa: E501
        """ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._match_mode = None
        self._redirect_keys_to_s3 = None
        self.discriminator = None

        if match_mode is not None:
            self.match_mode = match_mode
        if redirect_keys_to_s3 is not None:
            self.redirect_keys_to_s3 = redirect_keys_to_s3

    @property
    def match_mode(self):
        """Gets the match_mode of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions.  # noqa: E501


        :return: The match_mode of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions.  # noqa: E501
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions.


        :param match_mode: The match_mode of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["use_fuzzy_search", "document_hash"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and match_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `match_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(match_mode, allowed_values)
            )

        self._match_mode = match_mode

    @property
    def redirect_keys_to_s3(self):
        """Gets the redirect_keys_to_s3 of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions.  # noqa: E501


        :return: The redirect_keys_to_s3 of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._redirect_keys_to_s3

    @redirect_keys_to_s3.setter
    def redirect_keys_to_s3(self, redirect_keys_to_s3):
        """Sets the redirect_keys_to_s3 of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions.


        :param redirect_keys_to_s3: The redirect_keys_to_s3 of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions.  # noqa: E501
        :type: list[str]
        """

        self._redirect_keys_to_s3 = redirect_keys_to_s3

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
        if not isinstance(other, ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions):
            return True

        return self.to_dict() != other.to_dict()
