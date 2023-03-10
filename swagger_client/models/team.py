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

class Team(object):
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
        'description': 'str',
        'email': 'str',
        'access': 'AccessType',
        'id': 'TeamId',
        'icon_hash': 'str',
        'owners': 'list[Email]',
        'members_count': 'float',
        'members': 'list[TeamMember]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'email': 'email',
        'access': 'access',
        'id': 'id',
        'icon_hash': 'iconHash',
        'owners': 'owners',
        'members_count': 'membersCount',
        'members': 'members'
    }

    def __init__(self, name=None, description=None, email=None, access=None, id=None, icon_hash=None, owners=None, members_count=None, members=None):  # noqa: E501
        """Team - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._email = None
        self._access = None
        self._id = None
        self._icon_hash = None
        self._owners = None
        self._members_count = None
        self._members = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        if email is not None:
            self.email = email
        self.access = access
        self.id = id
        self.icon_hash = icon_hash
        self.owners = owners
        self.members_count = members_count
        if members is not None:
            self.members = members

    @property
    def name(self):
        """Gets the name of this Team.  # noqa: E501

        Team name  # noqa: E501

        :return: The name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.

        Team name  # noqa: E501

        :param name: The name of this Team.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Team.  # noqa: E501

        A short description of the team motivations  # noqa: E501

        :return: The description of this Team.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Team.

        A short description of the team motivations  # noqa: E501

        :param description: The description of this Team.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email(self):
        """Gets the email of this Team.  # noqa: E501

        The team email will be used to notify all members  # noqa: E501

        :return: The email of this Team.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Team.

        The team email will be used to notify all members  # noqa: E501

        :param email: The email of this Team.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def access(self):
        """Gets the access of this Team.  # noqa: E501


        :return: The access of this Team.  # noqa: E501
        :rtype: AccessType
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this Team.


        :param access: The access of this Team.  # noqa: E501
        :type: AccessType
        """
        if access is None:
            raise ValueError("Invalid value for `access`, must not be `None`")  # noqa: E501

        self._access = access

    @property
    def id(self):
        """Gets the id of this Team.  # noqa: E501


        :return: The id of this Team.  # noqa: E501
        :rtype: TeamId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Team.


        :param id: The id of this Team.  # noqa: E501
        :type: TeamId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def icon_hash(self):
        """Gets the icon_hash of this Team.  # noqa: E501

        Hash associated to the Team's icon. Use it with the <a href=\"/v2/documentation#tag/Image/operation/GetImage\"><code>GET /image</code> endpoint</a> to fetch the icon binaries.  # noqa: E501

        :return: The icon_hash of this Team.  # noqa: E501
        :rtype: str
        """
        return self._icon_hash

    @icon_hash.setter
    def icon_hash(self, icon_hash):
        """Sets the icon_hash of this Team.

        Hash associated to the Team's icon. Use it with the <a href=\"/v2/documentation#tag/Image/operation/GetImage\"><code>GET /image</code> endpoint</a> to fetch the icon binaries.  # noqa: E501

        :param icon_hash: The icon_hash of this Team.  # noqa: E501
        :type: str
        """
        if icon_hash is None:
            raise ValueError("Invalid value for `icon_hash`, must not be `None`")  # noqa: E501

        self._icon_hash = icon_hash

    @property
    def owners(self):
        """Gets the owners of this Team.  # noqa: E501

        Team owner's email  # noqa: E501

        :return: The owners of this Team.  # noqa: E501
        :rtype: list[Email]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this Team.

        Team owner's email  # noqa: E501

        :param owners: The owners of this Team.  # noqa: E501
        :type: list[Email]
        """
        if owners is None:
            raise ValueError("Invalid value for `owners`, must not be `None`")  # noqa: E501

        self._owners = owners

    @property
    def members_count(self):
        """Gets the members_count of this Team.  # noqa: E501

        Total count of members, including the owner(s).  # noqa: E501

        :return: The members_count of this Team.  # noqa: E501
        :rtype: float
        """
        return self._members_count

    @members_count.setter
    def members_count(self, members_count):
        """Sets the members_count of this Team.

        Total count of members, including the owner(s).  # noqa: E501

        :param members_count: The members_count of this Team.  # noqa: E501
        :type: float
        """
        if members_count is None:
            raise ValueError("Invalid value for `members_count`, must not be `None`")  # noqa: E501

        self._members_count = members_count

    @property
    def members(self):
        """Gets the members of this Team.  # noqa: E501

        List of users that are part of the team  # noqa: E501

        :return: The members of this Team.  # noqa: E501
        :rtype: list[TeamMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Team.

        List of users that are part of the team  # noqa: E501

        :param members: The members of this Team.  # noqa: E501
        :type: list[TeamMember]
        """

        self._members = members

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
        if issubclass(Team, dict):
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
        if not isinstance(other, Team):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
