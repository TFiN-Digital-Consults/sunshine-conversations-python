# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ListTemplatesResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, templates=None, has_more=None, offset=None):
        """
        ListTemplatesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'templates': 'list[Template]',
            'has_more': 'bool',
            'offset': 'int'
        }

        self.attribute_map = {
            'templates': 'templates',
            'has_more': 'hasMore',
            'offset': 'offset'
        }

        self._templates = None
        self._has_more = None
        self._offset = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if templates is not None:
          self.templates = templates
        if has_more is not None:
          self.has_more = has_more
        if offset is not None:
          self.offset = offset

    @property
    def templates(self):
        """
        Gets the templates of this ListTemplatesResponse.
        The list of templates.

        :return: The templates of this ListTemplatesResponse.
        :rtype: list[Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this ListTemplatesResponse.
        The list of templates.

        :param templates: The templates of this ListTemplatesResponse.
        :type: list[Template]
        """
        if templates is None:
            raise ValueError("Invalid value for `templates`, must not be `None`")

        self._templates = templates

    @property
    def has_more(self):
        """
        Gets the has_more of this ListTemplatesResponse.
        Flag indicating if there are more templates that are not present in the response.

        :return: The has_more of this ListTemplatesResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this ListTemplatesResponse.
        Flag indicating if there are more templates that are not present in the response.

        :param has_more: The has_more of this ListTemplatesResponse.
        :type: bool
        """

        self._has_more = has_more

    @property
    def offset(self):
        """
        Gets the offset of this ListTemplatesResponse.
        The number of template records skipped in the returned list.

        :return: The offset of this ListTemplatesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this ListTemplatesResponse.
        The number of template records skipped in the returned list.

        :param offset: The offset of this ListTemplatesResponse.
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
        if not isinstance(other, ListTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
