# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class App(object):
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
        'display_name': 'str',
        'settings': 'AppSettings',
        'metadata': 'object'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'settings': 'settings',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, id=None, display_name=None, settings=None, metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """App - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._settings = None
        self._metadata = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if settings is not None:
            self.settings = settings
        self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this App.  # noqa: E501

        A canonical ID that can be used to retrieve the Sunshine Conversations app.  # noqa: E501

        :return: The id of this App.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this App.

        A canonical ID that can be used to retrieve the Sunshine Conversations app.  # noqa: E501

        :param id: The id of this App.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this App.  # noqa: E501

        The friendly name of the app.  # noqa: E501

        :return: The display_name of this App.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this App.

        The friendly name of the app.  # noqa: E501

        :param display_name: The display_name of this App.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def settings(self):
        """Gets the settings of this App.  # noqa: E501


        :return: The settings of this App.  # noqa: E501
        :rtype: AppSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this App.


        :param settings: The settings of this App.  # noqa: E501
        :type: AppSettings
        """

        self._settings = settings

    @property
    def metadata(self):
        """Gets the metadata of this App.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this App.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this App.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this App.  # noqa: E501
        :type: object
        """
        if type(metadata) is Undefined:
            metadata = None
            self.nulls.discard("metadata")
        elif metadata is None:
            self.nulls.add("metadata")
        else:
            self.nulls.discard("metadata")

        self._metadata = metadata

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
        if not isinstance(other, App):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, App):
            return True

        return self.to_dict() != other.to_dict()
