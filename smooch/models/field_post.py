# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FieldPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, name=None, label=None, placeholder=None, min_size=None, max_size=None, options=None):
        """
        FieldPost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'label': 'str',
            'placeholder': 'str',
            'min_size': 'int',
            'max_size': 'int',
            'options': 'list[Option]'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'label': 'label',
            'placeholder': 'placeholder',
            'min_size': 'minSize',
            'max_size': 'maxSize',
            'options': 'options'
        }

        self._type = None
        self._name = None
        self._label = None
        self._placeholder = None
        self._min_size = None
        self._max_size = None
        self._options = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if type is not None:
          self.type = type
        if name is not None:
          self.name = name
        if label is not None:
          self.label = label
        if placeholder is not None:
          self.placeholder = placeholder
        if min_size is not None:
          self.min_size = min_size
        if max_size is not None:
          self.max_size = max_size
        if options is not None:
          self.options = options

    @property
    def type(self):
        """
        Gets the type of this FieldPost.
        The field type. See [**FieldTypeEnum**](Enums.md#FieldTypeEnum) for available values.

        :return: The type of this FieldPost.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FieldPost.
        The field type. See [**FieldTypeEnum**](Enums.md#FieldTypeEnum) for available values.

        :param type: The type of this FieldPost.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this FieldPost.
        The name of the field. Each field name must be unique per form.

        :return: The name of this FieldPost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FieldPost.
        The name of the field. Each field name must be unique per form.

        :param name: The name of this FieldPost.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def label(self):
        """
        Gets the label of this FieldPost.
        The label to be displayed with the field.

        :return: The label of this FieldPost.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this FieldPost.
        The label to be displayed with the field.

        :param label: The label of this FieldPost.
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def placeholder(self):
        """
        Gets the placeholder of this FieldPost.
        The placeholder text of the field that will be rendered. Only for form messages 

        :return: The placeholder of this FieldPost.
        :rtype: str
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """
        Sets the placeholder of this FieldPost.
        The placeholder text of the field that will be rendered. Only for form messages 

        :param placeholder: The placeholder of this FieldPost.
        :type: str
        """

        self._placeholder = placeholder

    @property
    def min_size(self):
        """
        Gets the min_size of this FieldPost.
        The minimum possible length of the response. Defaults to 1 if not specified. Only for text fields in form messages. 

        :return: The min_size of this FieldPost.
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """
        Sets the min_size of this FieldPost.
        The minimum possible length of the response. Defaults to 1 if not specified. Only for text fields in form messages. 

        :param min_size: The min_size of this FieldPost.
        :type: int
        """

        self._min_size = min_size

    @property
    def max_size(self):
        """
        Gets the max_size of this FieldPost.
        The maximum possible length of the response. Defaults to 128 if not specified. Only for text fields in form messages. 

        :return: The max_size of this FieldPost.
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """
        Sets the max_size of this FieldPost.
        The maximum possible length of the response. Defaults to 128 if not specified. Only for text fields in form messages. 

        :param max_size: The max_size of this FieldPost.
        :type: int
        """

        self._max_size = max_size

    @property
    def options(self):
        """
        Gets the options of this FieldPost.
        The field options that can be selected. The array is limited to 20 options. Only for select fields in form messages. 

        :return: The options of this FieldPost.
        :rtype: list[Option]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this FieldPost.
        The field options that can be selected. The array is limited to 20 options. Only for select fields in form messages. 

        :param options: The options of this FieldPost.
        :type: list[Option]
        """

        self._options = options

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
        if not isinstance(other, FieldPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
