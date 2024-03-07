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


class FormMessageFieldAllOf(object):
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
        'placeholder': 'str',
        'min_size': 'int',
        'max_size': 'int',
        'options': 'list[object]'
    }

    attribute_map = {
        'placeholder': 'placeholder',
        'min_size': 'minSize',
        'max_size': 'maxSize',
        'options': 'options'
    }

    nulls = set()

    def __init__(self, placeholder=None, min_size=1, max_size=128, options=None, local_vars_configuration=None):  # noqa: E501
        """FormMessageFieldAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._placeholder = None
        self._min_size = None
        self._max_size = None
        self._options = None
        self.discriminator = None

        if placeholder is not None:
            self.placeholder = placeholder
        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if options is not None:
            self.options = options

    @property
    def placeholder(self):
        """Gets the placeholder of this FormMessageFieldAllOf.  # noqa: E501

        Placeholder text for the field. Form message only.  # noqa: E501

        :return: The placeholder of this FormMessageFieldAllOf.  # noqa: E501
        :rtype: str
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """Sets the placeholder of this FormMessageFieldAllOf.

        Placeholder text for the field. Form message only.  # noqa: E501

        :param placeholder: The placeholder of this FormMessageFieldAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                placeholder is not None and len(placeholder) > 128):
            raise ValueError("Invalid value for `placeholder`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                placeholder is not None and len(placeholder) < 1):
            raise ValueError("Invalid value for `placeholder`, length must be greater than or equal to `1`")  # noqa: E501

        self._placeholder = placeholder

    @property
    def min_size(self):
        """Gets the min_size of this FormMessageFieldAllOf.  # noqa: E501

        The minimum allowed length for the response for a field of type text. Form message only.  # noqa: E501

        :return: The min_size of this FormMessageFieldAllOf.  # noqa: E501
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this FormMessageFieldAllOf.

        The minimum allowed length for the response for a field of type text. Form message only.  # noqa: E501

        :param min_size: The min_size of this FormMessageFieldAllOf.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                min_size is not None and min_size > 256):  # noqa: E501
            raise ValueError("Invalid value for `min_size`, must be a value less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_size is not None and min_size < 1):  # noqa: E501
            raise ValueError("Invalid value for `min_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._min_size = min_size

    @property
    def max_size(self):
        """Gets the max_size of this FormMessageFieldAllOf.  # noqa: E501

        The maximum allowed length for the response for a field of type text. Form message only.  # noqa: E501

        :return: The max_size of this FormMessageFieldAllOf.  # noqa: E501
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this FormMessageFieldAllOf.

        The maximum allowed length for the response for a field of type text. Form message only.  # noqa: E501

        :param max_size: The max_size of this FormMessageFieldAllOf.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_size is not None and max_size > 256):  # noqa: E501
            raise ValueError("Invalid value for `max_size`, must be a value less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_size is not None and max_size < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_size = max_size

    @property
    def options(self):
        """Gets the options of this FormMessageFieldAllOf.  # noqa: E501

        Array of objects representing options for a field of type select.  # noqa: E501

        :return: The options of this FormMessageFieldAllOf.  # noqa: E501
        :rtype: list[object]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this FormMessageFieldAllOf.

        Array of objects representing options for a field of type select.  # noqa: E501

        :param options: The options of this FormMessageFieldAllOf.  # noqa: E501
        :type: list[object]
        """

        self._options = options

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
        if not isinstance(other, FormMessageFieldAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormMessageFieldAllOf):
            return True

        return self.to_dict() != other.to_dict()
