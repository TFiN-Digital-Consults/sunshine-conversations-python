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


class Meta(object):
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
        'has_more': 'bool',
        'after_cursor': 'str',
        'before_cursor': 'str'
    }

    attribute_map = {
        'has_more': 'hasMore',
        'after_cursor': 'afterCursor',
        'before_cursor': 'beforeCursor'
    }

    nulls = set()

    def __init__(self, has_more=None, after_cursor=None, before_cursor=None, local_vars_configuration=None):  # noqa: E501
        """Meta - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._has_more = None
        self._after_cursor = None
        self._before_cursor = None
        self.discriminator = None

        if has_more is not None:
            self.has_more = has_more
        if after_cursor is not None:
            self.after_cursor = after_cursor
        if before_cursor is not None:
            self.before_cursor = before_cursor

    @property
    def has_more(self):
        """Gets the has_more of this Meta.  # noqa: E501

        A flag that indicates if there are more records that can be fetched.  # noqa: E501

        :return: The has_more of this Meta.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this Meta.

        A flag that indicates if there are more records that can be fetched.  # noqa: E501

        :param has_more: The has_more of this Meta.  # noqa: E501
        :type: bool
        """

        self._has_more = has_more

    @property
    def after_cursor(self):
        """Gets the after_cursor of this Meta.  # noqa: E501

        A record id that can be used as a `page[after]` parameter in a new request to get the next page.  Not specified if there are no subsequent pages.   # noqa: E501

        :return: The after_cursor of this Meta.  # noqa: E501
        :rtype: str
        """
        return self._after_cursor

    @after_cursor.setter
    def after_cursor(self, after_cursor):
        """Sets the after_cursor of this Meta.

        A record id that can be used as a `page[after]` parameter in a new request to get the next page.  Not specified if there are no subsequent pages.   # noqa: E501

        :param after_cursor: The after_cursor of this Meta.  # noqa: E501
        :type: str
        """

        self._after_cursor = after_cursor

    @property
    def before_cursor(self):
        """Gets the before_cursor of this Meta.  # noqa: E501

        A record id that can be used as a `page[before]` parameter in a new request to get the previous page.  Not specified if there are no previous pages.   # noqa: E501

        :return: The before_cursor of this Meta.  # noqa: E501
        :rtype: str
        """
        return self._before_cursor

    @before_cursor.setter
    def before_cursor(self, before_cursor):
        """Sets the before_cursor of this Meta.

        A record id that can be used as a `page[before]` parameter in a new request to get the previous page.  Not specified if there are no previous pages.   # noqa: E501

        :param before_cursor: The before_cursor of this Meta.  # noqa: E501
        :type: str
        """

        self._before_cursor = before_cursor

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
        if not isinstance(other, Meta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Meta):
            return True

        return self.to_dict() != other.to_dict()
