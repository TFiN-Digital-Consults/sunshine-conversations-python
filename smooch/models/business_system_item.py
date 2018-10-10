# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 3.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BusinessSystemItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, channel_id=None, ticket_id=None, room_id=None, conversation_id=None):
        """
        BusinessSystemItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'channel_id': 'str',
            'ticket_id': 'str',
            'room_id': 'int',
            'conversation_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'channel_id': 'channelId',
            'ticket_id': 'ticketId',
            'room_id': 'roomId',
            'conversation_id': 'conversationId'
        }

        self._type = None
        self._channel_id = None
        self._ticket_id = None
        self._room_id = None
        self._conversation_id = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if type is not None:
          self.type = type
        if channel_id is not None:
          self.channel_id = channel_id
        if ticket_id is not None:
          self.ticket_id = ticket_id
        if room_id is not None:
          self.room_id = room_id
        if conversation_id is not None:
          self.conversation_id = conversation_id

    @property
    def type(self):
        """
        Gets the type of this BusinessSystemItem.
        The type of business system (ex. slack, hipchat, zendesk etc...)

        :return: The type of this BusinessSystemItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BusinessSystemItem.
        The type of business system (ex. slack, hipchat, zendesk etc...)

        :param type: The type of this BusinessSystemItem.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def channel_id(self):
        """
        Gets the channel_id of this BusinessSystemItem.
        The channel id for a *slack* integration

        :return: The channel_id of this BusinessSystemItem.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """
        Sets the channel_id of this BusinessSystemItem.
        The channel id for a *slack* integration

        :param channel_id: The channel_id of this BusinessSystemItem.
        :type: str
        """

        self._channel_id = channel_id

    @property
    def ticket_id(self):
        """
        Gets the ticket_id of this BusinessSystemItem.
        The ticket id for a *zendesk* integration

        :return: The ticket_id of this BusinessSystemItem.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """
        Sets the ticket_id of this BusinessSystemItem.
        The ticket id for a *zendesk* integration

        :param ticket_id: The ticket_id of this BusinessSystemItem.
        :type: str
        """

        self._ticket_id = ticket_id

    @property
    def room_id(self):
        """
        Gets the room_id of this BusinessSystemItem.
        The room id for a *hipchat* integration

        :return: The room_id of this BusinessSystemItem.
        :rtype: int
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """
        Sets the room_id of this BusinessSystemItem.
        The room id for a *hipchat* integration

        :param room_id: The room_id of this BusinessSystemItem.
        :type: int
        """

        self._room_id = room_id

    @property
    def conversation_id(self):
        """
        Gets the conversation_id of this BusinessSystemItem.
        The conversation id for a *helpscout* integration

        :return: The conversation_id of this BusinessSystemItem.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """
        Sets the conversation_id of this BusinessSystemItem.
        The conversation id for a *helpscout* integration

        :param conversation_id: The conversation_id of this BusinessSystemItem.
        :type: str
        """

        self._conversation_id = conversation_id

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
        if not isinstance(other, BusinessSystemItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
