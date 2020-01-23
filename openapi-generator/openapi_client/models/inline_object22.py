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


class InlineObject22(object):
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
        'index': 'int',
        'description': 'str',
        'title': 'str',
        'editable': 'bool',
        'page_size': 'int',
        'time_range': 'int',
        'width_as_percentage': 'int',
        'removable': 'bool',
        'dashboard_id': 'str',
        'query': 'str',
        'is_hidden': 'bool',
        'customer_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'index': 'index',
        'description': 'description',
        'title': 'title',
        'editable': 'editable',
        'page_size': 'page_size',
        'time_range': 'time_range',
        'width_as_percentage': 'widthAsPercentage',
        'removable': 'removable',
        'dashboard_id': 'dashboardID',
        'query': 'query',
        'is_hidden': 'is_hidden',
        'customer_id': 'customer_id',
        'type': 'type'
    }

    def __init__(self, index=None, description=None, title=None, editable=None, page_size=None, time_range=None, width_as_percentage=None, removable=None, dashboard_id=None, query=None, is_hidden=None, customer_id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject22 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._description = None
        self._title = None
        self._editable = None
        self._page_size = None
        self._time_range = None
        self._width_as_percentage = None
        self._removable = None
        self._dashboard_id = None
        self._query = None
        self._is_hidden = None
        self._customer_id = None
        self._type = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if description is not None:
            self.description = description
        self.title = title
        if editable is not None:
            self.editable = editable
        if page_size is not None:
            self.page_size = page_size
        if time_range is not None:
            self.time_range = time_range
        if width_as_percentage is not None:
            self.width_as_percentage = width_as_percentage
        if removable is not None:
            self.removable = removable
        self.dashboard_id = dashboard_id
        if query is not None:
            self.query = query
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if customer_id is not None:
            self.customer_id = customer_id
        if type is not None:
            self.type = type

    @property
    def index(self):
        """Gets the index of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The index of this InlineObject22.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this InlineObject22.

          # noqa: E501

        :param index: The index of this InlineObject22.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def description(self):
        """Gets the description of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject22.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject22.

          # noqa: E501

        :param description: The description of this InlineObject22.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def title(self):
        """Gets the title of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The title of this InlineObject22.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineObject22.

          # noqa: E501

        :param title: The title of this InlineObject22.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def editable(self):
        """Gets the editable of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The editable of this InlineObject22.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this InlineObject22.

          # noqa: E501

        :param editable: The editable of this InlineObject22.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def page_size(self):
        """Gets the page_size of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The page_size of this InlineObject22.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InlineObject22.

          # noqa: E501

        :param page_size: The page_size of this InlineObject22.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def time_range(self):
        """Gets the time_range of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The time_range of this InlineObject22.  # noqa: E501
        :rtype: int
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this InlineObject22.

          # noqa: E501

        :param time_range: The time_range of this InlineObject22.  # noqa: E501
        :type: int
        """

        self._time_range = time_range

    @property
    def width_as_percentage(self):
        """Gets the width_as_percentage of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The width_as_percentage of this InlineObject22.  # noqa: E501
        :rtype: int
        """
        return self._width_as_percentage

    @width_as_percentage.setter
    def width_as_percentage(self, width_as_percentage):
        """Sets the width_as_percentage of this InlineObject22.

          # noqa: E501

        :param width_as_percentage: The width_as_percentage of this InlineObject22.  # noqa: E501
        :type: int
        """

        self._width_as_percentage = width_as_percentage

    @property
    def removable(self):
        """Gets the removable of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The removable of this InlineObject22.  # noqa: E501
        :rtype: bool
        """
        return self._removable

    @removable.setter
    def removable(self, removable):
        """Sets the removable of this InlineObject22.

          # noqa: E501

        :param removable: The removable of this InlineObject22.  # noqa: E501
        :type: bool
        """

        self._removable = removable

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The dashboard_id of this InlineObject22.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this InlineObject22.

          # noqa: E501

        :param dashboard_id: The dashboard_id of this InlineObject22.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dashboard_id is None:  # noqa: E501
            raise ValueError("Invalid value for `dashboard_id`, must not be `None`")  # noqa: E501

        self._dashboard_id = dashboard_id

    @property
    def query(self):
        """Gets the query of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The query of this InlineObject22.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this InlineObject22.

          # noqa: E501

        :param query: The query of this InlineObject22.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject22.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject22.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject22.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject22.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject22.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject22.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def type(self):
        """Gets the type of this InlineObject22.  # noqa: E501

          # noqa: E501

        :return: The type of this InlineObject22.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineObject22.

          # noqa: E501

        :param type: The type of this InlineObject22.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, InlineObject22):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject22):
            return True

        return self.to_dict() != other.to_dict()
