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


class UserUpdateBody(object):
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
        'signed_up_at': 'str',
        'profile': 'Profile',
        'metadata': 'object'
    }

    attribute_map = {
        'signed_up_at': 'signedUpAt',
        'profile': 'profile',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, signed_up_at=None, profile=None, metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """UserUpdateBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._signed_up_at = None
        self._profile = None
        self._metadata = None
        self.discriminator = None

        if signed_up_at is not None:
            self.signed_up_at = signed_up_at
        if profile is not None:
            self.profile = profile
        self.metadata = metadata

    @property
    def signed_up_at(self):
        """Gets the signed_up_at of this UserUpdateBody.  # noqa: E501


        :return: The signed_up_at of this UserUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._signed_up_at

    @signed_up_at.setter
    def signed_up_at(self, signed_up_at):
        """Sets the signed_up_at of this UserUpdateBody.


        :param signed_up_at: The signed_up_at of this UserUpdateBody.  # noqa: E501
        :type: str
        """

        self._signed_up_at = signed_up_at

    @property
    def profile(self):
        """Gets the profile of this UserUpdateBody.  # noqa: E501


        :return: The profile of this UserUpdateBody.  # noqa: E501
        :rtype: Profile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this UserUpdateBody.


        :param profile: The profile of this UserUpdateBody.  # noqa: E501
        :type: Profile
        """

        self._profile = profile

    @property
    def metadata(self):
        """Gets the metadata of this UserUpdateBody.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this UserUpdateBody.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UserUpdateBody.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this UserUpdateBody.  # noqa: E501
        :type: object
        """
        if type(metadata) is Undefined:
            metadata = None
            self.nulls.discard("metadata")
        elif metadata is None:
            self.nulls.add("metadata")
        else:
            self.nulls.discard("metadata")

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
        if not isinstance(other, UserUpdateBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserUpdateBody):
            return True

        return self.to_dict() != other.to_dict()
