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

class ForeignKeyPayload(object):
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
        'fk_technical_name': 'str',
        'pk_technical_name': 'str',
        'pk_table_path': 'str',
        'pk_column_name': 'str',
        'fk_table_path': 'str',
        'fk_column_name': 'str',
        'fk_display_name': 'str',
        'summary': 'str'
    }

    attribute_map = {
        'fk_technical_name': 'fkTechnicalName',
        'pk_technical_name': 'pkTechnicalName',
        'pk_table_path': 'pkTablePath',
        'pk_column_name': 'pkColumnName',
        'fk_table_path': 'fkTablePath',
        'fk_column_name': 'fkColumnName',
        'fk_display_name': 'fkDisplayName',
        'summary': 'summary'
    }

    def __init__(self, fk_technical_name=None, pk_technical_name=None, pk_table_path=None, pk_column_name=None, fk_table_path=None, fk_column_name=None, fk_display_name=None, summary=None):  # noqa: E501
        """ForeignKeyPayload - a model defined in Swagger"""  # noqa: E501
        self._fk_technical_name = None
        self._pk_technical_name = None
        self._pk_table_path = None
        self._pk_column_name = None
        self._fk_table_path = None
        self._fk_column_name = None
        self._fk_display_name = None
        self._summary = None
        self.discriminator = None
        self.fk_technical_name = fk_technical_name
        self.pk_technical_name = pk_technical_name
        self.pk_table_path = pk_table_path
        self.pk_column_name = pk_column_name
        self.fk_table_path = fk_table_path
        self.fk_column_name = fk_column_name
        self.fk_display_name = fk_display_name
        if summary is not None:
            self.summary = summary

    @property
    def fk_technical_name(self):
        """Gets the fk_technical_name of this ForeignKeyPayload.  # noqa: E501


        :return: The fk_technical_name of this ForeignKeyPayload.  # noqa: E501
        :rtype: str
        """
        return self._fk_technical_name

    @fk_technical_name.setter
    def fk_technical_name(self, fk_technical_name):
        """Sets the fk_technical_name of this ForeignKeyPayload.


        :param fk_technical_name: The fk_technical_name of this ForeignKeyPayload.  # noqa: E501
        :type: str
        """
        if fk_technical_name is None:
            raise ValueError("Invalid value for `fk_technical_name`, must not be `None`")  # noqa: E501

        self._fk_technical_name = fk_technical_name

    @property
    def pk_technical_name(self):
        """Gets the pk_technical_name of this ForeignKeyPayload.  # noqa: E501


        :return: The pk_technical_name of this ForeignKeyPayload.  # noqa: E501
        :rtype: str
        """
        return self._pk_technical_name

    @pk_technical_name.setter
    def pk_technical_name(self, pk_technical_name):
        """Sets the pk_technical_name of this ForeignKeyPayload.


        :param pk_technical_name: The pk_technical_name of this ForeignKeyPayload.  # noqa: E501
        :type: str
        """
        if pk_technical_name is None:
            raise ValueError("Invalid value for `pk_technical_name`, must not be `None`")  # noqa: E501

        self._pk_technical_name = pk_technical_name

    @property
    def pk_table_path(self):
        """Gets the pk_table_path of this ForeignKeyPayload.  # noqa: E501


        :return: The pk_table_path of this ForeignKeyPayload.  # noqa: E501
        :rtype: str
        """
        return self._pk_table_path

    @pk_table_path.setter
    def pk_table_path(self, pk_table_path):
        """Sets the pk_table_path of this ForeignKeyPayload.


        :param pk_table_path: The pk_table_path of this ForeignKeyPayload.  # noqa: E501
        :type: str
        """
        if pk_table_path is None:
            raise ValueError("Invalid value for `pk_table_path`, must not be `None`")  # noqa: E501

        self._pk_table_path = pk_table_path

    @property
    def pk_column_name(self):
        """Gets the pk_column_name of this ForeignKeyPayload.  # noqa: E501


        :return: The pk_column_name of this ForeignKeyPayload.  # noqa: E501
        :rtype: str
        """
        return self._pk_column_name

    @pk_column_name.setter
    def pk_column_name(self, pk_column_name):
        """Sets the pk_column_name of this ForeignKeyPayload.


        :param pk_column_name: The pk_column_name of this ForeignKeyPayload.  # noqa: E501
        :type: str
        """
        if pk_column_name is None:
            raise ValueError("Invalid value for `pk_column_name`, must not be `None`")  # noqa: E501

        self._pk_column_name = pk_column_name

    @property
    def fk_table_path(self):
        """Gets the fk_table_path of this ForeignKeyPayload.  # noqa: E501


        :return: The fk_table_path of this ForeignKeyPayload.  # noqa: E501
        :rtype: str
        """
        return self._fk_table_path

    @fk_table_path.setter
    def fk_table_path(self, fk_table_path):
        """Sets the fk_table_path of this ForeignKeyPayload.


        :param fk_table_path: The fk_table_path of this ForeignKeyPayload.  # noqa: E501
        :type: str
        """
        if fk_table_path is None:
            raise ValueError("Invalid value for `fk_table_path`, must not be `None`")  # noqa: E501

        self._fk_table_path = fk_table_path

    @property
    def fk_column_name(self):
        """Gets the fk_column_name of this ForeignKeyPayload.  # noqa: E501


        :return: The fk_column_name of this ForeignKeyPayload.  # noqa: E501
        :rtype: str
        """
        return self._fk_column_name

    @fk_column_name.setter
    def fk_column_name(self, fk_column_name):
        """Sets the fk_column_name of this ForeignKeyPayload.


        :param fk_column_name: The fk_column_name of this ForeignKeyPayload.  # noqa: E501
        :type: str
        """
        if fk_column_name is None:
            raise ValueError("Invalid value for `fk_column_name`, must not be `None`")  # noqa: E501

        self._fk_column_name = fk_column_name

    @property
    def fk_display_name(self):
        """Gets the fk_display_name of this ForeignKeyPayload.  # noqa: E501


        :return: The fk_display_name of this ForeignKeyPayload.  # noqa: E501
        :rtype: str
        """
        return self._fk_display_name

    @fk_display_name.setter
    def fk_display_name(self, fk_display_name):
        """Sets the fk_display_name of this ForeignKeyPayload.


        :param fk_display_name: The fk_display_name of this ForeignKeyPayload.  # noqa: E501
        :type: str
        """
        if fk_display_name is None:
            raise ValueError("Invalid value for `fk_display_name`, must not be `None`")  # noqa: E501

        self._fk_display_name = fk_display_name

    @property
    def summary(self):
        """Gets the summary of this ForeignKeyPayload.  # noqa: E501


        :return: The summary of this ForeignKeyPayload.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ForeignKeyPayload.


        :param summary: The summary of this ForeignKeyPayload.  # noqa: E501
        :type: str
        """

        self._summary = summary

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
        if issubclass(ForeignKeyPayload, dict):
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
        if not isinstance(other, ForeignKeyPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
