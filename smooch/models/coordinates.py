# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Coordinates(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, lat=None, long=None):
        """
        Coordinates - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'lat': 'float',
            'long': 'float'
        }

        self.attribute_map = {
            'lat': 'lat',
            'long': 'long'
        }

        self._lat = None
        self._long = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if lat is not None:
          self.lat = lat
        if long is not None:
          self.long = long

    @property
    def lat(self):
        """
        Gets the lat of this Coordinates.
        A floating point value representing the latitude of the location.

        :return: The lat of this Coordinates.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """
        Sets the lat of this Coordinates.
        A floating point value representing the latitude of the location.

        :param lat: The lat of this Coordinates.
        :type: float
        """
        if lat is None:
            raise ValueError("Invalid value for `lat`, must not be `None`")

        self._lat = lat

    @property
    def long(self):
        """
        Gets the long of this Coordinates.
        A floating point value representing the longitude of the location.

        :return: The long of this Coordinates.
        :rtype: float
        """
        return self._long

    @long.setter
    def long(self, long):
        """
        Sets the long of this Coordinates.
        A floating point value representing the longitude of the location.

        :param long: The long of this Coordinates.
        :type: float
        """
        if long is None:
            raise ValueError("Invalid value for `long`, must not be `None`")

        self._long = long

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Coordinates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
