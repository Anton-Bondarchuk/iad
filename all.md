# Объединенная документация
Создано: sob, 19 kwi 2025, 15:14:28 CEST



## Файл: docs/Category.md

# Category


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор категории | [optional] 
**name** | **str** | Название категории | [optional] 
**parent_id** | **int** | Идентификатор родительской категории | [optional] 
**children** | [**List[Category]**](Category.md) | Дочерние категории | [optional] 

## Example

```python
from pc_assembler_client.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_from_dict = Category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/CategoryParameter.md

# CategoryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор параметра | [optional] 
**name** | **str** | Название параметра | [optional] 
**type** | **str** | Тип параметра | [optional] 
**unit** | **str** | Единица измерения | [optional] 
**required** | **bool** | Обязательность параметра | [optional] 
**values** | **List[str]** | Допустимые значения для ENUM параметров | [optional] 

## Example

```python
from pc_assembler_client.models.category_parameter import CategoryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryParameter from a JSON string
category_parameter_instance = CategoryParameter.from_json(json)
# print the JSON string representation of the object
print(CategoryParameter.to_json())

# convert the object into a dict
category_parameter_dict = category_parameter_instance.to_dict()
# create an instance of CategoryParameter from a dict
category_parameter_from_dict = CategoryParameter.from_dict(category_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/CategoryParametersResponse.md

# CategoryParametersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** |  | [optional] 
**parameters** | [**List[CategoryParameter]**](CategoryParameter.md) |  | [optional] 

## Example

```python
from pc_assembler_client.models.category_parameters_response import CategoryParametersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryParametersResponse from a JSON string
category_parameters_response_instance = CategoryParametersResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryParametersResponse.to_json())

# convert the object into a dict
category_parameters_response_dict = category_parameters_response_instance.to_dict()
# create an instance of CategoryParametersResponse from a dict
category_parameters_response_from_dict = CategoryParametersResponse.from_dict(category_parameters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/CategoryTreeResponse.md

# CategoryTreeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[Category]**](Category.md) |  | [optional] 

## Example

```python
from pc_assembler_client.models.category_tree_response import CategoryTreeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryTreeResponse from a JSON string
category_tree_response_instance = CategoryTreeResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryTreeResponse.to_json())

# convert the object into a dict
category_tree_response_dict = category_tree_response_instance.to_dict()
# create an instance of CategoryTreeResponse from a dict
category_tree_response_from_dict = CategoryTreeResponse.from_dict(category_tree_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/DefaultApi.md

# pc_assembler_client.DefaultApi

All URIs are relative to *https://api.partner.market.yandex.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaign_offers**](DefaultApi.md#get_campaign_offers) | **GET** /campaigns/{campaignId}/offers | Список товаров
[**get_category_parameters**](DefaultApi.md#get_category_parameters) | **GET** /category/{categoryId}/parameters | Параметры категории
[**get_category_tree**](DefaultApi.md#get_category_tree) | **GET** /categories/tree | Дерево категорий
[**get_model_by_id**](DefaultApi.md#get_model_by_id) | **GET** /models/{modelId} | Информация о модели
[**get_model_offers**](DefaultApi.md#get_model_offers) | **GET** /models/{modelId}/offers | Предложения для модели
[**get_models**](DefaultApi.md#get_models) | **GET** /models | Информация о моделях
[**get_offer_prices**](DefaultApi.md#get_offer_prices) | **GET** /campaigns/{campaignId}/offer-prices | Список цен
[**get_offer_stocks**](DefaultApi.md#get_offer_stocks) | **POST** /campaigns/{campaignId}/offers/stocks | Информация о наличии товаров


# **get_campaign_offers**
> GetCampaignOffersResponse get_campaign_offers(campaign_id, query=query, shop_category_id=shop_category_id, page=page, page_size=page_size)

Список товаров

Возвращает список товаров магазина

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (OAuth):

```python
import pc_assembler_client
from pc_assembler_client.models.get_campaign_offers_response import GetCampaignOffersResponse
from pc_assembler_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.partner.market.yandex.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pc_assembler_client.Configuration(
    host = "https://api.partner.market.yandex.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pc_assembler_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pc_assembler_client.DefaultApi(api_client)
    campaign_id = 56 # int | Идентификатор кампании
    query = 'query_example' # str | Поисковый запрос (optional)
    shop_category_id = 'shop_category_id_example' # str | Идентификатор категории магазина (optional)
    page = 1 # int | Номер страницы результатов (optional) (default to 1)
    page_size = 20 # int | Количество элементов на странице (optional) (default to 20)

    try:
        # Список товаров
        api_response = api_instance.get_campaign_offers(campaign_id, query=query, shop_category_id=shop_category_id, page=page, page_size=page_size)
        print("The response of DefaultApi->get_campaign_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_campaign_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Идентификатор кампании | 
 **query** | **str**| Поисковый запрос | [optional] 
 **shop_category_id** | **str**| Идентификатор категории магазина | [optional] 
 **page** | **int**| Номер страницы результатов | [optional] [default to 1]
 **page_size** | **int**| Количество элементов на странице | [optional] [default to 20]

### Return type

[**GetCampaignOffersResponse**](GetCampaignOffersResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_parameters**
> CategoryParametersResponse get_category_parameters(category_id, language=language)

Параметры категории

Возвращает список параметров для указанной категории

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (OAuth):

```python
import pc_assembler_client
from pc_assembler_client.models.category_parameters_response import CategoryParametersResponse
from pc_assembler_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.partner.market.yandex.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pc_assembler_client.Configuration(
    host = "https://api.partner.market.yandex.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pc_assembler_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pc_assembler_client.DefaultApi(api_client)
    category_id = 56 # int | Идентификатор категории
    language = 'ru' # str | Язык ответа (optional) (default to 'ru')

    try:
        # Параметры категории
        api_response = api_instance.get_category_parameters(category_id, language=language)
        print("The response of DefaultApi->get_category_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_category_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Идентификатор категории | 
 **language** | **str**| Язык ответа | [optional] [default to &#39;ru&#39;]

### Return type

[**CategoryParametersResponse**](CategoryParametersResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_tree**
> CategoryTreeResponse get_category_tree(language=language)

Дерево категорий

Возвращает дерево категорий товаров

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (OAuth):

```python
import pc_assembler_client
from pc_assembler_client.models.category_tree_response import CategoryTreeResponse
from pc_assembler_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.partner.market.yandex.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pc_assembler_client.Configuration(
    host = "https://api.partner.market.yandex.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pc_assembler_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pc_assembler_client.DefaultApi(api_client)
    language = 'ru' # str | Язык ответа (optional) (default to 'ru')

    try:
        # Дерево категорий
        api_response = api_instance.get_category_tree(language=language)
        print("The response of DefaultApi->get_category_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_category_tree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Язык ответа | [optional] [default to &#39;ru&#39;]

### Return type

[**CategoryTreeResponse**](CategoryTreeResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_by_id**
> GetModelResponse get_model_by_id(model_id)

Информация о модели

Возвращает информацию о конкретной модели по ее идентификатору

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (OAuth):

```python
import pc_assembler_client
from pc_assembler_client.models.get_model_response import GetModelResponse
from pc_assembler_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.partner.market.yandex.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pc_assembler_client.Configuration(
    host = "https://api.partner.market.yandex.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pc_assembler_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pc_assembler_client.DefaultApi(api_client)
    model_id = 56 # int | Идентификатор модели

    try:
        # Информация о модели
        api_response = api_instance.get_model_by_id(model_id)
        print("The response of DefaultApi->get_model_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_model_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| Идентификатор модели | 

### Return type

[**GetModelResponse**](GetModelResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_offers**
> GetModelOffersResponse get_model_offers(model_id, region_id=region_id, currency=currency)

Предложения для модели

Возвращает информацию о предложениях для конкретной модели

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (OAuth):

```python
import pc_assembler_client
from pc_assembler_client.models.get_model_offers_response import GetModelOffersResponse
from pc_assembler_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.partner.market.yandex.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pc_assembler_client.Configuration(
    host = "https://api.partner.market.yandex.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pc_assembler_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pc_assembler_client.DefaultApi(api_client)
    model_id = 56 # int | Идентификатор модели
    region_id = 56 # int | Идентификатор региона для фильтрации предложений (optional)
    currency = RUR # str | Валюта, в которой отображаются цены (optional) (default to RUR)

    try:
        # Предложения для модели
        api_response = api_instance.get_model_offers(model_id, region_id=region_id, currency=currency)
        print("The response of DefaultApi->get_model_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_model_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| Идентификатор модели | 
 **region_id** | **int**| Идентификатор региона для фильтрации предложений | [optional] 
 **currency** | **str**| Валюта, в которой отображаются цены | [optional] [default to RUR]

### Return type

[**GetModelOffersResponse**](GetModelOffersResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> GetModelsResponse get_models(category_id=category_id, page=page, page_size=page_size, search_query=search_query)

Информация о моделях

Возвращает информацию о моделях товаров

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (OAuth):

```python
import pc_assembler_client
from pc_assembler_client.models.get_models_response import GetModelsResponse
from pc_assembler_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.partner.market.yandex.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pc_assembler_client.Configuration(
    host = "https://api.partner.market.yandex.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pc_assembler_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pc_assembler_client.DefaultApi(api_client)
    category_id = 56 # int | Идентификатор категории (optional)
    page = 1 # int | Номер страницы результатов (optional) (default to 1)
    page_size = 20 # int | Количество элементов на странице (optional) (default to 20)
    search_query = 'search_query_example' # str | Поисковый запрос (optional)

    try:
        # Информация о моделях
        api_response = api_instance.get_models(category_id=category_id, page=page, page_size=page_size, search_query=search_query)
        print("The response of DefaultApi->get_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Идентификатор категории | [optional] 
 **page** | **int**| Номер страницы результатов | [optional] [default to 1]
 **page_size** | **int**| Количество элементов на странице | [optional] [default to 20]
 **search_query** | **str**| Поисковый запрос | [optional] 

### Return type

[**GetModelsResponse**](GetModelsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_prices**
> GetOfferPricesResponse get_offer_prices(campaign_id, page=page, page_size=page_size)

Список цен

Возвращает список цен на товары

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (OAuth):

```python
import pc_assembler_client
from pc_assembler_client.models.get_offer_prices_response import GetOfferPricesResponse
from pc_assembler_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.partner.market.yandex.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pc_assembler_client.Configuration(
    host = "https://api.partner.market.yandex.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pc_assembler_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pc_assembler_client.DefaultApi(api_client)
    campaign_id = 56 # int | Идентификатор кампании
    page = 1 # int | Номер страницы результатов (optional) (default to 1)
    page_size = 20 # int | Количество элементов на странице (optional) (default to 20)

    try:
        # Список цен
        api_response = api_instance.get_offer_prices(campaign_id, page=page, page_size=page_size)
        print("The response of DefaultApi->get_offer_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_offer_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Идентификатор кампании | 
 **page** | **int**| Номер страницы результатов | [optional] [default to 1]
 **page_size** | **int**| Количество элементов на странице | [optional] [default to 20]

### Return type

[**GetOfferPricesResponse**](GetOfferPricesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_stocks**
> GetStocksResponse get_offer_stocks(campaign_id, get_stocks_request)

Информация о наличии товаров

Возвращает информацию о наличии товаров на складах

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (OAuth):

```python
import pc_assembler_client
from pc_assembler_client.models.get_stocks_request import GetStocksRequest
from pc_assembler_client.models.get_stocks_response import GetStocksResponse
from pc_assembler_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.partner.market.yandex.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = pc_assembler_client.Configuration(
    host = "https://api.partner.market.yandex.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pc_assembler_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pc_assembler_client.DefaultApi(api_client)
    campaign_id = 56 # int | Идентификатор кампании
    get_stocks_request = pc_assembler_client.GetStocksRequest() # GetStocksRequest | 

    try:
        # Информация о наличии товаров
        api_response = api_instance.get_offer_stocks(campaign_id, get_stocks_request)
        print("The response of DefaultApi->get_offer_stocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_offer_stocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Идентификатор кампании | 
 **get_stocks_request** | [**GetStocksRequest**](GetStocksRequest.md)|  | 

### Return type

[**GetStocksResponse**](GetStocksResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



---



## Файл: docs/Error.md

# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Код ошибки | [optional] 
**message** | **str** | Сообщение об ошибке | [optional] 
**details** | **str** | Дополнительные детали ошибки | [optional] 

## Example

```python
from pc_assembler_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/GetCampaignOffersResponse.md

# GetCampaignOffersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pager** | [**Pager**](Pager.md) |  | [optional] 
**offers** | [**List[Offer]**](Offer.md) |  | [optional] 

## Example

```python
from pc_assembler_client.models.get_campaign_offers_response import GetCampaignOffersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaignOffersResponse from a JSON string
get_campaign_offers_response_instance = GetCampaignOffersResponse.from_json(json)
# print the JSON string representation of the object
print(GetCampaignOffersResponse.to_json())

# convert the object into a dict
get_campaign_offers_response_dict = get_campaign_offers_response_instance.to_dict()
# create an instance of GetCampaignOffersResponse from a dict
get_campaign_offers_response_from_dict = GetCampaignOffersResponse.from_dict(get_campaign_offers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/GetModelOffersResponse.md

# GetModelOffersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pager** | [**Pager**](Pager.md) |  | [optional] 
**offers** | [**List[Offer]**](Offer.md) |  | [optional] 

## Example

```python
from pc_assembler_client.models.get_model_offers_response import GetModelOffersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelOffersResponse from a JSON string
get_model_offers_response_instance = GetModelOffersResponse.from_json(json)
# print the JSON string representation of the object
print(GetModelOffersResponse.to_json())

# convert the object into a dict
get_model_offers_response_dict = get_model_offers_response_instance.to_dict()
# create an instance of GetModelOffersResponse from a dict
get_model_offers_response_from_dict = GetModelOffersResponse.from_dict(get_model_offers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/GetModelResponse.md

# GetModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**Model**](Model.md) |  | [optional] 

## Example

```python
from pc_assembler_client.models.get_model_response import GetModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelResponse from a JSON string
get_model_response_instance = GetModelResponse.from_json(json)
# print the JSON string representation of the object
print(GetModelResponse.to_json())

# convert the object into a dict
get_model_response_dict = get_model_response_instance.to_dict()
# create an instance of GetModelResponse from a dict
get_model_response_from_dict = GetModelResponse.from_dict(get_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/GetModelsResponse.md

# GetModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pager** | [**Pager**](Pager.md) |  | [optional] 
**models** | [**List[Model]**](Model.md) |  | [optional] 

## Example

```python
from pc_assembler_client.models.get_models_response import GetModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelsResponse from a JSON string
get_models_response_instance = GetModelsResponse.from_json(json)
# print the JSON string representation of the object
print(GetModelsResponse.to_json())

# convert the object into a dict
get_models_response_dict = get_models_response_instance.to_dict()
# create an instance of GetModelsResponse from a dict
get_models_response_from_dict = GetModelsResponse.from_dict(get_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/GetOfferPricesResponse.md

# GetOfferPricesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pager** | [**Pager**](Pager.md) |  | [optional] 
**prices** | [**List[Price]**](Price.md) |  | [optional] 

## Example

```python
from pc_assembler_client.models.get_offer_prices_response import GetOfferPricesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOfferPricesResponse from a JSON string
get_offer_prices_response_instance = GetOfferPricesResponse.from_json(json)
# print the JSON string representation of the object
print(GetOfferPricesResponse.to_json())

# convert the object into a dict
get_offer_prices_response_dict = get_offer_prices_response_instance.to_dict()
# create an instance of GetOfferPricesResponse from a dict
get_offer_prices_response_from_dict = GetOfferPricesResponse.from_dict(get_offer_prices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/GetStocksRequest.md

# GetStocksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_ids** | **List[str]** | Список идентификаторов предложений | [optional] 
**warehouse_ids** | **List[int]** | Список идентификаторов складов (опционально) | [optional] 

## Example

```python
from pc_assembler_client.models.get_stocks_request import GetStocksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStocksRequest from a JSON string
get_stocks_request_instance = GetStocksRequest.from_json(json)
# print the JSON string representation of the object
print(GetStocksRequest.to_json())

# convert the object into a dict
get_stocks_request_dict = get_stocks_request_instance.to_dict()
# create an instance of GetStocksRequest from a dict
get_stocks_request_from_dict = GetStocksRequest.from_dict(get_stocks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/GetStocksResponse.md

# GetStocksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stocks** | [**List[Stock]**](Stock.md) |  | [optional] 

## Example

```python
from pc_assembler_client.models.get_stocks_response import GetStocksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStocksResponse from a JSON string
get_stocks_response_instance = GetStocksResponse.from_json(json)
# print the JSON string representation of the object
print(GetStocksResponse.to_json())

# convert the object into a dict
get_stocks_response_dict = get_stocks_response_instance.to_dict()
# create an instance of GetStocksResponse from a dict
get_stocks_response_from_dict = GetStocksResponse.from_dict(get_stocks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/Model.md

# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор модели | [optional] 
**name** | **str** | Название модели | [optional] 
**category_id** | **int** | Идентификатор категории | [optional] 
**vendor** | **str** | Производитель | [optional] 
**description** | **str** | Описание модели | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | Параметры модели | [optional] 
**pictures** | **List[str]** | Изображения модели | [optional] 
**min_price** | **float** | Минимальная цена | [optional] 
**average_price** | **float** | Средняя цена | [optional] 
**offers_count** | **int** | Количество предложений | [optional] 

## Example

```python
from pc_assembler_client.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/Offer.md

# Offer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор предложения | [optional] 
**model_id** | **int** | Идентификатор модели | [optional] 
**name** | **str** | Название предложения | [optional] 
**shop_name** | **str** | Название магазина | [optional] 
**price** | **float** | Цена | [optional] 
**original_price** | **float** | Оригинальная цена (до скидки) | [optional] 
**discount** | **int** | Скидка в процентах | [optional] 
**is_available** | **bool** | Доступность товара | [optional] 
**warranty** | **bool** | Наличие гарантии | [optional] 
**description** | **str** | Описание предложения | [optional] 
**url** | **str** | URL предложения | [optional] 
**pictures** | **List[str]** | Изображения предложения | [optional] 

## Example

```python
from pc_assembler_client.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print(Offer.to_json())

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_from_dict = Offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/Pager.md

# Pager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** | Текущая страница | [optional] 
**page_size** | **int** | Размер страницы | [optional] 
**total** | **int** | Общее количество элементов | [optional] 
**total_pages** | **int** | Общее количество страниц | [optional] 

## Example

```python
from pc_assembler_client.models.pager import Pager

# TODO update the JSON string below
json = "{}"
# create an instance of Pager from a JSON string
pager_instance = Pager.from_json(json)
# print the JSON string representation of the object
print(Pager.to_json())

# convert the object into a dict
pager_dict = pager_instance.to_dict()
# create an instance of Pager from a dict
pager_from_dict = Pager.from_dict(pager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/Parameter.md

# Parameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор параметра | [optional] 
**name** | **str** | Название параметра | [optional] 
**value** | **str** | Значение параметра | [optional] 
**unit** | **str** | Единица измерения | [optional] 

## Example

```python
from pc_assembler_client.models.parameter import Parameter

# TODO update the JSON string below
json = "{}"
# create an instance of Parameter from a JSON string
parameter_instance = Parameter.from_json(json)
# print the JSON string representation of the object
print(Parameter.to_json())

# convert the object into a dict
parameter_dict = parameter_instance.to_dict()
# create an instance of Parameter from a dict
parameter_from_dict = Parameter.from_dict(parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/Price.md

# Price


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Идентификатор предложения | [optional] 
**price** | **float** | Цена | [optional] 
**discount_price** | **float** | Цена со скидкой | [optional] 
**currency_id** | **str** | Код валюты (RUR, USD, EUR) | [optional] 
**updated_at** | **datetime** | Дата и время обновления цены | [optional] 

## Example

```python
from pc_assembler_client.models.price import Price

# TODO update the JSON string below
json = "{}"
# create an instance of Price from a JSON string
price_instance = Price.from_json(json)
# print the JSON string representation of the object
print(Price.to_json())

# convert the object into a dict
price_dict = price_instance.to_dict()
# create an instance of Price from a dict
price_from_dict = Price.from_dict(price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---



## Файл: docs/Stock.md

# Stock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Идентификатор предложения | [optional] 
**warehouse_id** | **int** | Идентификатор склада | [optional] 
**count** | **int** | Количество товара | [optional] 
**updated_at** | **datetime** | Дата и время обновления информации о наличии | [optional] 

## Example

```python
from pc_assembler_client.models.stock import Stock

# TODO update the JSON string below
json = "{}"
# create an instance of Stock from a JSON string
stock_instance = Stock.from_json(json)
# print the JSON string representation of the object
print(Stock.to_json())

# convert the object into a dict
stock_dict = stock_instance.to_dict()
# create an instance of Stock from a dict
stock_from_dict = Stock.from_dict(stock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)




---

