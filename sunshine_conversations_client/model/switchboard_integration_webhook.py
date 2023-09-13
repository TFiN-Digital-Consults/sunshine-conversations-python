# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 10.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class SwitchboardIntegrationWebhook(object):
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
        'id': 'str',
        'name': 'str',
        'integration_id': 'str',
        'integration_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'integration_id': 'integrationId',
        'integration_type': 'integrationType'
    }

    nulls = set()

    def __init__(self, id=None, name=None, integration_id=None, integration_type=None, local_vars_configuration=None):  # noqa: E501
        """SwitchboardIntegrationWebhook - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._integration_id = None
        self._integration_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if integration_id is not None:
            self.integration_id = integration_id
        if integration_type is not None:
            self.integration_type = integration_type

    @property
    def id(self):
        """Gets the id of this SwitchboardIntegrationWebhook.  # noqa: E501

        The unique ID of the switchboard integration.  # noqa: E501

        :return: The id of this SwitchboardIntegrationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SwitchboardIntegrationWebhook.

        The unique ID of the switchboard integration.  # noqa: E501

        :param id: The id of this SwitchboardIntegrationWebhook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SwitchboardIntegrationWebhook.  # noqa: E501

        Identifier for use in control transfer protocols. Restricted to alphanumeric characters, `-` and `_`.  # noqa: E501

        :return: The name of this SwitchboardIntegrationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SwitchboardIntegrationWebhook.

        Identifier for use in control transfer protocols. Restricted to alphanumeric characters, `-` and `_`.  # noqa: E501

        :param name: The name of this SwitchboardIntegrationWebhook.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501

        self._name = name

    @property
    def integration_id(self):
        """Gets the integration_id of this SwitchboardIntegrationWebhook.  # noqa: E501

        Id of the integration that should deliver events routed by the switchboard.  # noqa: E501

        :return: The integration_id of this SwitchboardIntegrationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this SwitchboardIntegrationWebhook.

        Id of the integration that should deliver events routed by the switchboard.  # noqa: E501

        :param integration_id: The integration_id of this SwitchboardIntegrationWebhook.  # noqa: E501
        :type: str
        """

        self._integration_id = integration_id

    @property
    def integration_type(self):
        """Gets the integration_type of this SwitchboardIntegrationWebhook.  # noqa: E501

        Type of integration that should deliver events routed by the switchboard. If referencing an OAuth integration, the clientId issued by Sunshine Conversations during the OAuth partnership process will be the value of integrationType.  # noqa: E501

        :return: The integration_type of this SwitchboardIntegrationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this SwitchboardIntegrationWebhook.

        Type of integration that should deliver events routed by the switchboard. If referencing an OAuth integration, the clientId issued by Sunshine Conversations during the OAuth partnership process will be the value of integrationType.  # noqa: E501

        :param integration_type: The integration_type of this SwitchboardIntegrationWebhook.  # noqa: E501
        :type: str
        """

        self._integration_type = integration_type

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
        if not isinstance(other, SwitchboardIntegrationWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SwitchboardIntegrationWebhook):
            return True

        return self.to_dict() != other.to_dict()
