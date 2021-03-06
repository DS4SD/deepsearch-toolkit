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


class ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs(object):
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
        'auth_token': 'str',
        'export_package_mongo_options': 'ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions',
        'proj_key': 'str',
        'source_collection_name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'auth_token': 'auth_token',
        'export_package_mongo_options': 'export_package_mongo_options',
        'proj_key': 'proj_key',
        'source_collection_name': 'source_collection_name',
        'url': 'url'
    }

    def __init__(self, auth_token=None, export_package_mongo_options=None, proj_key=None, source_collection_name=None, url=None, local_vars_configuration=None):  # noqa: E501
        """ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth_token = None
        self._export_package_mongo_options = None
        self._proj_key = None
        self._source_collection_name = None
        self._url = None
        self.discriminator = None

        if auth_token is not None:
            self.auth_token = auth_token
        if export_package_mongo_options is not None:
            self.export_package_mongo_options = export_package_mongo_options
        self.proj_key = proj_key
        if source_collection_name is not None:
            self.source_collection_name = source_collection_name
        if url is not None:
            self.url = url

    @property
    def auth_token(self):
        """Gets the auth_token of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501


        :return: The auth_token of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.


        :param auth_token: The auth_token of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :type: str
        """

        self._auth_token = auth_token

    @property
    def export_package_mongo_options(self):
        """Gets the export_package_mongo_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501


        :return: The export_package_mongo_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :rtype: ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions
        """
        return self._export_package_mongo_options

    @export_package_mongo_options.setter
    def export_package_mongo_options(self, export_package_mongo_options):
        """Sets the export_package_mongo_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.


        :param export_package_mongo_options: The export_package_mongo_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :type: ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions
        """

        self._export_package_mongo_options = export_package_mongo_options

    @property
    def proj_key(self):
        """Gets the proj_key of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501


        :return: The proj_key of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.


        :param proj_key: The proj_key of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and proj_key is None:  # noqa: E501
            raise ValueError("Invalid value for `proj_key`, must not be `None`")  # noqa: E501

        self._proj_key = proj_key

    @property
    def source_collection_name(self):
        """Gets the source_collection_name of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501


        :return: The source_collection_name of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :rtype: str
        """
        return self._source_collection_name

    @source_collection_name.setter
    def source_collection_name(self, source_collection_name):
        """Sets the source_collection_name of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.


        :param source_collection_name: The source_collection_name of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :type: str
        """

        self._source_collection_name = source_collection_name

    @property
    def url(self):
        """Gets the url of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501


        :return: The url of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.


        :param url: The url of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcs):
            return True

        return self.to_dict() != other.to_dict()
