# smooch-python

The Python package for the Smooch API.

The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

This SDK is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project using the [Smooch api spec](https://github.com/smooch/api-spec).

## Requirements

Python 2.7 or 3.4+

## Installation
```sh
pip install smooch
```
(you may need to run `pip` with root permission: `sudo pip install smooch`)

## Getting Started

### Authentication with JSON Web Tokens (JWTs)

JSON Web Tokens (JWTs) are an industry standard authentication mechanism. A great introduction to the technology is available [here](https://jwt.io/introduction/), and a broad set of supported JWT libraries for a variety of languages and platforms are available.

A JWT is composed of a header, a payload, and a signature. The payload contains information called claims which describe the subject to whom the token was issued.

Before you can make calls to the Smooch API, you'll need to create a JWT that proves you are authorized to use the API.

#### **Step 1** Generate a KEY ID and SECRET on the settings tab in the [Smooch Dashboard](https://app.smooch.io/).

![secret key and id](https://docs.smooch.io/images/secret_keys.png)

 #### **Step 2** Generate the JWT

Using the [pyjwt](https://github.com/jpadilla/pyjwt/) module:

```python
import jwt
token_bytes = jwt.encode({'scope': 'app'},
                         'SECRET',
                         algorithm='HS256',
                         headers={'kid': 'KEY_ID'})
token = token_bytes.decode('utf-8')
```

### Running the code

```python
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_create_body = smooch.AppCreate() # AppCreate | Body for a createApp request.

try:
    api_response = api_instance.create_app(app_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->create_app: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.smooch.io/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppApi* | [**create_app**](docs/AppApi.md#create_app) | **POST** /apps | 
*AppApi* | [**create_secret_key**](docs/AppApi.md#create_secret_key) | **POST** /apps/{appId}/keys | 
*AppApi* | [**delete_app**](docs/AppApi.md#delete_app) | **DELETE** /apps/{appId} | 
*AppApi* | [**delete_secret_key**](docs/AppApi.md#delete_secret_key) | **DELETE** /apps/{appId}/keys/{keyId} | 
*AppApi* | [**get_app**](docs/AppApi.md#get_app) | **GET** /apps/{appId} | 
*AppApi* | [**get_app_jwt**](docs/AppApi.md#get_app_jwt) | **GET** /apps/{appId}/keys/{keyId}/jwt | 
*AppApi* | [**get_secret_key**](docs/AppApi.md#get_secret_key) | **GET** /apps/{appId}/keys/{keyId} | 
*AppApi* | [**list_apps**](docs/AppApi.md#list_apps) | **GET** /apps | 
*AppApi* | [**list_secret_keys**](docs/AppApi.md#list_secret_keys) | **GET** /apps/{appId}/keys | 
*AppApi* | [**update_app**](docs/AppApi.md#update_app) | **PUT** /apps/{appId} | 
*AppUserApi* | [**app_user_device_update**](docs/AppUserApi.md#app_user_device_update) | **PUT** /appusers/{userId}/devices/{deviceId} | 
*AppUserApi* | [**delete_app_user_profile**](docs/AppUserApi.md#delete_app_user_profile) | **DELETE** /appusers/{userId}/profile | 
*AppUserApi* | [**get_app_user**](docs/AppUserApi.md#get_app_user) | **GET** /appusers/{userId} | 
*AppUserApi* | [**get_app_user_entity_ids**](docs/AppUserApi.md#get_app_user_entity_ids) | **GET** /appusers/{userId}/channels | 
*AppUserApi* | [**link_app_user**](docs/AppUserApi.md#link_app_user) | **POST** /appusers/{userId}/channels | 
*AppUserApi* | [**post_image_message**](docs/AppUserApi.md#post_image_message) | **POST** /appusers/{userId}/images | 
*AppUserApi* | [**pre_create_app_user**](docs/AppUserApi.md#pre_create_app_user) | **POST** /appusers | 
*AppUserApi* | [**track_event**](docs/AppUserApi.md#track_event) | **POST** /appusers/{userId}/events | 
*AppUserApi* | [**unlink_app_user**](docs/AppUserApi.md#unlink_app_user) | **DELETE** /appusers/{userId}/channels/{channel} | 
*AppUserApi* | [**update_app_user**](docs/AppUserApi.md#update_app_user) | **PUT** /appusers/{userId} | 
*AttachmentsApi* | [**upload_attachment**](docs/AttachmentsApi.md#upload_attachment) | **POST** /apps/{appId}/attachments | 
*ConversationApi* | [**delete_messages**](docs/ConversationApi.md#delete_messages) | **DELETE** /appusers/{userId}/messages | 
*ConversationApi* | [**get_messages**](docs/ConversationApi.md#get_messages) | **GET** /appusers/{userId}/messages | 
*ConversationApi* | [**post_message**](docs/ConversationApi.md#post_message) | **POST** /appusers/{userId}/messages | 
*ConversationApi* | [**reset_unread_count**](docs/ConversationApi.md#reset_unread_count) | **POST** /appusers/{userId}/conversation/read | 
*ConversationApi* | [**trigger_typing_activity**](docs/ConversationApi.md#trigger_typing_activity) | **POST** /appusers/{userId}/conversation/activity | 
*InitApi* | [**init**](docs/InitApi.md#init) | **POST** /init | 
*IntegrationApi* | [**create_integration**](docs/IntegrationApi.md#create_integration) | **POST** /apps/{appId}/integrations | 
*IntegrationApi* | [**create_integration_menu**](docs/IntegrationApi.md#create_integration_menu) | **POST** /apps/{appId}/integrations/{integrationId}/menu | 
*IntegrationApi* | [**delete_integration**](docs/IntegrationApi.md#delete_integration) | **DELETE** /apps/{appId}/integrations/{integrationId} | 
*IntegrationApi* | [**delete_integration_menu**](docs/IntegrationApi.md#delete_integration_menu) | **DELETE** /apps/{appId}/integrations/{integrationId}/menu | 
*IntegrationApi* | [**get_integration**](docs/IntegrationApi.md#get_integration) | **GET** /apps/{appId}/integrations/{integrationId} | 
*IntegrationApi* | [**get_integration_menu**](docs/IntegrationApi.md#get_integration_menu) | **GET** /apps/{appId}/integrations/{integrationId}/menu | 
*IntegrationApi* | [**list_integrations**](docs/IntegrationApi.md#list_integrations) | **GET** /apps/{appId}/integrations | 
*IntegrationApi* | [**update_integration_menu**](docs/IntegrationApi.md#update_integration_menu) | **PUT** /apps/{appId}/integrations/{integrationId}/menu | 
*MenuApi* | [**delete_menu**](docs/MenuApi.md#delete_menu) | **DELETE** /menu | 
*MenuApi* | [**get_menu**](docs/MenuApi.md#get_menu) | **GET** /menu | 
*MenuApi* | [**update_menu**](docs/MenuApi.md#update_menu) | **PUT** /menu | 
*WebhookApi* | [**create_webhook**](docs/WebhookApi.md#create_webhook) | **POST** /apps/{appId}/webhooks | 
*WebhookApi* | [**delete_webhook**](docs/WebhookApi.md#delete_webhook) | **DELETE** /apps/{appId}/webhooks/{webhookId} | 
*WebhookApi* | [**get_webhook**](docs/WebhookApi.md#get_webhook) | **GET** /apps/{appId}/webhooks/{webhookId} | 
*WebhookApi* | [**list_webhooks**](docs/WebhookApi.md#list_webhooks) | **GET** /apps/{appId}/webhooks | 
*WebhookApi* | [**update_webhook**](docs/WebhookApi.md#update_webhook) | **PUT** /apps/{appId}/webhooks/{webhookId} | 


## Documentation For Models

 - [Action](docs/Action.md)
 - [App](docs/App.md)
 - [AppCreate](docs/AppCreate.md)
 - [AppResponse](docs/AppResponse.md)
 - [AppSettings](docs/AppSettings.md)
 - [AppUpdate](docs/AppUpdate.md)
 - [AppUser](docs/AppUser.md)
 - [AppUserLink](docs/AppUserLink.md)
 - [AppUserPreCreate](docs/AppUserPreCreate.md)
 - [AppUserResponse](docs/AppUserResponse.md)
 - [AppUserUpdate](docs/AppUserUpdate.md)
 - [AttachmentResponse](docs/AttachmentResponse.md)
 - [Client](docs/Client.md)
 - [ClientInfo](docs/ClientInfo.md)
 - [Conversation](docs/Conversation.md)
 - [Destination](docs/Destination.md)
 - [DeviceInit](docs/DeviceInit.md)
 - [DeviceResponse](docs/DeviceResponse.md)
 - [DeviceUpdate](docs/DeviceUpdate.md)
 - [DisplaySettings](docs/DisplaySettings.md)
 - [Event](docs/Event.md)
 - [GetMessagesResponse](docs/GetMessagesResponse.md)
 - [Init](docs/Init.md)
 - [InitResponse](docs/InitResponse.md)
 - [Integration](docs/Integration.md)
 - [IntegrationCreate](docs/IntegrationCreate.md)
 - [IntegrationResponse](docs/IntegrationResponse.md)
 - [JwtResponse](docs/JwtResponse.md)
 - [ListAppsResponse](docs/ListAppsResponse.md)
 - [ListIntegrationsResponse](docs/ListIntegrationsResponse.md)
 - [ListSecretKeysResponse](docs/ListSecretKeysResponse.md)
 - [ListWebhooksResponse](docs/ListWebhooksResponse.md)
 - [Menu](docs/Menu.md)
 - [MenuItem](docs/MenuItem.md)
 - [MenuResponse](docs/MenuResponse.md)
 - [Message](docs/Message.md)
 - [MessageItem](docs/MessageItem.md)
 - [MessagePost](docs/MessagePost.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [SecretKey](docs/SecretKey.md)
 - [SecretKeyCreate](docs/SecretKeyCreate.md)
 - [SecretKeyResponse](docs/SecretKeyResponse.md)
 - [TrackEventResponse](docs/TrackEventResponse.md)
 - [TypingActivityTrigger](docs/TypingActivityTrigger.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookCreate](docs/WebhookCreate.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhookUpdate](docs/WebhookUpdate.md)


## Documentation For Authorization


## jwt

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

