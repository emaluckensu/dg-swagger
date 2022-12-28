# coding: utf-8

"""
    Developer API - DataGalaxy

    # Overview  The DataGalaxy API gives you access to CRUD actions on your metamodel, users and licenses.  Our API is organized around REST. It accepts and returns JSON-encoded data, and uses standard HTTP response codes, verbs and authentication with access tokens.  To get the full picture of DataGalaxy, please feel free to consult our <a href='https://datagalaxy.freshdesk.com/solution/articles/35000131583--basics-datagalaxy-s-main-concepts-/en' target='_new'>online documentation.</a><br/> Have a look at our <a href='https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000151096--quick-start-datagalaxy-public-api-v2' target='_new'>step by step guide</a> for a quick start on how to use our API.  ## Response Status Codes  | Status Code  | Description       | Notes | | ------------ | ----------------- | ----- | | 200          | OK                | The request was successful | | 400          | Bad Request       | Incoming request contains parameters that might not be valid | | 401          | Unauthorized      | The supplied credentials, if any, are not sufficient to access the resource | | 404          | Not Found         | The requested resource is not found | | 429          | Too Many Requests | Too many requests have been (Rate limiting) | | 500          | Server Error      | The server could not return the representation due to an internal server error | | 501          | Not Implemented   | The requested operation is not supported (e.g. supports GET but not POST etc.) |  ## Rate Limits  The DataGalaxy API has 2 kinds of limitations: rate limiting and throttling.  <b>Pro tip:</b> You can track your rate limiting status with the response header `X-RateLimit-Remaining`. It will display how many requests you can send until the next reset.  | Method        | Rate                 | Note | | ------------- | -------------------- | ---- | | Rate limiting | 7200 requests / hour | When exceeded, your IP will be blocked for 15 minutes. | | Throttling    | 2 requests / second  | When exceeded, each request will be delayed by 500ms. | | Payload size  | 100 MB               | When exceeded, request will be rejected. |  ## Pagination  All routes returning lists share the same pagination format. These routes take two optional parameters as querystrings: <code>limit</code> and <code>page</code>.<br>  | QueryString | Definition | |------------ | ---------- | | limit       | Integer ranging from 1 to 5000. It sets the maximum amount of objects per page. Default value is 20. | | page        | Integer starting at 1. It determines the page returned by the request. Default value is 1. |  The response payload contains 5 properties:  | Property  | Definition | | --------- | ---------- | | pages     | Total number of pages. | | total     | Number of objects returned. | | total_sum | Sum of all existing objects. | | next_page | URL of the next page. <i>Value will be null if there is none.</i> | | results   | List of objects. |  # Authentication  The DataGalaxy API uses <b>Bearer Authentication</b> to authenticate requests. Every request must contain an <code>Authorization</code> header with, either an <i>AccessToken</i> or an <i>IntegrationToken</i>.  ## AccessToken  Here is a quick example using CURL:  <pre><code>curl -X GET \"https://api.datagalaxy.com/v2/workspaces\" -H \"Authorization: Bearer <i>AccessToken</i>\"</code></pre>  The first steps of our <a href='https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000151096--quick-start-datagalaxy-public-api-v2' target='_new'>quick start guide</a> will give you instructions to obtain your <code>accesstoken</code>.  ## IntegrationToken  An integration token can be generated from the \"Integration\" page on the DataGalaxy Administration space.  <pre><code>curl -X GET \"https://api.datagalaxy.com/v2/workspaces\" -H \"Authorization: Bearer <i>IntegrationToken</i>\"</code></pre>  # Changelog  The DataGalaxy Developer API is updated frequently with new features, improvements and fixes.  All these changes will be documented in our <button><a href='/v2/documentation/changelog' target='_blank'><b>changelog</b></a></button>.  # Documentation layout  We provide two API documentation layouts:  - [Default layout](/v2/documentation)<br> This layout displays informations in a modern way and contains more informations about requests parameters - [Swagger layout](/v2/documentation/old)<br> This is our legacy layout. It's main perk is the \"Try it\" feature which let's you send requests directly from the documentation.  # noqa: E501

    OpenAPI spec version: 2.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaginatedResponseVersion_(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pages': 'float',
        'total': 'float',
        'total_sum': 'float',
        'next_page': 'str',
        'results': 'list[Version]'
    }

    attribute_map = {
        'pages': 'pages',
        'total': 'total',
        'total_sum': 'total_sum',
        'next_page': 'next_page',
        'results': 'results'
    }

    def __init__(self, pages=None, total=None, total_sum=None, next_page=None, results=None):  # noqa: E501
        """PaginatedResponseVersion_ - a model defined in Swagger"""  # noqa: E501
        self._pages = None
        self._total = None
        self._total_sum = None
        self._next_page = None
        self._results = None
        self.discriminator = None
        self.pages = pages
        self.total = total
        self.total_sum = total_sum
        self.next_page = next_page
        self.results = results

    @property
    def pages(self):
        """Gets the pages of this PaginatedResponseVersion_.  # noqa: E501

        Total number of pages  # noqa: E501

        :return: The pages of this PaginatedResponseVersion_.  # noqa: E501
        :rtype: float
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this PaginatedResponseVersion_.

        Total number of pages  # noqa: E501

        :param pages: The pages of this PaginatedResponseVersion_.  # noqa: E501
        :type: float
        """
        if pages is None:
            raise ValueError("Invalid value for `pages`, must not be `None`")  # noqa: E501

        self._pages = pages

    @property
    def total(self):
        """Gets the total of this PaginatedResponseVersion_.  # noqa: E501

        Number of objects returned  # noqa: E501

        :return: The total of this PaginatedResponseVersion_.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PaginatedResponseVersion_.

        Number of objects returned  # noqa: E501

        :param total: The total of this PaginatedResponseVersion_.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def total_sum(self):
        """Gets the total_sum of this PaginatedResponseVersion_.  # noqa: E501

        Sum of all existing objects  # noqa: E501

        :return: The total_sum of this PaginatedResponseVersion_.  # noqa: E501
        :rtype: float
        """
        return self._total_sum

    @total_sum.setter
    def total_sum(self, total_sum):
        """Sets the total_sum of this PaginatedResponseVersion_.

        Sum of all existing objects  # noqa: E501

        :param total_sum: The total_sum of this PaginatedResponseVersion_.  # noqa: E501
        :type: float
        """
        if total_sum is None:
            raise ValueError("Invalid value for `total_sum`, must not be `None`")  # noqa: E501

        self._total_sum = total_sum

    @property
    def next_page(self):
        """Gets the next_page of this PaginatedResponseVersion_.  # noqa: E501

        Next page's URL. Value will be null if there is none  # noqa: E501

        :return: The next_page of this PaginatedResponseVersion_.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this PaginatedResponseVersion_.

        Next page's URL. Value will be null if there is none  # noqa: E501

        :param next_page: The next_page of this PaginatedResponseVersion_.  # noqa: E501
        :type: str
        """
        if next_page is None:
            raise ValueError("Invalid value for `next_page`, must not be `None`")  # noqa: E501

        self._next_page = next_page

    @property
    def results(self):
        """Gets the results of this PaginatedResponseVersion_.  # noqa: E501

        List of objects  # noqa: E501

        :return: The results of this PaginatedResponseVersion_.  # noqa: E501
        :rtype: list[Version]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedResponseVersion_.

        List of objects  # noqa: E501

        :param results: The results of this PaginatedResponseVersion_.  # noqa: E501
        :type: list[Version]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PaginatedResponseVersion_, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaginatedResponseVersion_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
