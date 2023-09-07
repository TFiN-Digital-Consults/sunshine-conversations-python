# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.15.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class TwilioAllOf(object):
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
        'account_sid': 'str',
        'auth_token': 'str',
        'phone_number_sid': 'str',
        'messaging_service_sid': 'str'
    }

    attribute_map = {
        'type': 'type',
        'account_sid': 'accountSid',
        'auth_token': 'authToken',
        'phone_number_sid': 'phoneNumberSid',
        'messaging_service_sid': 'messagingServiceSid'
    }

    nulls = set()

    def __init__(self, type='twilio', account_sid=None, auth_token=None, phone_number_sid=None, messaging_service_sid=None, local_vars_configuration=None):  # noqa: E501
        """TwilioAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._account_sid = None
        self._auth_token = None
        self._phone_number_sid = None
        self._messaging_service_sid = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.account_sid = account_sid
        if auth_token is not None:
            self.auth_token = auth_token
        if phone_number_sid is not None:
            self.phone_number_sid = phone_number_sid
        if messaging_service_sid is not None:
            self.messaging_service_sid = messaging_service_sid

    @property
    def type(self):
        """Gets the type of this TwilioAllOf.  # noqa: E501

        To configure a Twilio integration, acquire the required information from the user and call the Create Integration endpoint.   # noqa: E501

        :return: The type of this TwilioAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TwilioAllOf.

        To configure a Twilio integration, acquire the required information from the user and call the Create Integration endpoint.   # noqa: E501

        :param type: The type of this TwilioAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def account_sid(self):
        """Gets the account_sid of this TwilioAllOf.  # noqa: E501

        Twilio Account SID.  # noqa: E501

        :return: The account_sid of this TwilioAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_sid

    @account_sid.setter
    def account_sid(self, account_sid):
        """Sets the account_sid of this TwilioAllOf.

        Twilio Account SID.  # noqa: E501

        :param account_sid: The account_sid of this TwilioAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_sid is None:  # noqa: E501
            raise ValueError("Invalid value for `account_sid`, must not be `None`")  # noqa: E501

        self._account_sid = account_sid

    @property
    def auth_token(self):
        """Gets the auth_token of this TwilioAllOf.  # noqa: E501

        Twilio Auth Token.  # noqa: E501

        :return: The auth_token of this TwilioAllOf.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this TwilioAllOf.

        Twilio Auth Token.  # noqa: E501

        :param auth_token: The auth_token of this TwilioAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and auth_token is None:  # noqa: E501
            raise ValueError("Invalid value for `auth_token`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                auth_token is not None and len(auth_token) < 1):
            raise ValueError("Invalid value for `auth_token`, length must be greater than or equal to `1`")  # noqa: E501

        self._auth_token = auth_token

    @property
    def phone_number_sid(self):
        """Gets the phone_number_sid of this TwilioAllOf.  # noqa: E501

        SID for specific phone number. One of `messagingServiceSid` or `phoneNumberSid` must be provided when creating a Twilio integration.  # noqa: E501

        :return: The phone_number_sid of this TwilioAllOf.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_sid

    @phone_number_sid.setter
    def phone_number_sid(self, phone_number_sid):
        """Sets the phone_number_sid of this TwilioAllOf.

        SID for specific phone number. One of `messagingServiceSid` or `phoneNumberSid` must be provided when creating a Twilio integration.  # noqa: E501

        :param phone_number_sid: The phone_number_sid of this TwilioAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone_number_sid is not None and len(phone_number_sid) < 1):
            raise ValueError("Invalid value for `phone_number_sid`, length must be greater than or equal to `1`")  # noqa: E501

        self._phone_number_sid = phone_number_sid

    @property
    def messaging_service_sid(self):
        """Gets the messaging_service_sid of this TwilioAllOf.  # noqa: E501

        SID for specific messaging service. One of `messagingServiceSid` or `phoneNumberSid` must be provided when creating a Twilio integration.  # noqa: E501

        :return: The messaging_service_sid of this TwilioAllOf.  # noqa: E501
        :rtype: str
        """
        return self._messaging_service_sid

    @messaging_service_sid.setter
    def messaging_service_sid(self, messaging_service_sid):
        """Sets the messaging_service_sid of this TwilioAllOf.

        SID for specific messaging service. One of `messagingServiceSid` or `phoneNumberSid` must be provided when creating a Twilio integration.  # noqa: E501

        :param messaging_service_sid: The messaging_service_sid of this TwilioAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                messaging_service_sid is not None and len(messaging_service_sid) < 1):
            raise ValueError("Invalid value for `messaging_service_sid`, length must be greater than or equal to `1`")  # noqa: E501

        self._messaging_service_sid = messaging_service_sid

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
        if not isinstance(other, TwilioAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TwilioAllOf):
            return True

        return self.to_dict() != other.to_dict()
