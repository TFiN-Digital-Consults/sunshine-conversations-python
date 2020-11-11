# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class MessagebirdAllOf(object):
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
        'access_key': 'str',
        'signing_key': 'str',
        'originator': 'str',
        'webhook_secret': 'str'
    }

    attribute_map = {
        'type': 'type',
        'access_key': 'accessKey',
        'signing_key': 'signingKey',
        'originator': 'originator',
        'webhook_secret': 'webhookSecret'
    }

    nulls = set()

    def __init__(self, type='messagebird', access_key=None, signing_key=None, originator=None, webhook_secret=None, local_vars_configuration=None):  # noqa: E501
        """MessagebirdAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._access_key = None
        self._signing_key = None
        self._originator = None
        self._webhook_secret = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if access_key is not None:
            self.access_key = access_key
        if signing_key is not None:
            self.signing_key = signing_key
        self.originator = originator
        if webhook_secret is not None:
            self.webhook_secret = webhook_secret

    @property
    def type(self):
        """Gets the type of this MessagebirdAllOf.  # noqa: E501

        The type of integration.  # noqa: E501

        :return: The type of this MessagebirdAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MessagebirdAllOf.

        The type of integration.  # noqa: E501

        :param type: The type of this MessagebirdAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def access_key(self):
        """Gets the access_key of this MessagebirdAllOf.  # noqa: E501

        The public API key of your MessageBird account.  # noqa: E501

        :return: The access_key of this MessagebirdAllOf.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this MessagebirdAllOf.

        The public API key of your MessageBird account.  # noqa: E501

        :param access_key: The access_key of this MessagebirdAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `access_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                access_key is not None and len(access_key) < 1):
            raise ValueError("Invalid value for `access_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._access_key = access_key

    @property
    def signing_key(self):
        """Gets the signing_key of this MessagebirdAllOf.  # noqa: E501

        The signing key of your MessageBird account. Used to validate the webhooks' origin.  # noqa: E501

        :return: The signing_key of this MessagebirdAllOf.  # noqa: E501
        :rtype: str
        """
        return self._signing_key

    @signing_key.setter
    def signing_key(self, signing_key):
        """Sets the signing_key of this MessagebirdAllOf.

        The signing key of your MessageBird account. Used to validate the webhooks' origin.  # noqa: E501

        :param signing_key: The signing_key of this MessagebirdAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signing_key is None:  # noqa: E501
            raise ValueError("Invalid value for `signing_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                signing_key is not None and len(signing_key) < 1):
            raise ValueError("Invalid value for `signing_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._signing_key = signing_key

    @property
    def originator(self):
        """Gets the originator of this MessagebirdAllOf.  # noqa: E501

        Sunshine Conversations will receive all messages sent to this phone number.  # noqa: E501

        :return: The originator of this MessagebirdAllOf.  # noqa: E501
        :rtype: str
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this MessagebirdAllOf.

        Sunshine Conversations will receive all messages sent to this phone number.  # noqa: E501

        :param originator: The originator of this MessagebirdAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and originator is None:  # noqa: E501
            raise ValueError("Invalid value for `originator`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                originator is not None and len(originator) < 1):
            raise ValueError("Invalid value for `originator`, length must be greater than or equal to `1`")  # noqa: E501

        self._originator = originator

    @property
    def webhook_secret(self):
        """Gets the webhook_secret of this MessagebirdAllOf.  # noqa: E501

        The secret that is used to configure webhooks in MessageBird.  # noqa: E501

        :return: The webhook_secret of this MessagebirdAllOf.  # noqa: E501
        :rtype: str
        """
        return self._webhook_secret

    @webhook_secret.setter
    def webhook_secret(self, webhook_secret):
        """Sets the webhook_secret of this MessagebirdAllOf.

        The secret that is used to configure webhooks in MessageBird.  # noqa: E501

        :param webhook_secret: The webhook_secret of this MessagebirdAllOf.  # noqa: E501
        :type: str
        """

        self._webhook_secret = webhook_secret

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
        if not isinstance(other, MessagebirdAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessagebirdAllOf):
            return True

        return self.to_dict() != other.to_dict()
