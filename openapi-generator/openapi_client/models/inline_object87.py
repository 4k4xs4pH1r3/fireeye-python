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


class InlineObject87(object):
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
        'total_results': 'int',
        'query': 'str',
        'customer_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'total_results': 'totalResults',
        'query': 'query',
        'customer_id': 'customer_id',
        'user_id': 'userId'
    }

    def __init__(self, total_results=None, query=None, customer_id=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject87 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_results = None
        self._query = None
        self._customer_id = None
        self._user_id = None
        self.discriminator = None

        self.total_results = total_results
        self.query = query
        if customer_id is not None:
            self.customer_id = customer_id
        self.user_id = user_id

    @property
    def total_results(self):
        """Gets the total_results of this InlineObject87.  # noqa: E501

          # noqa: E501

        :return: The total_results of this InlineObject87.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this InlineObject87.

          # noqa: E501

        :param total_results: The total_results of this InlineObject87.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_results is None:  # noqa: E501
            raise ValueError("Invalid value for `total_results`, must not be `None`")  # noqa: E501

        self._total_results = total_results

    @property
    def query(self):
        """Gets the query of this InlineObject87.  # noqa: E501

          # noqa: E501

        :return: The query of this InlineObject87.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this InlineObject87.

          # noqa: E501

        :param query: The query of this InlineObject87.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and query is None:  # noqa: E501
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject87.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject87.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject87.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject87.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def user_id(self):
        """Gets the user_id of this InlineObject87.  # noqa: E501

          # noqa: E501

        :return: The user_id of this InlineObject87.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InlineObject87.

          # noqa: E501

        :param user_id: The user_id of this InlineObject87.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if not isinstance(other, InlineObject87):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject87):
            return True

        return self.to_dict() != other.to_dict()
