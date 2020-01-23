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


class InlineObject2(object):
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
        'created_by': 'str',
        'end_date': 'str',
        'create_date': 'str',
        'updated_by': 'str',
        'trigger_id': 'str',
        'update_date': 'str',
        'distinguishers': 'str',
        'origin_id': 'str'
    }

    attribute_map = {
        'created_by': '_createdBy',
        'end_date': 'endDate',
        'create_date': 'createDate',
        'updated_by': '_updatedBy',
        'trigger_id': 'triggerId',
        'update_date': 'updateDate',
        'distinguishers': 'distinguishers',
        'origin_id': 'originId'
    }

    def __init__(self, created_by=None, end_date=None, create_date=None, updated_by=None, trigger_id=None, update_date=None, distinguishers=None, origin_id=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_by = None
        self._end_date = None
        self._create_date = None
        self._updated_by = None
        self._trigger_id = None
        self._update_date = None
        self._distinguishers = None
        self._origin_id = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if end_date is not None:
            self.end_date = end_date
        if create_date is not None:
            self.create_date = create_date
        if updated_by is not None:
            self.updated_by = updated_by
        if trigger_id is not None:
            self.trigger_id = trigger_id
        if update_date is not None:
            self.update_date = update_date
        if distinguishers is not None:
            self.distinguishers = distinguishers
        if origin_id is not None:
            self.origin_id = origin_id

    @property
    def created_by(self):
        """Gets the created_by of this InlineObject2.  # noqa: E501

          # noqa: E501

        :return: The created_by of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InlineObject2.

          # noqa: E501

        :param created_by: The created_by of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def end_date(self):
        """Gets the end_date of this InlineObject2.  # noqa: E501

          # noqa: E501

        :return: The end_date of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this InlineObject2.

          # noqa: E501

        :param end_date: The end_date of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def create_date(self):
        """Gets the create_date of this InlineObject2.  # noqa: E501

          # noqa: E501

        :return: The create_date of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this InlineObject2.

          # noqa: E501

        :param create_date: The create_date of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def updated_by(self):
        """Gets the updated_by of this InlineObject2.  # noqa: E501

          # noqa: E501

        :return: The updated_by of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this InlineObject2.

          # noqa: E501

        :param updated_by: The updated_by of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def trigger_id(self):
        """Gets the trigger_id of this InlineObject2.  # noqa: E501

          # noqa: E501

        :return: The trigger_id of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this InlineObject2.

          # noqa: E501

        :param trigger_id: The trigger_id of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._trigger_id = trigger_id

    @property
    def update_date(self):
        """Gets the update_date of this InlineObject2.  # noqa: E501

          # noqa: E501

        :return: The update_date of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this InlineObject2.

          # noqa: E501

        :param update_date: The update_date of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

    @property
    def distinguishers(self):
        """Gets the distinguishers of this InlineObject2.  # noqa: E501

          # noqa: E501

        :return: The distinguishers of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._distinguishers

    @distinguishers.setter
    def distinguishers(self, distinguishers):
        """Sets the distinguishers of this InlineObject2.

          # noqa: E501

        :param distinguishers: The distinguishers of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._distinguishers = distinguishers

    @property
    def origin_id(self):
        """Gets the origin_id of this InlineObject2.  # noqa: E501

          # noqa: E501

        :return: The origin_id of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._origin_id

    @origin_id.setter
    def origin_id(self, origin_id):
        """Sets the origin_id of this InlineObject2.

          # noqa: E501

        :param origin_id: The origin_id of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._origin_id = origin_id

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
        if not isinstance(other, InlineObject2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject2):
            return True

        return self.to_dict() != other.to_dict()
