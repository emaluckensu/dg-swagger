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

class Attribute(object):
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
        'name': 'AttributeName',
        'attribute_key': 'AttributeKey',
        'format': 'AttributeFormats',
        'data_type': 'DataTypesClientMapping',
        'description': 'str',
        'default_value': 'AnyOfAttributeDefaultValue',
        'is_custom': 'bool',
        'is_mandatory': 'bool',
        'is_editable': 'bool',
        'values': 'list[AttributeValue]',
        'time_series_color_rule': 'TimeSeriesColorRule',
        'time_series_frequency': 'TimeSeriesFrequency'
    }

    attribute_map = {
        'name': 'name',
        'attribute_key': 'attributeKey',
        'format': 'format',
        'data_type': 'dataType',
        'description': 'description',
        'default_value': 'defaultValue',
        'is_custom': 'isCustom',
        'is_mandatory': 'isMandatory',
        'is_editable': 'isEditable',
        'values': 'values',
        'time_series_color_rule': 'timeSeriesColorRule',
        'time_series_frequency': 'timeSeriesFrequency'
    }

    def __init__(self, name=None, attribute_key=None, format=None, data_type=None, description=None, default_value=None, is_custom=None, is_mandatory=None, is_editable=None, values=None, time_series_color_rule=None, time_series_frequency=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._attribute_key = None
        self._format = None
        self._data_type = None
        self._description = None
        self._default_value = None
        self._is_custom = None
        self._is_mandatory = None
        self._is_editable = None
        self._values = None
        self._time_series_color_rule = None
        self._time_series_frequency = None
        self.discriminator = None
        self.name = name
        self.attribute_key = attribute_key
        self.format = format
        self.data_type = data_type
        self.description = description
        self.default_value = default_value
        self.is_custom = is_custom
        self.is_mandatory = is_mandatory
        self.is_editable = is_editable
        if values is not None:
            self.values = values
        if time_series_color_rule is not None:
            self.time_series_color_rule = time_series_color_rule
        if time_series_frequency is not None:
            self.time_series_frequency = time_series_frequency

    @property
    def name(self):
        """Gets the name of this Attribute.  # noqa: E501


        :return: The name of this Attribute.  # noqa: E501
        :rtype: AttributeName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attribute.


        :param name: The name of this Attribute.  # noqa: E501
        :type: AttributeName
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def attribute_key(self):
        """Gets the attribute_key of this Attribute.  # noqa: E501


        :return: The attribute_key of this Attribute.  # noqa: E501
        :rtype: AttributeKey
        """
        return self._attribute_key

    @attribute_key.setter
    def attribute_key(self, attribute_key):
        """Sets the attribute_key of this Attribute.


        :param attribute_key: The attribute_key of this Attribute.  # noqa: E501
        :type: AttributeKey
        """
        if attribute_key is None:
            raise ValueError("Invalid value for `attribute_key`, must not be `None`")  # noqa: E501

        self._attribute_key = attribute_key

    @property
    def format(self):
        """Gets the format of this Attribute.  # noqa: E501


        :return: The format of this Attribute.  # noqa: E501
        :rtype: AttributeFormats
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Attribute.


        :param format: The format of this Attribute.  # noqa: E501
        :type: AttributeFormats
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501

        self._format = format

    @property
    def data_type(self):
        """Gets the data_type of this Attribute.  # noqa: E501


        :return: The data_type of this Attribute.  # noqa: E501
        :rtype: DataTypesClientMapping
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Attribute.


        :param data_type: The data_type of this Attribute.  # noqa: E501
        :type: DataTypesClientMapping
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501

        self._data_type = data_type

    @property
    def description(self):
        """Gets the description of this Attribute.  # noqa: E501


        :return: The description of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Attribute.


        :param description: The description of this Attribute.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def default_value(self):
        """Gets the default_value of this Attribute.  # noqa: E501


        :return: The default_value of this Attribute.  # noqa: E501
        :rtype: AnyOfAttributeDefaultValue
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this Attribute.


        :param default_value: The default_value of this Attribute.  # noqa: E501
        :type: AnyOfAttributeDefaultValue
        """
        if default_value is None:
            raise ValueError("Invalid value for `default_value`, must not be `None`")  # noqa: E501

        self._default_value = default_value

    @property
    def is_custom(self):
        """Gets the is_custom of this Attribute.  # noqa: E501


        :return: The is_custom of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_custom

    @is_custom.setter
    def is_custom(self, is_custom):
        """Sets the is_custom of this Attribute.


        :param is_custom: The is_custom of this Attribute.  # noqa: E501
        :type: bool
        """
        if is_custom is None:
            raise ValueError("Invalid value for `is_custom`, must not be `None`")  # noqa: E501

        self._is_custom = is_custom

    @property
    def is_mandatory(self):
        """Gets the is_mandatory of this Attribute.  # noqa: E501


        :return: The is_mandatory of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """Sets the is_mandatory of this Attribute.


        :param is_mandatory: The is_mandatory of this Attribute.  # noqa: E501
        :type: bool
        """
        if is_mandatory is None:
            raise ValueError("Invalid value for `is_mandatory`, must not be `None`")  # noqa: E501

        self._is_mandatory = is_mandatory

    @property
    def is_editable(self):
        """Gets the is_editable of this Attribute.  # noqa: E501


        :return: The is_editable of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """Sets the is_editable of this Attribute.


        :param is_editable: The is_editable of this Attribute.  # noqa: E501
        :type: bool
        """
        if is_editable is None:
            raise ValueError("Invalid value for `is_editable`, must not be `None`")  # noqa: E501

        self._is_editable = is_editable

    @property
    def values(self):
        """Gets the values of this Attribute.  # noqa: E501


        :return: The values of this Attribute.  # noqa: E501
        :rtype: list[AttributeValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Attribute.


        :param values: The values of this Attribute.  # noqa: E501
        :type: list[AttributeValue]
        """

        self._values = values

    @property
    def time_series_color_rule(self):
        """Gets the time_series_color_rule of this Attribute.  # noqa: E501


        :return: The time_series_color_rule of this Attribute.  # noqa: E501
        :rtype: TimeSeriesColorRule
        """
        return self._time_series_color_rule

    @time_series_color_rule.setter
    def time_series_color_rule(self, time_series_color_rule):
        """Sets the time_series_color_rule of this Attribute.


        :param time_series_color_rule: The time_series_color_rule of this Attribute.  # noqa: E501
        :type: TimeSeriesColorRule
        """

        self._time_series_color_rule = time_series_color_rule

    @property
    def time_series_frequency(self):
        """Gets the time_series_frequency of this Attribute.  # noqa: E501


        :return: The time_series_frequency of this Attribute.  # noqa: E501
        :rtype: TimeSeriesFrequency
        """
        return self._time_series_frequency

    @time_series_frequency.setter
    def time_series_frequency(self, time_series_frequency):
        """Sets the time_series_frequency of this Attribute.


        :param time_series_frequency: The time_series_frequency of this Attribute.  # noqa: E501
        :type: TimeSeriesFrequency
        """

        self._time_series_frequency = time_series_frequency

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
        if issubclass(Attribute, dict):
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
