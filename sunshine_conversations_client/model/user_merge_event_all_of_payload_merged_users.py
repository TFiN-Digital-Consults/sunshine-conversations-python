# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class UserMergeEventAllOfPayloadMergedUsers(object):
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
        'surviving': 'User',
        'discarded': 'User'
    }

    attribute_map = {
        'surviving': 'surviving',
        'discarded': 'discarded'
    }

    nulls = set()

    def __init__(self, surviving=None, discarded=None, local_vars_configuration=None):  # noqa: E501
        """UserMergeEventAllOfPayloadMergedUsers - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._surviving = None
        self._discarded = None
        self.discriminator = None

        if surviving is not None:
            self.surviving = surviving
        if discarded is not None:
            self.discarded = discarded

    @property
    def surviving(self):
        """Gets the surviving of this UserMergeEventAllOfPayloadMergedUsers.  # noqa: E501

        The user that now represents the merged user object.  # noqa: E501

        :return: The surviving of this UserMergeEventAllOfPayloadMergedUsers.  # noqa: E501
        :rtype: User
        """
        return self._surviving

    @surviving.setter
    def surviving(self, surviving):
        """Sets the surviving of this UserMergeEventAllOfPayloadMergedUsers.

        The user that now represents the merged user object.  # noqa: E501

        :param surviving: The surviving of this UserMergeEventAllOfPayloadMergedUsers.  # noqa: E501
        :type: User
        """

        self._surviving = surviving

    @property
    def discarded(self):
        """Gets the discarded of this UserMergeEventAllOfPayloadMergedUsers.  # noqa: E501

        The user that was unified into the surviving user object.  # noqa: E501

        :return: The discarded of this UserMergeEventAllOfPayloadMergedUsers.  # noqa: E501
        :rtype: User
        """
        return self._discarded

    @discarded.setter
    def discarded(self, discarded):
        """Sets the discarded of this UserMergeEventAllOfPayloadMergedUsers.

        The user that was unified into the surviving user object.  # noqa: E501

        :param discarded: The discarded of this UserMergeEventAllOfPayloadMergedUsers.  # noqa: E501
        :type: User
        """

        self._discarded = discarded

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
        if not isinstance(other, UserMergeEventAllOfPayloadMergedUsers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserMergeEventAllOfPayloadMergedUsers):
            return True

        return self.to_dict() != other.to_dict()