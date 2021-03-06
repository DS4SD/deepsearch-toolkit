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


class KnowledgeGraphSystemInformation(object):
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
        'backend': 'dict(str, SystemKgsBackend)',
        'bag_domain': 'str',
        'bag_key': 'str',
        'bag_url': 'str',
        'name': 'str',
        'proj_key': 'str',
        'project_name': 'str',
        'public': 'bool',
        'slug': 'str',
        'timestamp': 'float'
    }

    attribute_map = {
        'backend': 'backend',
        'bag_domain': 'bag_domain',
        'bag_key': 'bag_key',
        'bag_url': 'bag_url',
        'name': 'name',
        'proj_key': 'proj_key',
        'project_name': 'project_name',
        'public': 'public',
        'slug': 'slug',
        'timestamp': 'timestamp'
    }

    def __init__(self, backend=None, bag_domain=None, bag_key=None, bag_url=None, name=None, proj_key=None, project_name=None, public=None, slug=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """KnowledgeGraphSystemInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._backend = None
        self._bag_domain = None
        self._bag_key = None
        self._bag_url = None
        self._name = None
        self._proj_key = None
        self._project_name = None
        self._public = None
        self._slug = None
        self._timestamp = None
        self.discriminator = None

        if backend is not None:
            self.backend = backend
        if bag_domain is not None:
            self.bag_domain = bag_domain
        if bag_key is not None:
            self.bag_key = bag_key
        if bag_url is not None:
            self.bag_url = bag_url
        if name is not None:
            self.name = name
        if proj_key is not None:
            self.proj_key = proj_key
        if project_name is not None:
            self.project_name = project_name
        if public is not None:
            self.public = public
        if slug is not None:
            self.slug = slug
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def backend(self):
        """Gets the backend of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The backend of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: dict(str, SystemKgsBackend)
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this KnowledgeGraphSystemInformation.


        :param backend: The backend of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: dict(str, SystemKgsBackend)
        """

        self._backend = backend

    @property
    def bag_domain(self):
        """Gets the bag_domain of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The bag_domain of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: str
        """
        return self._bag_domain

    @bag_domain.setter
    def bag_domain(self, bag_domain):
        """Sets the bag_domain of this KnowledgeGraphSystemInformation.


        :param bag_domain: The bag_domain of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: str
        """

        self._bag_domain = bag_domain

    @property
    def bag_key(self):
        """Gets the bag_key of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The bag_key of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: str
        """
        return self._bag_key

    @bag_key.setter
    def bag_key(self, bag_key):
        """Sets the bag_key of this KnowledgeGraphSystemInformation.


        :param bag_key: The bag_key of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: str
        """

        self._bag_key = bag_key

    @property
    def bag_url(self):
        """Gets the bag_url of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The bag_url of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: str
        """
        return self._bag_url

    @bag_url.setter
    def bag_url(self, bag_url):
        """Sets the bag_url of this KnowledgeGraphSystemInformation.


        :param bag_url: The bag_url of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: str
        """

        self._bag_url = bag_url

    @property
    def name(self):
        """Gets the name of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The name of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KnowledgeGraphSystemInformation.


        :param name: The name of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def proj_key(self):
        """Gets the proj_key of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The proj_key of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this KnowledgeGraphSystemInformation.


        :param proj_key: The proj_key of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: str
        """

        self._proj_key = proj_key

    @property
    def project_name(self):
        """Gets the project_name of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The project_name of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this KnowledgeGraphSystemInformation.


        :param project_name: The project_name of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def public(self):
        """Gets the public of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The public of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this KnowledgeGraphSystemInformation.


        :param public: The public of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def slug(self):
        """Gets the slug of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The slug of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this KnowledgeGraphSystemInformation.


        :param slug: The slug of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def timestamp(self):
        """Gets the timestamp of this KnowledgeGraphSystemInformation.  # noqa: E501


        :return: The timestamp of this KnowledgeGraphSystemInformation.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this KnowledgeGraphSystemInformation.


        :param timestamp: The timestamp of this KnowledgeGraphSystemInformation.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

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
        if not isinstance(other, KnowledgeGraphSystemInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KnowledgeGraphSystemInformation):
            return True

        return self.to_dict() != other.to_dict()
