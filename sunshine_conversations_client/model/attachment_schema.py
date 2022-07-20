# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.10.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class AttachmentSchema(object):
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
        'media_url': 'str',
        'media_type': 'str'
    }

    attribute_map = {
        'media_url': 'mediaUrl',
        'media_type': 'mediaType'
    }

    nulls = set()

    def __init__(self, media_url=None, media_type=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentSchema - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._media_url = None
        self._media_type = None
        self.discriminator = None

        if media_url is not None:
            self.media_url = media_url
        if media_type is not None:
            self.media_type = media_type

    @property
    def media_url(self):
        """Gets the media_url of this AttachmentSchema.  # noqa: E501

        Uploaded attachment’s url  # noqa: E501

        :return: The media_url of this AttachmentSchema.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this AttachmentSchema.

        Uploaded attachment’s url  # noqa: E501

        :param media_url: The media_url of this AttachmentSchema.  # noqa: E501
        :type: str
        """

        self._media_url = media_url

    @property
    def media_type(self):
        """Gets the media_type of this AttachmentSchema.  # noqa: E501

        Uploaded attachment's media type  # noqa: E501

        :return: The media_type of this AttachmentSchema.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this AttachmentSchema.

        Uploaded attachment's media type  # noqa: E501

        :param media_type: The media_type of this AttachmentSchema.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

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
        if not isinstance(other, AttachmentSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentSchema):
            return True

        return self.to_dict() != other.to_dict()
