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


class S3CoordinatesWithBackupKey(object):
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
        'access_key': 'str',
        'backup_key': 'str',
        'bucket': 'str',
        'host': 'str',
        'location': 'str',
        'port': 'int',
        'presigned': 'S3CoordinatesWithBackupKeyPresigned',
        'secret_key': 'str',
        'ssl': 'bool',
        'verify_ssl': 'bool'
    }

    attribute_map = {
        'access_key': 'access-key',
        'backup_key': 'backup_key',
        'bucket': 'bucket',
        'host': 'host',
        'location': 'location',
        'port': 'port',
        'presigned': 'presigned',
        'secret_key': 'secret-key',
        'ssl': 'ssl',
        'verify_ssl': 'verifySSL'
    }

    def __init__(self, access_key=None, backup_key=None, bucket=None, host=None, location=None, port=None, presigned=None, secret_key=None, ssl=None, verify_ssl=None, local_vars_configuration=None):  # noqa: E501
        """S3CoordinatesWithBackupKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key = None
        self._backup_key = None
        self._bucket = None
        self._host = None
        self._location = None
        self._port = None
        self._presigned = None
        self._secret_key = None
        self._ssl = None
        self._verify_ssl = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        self.backup_key = backup_key
        self.bucket = bucket
        if host is not None:
            self.host = host
        if location is not None:
            self.location = location
        if port is not None:
            self.port = port
        if presigned is not None:
            self.presigned = presigned
        if secret_key is not None:
            self.secret_key = secret_key
        if ssl is not None:
            self.ssl = ssl
        if verify_ssl is not None:
            self.verify_ssl = verify_ssl

    @property
    def access_key(self):
        """Gets the access_key of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The access_key of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this S3CoordinatesWithBackupKey.


        :param access_key: The access_key of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def backup_key(self):
        """Gets the backup_key of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The backup_key of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: str
        """
        return self._backup_key

    @backup_key.setter
    def backup_key(self, backup_key):
        """Sets the backup_key of this S3CoordinatesWithBackupKey.


        :param backup_key: The backup_key of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and backup_key is None:  # noqa: E501
            raise ValueError("Invalid value for `backup_key`, must not be `None`")  # noqa: E501

        self._backup_key = backup_key

    @property
    def bucket(self):
        """Gets the bucket of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The bucket of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this S3CoordinatesWithBackupKey.


        :param bucket: The bucket of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bucket is None:  # noqa: E501
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501

        self._bucket = bucket

    @property
    def host(self):
        """Gets the host of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The host of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this S3CoordinatesWithBackupKey.


        :param host: The host of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def location(self):
        """Gets the location of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The location of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this S3CoordinatesWithBackupKey.


        :param location: The location of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def port(self):
        """Gets the port of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The port of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this S3CoordinatesWithBackupKey.


        :param port: The port of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def presigned(self):
        """Gets the presigned of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The presigned of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: S3CoordinatesWithBackupKeyPresigned
        """
        return self._presigned

    @presigned.setter
    def presigned(self, presigned):
        """Sets the presigned of this S3CoordinatesWithBackupKey.


        :param presigned: The presigned of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: S3CoordinatesWithBackupKeyPresigned
        """

        self._presigned = presigned

    @property
    def secret_key(self):
        """Gets the secret_key of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The secret_key of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this S3CoordinatesWithBackupKey.


        :param secret_key: The secret_key of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def ssl(self):
        """Gets the ssl of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The ssl of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this S3CoordinatesWithBackupKey.


        :param ssl: The ssl of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: bool
        """

        self._ssl = ssl

    @property
    def verify_ssl(self):
        """Gets the verify_ssl of this S3CoordinatesWithBackupKey.  # noqa: E501


        :return: The verify_ssl of this S3CoordinatesWithBackupKey.  # noqa: E501
        :rtype: bool
        """
        return self._verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, verify_ssl):
        """Sets the verify_ssl of this S3CoordinatesWithBackupKey.


        :param verify_ssl: The verify_ssl of this S3CoordinatesWithBackupKey.  # noqa: E501
        :type: bool
        """

        self._verify_ssl = verify_ssl

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
        if not isinstance(other, S3CoordinatesWithBackupKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, S3CoordinatesWithBackupKey):
            return True

        return self.to_dict() != other.to_dict()
