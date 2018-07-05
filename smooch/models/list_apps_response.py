# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 3.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ListAppsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, apps=None, has_more=None, offset=None):
        """
        ListAppsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'apps': 'list[App]',
            'has_more': 'bool',
            'offset': 'int'
        }

        self.attribute_map = {
            'apps': 'apps',
            'has_more': 'hasMore',
            'offset': 'offset'
        }

        self._apps = None
        self._has_more = None
        self._offset = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if apps is not None:
          self.apps = apps
        if has_more is not None:
          self.has_more = has_more
        if offset is not None:
          self.offset = offset

    @property
    def apps(self):
        """
        Gets the apps of this ListAppsResponse.
        The list of apps.

        :return: The apps of this ListAppsResponse.
        :rtype: list[App]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """
        Sets the apps of this ListAppsResponse.
        The list of apps.

        :param apps: The apps of this ListAppsResponse.
        :type: list[App]
        """

        self._apps = apps

    @property
    def has_more(self):
        """
        Gets the has_more of this ListAppsResponse.
        Flag indicating if there are more apps that are not present in the response.

        :return: The has_more of this ListAppsResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this ListAppsResponse.
        Flag indicating if there are more apps that are not present in the response.

        :param has_more: The has_more of this ListAppsResponse.
        :type: bool
        """

        self._has_more = has_more

    @property
    def offset(self):
        """
        Gets the offset of this ListAppsResponse.
        The number of app records skipped in the returned list.

        :return: The offset of this ListAppsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this ListAppsResponse.
        The number of app records skipped in the returned list.

        :param offset: The offset of this ListAppsResponse.
        :type: int
        """

        self._offset = offset

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
        if not isinstance(other, ListAppsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
