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

class PropertiesBulkTreeCreationRequest(object):
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
        'type': 'PropertyType',
        'status': 'EntityStatus',
        'owners': 'list[Email]',
        'stewards': 'list[Email]',
        'tags': 'list[str]',
        'description': 'str',
        'summary': 'str',
        'code': 'str',
        'name': 'str',
        'children': 'list[PropertiesBulkTreeCreationRequest]'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'owners': 'owners',
        'stewards': 'stewards',
        'tags': 'tags',
        'description': 'description',
        'summary': 'summary',
        'code': 'code',
        'name': 'name',
        'children': 'children'
    }

    def __init__(self, type=None, status=None, owners=None, stewards=None, tags=None, description=None, summary=None, code=None, name=None, children=None):  # noqa: E501
        """PropertiesBulkTreeCreationRequest - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._status = None
        self._owners = None
        self._stewards = None
        self._tags = None
        self._description = None
        self._summary = None
        self._code = None
        self._name = None
        self._children = None
        self.discriminator = None
        self.type = type
        if status is not None:
            self.status = status
        if owners is not None:
            self.owners = owners
        if stewards is not None:
            self.stewards = stewards
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if summary is not None:
            self.summary = summary
        if code is not None:
            self.code = code
        self.name = name
        if children is not None:
            self.children = children

    @property
    def type(self):
        """Gets the type of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The type of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: PropertyType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertiesBulkTreeCreationRequest.


        :param type: The type of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: PropertyType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The status of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: EntityStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PropertiesBulkTreeCreationRequest.


        :param status: The status of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: EntityStatus
        """

        self._status = status

    @property
    def owners(self):
        """Gets the owners of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The owners of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: list[Email]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this PropertiesBulkTreeCreationRequest.


        :param owners: The owners of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: list[Email]
        """

        self._owners = owners

    @property
    def stewards(self):
        """Gets the stewards of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The stewards of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: list[Email]
        """
        return self._stewards

    @stewards.setter
    def stewards(self, stewards):
        """Sets the stewards of this PropertiesBulkTreeCreationRequest.


        :param stewards: The stewards of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: list[Email]
        """

        self._stewards = stewards

    @property
    def tags(self):
        """Gets the tags of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The tags of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PropertiesBulkTreeCreationRequest.


        :param tags: The tags of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def description(self):
        """Gets the description of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The description of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PropertiesBulkTreeCreationRequest.


        :param description: The description of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def summary(self):
        """Gets the summary of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The summary of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PropertiesBulkTreeCreationRequest.


        :param summary: The summary of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def code(self):
        """Gets the code of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The code of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PropertiesBulkTreeCreationRequest.


        :param code: The code of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The name of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertiesBulkTreeCreationRequest.


        :param name: The name of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def children(self):
        """Gets the children of this PropertiesBulkTreeCreationRequest.  # noqa: E501


        :return: The children of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :rtype: list[PropertiesBulkTreeCreationRequest]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this PropertiesBulkTreeCreationRequest.


        :param children: The children of this PropertiesBulkTreeCreationRequest.  # noqa: E501
        :type: list[PropertiesBulkTreeCreationRequest]
        """

        self._children = children

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
        if issubclass(PropertiesBulkTreeCreationRequest, dict):
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
        if not isinstance(other, PropertiesBulkTreeCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other