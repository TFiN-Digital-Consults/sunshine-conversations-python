# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class InstagramUpdate(object):
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
        'display_name': 'str',
        'page_access_token': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'page_access_token': 'pageAccessToken'
    }

    nulls = set()

    def __init__(self, display_name=Undefined(), page_access_token=None, local_vars_configuration=None):  # noqa: E501
        """InstagramUpdate - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._page_access_token = None
        self.discriminator = None

        self.display_name = display_name
        if page_access_token is not None:
            self.page_access_token = page_access_token

    @property
    def display_name(self):
        """Gets the display_name of this InstagramUpdate.  # noqa: E501

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :return: The display_name of this InstagramUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InstagramUpdate.

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :param display_name: The display_name of this InstagramUpdate.  # noqa: E501
        :type: str
        """
        if type(display_name) is Undefined:
            display_name = None
            self.nulls.discard("display_name")
        elif display_name is None:
            self.nulls.add("display_name")
        else:
            self.nulls.discard("display_name")
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 100):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def page_access_token(self):
        """Gets the page_access_token of this InstagramUpdate.  # noqa: E501

        A Facebook Page Access Token.  # noqa: E501

        :return: The page_access_token of this InstagramUpdate.  # noqa: E501
        :rtype: str
        """
        return self._page_access_token

    @page_access_token.setter
    def page_access_token(self, page_access_token):
        """Sets the page_access_token of this InstagramUpdate.

        A Facebook Page Access Token.  # noqa: E501

        :param page_access_token: The page_access_token of this InstagramUpdate.  # noqa: E501
        :type: str
        """

        self._page_access_token = page_access_token

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
        if not isinstance(other, InstagramUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstagramUpdate):
            return True

        return self.to_dict() != other.to_dict()
