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


class DeploymentCreate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, hosting=None, base_url=None, username=None, password=None, callback_url=None):
        """
        DeploymentCreate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'hosting': 'str',
            'base_url': 'str',
            'username': 'str',
            'password': 'str',
            'callback_url': 'str'
        }

        self.attribute_map = {
            'hosting': 'hosting',
            'base_url': 'baseUrl',
            'username': 'username',
            'password': 'password',
            'callback_url': 'callbackUrl'
        }

        self._hosting = None
        self._base_url = None
        self._username = None
        self._password = None
        self._callback_url = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if hosting is not None:
          self.hosting = hosting
        if base_url is not None:
          self.base_url = base_url
        if username is not None:
          self.username = username
        if password is not None:
          self.password = password
        if callback_url is not None:
          self.callback_url = callback_url

    @property
    def hosting(self):
        """
        Gets the hosting of this DeploymentCreate.
        The deployment hosting. See [**DeploymentHostingEnum**](Enums.md#DeploymentHostingEnum) for available values.

        :return: The hosting of this DeploymentCreate.
        :rtype: str
        """
        return self._hosting

    @hosting.setter
    def hosting(self, hosting):
        """
        Sets the hosting of this DeploymentCreate.
        The deployment hosting. See [**DeploymentHostingEnum**](Enums.md#DeploymentHostingEnum) for available values.

        :param hosting: The hosting of this DeploymentCreate.
        :type: str
        """
        if hosting is None:
            raise ValueError("Invalid value for `hosting`, must not be `None`")

        self._hosting = hosting

    @property
    def base_url(self):
        """
        Gets the base_url of this DeploymentCreate.
        The base URL to access your WhatsApp EC. Only provide for `self` hosted deployments.

        :return: The base_url of this DeploymentCreate.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """
        Sets the base_url of this DeploymentCreate.
        The base URL to access your WhatsApp EC. Only provide for `self` hosted deployments.

        :param base_url: The base_url of this DeploymentCreate.
        :type: str
        """

        self._base_url = base_url

    @property
    def username(self):
        """
        Gets the username of this DeploymentCreate.
        The username to access your WhatsApp EC. Only provide for `self` hosted deployments.

        :return: The username of this DeploymentCreate.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DeploymentCreate.
        The username to access your WhatsApp EC. Only provide for `self` hosted deployments.

        :param username: The username of this DeploymentCreate.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this DeploymentCreate.
        The password to access your WhatsApp EC. Only provide for `self` hosted deployments.

        :return: The password of this DeploymentCreate.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this DeploymentCreate.
        The password to access your WhatsApp EC. Only provide for `self` hosted deployments.

        :param password: The password of this DeploymentCreate.
        :type: str
        """

        self._password = password

    @property
    def callback_url(self):
        """
        Gets the callback_url of this DeploymentCreate.
        The URL to be called by Smooch when the status of the deployment changes.

        :return: The callback_url of this DeploymentCreate.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """
        Sets the callback_url of this DeploymentCreate.
        The URL to be called by Smooch when the status of the deployment changes.

        :param callback_url: The callback_url of this DeploymentCreate.
        :type: str
        """

        self._callback_url = callback_url

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
        if not isinstance(other, DeploymentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
