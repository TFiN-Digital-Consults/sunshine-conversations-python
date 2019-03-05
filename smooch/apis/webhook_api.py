# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class WebhookApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_webhook(self, app_id, webhook_create_body, **kwargs):
        """
        Create a webhook for the specified app.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_webhook(app_id, webhook_create_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param WebhookCreate webhook_create_body: Body for a createWebhook request.  (required)
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_webhook_with_http_info(app_id, webhook_create_body, **kwargs)
        else:
            (data) = self.create_webhook_with_http_info(app_id, webhook_create_body, **kwargs)
            return data

    def create_webhook_with_http_info(self, app_id, webhook_create_body, **kwargs):
        """
        Create a webhook for the specified app.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_webhook_with_http_info(app_id, webhook_create_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param WebhookCreate webhook_create_body: Body for a createWebhook request.  (required)
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'webhook_create_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `create_webhook`")
        # verify the required parameter 'webhook_create_body' is set
        if ('webhook_create_body' not in params) or (params['webhook_create_body'] is None):
            raise ValueError("Missing the required parameter `webhook_create_body` when calling `create_webhook`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook_create_body' in params:
            body_params = params['webhook_create_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/webhooks', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhookResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_webhook(self, app_id, webhook_id, **kwargs):
        """
        Delete the specified webhook.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_webhook(app_id, webhook_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str webhook_id: Identifies the webhook. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_webhook_with_http_info(app_id, webhook_id, **kwargs)
        else:
            (data) = self.delete_webhook_with_http_info(app_id, webhook_id, **kwargs)
            return data

    def delete_webhook_with_http_info(self, app_id, webhook_id, **kwargs):
        """
        Delete the specified webhook.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_webhook_with_http_info(app_id, webhook_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str webhook_id: Identifies the webhook. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'webhook_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `delete_webhook`")
        # verify the required parameter 'webhook_id' is set
        if ('webhook_id' not in params) or (params['webhook_id'] is None):
            raise ValueError("Missing the required parameter `webhook_id` when calling `delete_webhook`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']
        if 'webhook_id' in params:
            path_params['webhookId'] = params['webhook_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/webhooks/{webhookId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_webhook(self, app_id, webhook_id, **kwargs):
        """
        Get the specified webhook.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_webhook(app_id, webhook_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str webhook_id: Identifies the webhook. (required)
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_webhook_with_http_info(app_id, webhook_id, **kwargs)
        else:
            (data) = self.get_webhook_with_http_info(app_id, webhook_id, **kwargs)
            return data

    def get_webhook_with_http_info(self, app_id, webhook_id, **kwargs):
        """
        Get the specified webhook.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_webhook_with_http_info(app_id, webhook_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str webhook_id: Identifies the webhook. (required)
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'webhook_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `get_webhook`")
        # verify the required parameter 'webhook_id' is set
        if ('webhook_id' not in params) or (params['webhook_id'] is None):
            raise ValueError("Missing the required parameter `webhook_id` when calling `get_webhook`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']
        if 'webhook_id' in params:
            path_params['webhookId'] = params['webhook_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/webhooks/{webhookId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhookResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_webhooks(self, app_id, **kwargs):
        """
        List webhooks for the specified app.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_webhooks(app_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :return: ListWebhooksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_webhooks_with_http_info(app_id, **kwargs)
        else:
            (data) = self.list_webhooks_with_http_info(app_id, **kwargs)
            return data

    def list_webhooks_with_http_info(self, app_id, **kwargs):
        """
        List webhooks for the specified app.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_webhooks_with_http_info(app_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :return: ListWebhooksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_webhooks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `list_webhooks`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/webhooks', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListWebhooksResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_webhook(self, app_id, webhook_id, webhook_update_body, **kwargs):
        """
        Update the specified webhook.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_webhook(app_id, webhook_id, webhook_update_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str webhook_id: Identifies the webhook. (required)
        :param WebhookUpdate webhook_update_body: Body for an updateWebhook request.  (required)
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_webhook_with_http_info(app_id, webhook_id, webhook_update_body, **kwargs)
        else:
            (data) = self.update_webhook_with_http_info(app_id, webhook_id, webhook_update_body, **kwargs)
            return data

    def update_webhook_with_http_info(self, app_id, webhook_id, webhook_update_body, **kwargs):
        """
        Update the specified webhook.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_webhook_with_http_info(app_id, webhook_id, webhook_update_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str webhook_id: Identifies the webhook. (required)
        :param WebhookUpdate webhook_update_body: Body for an updateWebhook request.  (required)
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'webhook_id', 'webhook_update_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `update_webhook`")
        # verify the required parameter 'webhook_id' is set
        if ('webhook_id' not in params) or (params['webhook_id'] is None):
            raise ValueError("Missing the required parameter `webhook_id` when calling `update_webhook`")
        # verify the required parameter 'webhook_update_body' is set
        if ('webhook_update_body' not in params) or (params['webhook_update_body'] is None):
            raise ValueError("Missing the required parameter `webhook_update_body` when calling `update_webhook`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']
        if 'webhook_id' in params:
            path_params['webhookId'] = params['webhook_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook_update_body' in params:
            body_params = params['webhook_update_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/webhooks/{webhookId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WebhookResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
