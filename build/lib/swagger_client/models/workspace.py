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

class Workspace(object):
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
        'id': 'DoubleUuid',
        'description': 'str',
        'default_version_name': 'str',
        'default_version_id': 'VersionId',
        'is_versioning_enabled': 'bool',
        'default_owner_user': 'DefaultUser',
        'default_steward_user': 'DefaultUser',
        'trigram': 'str',
        'image_hash': 'ImageHash',
        'icon_hash': 'ImageHash'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'default_version_name': 'defaultVersionName',
        'default_version_id': 'defaultVersionId',
        'is_versioning_enabled': 'isVersioningEnabled',
        'default_owner_user': 'defaultOwnerUser',
        'default_steward_user': 'defaultStewardUser',
        'trigram': 'trigram',
        'image_hash': 'imageHash',
        'icon_hash': 'iconHash'
    }

    def __init__(self, name=None, id=None, description=None, default_version_name=None, default_version_id=None, is_versioning_enabled=None, default_owner_user=None, default_steward_user=None, trigram=None, image_hash=None, icon_hash=None):  # noqa: E501
        """Workspace - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._description = None
        self._default_version_name = None
        self._default_version_id = None
        self._is_versioning_enabled = None
        self._default_owner_user = None
        self._default_steward_user = None
        self._trigram = None
        self._image_hash = None
        self._icon_hash = None
        self.discriminator = None
        self.name = name
        self.id = id
        self.description = description
        if default_version_name is not None:
            self.default_version_name = default_version_name
        if default_version_id is not None:
            self.default_version_id = default_version_id
        self.is_versioning_enabled = is_versioning_enabled
        self.default_owner_user = default_owner_user
        self.default_steward_user = default_steward_user
        self.trigram = trigram
        self.image_hash = image_hash
        self.icon_hash = icon_hash

    @property
    def name(self):
        """Gets the name of this Workspace.  # noqa: E501


        :return: The name of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workspace.


        :param name: The name of this Workspace.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this Workspace.  # noqa: E501


        :return: The id of this Workspace.  # noqa: E501
        :rtype: DoubleUuid
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Workspace.


        :param id: The id of this Workspace.  # noqa: E501
        :type: DoubleUuid
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this Workspace.  # noqa: E501


        :return: The description of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Workspace.


        :param description: The description of this Workspace.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def default_version_name(self):
        """Gets the default_version_name of this Workspace.  # noqa: E501


        :return: The default_version_name of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._default_version_name

    @default_version_name.setter
    def default_version_name(self, default_version_name):
        """Sets the default_version_name of this Workspace.


        :param default_version_name: The default_version_name of this Workspace.  # noqa: E501
        :type: str
        """

        self._default_version_name = default_version_name

    @property
    def default_version_id(self):
        """Gets the default_version_id of this Workspace.  # noqa: E501


        :return: The default_version_id of this Workspace.  # noqa: E501
        :rtype: VersionId
        """
        return self._default_version_id

    @default_version_id.setter
    def default_version_id(self, default_version_id):
        """Sets the default_version_id of this Workspace.


        :param default_version_id: The default_version_id of this Workspace.  # noqa: E501
        :type: VersionId
        """

        self._default_version_id = default_version_id

    @property
    def is_versioning_enabled(self):
        """Gets the is_versioning_enabled of this Workspace.  # noqa: E501


        :return: The is_versioning_enabled of this Workspace.  # noqa: E501
        :rtype: bool
        """
        return self._is_versioning_enabled

    @is_versioning_enabled.setter
    def is_versioning_enabled(self, is_versioning_enabled):
        """Sets the is_versioning_enabled of this Workspace.


        :param is_versioning_enabled: The is_versioning_enabled of this Workspace.  # noqa: E501
        :type: bool
        """
        if is_versioning_enabled is None:
            raise ValueError("Invalid value for `is_versioning_enabled`, must not be `None`")  # noqa: E501

        self._is_versioning_enabled = is_versioning_enabled

    @property
    def default_owner_user(self):
        """Gets the default_owner_user of this Workspace.  # noqa: E501


        :return: The default_owner_user of this Workspace.  # noqa: E501
        :rtype: DefaultUser
        """
        return self._default_owner_user

    @default_owner_user.setter
    def default_owner_user(self, default_owner_user):
        """Sets the default_owner_user of this Workspace.


        :param default_owner_user: The default_owner_user of this Workspace.  # noqa: E501
        :type: DefaultUser
        """
        if default_owner_user is None:
            raise ValueError("Invalid value for `default_owner_user`, must not be `None`")  # noqa: E501

        self._default_owner_user = default_owner_user

    @property
    def default_steward_user(self):
        """Gets the default_steward_user of this Workspace.  # noqa: E501


        :return: The default_steward_user of this Workspace.  # noqa: E501
        :rtype: DefaultUser
        """
        return self._default_steward_user

    @default_steward_user.setter
    def default_steward_user(self, default_steward_user):
        """Sets the default_steward_user of this Workspace.


        :param default_steward_user: The default_steward_user of this Workspace.  # noqa: E501
        :type: DefaultUser
        """
        if default_steward_user is None:
            raise ValueError("Invalid value for `default_steward_user`, must not be `None`")  # noqa: E501

        self._default_steward_user = default_steward_user

    @property
    def trigram(self):
        """Gets the trigram of this Workspace.  # noqa: E501


        :return: The trigram of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._trigram

    @trigram.setter
    def trigram(self, trigram):
        """Sets the trigram of this Workspace.


        :param trigram: The trigram of this Workspace.  # noqa: E501
        :type: str
        """
        if trigram is None:
            raise ValueError("Invalid value for `trigram`, must not be `None`")  # noqa: E501

        self._trigram = trigram

    @property
    def image_hash(self):
        """Gets the image_hash of this Workspace.  # noqa: E501


        :return: The image_hash of this Workspace.  # noqa: E501
        :rtype: ImageHash
        """
        return self._image_hash

    @image_hash.setter
    def image_hash(self, image_hash):
        """Sets the image_hash of this Workspace.


        :param image_hash: The image_hash of this Workspace.  # noqa: E501
        :type: ImageHash
        """
        if image_hash is None:
            # TODO KENSU "fix" => this is apparently not always true
            # raise ValueError("Invalid value for `image_hash`, must not be `None`")  # noqa: E501
            pass

        self._image_hash = image_hash

    @property
    def icon_hash(self):
        """Gets the icon_hash of this Workspace.  # noqa: E501


        :return: The icon_hash of this Workspace.  # noqa: E501
        :rtype: ImageHash
        """
        return self._icon_hash

    @icon_hash.setter
    def icon_hash(self, icon_hash):
        """Sets the icon_hash of this Workspace.


        :param icon_hash: The icon_hash of this Workspace.  # noqa: E501
        :type: ImageHash
        """
        if icon_hash is None:
            # TODO KENSU "fix" => this is apparently not always true
            # raise ValueError("Invalid value for `icon_hash`, must not be `None`")  # noqa: E501
            pass

        self._icon_hash = icon_hash

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
        if issubclass(Workspace, dict):
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
        if not isinstance(other, Workspace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
