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


class BagBackendAware(object):
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
        'backend': 'BagBackends',
        'bag_key': 'str',
        'description': 'str',
        'last_coords_resolution': 'float',
        'name': 'str',
        'proj_key': 'str',
        'public': 'bool',
        'slug': 'str',
        'timestamp': 'float'
    }

    attribute_map = {
        'backend': 'backend',
        'bag_key': 'bag_key',
        'description': 'description',
        'last_coords_resolution': 'last_coords_resolution',
        'name': 'name',
        'proj_key': 'proj_key',
        'public': 'public',
        'slug': 'slug',
        'timestamp': 'timestamp'
    }

    def __init__(self, backend=None, bag_key=None, description=None, last_coords_resolution=None, name=None, proj_key=None, public=None, slug=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """BagBackendAware - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._backend = None
        self._bag_key = None
        self._description = None
        self._last_coords_resolution = None
        self._name = None
        self._proj_key = None
        self._public = None
        self._slug = None
        self._timestamp = None
        self.discriminator = None

        self.backend = backend
        self.bag_key = bag_key
        self.description = description
        if last_coords_resolution is not None:
            self.last_coords_resolution = last_coords_resolution
        self.name = name
        self.proj_key = proj_key
        self.public = public
        self.slug = slug
        self.timestamp = timestamp

    @property
    def backend(self):
        """Gets the backend of this BagBackendAware.  # noqa: E501


        :return: The backend of this BagBackendAware.  # noqa: E501
        :rtype: BagBackends
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this BagBackendAware.


        :param backend: The backend of this BagBackendAware.  # noqa: E501
        :type: BagBackends
        """
        if self.local_vars_configuration.client_side_validation and backend is None:  # noqa: E501
            raise ValueError("Invalid value for `backend`, must not be `None`")  # noqa: E501

        self._backend = backend

    @property
    def bag_key(self):
        """Gets the bag_key of this BagBackendAware.  # noqa: E501


        :return: The bag_key of this BagBackendAware.  # noqa: E501
        :rtype: str
        """
        return self._bag_key

    @bag_key.setter
    def bag_key(self, bag_key):
        """Sets the bag_key of this BagBackendAware.


        :param bag_key: The bag_key of this BagBackendAware.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bag_key is None:  # noqa: E501
            raise ValueError("Invalid value for `bag_key`, must not be `None`")  # noqa: E501

        self._bag_key = bag_key

    @property
    def description(self):
        """Gets the description of this BagBackendAware.  # noqa: E501


        :return: The description of this BagBackendAware.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BagBackendAware.


        :param description: The description of this BagBackendAware.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def last_coords_resolution(self):
        """Gets the last_coords_resolution of this BagBackendAware.  # noqa: E501


        :return: The last_coords_resolution of this BagBackendAware.  # noqa: E501
        :rtype: float
        """
        return self._last_coords_resolution

    @last_coords_resolution.setter
    def last_coords_resolution(self, last_coords_resolution):
        """Sets the last_coords_resolution of this BagBackendAware.


        :param last_coords_resolution: The last_coords_resolution of this BagBackendAware.  # noqa: E501
        :type: float
        """

        self._last_coords_resolution = last_coords_resolution

    @property
    def name(self):
        """Gets the name of this BagBackendAware.  # noqa: E501


        :return: The name of this BagBackendAware.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BagBackendAware.


        :param name: The name of this BagBackendAware.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def proj_key(self):
        """Gets the proj_key of this BagBackendAware.  # noqa: E501


        :return: The proj_key of this BagBackendAware.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this BagBackendAware.


        :param proj_key: The proj_key of this BagBackendAware.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and proj_key is None:  # noqa: E501
            raise ValueError("Invalid value for `proj_key`, must not be `None`")  # noqa: E501

        self._proj_key = proj_key

    @property
    def public(self):
        """Gets the public of this BagBackendAware.  # noqa: E501


        :return: The public of this BagBackendAware.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this BagBackendAware.


        :param public: The public of this BagBackendAware.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and public is None:  # noqa: E501
            raise ValueError("Invalid value for `public`, must not be `None`")  # noqa: E501

        self._public = public

    @property
    def slug(self):
        """Gets the slug of this BagBackendAware.  # noqa: E501


        :return: The slug of this BagBackendAware.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this BagBackendAware.


        :param slug: The slug of this BagBackendAware.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and slug is None:  # noqa: E501
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

    @property
    def timestamp(self):
        """Gets the timestamp of this BagBackendAware.  # noqa: E501


        :return: The timestamp of this BagBackendAware.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BagBackendAware.


        :param timestamp: The timestamp of this BagBackendAware.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, BagBackendAware):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BagBackendAware):
            return True

        return self.to_dict() != other.to_dict()
