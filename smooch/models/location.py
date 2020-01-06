# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Location(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address=None, name=None):
        """
        Location - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'name': 'name'
        }

        self._address = None
        self._name = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if address is not None:
          self.address = address
        if name is not None:
          self.name = name

    @property
    def address(self):
        """
        Gets the address of this Location.
        The location's street address.

        :return: The address of this Location.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Location.
        The location's street address.

        :param address: The address of this Location.
        :type: str
        """

        self._address = address

    @property
    def name(self):
        """
        Gets the name of this Location.
        A name for the location.

        :return: The name of this Location.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Location.
        A name for the location.

        :param name: The name of this Location.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
