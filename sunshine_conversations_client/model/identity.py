# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 10.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Identity(object):
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
        'type': 'str',
        'value': 'str',
        'verification': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'verification': 'verification'
    }

    nulls = set()

    def __init__(self, type=None, value=None, verification=None, local_vars_configuration=None):  # noqa: E501
        """Identity - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._value = None
        self._verification = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if verification is not None:
            self.verification = verification

    @property
    def type(self):
        """Gets the type of this Identity.  # noqa: E501

        The type of identity.  # noqa: E501

        :return: The type of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Identity.

        The type of identity.  # noqa: E501

        :param type: The type of this Identity.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this Identity.  # noqa: E501

        The identity value.  # noqa: E501

        :return: The value of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Identity.

        The identity value.  # noqa: E501

        :param value: The value of this Identity.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) > 128):
            raise ValueError("Invalid value for `value`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def verification(self):
        """Gets the verification of this Identity.  # noqa: E501

        The type of verification performed on the identity.  # noqa: E501

        :return: The verification of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        """Sets the verification of this Identity.

        The type of verification performed on the identity.  # noqa: E501

        :param verification: The verification of this Identity.  # noqa: E501
        :type: str
        """

        self._verification = verification

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
        if not isinstance(other, Identity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Identity):
            return True

        return self.to_dict() != other.to_dict()
