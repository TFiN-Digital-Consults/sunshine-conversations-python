# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sunshine_conversations_client.api_client import ApiClient
from sunshine_conversations_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ClientsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_client(self, app_id, user_id_or_external_id, client_create, **kwargs):  # noqa: E501
        """Create Client  # noqa: E501

        Create a client and link it to a channel specified by the `matchCriteria.type`. Note that the client is initially created with a `pending` status. The status of the linking request can be tracked by listening to the `link:match`, `link:success` and `link:failure` webhooks (only available in v1). For more information, see [link-events](https://docs.smooch.io/rest/v1/#link-events).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client(app_id, user_id_or_external_id, client_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str user_id_or_external_id: The user's id or externalId. (required)
        :param ClientCreate client_create: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ClientResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_client_with_http_info(app_id, user_id_or_external_id, client_create, **kwargs)  # noqa: E501

    def create_client_with_http_info(self, app_id, user_id_or_external_id, client_create, **kwargs):  # noqa: E501
        """Create Client  # noqa: E501

        Create a client and link it to a channel specified by the `matchCriteria.type`. Note that the client is initially created with a `pending` status. The status of the linking request can be tracked by listening to the `link:match`, `link:success` and `link:failure` webhooks (only available in v1). For more information, see [link-events](https://docs.smooch.io/rest/v1/#link-events).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_with_http_info(app_id, user_id_or_external_id, client_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str user_id_or_external_id: The user's id or externalId. (required)
        :param ClientCreate client_create: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ClientResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'user_id_or_external_id',
            'client_create'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_client" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `create_client`")  # noqa: E501
        # verify the required parameter 'user_id_or_external_id' is set
        if self.api_client.client_side_validation and ('user_id_or_external_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_id_or_external_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id_or_external_id` when calling `create_client`")  # noqa: E501
        # verify the required parameter 'client_create' is set
        if self.api_client.client_side_validation and ('client_create' not in local_var_params or  # noqa: E501
                                                        local_var_params['client_create'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `client_create` when calling `create_client`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'user_id_or_external_id' in local_var_params:
            path_params['userIdOrExternalId'] = local_var_params['user_id_or_external_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'client_create' in local_var_params:
            body_params = local_var_params['client_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/users/{userIdOrExternalId}/clients', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_clients(self, app_id, user_id_or_external_id, **kwargs):  # noqa: E501
        """List Clients  # noqa: E501

        Get all the clients for a particular user, including both linked clients and pending clients. This API is paginated through [cursor pagination](#section/Introduction/API-pagination-and-records-limits).  ```shell /v2/apps/:appId/users/:userId/clients?page[after]=5ebee0975ac5304b664a12fa ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_clients(app_id, user_id_or_external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str user_id_or_external_id: The user's id or externalId. (required)
        :param Page page: Contains parameters for applying cursor pagination.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ClientListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_clients_with_http_info(app_id, user_id_or_external_id, **kwargs)  # noqa: E501

    def list_clients_with_http_info(self, app_id, user_id_or_external_id, **kwargs):  # noqa: E501
        """List Clients  # noqa: E501

        Get all the clients for a particular user, including both linked clients and pending clients. This API is paginated through [cursor pagination](#section/Introduction/API-pagination-and-records-limits).  ```shell /v2/apps/:appId/users/:userId/clients?page[after]=5ebee0975ac5304b664a12fa ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_clients_with_http_info(app_id, user_id_or_external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str user_id_or_external_id: The user's id or externalId. (required)
        :param Page page: Contains parameters for applying cursor pagination.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ClientListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'user_id_or_external_id',
            'page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_clients" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `list_clients`")  # noqa: E501
        # verify the required parameter 'user_id_or_external_id' is set
        if self.api_client.client_side_validation and ('user_id_or_external_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_id_or_external_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id_or_external_id` when calling `list_clients`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'user_id_or_external_id' in local_var_params:
            path_params['userIdOrExternalId'] = local_var_params['user_id_or_external_id']  # noqa: E501

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/users/{userIdOrExternalId}/clients', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_client(self, app_id, user_id_or_external_id, client_id, **kwargs):  # noqa: E501
        """Remove Client  # noqa: E501

        Remove a particular client and unsubscribe it from all connected conversations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_client(app_id, user_id_or_external_id, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str user_id_or_external_id: The user's id or externalId. (required)
        :param str client_id: The client's id. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.remove_client_with_http_info(app_id, user_id_or_external_id, client_id, **kwargs)  # noqa: E501

    def remove_client_with_http_info(self, app_id, user_id_or_external_id, client_id, **kwargs):  # noqa: E501
        """Remove Client  # noqa: E501

        Remove a particular client and unsubscribe it from all connected conversations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_client_with_http_info(app_id, user_id_or_external_id, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str user_id_or_external_id: The user's id or externalId. (required)
        :param str client_id: The client's id. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'user_id_or_external_id',
            'client_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_client" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `remove_client`")  # noqa: E501
        # verify the required parameter 'user_id_or_external_id' is set
        if self.api_client.client_side_validation and ('user_id_or_external_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_id_or_external_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id_or_external_id` when calling `remove_client`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if self.api_client.client_side_validation and ('client_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['client_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `client_id` when calling `remove_client`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'user_id_or_external_id' in local_var_params:
            path_params['userIdOrExternalId'] = local_var_params['user_id_or_external_id']  # noqa: E501
        if 'client_id' in local_var_params:
            path_params['clientId'] = local_var_params['client_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/users/{userIdOrExternalId}/clients/{clientId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
