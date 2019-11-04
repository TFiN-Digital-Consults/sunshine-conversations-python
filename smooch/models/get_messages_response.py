# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetMessagesResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, conversation=None, messages=None, next=None):
        """
        GetMessagesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'conversation': 'Conversation',
            'messages': 'list[Message]',
            'next': 'str'
        }

        self.attribute_map = {
            'conversation': 'conversation',
            'messages': 'messages',
            'next': 'next'
        }

        self._conversation = None
        self._messages = None
        self._next = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if conversation is not None:
          self.conversation = conversation
        if messages is not None:
          self.messages = messages
        if next is not None:
          self.next = next

    @property
    def conversation(self):
        """
        Gets the conversation of this GetMessagesResponse.
        The conversation.

        :return: The conversation of this GetMessagesResponse.
        :rtype: Conversation
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """
        Sets the conversation of this GetMessagesResponse.
        The conversation.

        :param conversation: The conversation of this GetMessagesResponse.
        :type: Conversation
        """

        self._conversation = conversation

    @property
    def messages(self):
        """
        Gets the messages of this GetMessagesResponse.
        The messages.

        :return: The messages of this GetMessagesResponse.
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this GetMessagesResponse.
        The messages.

        :param messages: The messages of this GetMessagesResponse.
        :type: list[Message]
        """

        self._messages = messages

    @property
    def next(self):
        """
        Gets the next of this GetMessagesResponse.
        The URI for the next set of messages in the conversation.

        :return: The next of this GetMessagesResponse.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this GetMessagesResponse.
        The URI for the next set of messages in the conversation.

        :param next: The next of this GetMessagesResponse.
        :type: str
        """

        self._next = next

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
