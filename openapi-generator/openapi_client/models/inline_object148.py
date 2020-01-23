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


class InlineObject148(object):
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
        'category': 'str',
        'index': 'int',
        'description': 'str',
        'title': 'str',
        'page_size': 'int',
        'time_range': 'int',
        'is_editable': 'bool',
        'template': 'str',
        'dashboard': 'str',
        'is_removable': 'bool',
        'query': 'str',
        'is_public': 'bool',
        'is_hidden': 'bool',
        'type': 'str',
        'percent_width': 'int'
    }

    attribute_map = {
        'category': 'category',
        'index': 'index',
        'description': 'description',
        'title': 'title',
        'page_size': 'page_size',
        'time_range': 'time_range',
        'is_editable': 'is_editable',
        'template': 'template',
        'dashboard': 'dashboard',
        'is_removable': 'is_removable',
        'query': 'query',
        'is_public': 'is_public',
        'is_hidden': 'is_hidden',
        'type': 'type',
        'percent_width': 'percent_width'
    }

    def __init__(self, category=None, index=None, description=None, title=None, page_size=None, time_range=None, is_editable=None, template=None, dashboard=None, is_removable=None, query=None, is_public=None, is_hidden=None, type=None, percent_width=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject148 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._category = None
        self._index = None
        self._description = None
        self._title = None
        self._page_size = None
        self._time_range = None
        self._is_editable = None
        self._template = None
        self._dashboard = None
        self._is_removable = None
        self._query = None
        self._is_public = None
        self._is_hidden = None
        self._type = None
        self._percent_width = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if index is not None:
            self.index = index
        if description is not None:
            self.description = description
        self.title = title
        if page_size is not None:
            self.page_size = page_size
        if time_range is not None:
            self.time_range = time_range
        if is_editable is not None:
            self.is_editable = is_editable
        if template is not None:
            self.template = template
        self.dashboard = dashboard
        if is_removable is not None:
            self.is_removable = is_removable
        if query is not None:
            self.query = query
        if is_public is not None:
            self.is_public = is_public
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if type is not None:
            self.type = type
        if percent_width is not None:
            self.percent_width = percent_width

    @property
    def category(self):
        """Gets the category of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The category of this InlineObject148.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this InlineObject148.

          # noqa: E501

        :param category: The category of this InlineObject148.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def index(self):
        """Gets the index of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The index of this InlineObject148.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this InlineObject148.

          # noqa: E501

        :param index: The index of this InlineObject148.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def description(self):
        """Gets the description of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject148.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject148.

          # noqa: E501

        :param description: The description of this InlineObject148.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def title(self):
        """Gets the title of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The title of this InlineObject148.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineObject148.

          # noqa: E501

        :param title: The title of this InlineObject148.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def page_size(self):
        """Gets the page_size of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The page_size of this InlineObject148.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InlineObject148.

          # noqa: E501

        :param page_size: The page_size of this InlineObject148.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def time_range(self):
        """Gets the time_range of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The time_range of this InlineObject148.  # noqa: E501
        :rtype: int
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this InlineObject148.

          # noqa: E501

        :param time_range: The time_range of this InlineObject148.  # noqa: E501
        :type: int
        """

        self._time_range = time_range

    @property
    def is_editable(self):
        """Gets the is_editable of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The is_editable of this InlineObject148.  # noqa: E501
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """Sets the is_editable of this InlineObject148.

          # noqa: E501

        :param is_editable: The is_editable of this InlineObject148.  # noqa: E501
        :type: bool
        """

        self._is_editable = is_editable

    @property
    def template(self):
        """Gets the template of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The template of this InlineObject148.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this InlineObject148.

          # noqa: E501

        :param template: The template of this InlineObject148.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def dashboard(self):
        """Gets the dashboard of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The dashboard of this InlineObject148.  # noqa: E501
        :rtype: str
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """Sets the dashboard of this InlineObject148.

          # noqa: E501

        :param dashboard: The dashboard of this InlineObject148.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dashboard is None:  # noqa: E501
            raise ValueError("Invalid value for `dashboard`, must not be `None`")  # noqa: E501

        self._dashboard = dashboard

    @property
    def is_removable(self):
        """Gets the is_removable of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The is_removable of this InlineObject148.  # noqa: E501
        :rtype: bool
        """
        return self._is_removable

    @is_removable.setter
    def is_removable(self, is_removable):
        """Sets the is_removable of this InlineObject148.

          # noqa: E501

        :param is_removable: The is_removable of this InlineObject148.  # noqa: E501
        :type: bool
        """

        self._is_removable = is_removable

    @property
    def query(self):
        """Gets the query of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The query of this InlineObject148.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this InlineObject148.

          # noqa: E501

        :param query: The query of this InlineObject148.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def is_public(self):
        """Gets the is_public of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The is_public of this InlineObject148.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this InlineObject148.

          # noqa: E501

        :param is_public: The is_public of this InlineObject148.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject148.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject148.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject148.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def type(self):
        """Gets the type of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The type of this InlineObject148.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineObject148.

          # noqa: E501

        :param type: The type of this InlineObject148.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def percent_width(self):
        """Gets the percent_width of this InlineObject148.  # noqa: E501

          # noqa: E501

        :return: The percent_width of this InlineObject148.  # noqa: E501
        :rtype: int
        """
        return self._percent_width

    @percent_width.setter
    def percent_width(self, percent_width):
        """Sets the percent_width of this InlineObject148.

          # noqa: E501

        :param percent_width: The percent_width of this InlineObject148.  # noqa: E501
        :type: int
        """

        self._percent_width = percent_width

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
        if not isinstance(other, InlineObject148):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject148):
            return True

        return self.to_dict() != other.to_dict()
