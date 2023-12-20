# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class IntegrationType(object):
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
        'integration_type': 'str'
    }

    attribute_map = {
        'integration_type': 'integrationType'
    }

    nulls = set()

    def __init__(self, integration_type=None, local_vars_configuration=None):  # noqa: E501
        """IntegrationType - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._integration_type = None
        self.discriminator = None

        if integration_type is not None:
            self.integration_type = integration_type

    @property
    def integration_type(self):
        """Gets the integration_type of this IntegrationType.  # noqa: E501

        The type of the integration to deliver the message to. Can be set to `none` if sending a [silent message](https://docs.smooch.io/guide/sending-messages/#silent-messages). Will return an error if the user does not have a client of that type attached to the conversation.   # noqa: E501

        :return: The integration_type of this IntegrationType.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this IntegrationType.

        The type of the integration to deliver the message to. Can be set to `none` if sending a [silent message](https://docs.smooch.io/guide/sending-messages/#silent-messages). Will return an error if the user does not have a client of that type attached to the conversation.   # noqa: E501

        :param integration_type: The integration_type of this IntegrationType.  # noqa: E501
        :type: str
        """

        self._integration_type = integration_type

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
        if not isinstance(other, IntegrationType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationType):
            return True

        return self.to_dict() != other.to_dict()
