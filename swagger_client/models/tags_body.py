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

class TagsBody(object):
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
        'label': 'str',
        'description': 'str',
        'color': 'AnyOfTagsBodyColor',
        'keywords': 'list[str]',
        'is_active': 'bool',
        'is_user_suggestion_enabled': 'bool'
    }

    attribute_map = {
        'label': 'label',
        'description': 'description',
        'color': 'color',
        'keywords': 'keywords',
        'is_active': 'isActive',
        'is_user_suggestion_enabled': 'isUserSuggestionEnabled'
    }

    def __init__(self, label=None, description=None, color=None, keywords=None, is_active=None, is_user_suggestion_enabled=None):  # noqa: E501
        """TagsBody - a model defined in Swagger"""  # noqa: E501
        self._label = None
        self._description = None
        self._color = None
        self._keywords = None
        self._is_active = None
        self._is_user_suggestion_enabled = None
        self.discriminator = None
        self.label = label
        if description is not None:
            self.description = description
        if color is not None:
            self.color = color
        if keywords is not None:
            self.keywords = keywords
        if is_active is not None:
            self.is_active = is_active
        if is_user_suggestion_enabled is not None:
            self.is_user_suggestion_enabled = is_user_suggestion_enabled

    @property
    def label(self):
        """Gets the label of this TagsBody.  # noqa: E501


        :return: The label of this TagsBody.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TagsBody.


        :param label: The label of this TagsBody.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def description(self):
        """Gets the description of this TagsBody.  # noqa: E501


        :return: The description of this TagsBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TagsBody.


        :param description: The description of this TagsBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def color(self):
        """Gets the color of this TagsBody.  # noqa: E501


        :return: The color of this TagsBody.  # noqa: E501
        :rtype: AnyOfTagsBodyColor
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this TagsBody.


        :param color: The color of this TagsBody.  # noqa: E501
        :type: AnyOfTagsBodyColor
        """

        self._color = color

    @property
    def keywords(self):
        """Gets the keywords of this TagsBody.  # noqa: E501


        :return: The keywords of this TagsBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this TagsBody.


        :param keywords: The keywords of this TagsBody.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def is_active(self):
        """Gets the is_active of this TagsBody.  # noqa: E501


        :return: The is_active of this TagsBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this TagsBody.


        :param is_active: The is_active of this TagsBody.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_user_suggestion_enabled(self):
        """Gets the is_user_suggestion_enabled of this TagsBody.  # noqa: E501


        :return: The is_user_suggestion_enabled of this TagsBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_suggestion_enabled

    @is_user_suggestion_enabled.setter
    def is_user_suggestion_enabled(self, is_user_suggestion_enabled):
        """Sets the is_user_suggestion_enabled of this TagsBody.


        :param is_user_suggestion_enabled: The is_user_suggestion_enabled of this TagsBody.  # noqa: E501
        :type: bool
        """

        self._is_user_suggestion_enabled = is_user_suggestion_enabled

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
        if issubclass(TagsBody, dict):
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
        if not isinstance(other, TagsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
