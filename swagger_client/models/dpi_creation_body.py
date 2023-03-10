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

class DpiCreationBody(object):
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
        'name': 'str',
        'technical_name': 'str',
        'type': 'DataProcessingItemType',
        'summary': 'str',
        'description': 'str',
        'inputs': 'list[str]',
        'outputs': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'technical_name': 'technicalName',
        'type': 'type',
        'summary': 'summary',
        'description': 'description',
        'inputs': 'inputs',
        'outputs': 'outputs'
    }

    def __init__(self, name=None, technical_name=None, type=None, summary=None, description=None, inputs=None, outputs=None):  # noqa: E501
        """DpiCreationBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._technical_name = None
        self._type = None
        self._summary = None
        self._description = None
        self._inputs = None
        self._outputs = None
        self.discriminator = None
        self.name = name
        if technical_name is not None:
            self.technical_name = technical_name
        self.type = type
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs

    @property
    def name(self):
        """Gets the name of this DpiCreationBody.  # noqa: E501


        :return: The name of this DpiCreationBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DpiCreationBody.


        :param name: The name of this DpiCreationBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def technical_name(self):
        """Gets the technical_name of this DpiCreationBody.  # noqa: E501


        :return: The technical_name of this DpiCreationBody.  # noqa: E501
        :rtype: str
        """
        return self._technical_name

    @technical_name.setter
    def technical_name(self, technical_name):
        """Sets the technical_name of this DpiCreationBody.


        :param technical_name: The technical_name of this DpiCreationBody.  # noqa: E501
        :type: str
        """

        self._technical_name = technical_name

    @property
    def type(self):
        """Gets the type of this DpiCreationBody.  # noqa: E501


        :return: The type of this DpiCreationBody.  # noqa: E501
        :rtype: DataProcessingItemType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DpiCreationBody.


        :param type: The type of this DpiCreationBody.  # noqa: E501
        :type: DataProcessingItemType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def summary(self):
        """Gets the summary of this DpiCreationBody.  # noqa: E501


        :return: The summary of this DpiCreationBody.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this DpiCreationBody.


        :param summary: The summary of this DpiCreationBody.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def description(self):
        """Gets the description of this DpiCreationBody.  # noqa: E501


        :return: The description of this DpiCreationBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DpiCreationBody.


        :param description: The description of this DpiCreationBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def inputs(self):
        """Gets the inputs of this DpiCreationBody.  # noqa: E501


        :return: The inputs of this DpiCreationBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this DpiCreationBody.


        :param inputs: The inputs of this DpiCreationBody.  # noqa: E501
        :type: list[str]
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this DpiCreationBody.  # noqa: E501


        :return: The outputs of this DpiCreationBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this DpiCreationBody.


        :param outputs: The outputs of this DpiCreationBody.  # noqa: E501
        :type: list[str]
        """

        self._outputs = outputs

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
        if issubclass(DpiCreationBody, dict):
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
        if not isinstance(other, DpiCreationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
