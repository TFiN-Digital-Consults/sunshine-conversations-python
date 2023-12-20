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


class TextMessage(object):
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
        'text': 'str',
        'actions': 'list[Action]',
        'payload': 'str'
    }

    attribute_map = {
        'type': 'type',
        'text': 'text',
        'actions': 'actions',
        'payload': 'payload'
    }

    nulls = set()

    def __init__(self, type='text', text=None, actions=None, payload=None, local_vars_configuration=None):  # noqa: E501
        """TextMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._text = None
        self._actions = None
        self._payload = None
        self.discriminator = None

        self.type = type
        if text is not None:
            self.text = text
        if actions is not None:
            self.actions = actions
        if payload is not None:
            self.payload = payload

    @property
    def type(self):
        """Gets the type of this TextMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this TextMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TextMessage.

        The type of message.  # noqa: E501

        :param type: The type of this TextMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def text(self):
        """Gets the text of this TextMessage.  # noqa: E501

        The text content of the message. Optional only if actions are provided.  # noqa: E501

        :return: The text of this TextMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextMessage.

        The text content of the message. Optional only if actions are provided.  # noqa: E501

        :param text: The text of this TextMessage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                text is not None and len(text) > 4096):
            raise ValueError("Invalid value for `text`, length must be less than or equal to `4096`")  # noqa: E501

        self._text = text

    @property
    def actions(self):
        """Gets the actions of this TextMessage.  # noqa: E501

        Array of message actions.  # noqa: E501

        :return: The actions of this TextMessage.  # noqa: E501
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this TextMessage.

        Array of message actions.  # noqa: E501

        :param actions: The actions of this TextMessage.  # noqa: E501
        :type: list[Action]
        """

        self._actions = actions

    @property
    def payload(self):
        """Gets the payload of this TextMessage.  # noqa: E501

        The payload of a [reply button](https://docs.smooch.io/guide/structured-messages/#reply-buttons) response message.  # noqa: E501

        :return: The payload of this TextMessage.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this TextMessage.

        The payload of a [reply button](https://docs.smooch.io/guide/structured-messages/#reply-buttons) response message.  # noqa: E501

        :param payload: The payload of this TextMessage.  # noqa: E501
        :type: str
        """

        self._payload = payload

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
        if not isinstance(other, TextMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextMessage):
            return True

        return self.to_dict() != other.to_dict()
