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


class WebhookBody(object):
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
        'target': 'str',
        'triggers': 'list[str]',
        'include_full_user': 'bool',
        'include_full_source': 'bool'
    }

    attribute_map = {
        'target': 'target',
        'triggers': 'triggers',
        'include_full_user': 'includeFullUser',
        'include_full_source': 'includeFullSource'
    }

    nulls = set()

    def __init__(self, target=None, triggers=None, include_full_user=False, include_full_source=False, local_vars_configuration=None):  # noqa: E501
        """WebhookBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target = None
        self._triggers = None
        self._include_full_user = None
        self._include_full_source = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if triggers is not None:
            self.triggers = triggers
        if include_full_user is not None:
            self.include_full_user = include_full_user
        if include_full_source is not None:
            self.include_full_source = include_full_source

    @property
    def target(self):
        """Gets the target of this WebhookBody.  # noqa: E501

        URL to be called when the webhook is triggered.  # noqa: E501

        :return: The target of this WebhookBody.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this WebhookBody.

        URL to be called when the webhook is triggered.  # noqa: E501

        :param target: The target of this WebhookBody.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def triggers(self):
        """Gets the triggers of this WebhookBody.  # noqa: E501

        An array of triggers the integration is subscribed to. This property is case sensitive. [More details](https://docs.smooch.io/rest/#section/Webhook-Triggers).  # noqa: E501

        :return: The triggers of this WebhookBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this WebhookBody.

        An array of triggers the integration is subscribed to. This property is case sensitive. [More details](https://docs.smooch.io/rest/#section/Webhook-Triggers).  # noqa: E501

        :param triggers: The triggers of this WebhookBody.  # noqa: E501
        :type: list[str]
        """

        self._triggers = triggers

    @property
    def include_full_user(self):
        """Gets the include_full_user of this WebhookBody.  # noqa: E501

        A boolean specifying whether webhook payloads should include the complete user schema for events involving a specific user.  # noqa: E501

        :return: The include_full_user of this WebhookBody.  # noqa: E501
        :rtype: bool
        """
        return self._include_full_user

    @include_full_user.setter
    def include_full_user(self, include_full_user):
        """Sets the include_full_user of this WebhookBody.

        A boolean specifying whether webhook payloads should include the complete user schema for events involving a specific user.  # noqa: E501

        :param include_full_user: The include_full_user of this WebhookBody.  # noqa: E501
        :type: bool
        """

        self._include_full_user = include_full_user

    @property
    def include_full_source(self):
        """Gets the include_full_source of this WebhookBody.  # noqa: E501

        A boolean specifying whether webhook payloads should include the client and device object (when applicable).  # noqa: E501

        :return: The include_full_source of this WebhookBody.  # noqa: E501
        :rtype: bool
        """
        return self._include_full_source

    @include_full_source.setter
    def include_full_source(self, include_full_source):
        """Sets the include_full_source of this WebhookBody.

        A boolean specifying whether webhook payloads should include the client and device object (when applicable).  # noqa: E501

        :param include_full_source: The include_full_source of this WebhookBody.  # noqa: E501
        :type: bool
        """

        self._include_full_source = include_full_source

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
        if not isinstance(other, WebhookBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookBody):
            return True

        return self.to_dict() != other.to_dict()
