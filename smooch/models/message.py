# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 2.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Message(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, author_id=None, role=None, type=None, source=None, name=None, text=None, email=None, avatar_url=None, received=None, media_url=None, media_type=None, metadata=None, items=None, actions=None, payload=None, display_settings=None):
        """
        Message - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'author_id': 'str',
            'role': 'str',
            'type': 'str',
            'source': 'Source',
            'name': 'str',
            'text': 'str',
            'email': 'str',
            'avatar_url': 'str',
            'received': 'float',
            'media_url': 'str',
            'media_type': 'str',
            'metadata': 'object',
            'items': 'list[MessageItem]',
            'actions': 'list[Action]',
            'payload': 'str',
            'display_settings': 'DisplaySettings'
        }

        self.attribute_map = {
            'id': '_id',
            'author_id': 'authorId',
            'role': 'role',
            'type': 'type',
            'source': 'source',
            'name': 'name',
            'text': 'text',
            'email': 'email',
            'avatar_url': 'avatarUrl',
            'received': 'received',
            'media_url': 'mediaUrl',
            'media_type': 'mediaType',
            'metadata': 'metadata',
            'items': 'items',
            'actions': 'actions',
            'payload': 'payload',
            'display_settings': 'displaySettings'
        }

        self._id = None
        self._author_id = None
        self._role = None
        self._type = None
        self._source = None
        self._name = None
        self._text = None
        self._email = None
        self._avatar_url = None
        self._received = None
        self._media_url = None
        self._media_type = None
        self._metadata = None
        self._items = None
        self._actions = None
        self._payload = None
        self._display_settings = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if id is not None:
          self.id = id
        if author_id is not None:
          self.author_id = author_id
        if role is not None:
          self.role = role
        if type is not None:
          self.type = type
        if source is not None:
          self.source = source
        if name is not None:
          self.name = name
        if text is not None:
          self.text = text
        if email is not None:
          self.email = email
        if avatar_url is not None:
          self.avatar_url = avatar_url
        if received is not None:
          self.received = received
        if media_url is not None:
          self.media_url = media_url
        if media_type is not None:
          self.media_type = media_type
        if metadata is not None:
          self.metadata = metadata
        if items is not None:
          self.items = items
        if actions is not None:
          self.actions = actions
        if payload is not None:
          self.payload = payload
        if display_settings is not None:
          self.display_settings = display_settings

    @property
    def id(self):
        """
        Gets the id of this Message.
        The message ID, generated automatically.

        :return: The id of this Message.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Message.
        The message ID, generated automatically.

        :param id: The id of this Message.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def author_id(self):
        """
        Gets the author_id of this Message.
        The ID of the message's author.

        :return: The author_id of this Message.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """
        Sets the author_id of this Message.
        The ID of the message's author.

        :param author_id: The author_id of this Message.
        :type: str
        """
        if author_id is None:
            raise ValueError("Invalid value for `author_id`, must not be `None`")

        self._author_id = author_id

    @property
    def role(self):
        """
        Gets the role of this Message.
        The role of the individual posting the message. Can be either *appUser* or *appMaker*.

        :return: The role of this Message.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this Message.
        The role of the individual posting the message. Can be either *appUser* or *appMaker*.

        :param role: The role of this Message.
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

    @property
    def type(self):
        """
        Gets the type of this Message.
        The message type.

        :return: The type of this Message.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Message.
        The message type.

        :param type: The type of this Message.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def source(self):
        """
        Gets the source of this Message.
        The source of the message.

        :return: The source of this Message.
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Message.
        The source of the message.

        :param source: The source of this Message.
        :type: Source
        """

        self._source = source

    @property
    def name(self):
        """
        Gets the name of this Message.
        The display name of the message author.

        :return: The name of this Message.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Message.
        The display name of the message author.

        :param name: The name of this Message.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def text(self):
        """
        Gets the text of this Message.
        The message text. Required for text messages. 

        :return: The text of this Message.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Message.
        The message text. Required for text messages. 

        :param text: The text of this Message.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

    @property
    def email(self):
        """
        Gets the email of this Message.
        The email address of the message author.

        :return: The email of this Message.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Message.
        The email address of the message author.

        :param email: The email of this Message.
        :type: str
        """

        self._email = email

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this Message.
        The URL of the desired message avatar image.

        :return: The avatar_url of this Message.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this Message.
        The URL of the desired message avatar image.

        :param avatar_url: The avatar_url of this Message.
        :type: str
        """
        if avatar_url is None:
            raise ValueError("Invalid value for `avatar_url`, must not be `None`")

        self._avatar_url = avatar_url

    @property
    def received(self):
        """
        Gets the received of this Message.
        The unix timestamp of the moment the message was received.

        :return: The received of this Message.
        :rtype: float
        """
        return self._received

    @received.setter
    def received(self, received):
        """
        Sets the received of this Message.
        The unix timestamp of the moment the message was received.

        :param received: The received of this Message.
        :type: float
        """
        if received is None:
            raise ValueError("Invalid value for `received`, must not be `None`")

        self._received = received

    @property
    def media_url(self):
        """
        Gets the media_url of this Message.
        The mediaUrl for the message. Required for image/file messages. 

        :return: The media_url of this Message.
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """
        Sets the media_url of this Message.
        The mediaUrl for the message. Required for image/file messages. 

        :param media_url: The media_url of this Message.
        :type: str
        """

        self._media_url = media_url

    @property
    def media_type(self):
        """
        Gets the media_type of this Message.
        The mediaType for the message. Required for image/file messages. 

        :return: The media_type of this Message.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this Message.
        The mediaType for the message. Required for image/file messages. 

        :param media_type: The media_type of this Message.
        :type: str
        """

        self._media_type = media_type

    @property
    def metadata(self):
        """
        Gets the metadata of this Message.
        Flat JSON object containing any custom properties associated with the message.

        :return: The metadata of this Message.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Message.
        Flat JSON object containing any custom properties associated with the message.

        :param metadata: The metadata of this Message.
        :type: object
        """

        self._metadata = metadata

    @property
    def items(self):
        """
        Gets the items of this Message.
        The items in the message list. Required for carousel and list messages. 

        :return: The items of this Message.
        :rtype: list[MessageItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this Message.
        The items in the message list. Required for carousel and list messages. 

        :param items: The items of this Message.
        :type: list[MessageItem]
        """

        self._items = items

    @property
    def actions(self):
        """
        Gets the actions of this Message.
        The actions in the message.

        :return: The actions of this Message.
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this Message.
        The actions in the message.

        :param actions: The actions of this Message.
        :type: list[Action]
        """

        self._actions = actions

    @property
    def payload(self):
        """
        Gets the payload of this Message.
        The payload of a reply action, if applicable.

        :return: The payload of this Message.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this Message.
        The payload of a reply action, if applicable.

        :param payload: The payload of this Message.
        :type: str
        """

        self._payload = payload

    @property
    def display_settings(self):
        """
        Gets the display_settings of this Message.
        Settings to adjust the carousel layout. See [Display Settings](https://docs.smooch.io/rest/#display-settings).

        :return: The display_settings of this Message.
        :rtype: DisplaySettings
        """
        return self._display_settings

    @display_settings.setter
    def display_settings(self, display_settings):
        """
        Sets the display_settings of this Message.
        Settings to adjust the carousel layout. See [Display Settings](https://docs.smooch.io/rest/#display-settings).

        :param display_settings: The display_settings of this Message.
        :type: DisplaySettings
        """

        self._display_settings = display_settings

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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
