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


class AndroidAllOf(object):
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
        'server_key': 'str',
        'sender_id': 'str',
        'can_user_create_more_conversations': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'server_key': 'serverKey',
        'sender_id': 'senderId',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations'
    }

    nulls = set()

    def __init__(self, type='android', server_key=Undefined(), sender_id=Undefined(), can_user_create_more_conversations=None, local_vars_configuration=None):  # noqa: E501
        """AndroidAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._server_key = None
        self._sender_id = None
        self._can_user_create_more_conversations = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.server_key = server_key
        self.sender_id = sender_id
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def type(self):
        """Gets the type of this AndroidAllOf.  # noqa: E501

        To configure an android integration, first visit the [Firebase Console](https://console.firebase.google.com/). Copy the `serverKey` and `senderId` from the Cloud Messaging tab in the settings of your project and call the create integrations endpoint with this data. If you would like to continue using your legacy GCM `serverKey` you can also obtain it from the [Google Developer Console](https://console.developers.google.com/).   # noqa: E501

        :return: The type of this AndroidAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AndroidAllOf.

        To configure an android integration, first visit the [Firebase Console](https://console.firebase.google.com/). Copy the `serverKey` and `senderId` from the Cloud Messaging tab in the settings of your project and call the create integrations endpoint with this data. If you would like to continue using your legacy GCM `serverKey` you can also obtain it from the [Google Developer Console](https://console.developers.google.com/).   # noqa: E501

        :param type: The type of this AndroidAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def server_key(self):
        """Gets the server_key of this AndroidAllOf.  # noqa: E501

        Your server key from the fcm console.  # noqa: E501

        :return: The server_key of this AndroidAllOf.  # noqa: E501
        :rtype: str
        """
        return self._server_key

    @server_key.setter
    def server_key(self, server_key):
        """Sets the server_key of this AndroidAllOf.

        Your server key from the fcm console.  # noqa: E501

        :param server_key: The server_key of this AndroidAllOf.  # noqa: E501
        :type: str
        """
        if type(server_key) is Undefined:
            server_key = None
            self.nulls.discard("server_key")
        elif server_key is None:
            self.nulls.add("server_key")
        else:
            self.nulls.discard("server_key")
        if (self.local_vars_configuration.client_side_validation and
                server_key is not None and len(server_key) < 1):
            raise ValueError("Invalid value for `server_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._server_key = server_key

    @property
    def sender_id(self):
        """Gets the sender_id of this AndroidAllOf.  # noqa: E501

        Your sender id from the fcm console.  # noqa: E501

        :return: The sender_id of this AndroidAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this AndroidAllOf.

        Your sender id from the fcm console.  # noqa: E501

        :param sender_id: The sender_id of this AndroidAllOf.  # noqa: E501
        :type: str
        """
        if type(sender_id) is Undefined:
            sender_id = None
            self.nulls.discard("sender_id")
        elif sender_id is None:
            self.nulls.add("sender_id")
        else:
            self.nulls.discard("sender_id")
        if (self.local_vars_configuration.client_side_validation and
                sender_id is not None and len(sender_id) < 1):
            raise ValueError("Invalid value for `sender_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._sender_id = sender_id

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this AndroidAllOf.  # noqa: E501

        Allows users to create more than one conversation on the android integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this AndroidAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this AndroidAllOf.

        Allows users to create more than one conversation on the android integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this AndroidAllOf.  # noqa: E501
        :type: bool
        """

        self._can_user_create_more_conversations = can_user_create_more_conversations

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
        if not isinstance(other, AndroidAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidAllOf):
            return True

        return self.to_dict() != other.to_dict()
