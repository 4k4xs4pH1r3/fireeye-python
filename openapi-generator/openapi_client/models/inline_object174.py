# coding: utf-8

"""
    Helix API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class InlineObject174(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'saved_search': 'str',
        'user': 'str'
    }

    attribute_map = {
        'saved_search': 'saved_search',
        'user': 'user'
    }

    def __init__(self, saved_search=None, user=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject174 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._saved_search = None
        self._user = None
        self.discriminator = None

        self.saved_search = saved_search
        self.user = user

    @property
    def saved_search(self):
        """Gets the saved_search of this InlineObject174.  # noqa: E501

          # noqa: E501

        :return: The saved_search of this InlineObject174.  # noqa: E501
        :rtype: str
        """
        return self._saved_search

    @saved_search.setter
    def saved_search(self, saved_search):
        """Sets the saved_search of this InlineObject174.

          # noqa: E501

        :param saved_search: The saved_search of this InlineObject174.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and saved_search is None:  # noqa: E501
            raise ValueError("Invalid value for `saved_search`, must not be `None`")  # noqa: E501

        self._saved_search = saved_search

    @property
    def user(self):
        """Gets the user of this InlineObject174.  # noqa: E501

          # noqa: E501

        :return: The user of this InlineObject174.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this InlineObject174.

          # noqa: E501

        :param user: The user of this InlineObject174.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject174):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject174):
            return True

        return self.to_dict() != other.to_dict()
