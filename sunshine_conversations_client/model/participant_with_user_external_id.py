# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ParticipantWithUserExternalId(object):
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
        'user_external_id': 'str',
        'subscribe_sdk_client': 'bool'
    }

    attribute_map = {
        'user_external_id': 'userExternalId',
        'subscribe_sdk_client': 'subscribeSDKClient'
    }

    nulls = set()

    def __init__(self, user_external_id=None, subscribe_sdk_client=None, local_vars_configuration=None):  # noqa: E501
        """ParticipantWithUserExternalId - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_external_id = None
        self._subscribe_sdk_client = None
        self.discriminator = None

        if user_external_id is not None:
            self.user_external_id = user_external_id
        if subscribe_sdk_client is not None:
            self.subscribe_sdk_client = subscribe_sdk_client

    @property
    def user_external_id(self):
        """Gets the user_external_id of this ParticipantWithUserExternalId.  # noqa: E501

        The `externalId` of the user that will be participating in the conversation. It will return `404` if the user can’t be found. One of `userId` or `userExternalId` is required, but not both.  # noqa: E501

        :return: The user_external_id of this ParticipantWithUserExternalId.  # noqa: E501
        :rtype: str
        """
        return self._user_external_id

    @user_external_id.setter
    def user_external_id(self, user_external_id):
        """Sets the user_external_id of this ParticipantWithUserExternalId.

        The `externalId` of the user that will be participating in the conversation. It will return `404` if the user can’t be found. One of `userId` or `userExternalId` is required, but not both.  # noqa: E501

        :param user_external_id: The user_external_id of this ParticipantWithUserExternalId.  # noqa: E501
        :type: str
        """

        self._user_external_id = user_external_id

    @property
    def subscribe_sdk_client(self):
        """Gets the subscribe_sdk_client of this ParticipantWithUserExternalId.  # noqa: E501

        When passed as true, the SDK client of the concerned participant will be subscribed to the conversation. The user will start receiving push notifications for this conversation right away, without having to view the conversation on the SDK beforehand. An SDK client will be created for users that don’t already have one. This field is required if the conversation is of type `sdkGroup`.  # noqa: E501

        :return: The subscribe_sdk_client of this ParticipantWithUserExternalId.  # noqa: E501
        :rtype: bool
        """
        return self._subscribe_sdk_client

    @subscribe_sdk_client.setter
    def subscribe_sdk_client(self, subscribe_sdk_client):
        """Sets the subscribe_sdk_client of this ParticipantWithUserExternalId.

        When passed as true, the SDK client of the concerned participant will be subscribed to the conversation. The user will start receiving push notifications for this conversation right away, without having to view the conversation on the SDK beforehand. An SDK client will be created for users that don’t already have one. This field is required if the conversation is of type `sdkGroup`.  # noqa: E501

        :param subscribe_sdk_client: The subscribe_sdk_client of this ParticipantWithUserExternalId.  # noqa: E501
        :type: bool
        """

        self._subscribe_sdk_client = subscribe_sdk_client

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
        if not isinstance(other, ParticipantWithUserExternalId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParticipantWithUserExternalId):
            return True

        return self.to_dict() != other.to_dict()
