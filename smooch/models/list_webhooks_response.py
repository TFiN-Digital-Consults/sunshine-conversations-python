# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ListWebhooksResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, webhooks=None):
        """
        ListWebhooksResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'webhooks': 'list[Webhook]'
        }

        self.attribute_map = {
            'webhooks': 'webhooks'
        }

        self._webhooks = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if webhooks is not None:
          self.webhooks = webhooks

    @property
    def webhooks(self):
        """
        Gets the webhooks of this ListWebhooksResponse.
        The list of webhooks.

        :return: The webhooks of this ListWebhooksResponse.
        :rtype: list[Webhook]
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """
        Sets the webhooks of this ListWebhooksResponse.
        The list of webhooks.

        :param webhooks: The webhooks of this ListWebhooksResponse.
        :type: list[Webhook]
        """
        if webhooks is None:
            raise ValueError("Invalid value for `webhooks`, must not be `None`")

        self._webhooks = webhooks

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
        if not isinstance(other, ListWebhooksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
