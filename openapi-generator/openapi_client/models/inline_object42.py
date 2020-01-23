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


class InlineObject42(object):
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
        'status': 'str',
        'classification': 'str',
        'description': 'str',
        'info_links': 'list[str]',
        'assigned_to': 'object',
        'severity': 'int',
        'tags': 'list[str]',
        'alert': 'list[str]',
        'priority': 'str',
        'is_hidden': 'bool',
        'customer_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'classification': 'classification',
        'description': 'description',
        'info_links': 'infoLinks',
        'assigned_to': '_assignedTo',
        'severity': 'severity',
        'tags': 'tags',
        'alert': '_alert',
        'priority': 'priority',
        'is_hidden': 'is_hidden',
        'customer_id': 'customer_id',
        'name': 'name'
    }

    def __init__(self, status=None, classification=None, description=None, info_links=None, assigned_to=None, severity=None, tags=None, alert=None, priority=None, is_hidden=None, customer_id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject42 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._classification = None
        self._description = None
        self._info_links = None
        self._assigned_to = None
        self._severity = None
        self._tags = None
        self._alert = None
        self._priority = None
        self._is_hidden = None
        self._customer_id = None
        self._name = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if classification is not None:
            self.classification = classification
        if description is not None:
            self.description = description
        if info_links is not None:
            self.info_links = info_links
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if severity is not None:
            self.severity = severity
        if tags is not None:
            self.tags = tags
        if alert is not None:
            self.alert = alert
        if priority is not None:
            self.priority = priority
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if customer_id is not None:
            self.customer_id = customer_id
        self.name = name

    @property
    def status(self):
        """Gets the status of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The status of this InlineObject42.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineObject42.

          # noqa: E501

        :param status: The status of this InlineObject42.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def classification(self):
        """Gets the classification of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The classification of this InlineObject42.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this InlineObject42.

          # noqa: E501

        :param classification: The classification of this InlineObject42.  # noqa: E501
        :type: str
        """

        self._classification = classification

    @property
    def description(self):
        """Gets the description of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject42.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject42.

          # noqa: E501

        :param description: The description of this InlineObject42.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def info_links(self):
        """Gets the info_links of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The info_links of this InlineObject42.  # noqa: E501
        :rtype: list[str]
        """
        return self._info_links

    @info_links.setter
    def info_links(self, info_links):
        """Sets the info_links of this InlineObject42.

          # noqa: E501

        :param info_links: The info_links of this InlineObject42.  # noqa: E501
        :type: list[str]
        """

        self._info_links = info_links

    @property
    def assigned_to(self):
        """Gets the assigned_to of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The assigned_to of this InlineObject42.  # noqa: E501
        :rtype: object
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this InlineObject42.

          # noqa: E501

        :param assigned_to: The assigned_to of this InlineObject42.  # noqa: E501
        :type: object
        """

        self._assigned_to = assigned_to

    @property
    def severity(self):
        """Gets the severity of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The severity of this InlineObject42.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this InlineObject42.

          # noqa: E501

        :param severity: The severity of this InlineObject42.  # noqa: E501
        :type: int
        """

        self._severity = severity

    @property
    def tags(self):
        """Gets the tags of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The tags of this InlineObject42.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject42.

          # noqa: E501

        :param tags: The tags of this InlineObject42.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def alert(self):
        """Gets the alert of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The alert of this InlineObject42.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this InlineObject42.

          # noqa: E501

        :param alert: The alert of this InlineObject42.  # noqa: E501
        :type: list[str]
        """

        self._alert = alert

    @property
    def priority(self):
        """Gets the priority of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The priority of this InlineObject42.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this InlineObject42.

          # noqa: E501

        :param priority: The priority of this InlineObject42.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject42.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject42.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject42.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject42.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject42.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject42.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this InlineObject42.  # noqa: E501

          # noqa: E501

        :return: The name of this InlineObject42.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject42.

          # noqa: E501

        :param name: The name of this InlineObject42.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, InlineObject42):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject42):
            return True

        return self.to_dict() != other.to_dict()
