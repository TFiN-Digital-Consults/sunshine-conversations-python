# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class MessageOverride(object):
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
        'apple': 'MessageOverridePayload',
        'line': 'MessageOverridePayload',
        'messenger': 'MessageOverridePayload',
        'whatsapp': 'MessageOverridePayload'
    }

    attribute_map = {
        'apple': 'apple',
        'line': 'line',
        'messenger': 'messenger',
        'whatsapp': 'whatsapp'
    }

    nulls = set()

    def __init__(self, apple=None, line=None, messenger=None, whatsapp=None, local_vars_configuration=None):  # noqa: E501
        """MessageOverride - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._apple = None
        self._line = None
        self._messenger = None
        self._whatsapp = None
        self.discriminator = None

        if apple is not None:
            self.apple = apple
        if line is not None:
            self.line = line
        if messenger is not None:
            self.messenger = messenger
        if whatsapp is not None:
            self.whatsapp = whatsapp

    @property
    def apple(self):
        """Gets the apple of this MessageOverride.  # noqa: E501


        :return: The apple of this MessageOverride.  # noqa: E501
        :rtype: MessageOverridePayload
        """
        return self._apple

    @apple.setter
    def apple(self, apple):
        """Sets the apple of this MessageOverride.


        :param apple: The apple of this MessageOverride.  # noqa: E501
        :type: MessageOverridePayload
        """

        self._apple = apple

    @property
    def line(self):
        """Gets the line of this MessageOverride.  # noqa: E501


        :return: The line of this MessageOverride.  # noqa: E501
        :rtype: MessageOverridePayload
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this MessageOverride.


        :param line: The line of this MessageOverride.  # noqa: E501
        :type: MessageOverridePayload
        """

        self._line = line

    @property
    def messenger(self):
        """Gets the messenger of this MessageOverride.  # noqa: E501


        :return: The messenger of this MessageOverride.  # noqa: E501
        :rtype: MessageOverridePayload
        """
        return self._messenger

    @messenger.setter
    def messenger(self, messenger):
        """Sets the messenger of this MessageOverride.


        :param messenger: The messenger of this MessageOverride.  # noqa: E501
        :type: MessageOverridePayload
        """

        self._messenger = messenger

    @property
    def whatsapp(self):
        """Gets the whatsapp of this MessageOverride.  # noqa: E501


        :return: The whatsapp of this MessageOverride.  # noqa: E501
        :rtype: MessageOverridePayload
        """
        return self._whatsapp

    @whatsapp.setter
    def whatsapp(self, whatsapp):
        """Sets the whatsapp of this MessageOverride.


        :param whatsapp: The whatsapp of this MessageOverride.  # noqa: E501
        :type: MessageOverridePayload
        """

        self._whatsapp = whatsapp

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
        if not isinstance(other, MessageOverride):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageOverride):
            return True

        return self.to_dict() != other.to_dict()
