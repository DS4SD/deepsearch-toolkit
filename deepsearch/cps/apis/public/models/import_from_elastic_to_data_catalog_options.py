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


class ImportFromElasticToDataCatalogOptions(object):
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
        'coordinates': 'ElasticCoordinates',
        'elastic_id': 'str',
        'parameters': 'ImportFromElasticToDataCatalogOptionsParameters'
    }

    attribute_map = {
        'coordinates': 'coordinates',
        'elastic_id': 'elastic_id',
        'parameters': 'parameters'
    }

    def __init__(self, coordinates=None, elastic_id=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """ImportFromElasticToDataCatalogOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._coordinates = None
        self._elastic_id = None
        self._parameters = None
        self.discriminator = None

        if coordinates is not None:
            self.coordinates = coordinates
        if elastic_id is not None:
            self.elastic_id = elastic_id
        self.parameters = parameters

    @property
    def coordinates(self):
        """Gets the coordinates of this ImportFromElasticToDataCatalogOptions.  # noqa: E501


        :return: The coordinates of this ImportFromElasticToDataCatalogOptions.  # noqa: E501
        :rtype: ElasticCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this ImportFromElasticToDataCatalogOptions.


        :param coordinates: The coordinates of this ImportFromElasticToDataCatalogOptions.  # noqa: E501
        :type: ElasticCoordinates
        """

        self._coordinates = coordinates

    @property
    def elastic_id(self):
        """Gets the elastic_id of this ImportFromElasticToDataCatalogOptions.  # noqa: E501


        :return: The elastic_id of this ImportFromElasticToDataCatalogOptions.  # noqa: E501
        :rtype: str
        """
        return self._elastic_id

    @elastic_id.setter
    def elastic_id(self, elastic_id):
        """Sets the elastic_id of this ImportFromElasticToDataCatalogOptions.


        :param elastic_id: The elastic_id of this ImportFromElasticToDataCatalogOptions.  # noqa: E501
        :type: str
        """

        self._elastic_id = elastic_id

    @property
    def parameters(self):
        """Gets the parameters of this ImportFromElasticToDataCatalogOptions.  # noqa: E501


        :return: The parameters of this ImportFromElasticToDataCatalogOptions.  # noqa: E501
        :rtype: ImportFromElasticToDataCatalogOptionsParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ImportFromElasticToDataCatalogOptions.


        :param parameters: The parameters of this ImportFromElasticToDataCatalogOptions.  # noqa: E501
        :type: ImportFromElasticToDataCatalogOptionsParameters
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if not isinstance(other, ImportFromElasticToDataCatalogOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportFromElasticToDataCatalogOptions):
            return True

        return self.to_dict() != other.to_dict()
