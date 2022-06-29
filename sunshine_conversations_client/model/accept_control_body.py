# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.8.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class AcceptControlBody(object):
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
        'metadata': 'object'
    }

    attribute_map = {
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, metadata=None, local_vars_configuration=None):  # noqa: E501
        """AcceptControlBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metadata = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata

    @property
    def metadata(self):
        """Gets the metadata of this AcceptControlBody.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size. The metadata object will be included in the `switchboard:acceptControl` and `switchboard:acceptControl:failure` webhooks.  # noqa: E501

        :return: The metadata of this AcceptControlBody.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AcceptControlBody.

        Flat object containing custom properties. Strings, numbers and booleans are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size. The metadata object will be included in the `switchboard:acceptControl` and `switchboard:acceptControl:failure` webhooks.  # noqa: E501

        :param metadata: The metadata of this AcceptControlBody.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

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
        if not isinstance(other, AcceptControlBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AcceptControlBody):
            return True

        return self.to_dict() != other.to_dict()
