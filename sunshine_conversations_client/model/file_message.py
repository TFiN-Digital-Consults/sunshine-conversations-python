# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class FileMessage(object):
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
        'media_url': 'str',
        'media_size': 'float',
        'media_type': 'str',
        'alt_text': 'str',
        'text': 'str'
    }

    attribute_map = {
        'type': 'type',
        'media_url': 'mediaUrl',
        'media_size': 'mediaSize',
        'media_type': 'mediaType',
        'alt_text': 'altText',
        'text': 'text'
    }

    nulls = set()

    def __init__(self, type='file', media_url=None, media_size=None, media_type=None, alt_text=None, text=None, local_vars_configuration=None):  # noqa: E501
        """FileMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._media_url = None
        self._media_size = None
        self._media_type = None
        self._alt_text = None
        self._text = None
        self.discriminator = None

        self.type = type
        self.media_url = media_url
        if media_size is not None:
            self.media_size = media_size
        if media_type is not None:
            self.media_type = media_type
        if alt_text is not None:
            self.alt_text = alt_text
        if text is not None:
            self.text = text

    @property
    def type(self):
        """Gets the type of this FileMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this FileMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileMessage.

        The type of message.  # noqa: E501

        :param type: The type of this FileMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def media_url(self):
        """Gets the media_url of this FileMessage.  # noqa: E501

        The URL for media, such as an image, attached to the message.  # noqa: E501

        :return: The media_url of this FileMessage.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this FileMessage.

        The URL for media, such as an image, attached to the message.  # noqa: E501

        :param media_url: The media_url of this FileMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and media_url is None:  # noqa: E501
            raise ValueError("Invalid value for `media_url`, must not be `None`")  # noqa: E501

        self._media_url = media_url

    @property
    def media_size(self):
        """Gets the media_size of this FileMessage.  # noqa: E501

        The size of the media.  # noqa: E501

        :return: The media_size of this FileMessage.  # noqa: E501
        :rtype: float
        """
        return self._media_size

    @media_size.setter
    def media_size(self, media_size):
        """Sets the media_size of this FileMessage.

        The size of the media.  # noqa: E501

        :param media_size: The media_size of this FileMessage.  # noqa: E501
        :type: float
        """

        self._media_size = media_size

    @property
    def media_type(self):
        """Gets the media_type of this FileMessage.  # noqa: E501

        The media type of the file.  # noqa: E501

        :return: The media_type of this FileMessage.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this FileMessage.

        The media type of the file.  # noqa: E501

        :param media_type: The media_type of this FileMessage.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def alt_text(self):
        """Gets the alt_text of this FileMessage.  # noqa: E501

        An optional description of the file for accessibility purposes. The field will be saved by default with the file name as the value.  # noqa: E501

        :return: The alt_text of this FileMessage.  # noqa: E501
        :rtype: str
        """
        return self._alt_text

    @alt_text.setter
    def alt_text(self, alt_text):
        """Sets the alt_text of this FileMessage.

        An optional description of the file for accessibility purposes. The field will be saved by default with the file name as the value.  # noqa: E501

        :param alt_text: The alt_text of this FileMessage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                alt_text is not None and len(alt_text) > 128):
            raise ValueError("Invalid value for `alt_text`, length must be less than or equal to `128`")  # noqa: E501

        self._alt_text = alt_text

    @property
    def text(self):
        """Gets the text of this FileMessage.  # noqa: E501

        The text content of the message.  # noqa: E501

        :return: The text of this FileMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FileMessage.

        The text content of the message.  # noqa: E501

        :param text: The text of this FileMessage.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if not isinstance(other, FileMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileMessage):
            return True

        return self.to_dict() != other.to_dict()
