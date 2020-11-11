# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class IntegrationUpdate(object):
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
        'display_name': 'str',
        'server_key': 'str',
        'sender_id': 'str',
        'can_user_create_more_conversations': 'bool',
        'certificate': 'str',
        'password': 'str',
        'production': 'bool',
        'auto_update_badge': 'bool',
        'hide_unsubscribe_link': 'bool',
        'from_address': 'str',
        'page_access_token': 'str',
        'brand_color': 'str',
        'fixed_intro_pane': 'bool',
        'conversation_color': 'str',
        'action_color': 'str',
        'display_style': 'str',
        'button_icon_url': 'str',
        'button_width': 'str',
        'button_height': 'str',
        'integration_order': 'list[str]',
        'business_name': 'str',
        'business_icon_url': 'str',
        'background_image_url': 'str',
        'origin_whitelist': 'list[str]',
        'prechat_capture': 'PrechatCapture',
        'hsm_fallback_language': 'str',
        'account_id': 'str',
        'account_management_access_token': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'server_key': 'serverKey',
        'sender_id': 'senderId',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations',
        'certificate': 'certificate',
        'password': 'password',
        'production': 'production',
        'auto_update_badge': 'autoUpdateBadge',
        'hide_unsubscribe_link': 'hideUnsubscribeLink',
        'from_address': 'fromAddress',
        'page_access_token': 'pageAccessToken',
        'brand_color': 'brandColor',
        'fixed_intro_pane': 'fixedIntroPane',
        'conversation_color': 'conversationColor',
        'action_color': 'actionColor',
        'display_style': 'displayStyle',
        'button_icon_url': 'buttonIconUrl',
        'button_width': 'buttonWidth',
        'button_height': 'buttonHeight',
        'integration_order': 'integrationOrder',
        'business_name': 'businessName',
        'business_icon_url': 'businessIconUrl',
        'background_image_url': 'backgroundImageUrl',
        'origin_whitelist': 'originWhitelist',
        'prechat_capture': 'prechatCapture',
        'hsm_fallback_language': 'hsmFallbackLanguage',
        'account_id': 'accountId',
        'account_management_access_token': 'accountManagementAccessToken'
    }

    nulls = set()

    def __init__(self, display_name=Undefined(), server_key=Undefined(), sender_id=Undefined(), can_user_create_more_conversations=None, certificate=Undefined(), password=None, production=None, auto_update_badge=None, hide_unsubscribe_link=None, from_address=Undefined(), page_access_token=None, brand_color='65758e', fixed_intro_pane=False, conversation_color='0099ff', action_color='0099ff', display_style='button', button_icon_url=Undefined(), button_width='58', button_height='58', integration_order=Undefined(), business_name=None, business_icon_url=None, background_image_url=None, origin_whitelist=Undefined(), prechat_capture=None, hsm_fallback_language='en_US', account_id=Undefined(), account_management_access_token=Undefined(), local_vars_configuration=None):  # noqa: E501
        """IntegrationUpdate - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._server_key = None
        self._sender_id = None
        self._can_user_create_more_conversations = None
        self._certificate = None
        self._password = None
        self._production = None
        self._auto_update_badge = None
        self._hide_unsubscribe_link = None
        self._from_address = None
        self._page_access_token = None
        self._brand_color = None
        self._fixed_intro_pane = None
        self._conversation_color = None
        self._action_color = None
        self._display_style = None
        self._button_icon_url = None
        self._button_width = None
        self._button_height = None
        self._integration_order = None
        self._business_name = None
        self._business_icon_url = None
        self._background_image_url = None
        self._origin_whitelist = None
        self._prechat_capture = None
        self._hsm_fallback_language = None
        self._account_id = None
        self._account_management_access_token = None
        self.discriminator = None

        self.display_name = display_name
        self.server_key = server_key
        self.sender_id = sender_id
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations
        self.certificate = certificate
        if password is not None:
            self.password = password
        if production is not None:
            self.production = production
        if auto_update_badge is not None:
            self.auto_update_badge = auto_update_badge
        if hide_unsubscribe_link is not None:
            self.hide_unsubscribe_link = hide_unsubscribe_link
        self.from_address = from_address
        if page_access_token is not None:
            self.page_access_token = page_access_token
        if brand_color is not None:
            self.brand_color = brand_color
        if fixed_intro_pane is not None:
            self.fixed_intro_pane = fixed_intro_pane
        if conversation_color is not None:
            self.conversation_color = conversation_color
        if action_color is not None:
            self.action_color = action_color
        if display_style is not None:
            self.display_style = display_style
        self.button_icon_url = button_icon_url
        if button_width is not None:
            self.button_width = button_width
        if button_height is not None:
            self.button_height = button_height
        self.integration_order = integration_order
        if business_name is not None:
            self.business_name = business_name
        if business_icon_url is not None:
            self.business_icon_url = business_icon_url
        if background_image_url is not None:
            self.background_image_url = background_image_url
        self.origin_whitelist = origin_whitelist
        if prechat_capture is not None:
            self.prechat_capture = prechat_capture
        self.hsm_fallback_language = hsm_fallback_language
        self.account_id = account_id
        self.account_management_access_token = account_management_access_token

    @property
    def display_name(self):
        """Gets the display_name of this IntegrationUpdate.  # noqa: E501

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :return: The display_name of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IntegrationUpdate.

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :param display_name: The display_name of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(display_name) is Undefined:
            display_name = None
            self.nulls.discard("display_name")
        elif display_name is None:
            self.nulls.add("display_name")
        else:
            self.nulls.discard("display_name")
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 100):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def server_key(self):
        """Gets the server_key of this IntegrationUpdate.  # noqa: E501

        Your server key from the fcm console.  # noqa: E501

        :return: The server_key of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._server_key

    @server_key.setter
    def server_key(self, server_key):
        """Sets the server_key of this IntegrationUpdate.

        Your server key from the fcm console.  # noqa: E501

        :param server_key: The server_key of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(server_key) is Undefined:
            server_key = None
            self.nulls.discard("server_key")
        elif server_key is None:
            self.nulls.add("server_key")
        else:
            self.nulls.discard("server_key")
        if (self.local_vars_configuration.client_side_validation and
                server_key is not None and len(server_key) < 1):
            raise ValueError("Invalid value for `server_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._server_key = server_key

    @property
    def sender_id(self):
        """Gets the sender_id of this IntegrationUpdate.  # noqa: E501

        Your sender id from the fcm console.  # noqa: E501

        :return: The sender_id of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this IntegrationUpdate.

        Your sender id from the fcm console.  # noqa: E501

        :param sender_id: The sender_id of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(sender_id) is Undefined:
            sender_id = None
            self.nulls.discard("sender_id")
        elif sender_id is None:
            self.nulls.add("sender_id")
        else:
            self.nulls.discard("sender_id")
        if (self.local_vars_configuration.client_side_validation and
                sender_id is not None and len(sender_id) < 1):
            raise ValueError("Invalid value for `sender_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._sender_id = sender_id

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this IntegrationUpdate.  # noqa: E501

        Allows users to create more than one conversation on the web messenger integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this IntegrationUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this IntegrationUpdate.

        Allows users to create more than one conversation on the web messenger integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this IntegrationUpdate.  # noqa: E501
        :type: bool
        """

        self._can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def certificate(self):
        """Gets the certificate of this IntegrationUpdate.  # noqa: E501

        The binary of your APN certificate base64 encoded.  # noqa: E501

        :return: The certificate of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this IntegrationUpdate.

        The binary of your APN certificate base64 encoded.  # noqa: E501

        :param certificate: The certificate of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(certificate) is Undefined:
            certificate = None
            self.nulls.discard("certificate")
        elif certificate is None:
            self.nulls.add("certificate")
        else:
            self.nulls.discard("certificate")
        if (self.local_vars_configuration.client_side_validation and
                certificate is not None and len(certificate) < 1):
            raise ValueError("Invalid value for `certificate`, length must be greater than or equal to `1`")  # noqa: E501

        self._certificate = certificate

    @property
    def password(self):
        """Gets the password of this IntegrationUpdate.  # noqa: E501

        The password for your APN certificate.  # noqa: E501

        :return: The password of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this IntegrationUpdate.

        The password for your APN certificate.  # noqa: E501

        :param password: The password of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def production(self):
        """Gets the production of this IntegrationUpdate.  # noqa: E501

        The APN environment to connect to (Production, if true, or Sandbox). Defaults to value inferred from certificate if not specified.  # noqa: E501

        :return: The production of this IntegrationUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this IntegrationUpdate.

        The APN environment to connect to (Production, if true, or Sandbox). Defaults to value inferred from certificate if not specified.  # noqa: E501

        :param production: The production of this IntegrationUpdate.  # noqa: E501
        :type: bool
        """

        self._production = production

    @property
    def auto_update_badge(self):
        """Gets the auto_update_badge of this IntegrationUpdate.  # noqa: E501

        Use the unread count of the conversation as the application badge.  # noqa: E501

        :return: The auto_update_badge of this IntegrationUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._auto_update_badge

    @auto_update_badge.setter
    def auto_update_badge(self, auto_update_badge):
        """Sets the auto_update_badge of this IntegrationUpdate.

        Use the unread count of the conversation as the application badge.  # noqa: E501

        :param auto_update_badge: The auto_update_badge of this IntegrationUpdate.  # noqa: E501
        :type: bool
        """

        self._auto_update_badge = auto_update_badge

    @property
    def hide_unsubscribe_link(self):
        """Gets the hide_unsubscribe_link of this IntegrationUpdate.  # noqa: E501

        A boolean value indicating whether the unsubscribe link should be omitted from outgoing emails. When enabled, it is expected that the business is providing the user a way to unsubscribe by some other means. By default, the unsubscribe link will be included in all outgoing emails.  # noqa: E501

        :return: The hide_unsubscribe_link of this IntegrationUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._hide_unsubscribe_link

    @hide_unsubscribe_link.setter
    def hide_unsubscribe_link(self, hide_unsubscribe_link):
        """Sets the hide_unsubscribe_link of this IntegrationUpdate.

        A boolean value indicating whether the unsubscribe link should be omitted from outgoing emails. When enabled, it is expected that the business is providing the user a way to unsubscribe by some other means. By default, the unsubscribe link will be included in all outgoing emails.  # noqa: E501

        :param hide_unsubscribe_link: The hide_unsubscribe_link of this IntegrationUpdate.  # noqa: E501
        :type: bool
        """

        self._hide_unsubscribe_link = hide_unsubscribe_link

    @property
    def from_address(self):
        """Gets the from_address of this IntegrationUpdate.  # noqa: E501

        Email address to use as the From and Reply-To address if it must be different from incomingAddress. Only use this option if the address that you supply is configured to forward emails to the incomingAddress, otherwise user replies will be lost. You must also make sure that the domain is properly configured as a mail provider so as to not be flagged as spam by the user’s email client. May be unset with null.  # noqa: E501

        :return: The from_address of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this IntegrationUpdate.

        Email address to use as the From and Reply-To address if it must be different from incomingAddress. Only use this option if the address that you supply is configured to forward emails to the incomingAddress, otherwise user replies will be lost. You must also make sure that the domain is properly configured as a mail provider so as to not be flagged as spam by the user’s email client. May be unset with null.  # noqa: E501

        :param from_address: The from_address of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(from_address) is Undefined:
            from_address = None
            self.nulls.discard("from_address")
        elif from_address is None:
            self.nulls.add("from_address")
        else:
            self.nulls.discard("from_address")
        if (self.local_vars_configuration.client_side_validation and
                from_address is not None and len(from_address) < 1):
            raise ValueError("Invalid value for `from_address`, length must be greater than or equal to `1`")  # noqa: E501

        self._from_address = from_address

    @property
    def page_access_token(self):
        """Gets the page_access_token of this IntegrationUpdate.  # noqa: E501

        A Facebook Page Access Token.  # noqa: E501

        :return: The page_access_token of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._page_access_token

    @page_access_token.setter
    def page_access_token(self, page_access_token):
        """Sets the page_access_token of this IntegrationUpdate.

        A Facebook Page Access Token.  # noqa: E501

        :param page_access_token: The page_access_token of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._page_access_token = page_access_token

    @property
    def brand_color(self):
        """Gets the brand_color of this IntegrationUpdate.  # noqa: E501

        This color will be used in the messenger header and the button or tab in idle state. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :return: The brand_color of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._brand_color

    @brand_color.setter
    def brand_color(self, brand_color):
        """Sets the brand_color of this IntegrationUpdate.

        This color will be used in the messenger header and the button or tab in idle state. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :param brand_color: The brand_color of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._brand_color = brand_color

    @property
    def fixed_intro_pane(self):
        """Gets the fixed_intro_pane of this IntegrationUpdate.  # noqa: E501

        When true, the introduction pane will be pinned at the top of the conversation instead of scrolling with it.  # noqa: E501

        :return: The fixed_intro_pane of this IntegrationUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_intro_pane

    @fixed_intro_pane.setter
    def fixed_intro_pane(self, fixed_intro_pane):
        """Sets the fixed_intro_pane of this IntegrationUpdate.

        When true, the introduction pane will be pinned at the top of the conversation instead of scrolling with it.  # noqa: E501

        :param fixed_intro_pane: The fixed_intro_pane of this IntegrationUpdate.  # noqa: E501
        :type: bool
        """

        self._fixed_intro_pane = fixed_intro_pane

    @property
    def conversation_color(self):
        """Gets the conversation_color of this IntegrationUpdate.  # noqa: E501

        This color will be used for customer messages, quick replies and actions in the footer. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :return: The conversation_color of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._conversation_color

    @conversation_color.setter
    def conversation_color(self, conversation_color):
        """Sets the conversation_color of this IntegrationUpdate.

        This color will be used for customer messages, quick replies and actions in the footer. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :param conversation_color: The conversation_color of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._conversation_color = conversation_color

    @property
    def action_color(self):
        """Gets the action_color of this IntegrationUpdate.  # noqa: E501

        This color will be used for call-to-actions inside your messages. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :return: The action_color of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._action_color

    @action_color.setter
    def action_color(self, action_color):
        """Sets the action_color of this IntegrationUpdate.

        This color will be used for call-to-actions inside your messages. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :param action_color: The action_color of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._action_color = action_color

    @property
    def display_style(self):
        """Gets the display_style of this IntegrationUpdate.  # noqa: E501

        Choose how the messenger will appear on your website. Must be either button or tab.  # noqa: E501

        :return: The display_style of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_style

    @display_style.setter
    def display_style(self, display_style):
        """Sets the display_style of this IntegrationUpdate.

        Choose how the messenger will appear on your website. Must be either button or tab.  # noqa: E501

        :param display_style: The display_style of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._display_style = display_style

    @property
    def button_icon_url(self):
        """Gets the button_icon_url of this IntegrationUpdate.  # noqa: E501

        With the button style Web Messenger, you have the option of selecting your own button icon. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format.  # noqa: E501

        :return: The button_icon_url of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._button_icon_url

    @button_icon_url.setter
    def button_icon_url(self, button_icon_url):
        """Sets the button_icon_url of this IntegrationUpdate.

        With the button style Web Messenger, you have the option of selecting your own button icon. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format.  # noqa: E501

        :param button_icon_url: The button_icon_url of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(button_icon_url) is Undefined:
            button_icon_url = None
            self.nulls.discard("button_icon_url")
        elif button_icon_url is None:
            self.nulls.add("button_icon_url")
        else:
            self.nulls.discard("button_icon_url")

        self._button_icon_url = button_icon_url

    @property
    def button_width(self):
        """Gets the button_width of this IntegrationUpdate.  # noqa: E501

        With the button style Web Messenger, you have the option of specifying the button width.  # noqa: E501

        :return: The button_width of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._button_width

    @button_width.setter
    def button_width(self, button_width):
        """Sets the button_width of this IntegrationUpdate.

        With the button style Web Messenger, you have the option of specifying the button width.  # noqa: E501

        :param button_width: The button_width of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._button_width = button_width

    @property
    def button_height(self):
        """Gets the button_height of this IntegrationUpdate.  # noqa: E501

        With the button style Web Messenger, you have the option of specifying the button height.  # noqa: E501

        :return: The button_height of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._button_height

    @button_height.setter
    def button_height(self, button_height):
        """Sets the button_height of this IntegrationUpdate.

        With the button style Web Messenger, you have the option of specifying the button height.  # noqa: E501

        :param button_height: The button_height of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._button_height = button_height

    @property
    def integration_order(self):
        """Gets the integration_order of this IntegrationUpdate.  # noqa: E501

        Array of integration IDs, order will be reflected in the Web Messenger. When set, only integrations from this list will be displayed in the Web Messenger. If unset, all integrations will be displayed.  # noqa: E501

        :return: The integration_order of this IntegrationUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._integration_order

    @integration_order.setter
    def integration_order(self, integration_order):
        """Sets the integration_order of this IntegrationUpdate.

        Array of integration IDs, order will be reflected in the Web Messenger. When set, only integrations from this list will be displayed in the Web Messenger. If unset, all integrations will be displayed.  # noqa: E501

        :param integration_order: The integration_order of this IntegrationUpdate.  # noqa: E501
        :type: list[str]
        """
        if type(integration_order) is Undefined:
            integration_order = None
            self.nulls.discard("integration_order")
        elif integration_order is None:
            self.nulls.add("integration_order")
        else:
            self.nulls.discard("integration_order")

        self._integration_order = integration_order

    @property
    def business_name(self):
        """Gets the business_name of this IntegrationUpdate.  # noqa: E501

        A custom business name for the Web Messenger.  # noqa: E501

        :return: The business_name of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this IntegrationUpdate.

        A custom business name for the Web Messenger.  # noqa: E501

        :param business_name: The business_name of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def business_icon_url(self):
        """Gets the business_icon_url of this IntegrationUpdate.  # noqa: E501

        A custom business icon url for the Web Messenger. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format.  # noqa: E501

        :return: The business_icon_url of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._business_icon_url

    @business_icon_url.setter
    def business_icon_url(self, business_icon_url):
        """Sets the business_icon_url of this IntegrationUpdate.

        A custom business icon url for the Web Messenger. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format.  # noqa: E501

        :param business_icon_url: The business_icon_url of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._business_icon_url = business_icon_url

    @property
    def background_image_url(self):
        """Gets the background_image_url of this IntegrationUpdate.  # noqa: E501

        A background image url for the conversation. Image will be tiled to fit the window.  # noqa: E501

        :return: The background_image_url of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._background_image_url

    @background_image_url.setter
    def background_image_url(self, background_image_url):
        """Sets the background_image_url of this IntegrationUpdate.

        A background image url for the conversation. Image will be tiled to fit the window.  # noqa: E501

        :param background_image_url: The background_image_url of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._background_image_url = background_image_url

    @property
    def origin_whitelist(self):
        """Gets the origin_whitelist of this IntegrationUpdate.  # noqa: E501

        A list of origins to whitelist. When set, only the origins from this list will be able to initialize the Web Messenger. If unset, all origins are whitelisted. The elements in the list should follow the serialized-origin format from RFC 6454: scheme \"://\" host [ \":\" port ], where scheme is http or https.   # noqa: E501

        :return: The origin_whitelist of this IntegrationUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._origin_whitelist

    @origin_whitelist.setter
    def origin_whitelist(self, origin_whitelist):
        """Sets the origin_whitelist of this IntegrationUpdate.

        A list of origins to whitelist. When set, only the origins from this list will be able to initialize the Web Messenger. If unset, all origins are whitelisted. The elements in the list should follow the serialized-origin format from RFC 6454: scheme \"://\" host [ \":\" port ], where scheme is http or https.   # noqa: E501

        :param origin_whitelist: The origin_whitelist of this IntegrationUpdate.  # noqa: E501
        :type: list[str]
        """
        if type(origin_whitelist) is Undefined:
            origin_whitelist = None
            self.nulls.discard("origin_whitelist")
        elif origin_whitelist is None:
            self.nulls.add("origin_whitelist")
        else:
            self.nulls.discard("origin_whitelist")

        self._origin_whitelist = origin_whitelist

    @property
    def prechat_capture(self):
        """Gets the prechat_capture of this IntegrationUpdate.  # noqa: E501

        Object whose properties can be set to specify the add-on’s options. See the [guide](https://docs.smooch.io/guide/web-messenger/#prechat-capture) to learn more about Prechat Capture.  # noqa: E501

        :return: The prechat_capture of this IntegrationUpdate.  # noqa: E501
        :rtype: PrechatCapture
        """
        return self._prechat_capture

    @prechat_capture.setter
    def prechat_capture(self, prechat_capture):
        """Sets the prechat_capture of this IntegrationUpdate.

        Object whose properties can be set to specify the add-on’s options. See the [guide](https://docs.smooch.io/guide/web-messenger/#prechat-capture) to learn more about Prechat Capture.  # noqa: E501

        :param prechat_capture: The prechat_capture of this IntegrationUpdate.  # noqa: E501
        :type: PrechatCapture
        """

        self._prechat_capture = prechat_capture

    @property
    def hsm_fallback_language(self):
        """Gets the hsm_fallback_language of this IntegrationUpdate.  # noqa: E501

        Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info.  # noqa: E501

        :return: The hsm_fallback_language of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._hsm_fallback_language

    @hsm_fallback_language.setter
    def hsm_fallback_language(self, hsm_fallback_language):
        """Sets the hsm_fallback_language of this IntegrationUpdate.

        Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info.  # noqa: E501

        :param hsm_fallback_language: The hsm_fallback_language of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(hsm_fallback_language) is Undefined:
            hsm_fallback_language = None
            self.nulls.discard("hsm_fallback_language")
        elif hsm_fallback_language is None:
            self.nulls.add("hsm_fallback_language")
        else:
            self.nulls.discard("hsm_fallback_language")

        self._hsm_fallback_language = hsm_fallback_language

    @property
    def account_id(self):
        """Gets the account_id of this IntegrationUpdate.  # noqa: E501

        The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction.  # noqa: E501

        :return: The account_id of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this IntegrationUpdate.

        The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction.  # noqa: E501

        :param account_id: The account_id of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(account_id) is Undefined:
            account_id = None
            self.nulls.discard("account_id")
        elif account_id is None:
            self.nulls.add("account_id")
        else:
            self.nulls.discard("account_id")

        self._account_id = account_id

    @property
    def account_management_access_token(self):
        """Gets the account_management_access_token of this IntegrationUpdate.  # noqa: E501

        An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction.  # noqa: E501

        :return: The account_management_access_token of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._account_management_access_token

    @account_management_access_token.setter
    def account_management_access_token(self, account_management_access_token):
        """Sets the account_management_access_token of this IntegrationUpdate.

        An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction.  # noqa: E501

        :param account_management_access_token: The account_management_access_token of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        if type(account_management_access_token) is Undefined:
            account_management_access_token = None
            self.nulls.discard("account_management_access_token")
        elif account_management_access_token is None:
            self.nulls.add("account_management_access_token")
        else:
            self.nulls.discard("account_management_access_token")

        self._account_management_access_token = account_management_access_token

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
        if not isinstance(other, IntegrationUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationUpdate):
            return True

        return self.to_dict() != other.to_dict()
