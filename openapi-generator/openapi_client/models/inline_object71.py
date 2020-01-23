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


class InlineObject71(object):
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
        'last_run': 'str',
        'repeat': 'str',
        'name': 'str',
        'repeat_on': 'str',
        'deleted': 'bool',
        'state': 'str',
        'query': 'str',
        'run_time': 'str',
        'customer_id': 'str',
        'history': 'bool'
    }

    attribute_map = {
        'last_run': 'lastRun',
        'repeat': 'repeat',
        'name': 'name',
        'repeat_on': 'repeatOn',
        'deleted': 'deleted',
        'state': 'state',
        'query': 'query',
        'run_time': 'runTime',
        'customer_id': 'customer_id',
        'history': 'history'
    }

    def __init__(self, last_run=None, repeat=None, name=None, repeat_on=None, deleted=None, state=None, query=None, run_time=None, customer_id=None, history=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject71 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_run = None
        self._repeat = None
        self._name = None
        self._repeat_on = None
        self._deleted = None
        self._state = None
        self._query = None
        self._run_time = None
        self._customer_id = None
        self._history = None
        self.discriminator = None

        if last_run is not None:
            self.last_run = last_run
        if repeat is not None:
            self.repeat = repeat
        self.name = name
        if repeat_on is not None:
            self.repeat_on = repeat_on
        if deleted is not None:
            self.deleted = deleted
        if state is not None:
            self.state = state
        self.query = query
        if run_time is not None:
            self.run_time = run_time
        if customer_id is not None:
            self.customer_id = customer_id
        if history is not None:
            self.history = history

    @property
    def last_run(self):
        """Gets the last_run of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The last_run of this InlineObject71.  # noqa: E501
        :rtype: str
        """
        return self._last_run

    @last_run.setter
    def last_run(self, last_run):
        """Sets the last_run of this InlineObject71.

          # noqa: E501

        :param last_run: The last_run of this InlineObject71.  # noqa: E501
        :type: str
        """

        self._last_run = last_run

    @property
    def repeat(self):
        """Gets the repeat of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The repeat of this InlineObject71.  # noqa: E501
        :rtype: str
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """Sets the repeat of this InlineObject71.

          # noqa: E501

        :param repeat: The repeat of this InlineObject71.  # noqa: E501
        :type: str
        """

        self._repeat = repeat

    @property
    def name(self):
        """Gets the name of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The name of this InlineObject71.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject71.

          # noqa: E501

        :param name: The name of this InlineObject71.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def repeat_on(self):
        """Gets the repeat_on of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The repeat_on of this InlineObject71.  # noqa: E501
        :rtype: str
        """
        return self._repeat_on

    @repeat_on.setter
    def repeat_on(self, repeat_on):
        """Sets the repeat_on of this InlineObject71.

          # noqa: E501

        :param repeat_on: The repeat_on of this InlineObject71.  # noqa: E501
        :type: str
        """

        self._repeat_on = repeat_on

    @property
    def deleted(self):
        """Gets the deleted of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The deleted of this InlineObject71.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this InlineObject71.

          # noqa: E501

        :param deleted: The deleted of this InlineObject71.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def state(self):
        """Gets the state of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The state of this InlineObject71.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineObject71.

          # noqa: E501

        :param state: The state of this InlineObject71.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def query(self):
        """Gets the query of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The query of this InlineObject71.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this InlineObject71.

          # noqa: E501

        :param query: The query of this InlineObject71.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and query is None:  # noqa: E501
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def run_time(self):
        """Gets the run_time of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The run_time of this InlineObject71.  # noqa: E501
        :rtype: str
        """
        return self._run_time

    @run_time.setter
    def run_time(self, run_time):
        """Sets the run_time of this InlineObject71.

          # noqa: E501

        :param run_time: The run_time of this InlineObject71.  # noqa: E501
        :type: str
        """

        self._run_time = run_time

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject71.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject71.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject71.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def history(self):
        """Gets the history of this InlineObject71.  # noqa: E501

          # noqa: E501

        :return: The history of this InlineObject71.  # noqa: E501
        :rtype: bool
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this InlineObject71.

          # noqa: E501

        :param history: The history of this InlineObject71.  # noqa: E501
        :type: bool
        """

        self._history = history

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
        if not isinstance(other, InlineObject71):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject71):
            return True

        return self.to_dict() != other.to_dict()
