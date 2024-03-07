# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.3.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ExtraChannelOptionsMessenger(object):
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
        'messenger_extensions': 'bool',
        'webview_share_button': 'str'
    }

    attribute_map = {
        'messenger_extensions': 'messenger_extensions',
        'webview_share_button': 'webview_share_button'
    }

    nulls = set()

    def __init__(self, messenger_extensions=False, webview_share_button=None, local_vars_configuration=None):  # noqa: E501
        """ExtraChannelOptionsMessenger - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._messenger_extensions = None
        self._webview_share_button = None
        self.discriminator = None

        if messenger_extensions is not None:
            self.messenger_extensions = messenger_extensions
        if webview_share_button is not None:
            self.webview_share_button = webview_share_button

    @property
    def messenger_extensions(self):
        """Gets the messenger_extensions of this ExtraChannelOptionsMessenger.  # noqa: E501

        For webview type actions, a boolean value indicating whether the URL should be loaded with Messenger Extensions enabled. [More info](https://developers.facebook.com/docs/messenger-platform/send-api-reference/url-button).  # noqa: E501

        :return: The messenger_extensions of this ExtraChannelOptionsMessenger.  # noqa: E501
        :rtype: bool
        """
        return self._messenger_extensions

    @messenger_extensions.setter
    def messenger_extensions(self, messenger_extensions):
        """Sets the messenger_extensions of this ExtraChannelOptionsMessenger.

        For webview type actions, a boolean value indicating whether the URL should be loaded with Messenger Extensions enabled. [More info](https://developers.facebook.com/docs/messenger-platform/send-api-reference/url-button).  # noqa: E501

        :param messenger_extensions: The messenger_extensions of this ExtraChannelOptionsMessenger.  # noqa: E501
        :type: bool
        """

        self._messenger_extensions = messenger_extensions

    @property
    def webview_share_button(self):
        """Gets the webview_share_button of this ExtraChannelOptionsMessenger.  # noqa: E501

        For webview type actions, a string value indicating if the share button should be hidden. [More Info](https://developers.facebook.com/docs/messenger-platform/reference/buttons/url).  # noqa: E501

        :return: The webview_share_button of this ExtraChannelOptionsMessenger.  # noqa: E501
        :rtype: str
        """
        return self._webview_share_button

    @webview_share_button.setter
    def webview_share_button(self, webview_share_button):
        """Sets the webview_share_button of this ExtraChannelOptionsMessenger.

        For webview type actions, a string value indicating if the share button should be hidden. [More Info](https://developers.facebook.com/docs/messenger-platform/reference/buttons/url).  # noqa: E501

        :param webview_share_button: The webview_share_button of this ExtraChannelOptionsMessenger.  # noqa: E501
        :type: str
        """
        allowed_values = ["hide"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and webview_share_button not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `webview_share_button` ({0}), must be one of {1}"  # noqa: E501
                .format(webview_share_button, allowed_values)
            )

        self._webview_share_button = webview_share_button

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
        if not isinstance(other, ExtraChannelOptionsMessenger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtraChannelOptionsMessenger):
            return True

        return self.to_dict() != other.to_dict()
