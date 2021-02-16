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


class ConversationMessageDeliveryPayload(object):
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
        'user': 'User',
        'conversation': 'ConversationTruncated',
        'message': 'ConversationMessageDeliveryPayloadMessage',
        'destination': 'ConversationMessageDeliveryPayloadDestination',
        'external_messages': 'list[ConversationMessageDeliveryPayloadExternalMessages]',
        'is_final_event': 'bool'
    }

    attribute_map = {
        'user': 'user',
        'conversation': 'conversation',
        'message': 'message',
        'destination': 'destination',
        'external_messages': 'externalMessages',
        'is_final_event': 'isFinalEvent'
    }

    nulls = set()

    def __init__(self, user=None, conversation=None, message=None, destination=None, external_messages=Undefined(), is_final_event=None, local_vars_configuration=None):  # noqa: E501
        """ConversationMessageDeliveryPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._conversation = None
        self._message = None
        self._destination = None
        self._external_messages = None
        self._is_final_event = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if conversation is not None:
            self.conversation = conversation
        if message is not None:
            self.message = message
        if destination is not None:
            self.destination = destination
        self.external_messages = external_messages
        if is_final_event is not None:
            self.is_final_event = is_final_event

    @property
    def user(self):
        """Gets the user of this ConversationMessageDeliveryPayload.  # noqa: E501

        The user associated with the conversation.  # noqa: E501

        :return: The user of this ConversationMessageDeliveryPayload.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ConversationMessageDeliveryPayload.

        The user associated with the conversation.  # noqa: E501

        :param user: The user of this ConversationMessageDeliveryPayload.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def conversation(self):
        """Gets the conversation of this ConversationMessageDeliveryPayload.  # noqa: E501

        The conversation in which the message was sent.  # noqa: E501

        :return: The conversation of this ConversationMessageDeliveryPayload.  # noqa: E501
        :rtype: ConversationTruncated
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this ConversationMessageDeliveryPayload.

        The conversation in which the message was sent.  # noqa: E501

        :param conversation: The conversation of this ConversationMessageDeliveryPayload.  # noqa: E501
        :type: ConversationTruncated
        """

        self._conversation = conversation

    @property
    def message(self):
        """Gets the message of this ConversationMessageDeliveryPayload.  # noqa: E501


        :return: The message of this ConversationMessageDeliveryPayload.  # noqa: E501
        :rtype: ConversationMessageDeliveryPayloadMessage
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ConversationMessageDeliveryPayload.


        :param message: The message of this ConversationMessageDeliveryPayload.  # noqa: E501
        :type: ConversationMessageDeliveryPayloadMessage
        """

        self._message = message

    @property
    def destination(self):
        """Gets the destination of this ConversationMessageDeliveryPayload.  # noqa: E501


        :return: The destination of this ConversationMessageDeliveryPayload.  # noqa: E501
        :rtype: ConversationMessageDeliveryPayloadDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ConversationMessageDeliveryPayload.


        :param destination: The destination of this ConversationMessageDeliveryPayload.  # noqa: E501
        :type: ConversationMessageDeliveryPayloadDestination
        """

        self._destination = destination

    @property
    def external_messages(self):
        """Gets the external_messages of this ConversationMessageDeliveryPayload.  # noqa: E501

        An array of objects representing the third-party messages associated with the event. The order of the external messages is not guaranteed to be the same across the different triggers. Note that some channels don’t expose message IDs, in which case this field will be unset.  # noqa: E501

        :return: The external_messages of this ConversationMessageDeliveryPayload.  # noqa: E501
        :rtype: list[ConversationMessageDeliveryPayloadExternalMessages]
        """
        return self._external_messages

    @external_messages.setter
    def external_messages(self, external_messages):
        """Sets the external_messages of this ConversationMessageDeliveryPayload.

        An array of objects representing the third-party messages associated with the event. The order of the external messages is not guaranteed to be the same across the different triggers. Note that some channels don’t expose message IDs, in which case this field will be unset.  # noqa: E501

        :param external_messages: The external_messages of this ConversationMessageDeliveryPayload.  # noqa: E501
        :type: list[ConversationMessageDeliveryPayloadExternalMessages]
        """
        if type(external_messages) is Undefined:
            external_messages = None
            self.nulls.discard("external_messages")
        elif external_messages is None:
            self.nulls.add("external_messages")
        else:
            self.nulls.discard("external_messages")

        self._external_messages = external_messages

    @property
    def is_final_event(self):
        """Gets the is_final_event of this ConversationMessageDeliveryPayload.  # noqa: E501

        A boolean indicating whether the webhook is the final one for the `message.id` and `destination.type` pair.  # noqa: E501

        :return: The is_final_event of this ConversationMessageDeliveryPayload.  # noqa: E501
        :rtype: bool
        """
        return self._is_final_event

    @is_final_event.setter
    def is_final_event(self, is_final_event):
        """Sets the is_final_event of this ConversationMessageDeliveryPayload.

        A boolean indicating whether the webhook is the final one for the `message.id` and `destination.type` pair.  # noqa: E501

        :param is_final_event: The is_final_event of this ConversationMessageDeliveryPayload.  # noqa: E501
        :type: bool
        """

        self._is_final_event = is_final_event

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
        if not isinstance(other, ConversationMessageDeliveryPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationMessageDeliveryPayload):
            return True

        return self.to_dict() != other.to_dict()
