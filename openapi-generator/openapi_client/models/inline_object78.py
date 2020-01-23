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


class InlineObject78(object):
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
        'email_notify': 'bool',
        'num_results': 'int',
        'search_end_date': 'str',
        'errors': 'list[str]',
        'is_part_of_report': 'bool',
        'name': 'str',
        'source_bucket': 'str',
        'search_start_date': 'str',
        'complete_after_count': 'int',
        'is_mssp': 'bool',
        'state': 'str',
        'search_customer_ids': 'list[str]',
        'percent_complete': 'float',
        'time_remaining': 'float',
        'query': 'str',
        'is_hidden': 'bool',
        'customer_id': 'str',
        'complete_after_duration': 'int'
    }

    attribute_map = {
        'email_notify': 'emailNotify',
        'num_results': 'numResults',
        'search_end_date': 'searchEndDate',
        'errors': 'errors',
        'is_part_of_report': 'is_part_of_report',
        'name': 'name',
        'source_bucket': 'sourceBucket',
        'search_start_date': 'searchStartDate',
        'complete_after_count': 'completeAfterCount',
        'is_mssp': 'is_mssp',
        'state': 'state',
        'search_customer_ids': 'search_customer_ids',
        'percent_complete': 'percentComplete',
        'time_remaining': 'timeRemaining',
        'query': 'query',
        'is_hidden': 'is_hidden',
        'customer_id': 'customer_id',
        'complete_after_duration': 'completeAfterDuration'
    }

    def __init__(self, email_notify=None, num_results=None, search_end_date=None, errors=None, is_part_of_report=None, name=None, source_bucket=None, search_start_date=None, complete_after_count=None, is_mssp=None, state=None, search_customer_ids=None, percent_complete=None, time_remaining=None, query=None, is_hidden=None, customer_id=None, complete_after_duration=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject78 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_notify = None
        self._num_results = None
        self._search_end_date = None
        self._errors = None
        self._is_part_of_report = None
        self._name = None
        self._source_bucket = None
        self._search_start_date = None
        self._complete_after_count = None
        self._is_mssp = None
        self._state = None
        self._search_customer_ids = None
        self._percent_complete = None
        self._time_remaining = None
        self._query = None
        self._is_hidden = None
        self._customer_id = None
        self._complete_after_duration = None
        self.discriminator = None

        if email_notify is not None:
            self.email_notify = email_notify
        if num_results is not None:
            self.num_results = num_results
        if search_end_date is not None:
            self.search_end_date = search_end_date
        if errors is not None:
            self.errors = errors
        if is_part_of_report is not None:
            self.is_part_of_report = is_part_of_report
        if name is not None:
            self.name = name
        if source_bucket is not None:
            self.source_bucket = source_bucket
        if search_start_date is not None:
            self.search_start_date = search_start_date
        if complete_after_count is not None:
            self.complete_after_count = complete_after_count
        if is_mssp is not None:
            self.is_mssp = is_mssp
        if state is not None:
            self.state = state
        if search_customer_ids is not None:
            self.search_customer_ids = search_customer_ids
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if time_remaining is not None:
            self.time_remaining = time_remaining
        self.query = query
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if customer_id is not None:
            self.customer_id = customer_id
        if complete_after_duration is not None:
            self.complete_after_duration = complete_after_duration

    @property
    def email_notify(self):
        """Gets the email_notify of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The email_notify of this InlineObject78.  # noqa: E501
        :rtype: bool
        """
        return self._email_notify

    @email_notify.setter
    def email_notify(self, email_notify):
        """Sets the email_notify of this InlineObject78.

          # noqa: E501

        :param email_notify: The email_notify of this InlineObject78.  # noqa: E501
        :type: bool
        """

        self._email_notify = email_notify

    @property
    def num_results(self):
        """Gets the num_results of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The num_results of this InlineObject78.  # noqa: E501
        :rtype: int
        """
        return self._num_results

    @num_results.setter
    def num_results(self, num_results):
        """Sets the num_results of this InlineObject78.

          # noqa: E501

        :param num_results: The num_results of this InlineObject78.  # noqa: E501
        :type: int
        """

        self._num_results = num_results

    @property
    def search_end_date(self):
        """Gets the search_end_date of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The search_end_date of this InlineObject78.  # noqa: E501
        :rtype: str
        """
        return self._search_end_date

    @search_end_date.setter
    def search_end_date(self, search_end_date):
        """Sets the search_end_date of this InlineObject78.

          # noqa: E501

        :param search_end_date: The search_end_date of this InlineObject78.  # noqa: E501
        :type: str
        """

        self._search_end_date = search_end_date

    @property
    def errors(self):
        """Gets the errors of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The errors of this InlineObject78.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineObject78.

          # noqa: E501

        :param errors: The errors of this InlineObject78.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

    @property
    def is_part_of_report(self):
        """Gets the is_part_of_report of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The is_part_of_report of this InlineObject78.  # noqa: E501
        :rtype: bool
        """
        return self._is_part_of_report

    @is_part_of_report.setter
    def is_part_of_report(self, is_part_of_report):
        """Sets the is_part_of_report of this InlineObject78.

          # noqa: E501

        :param is_part_of_report: The is_part_of_report of this InlineObject78.  # noqa: E501
        :type: bool
        """

        self._is_part_of_report = is_part_of_report

    @property
    def name(self):
        """Gets the name of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The name of this InlineObject78.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject78.

          # noqa: E501

        :param name: The name of this InlineObject78.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_bucket(self):
        """Gets the source_bucket of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The source_bucket of this InlineObject78.  # noqa: E501
        :rtype: str
        """
        return self._source_bucket

    @source_bucket.setter
    def source_bucket(self, source_bucket):
        """Sets the source_bucket of this InlineObject78.

          # noqa: E501

        :param source_bucket: The source_bucket of this InlineObject78.  # noqa: E501
        :type: str
        """

        self._source_bucket = source_bucket

    @property
    def search_start_date(self):
        """Gets the search_start_date of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The search_start_date of this InlineObject78.  # noqa: E501
        :rtype: str
        """
        return self._search_start_date

    @search_start_date.setter
    def search_start_date(self, search_start_date):
        """Sets the search_start_date of this InlineObject78.

          # noqa: E501

        :param search_start_date: The search_start_date of this InlineObject78.  # noqa: E501
        :type: str
        """

        self._search_start_date = search_start_date

    @property
    def complete_after_count(self):
        """Gets the complete_after_count of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The complete_after_count of this InlineObject78.  # noqa: E501
        :rtype: int
        """
        return self._complete_after_count

    @complete_after_count.setter
    def complete_after_count(self, complete_after_count):
        """Sets the complete_after_count of this InlineObject78.

          # noqa: E501

        :param complete_after_count: The complete_after_count of this InlineObject78.  # noqa: E501
        :type: int
        """

        self._complete_after_count = complete_after_count

    @property
    def is_mssp(self):
        """Gets the is_mssp of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The is_mssp of this InlineObject78.  # noqa: E501
        :rtype: bool
        """
        return self._is_mssp

    @is_mssp.setter
    def is_mssp(self, is_mssp):
        """Sets the is_mssp of this InlineObject78.

          # noqa: E501

        :param is_mssp: The is_mssp of this InlineObject78.  # noqa: E501
        :type: bool
        """

        self._is_mssp = is_mssp

    @property
    def state(self):
        """Gets the state of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The state of this InlineObject78.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineObject78.

          # noqa: E501

        :param state: The state of this InlineObject78.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def search_customer_ids(self):
        """Gets the search_customer_ids of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The search_customer_ids of this InlineObject78.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_customer_ids

    @search_customer_ids.setter
    def search_customer_ids(self, search_customer_ids):
        """Sets the search_customer_ids of this InlineObject78.

          # noqa: E501

        :param search_customer_ids: The search_customer_ids of this InlineObject78.  # noqa: E501
        :type: list[str]
        """

        self._search_customer_ids = search_customer_ids

    @property
    def percent_complete(self):
        """Gets the percent_complete of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The percent_complete of this InlineObject78.  # noqa: E501
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this InlineObject78.

          # noqa: E501

        :param percent_complete: The percent_complete of this InlineObject78.  # noqa: E501
        :type: float
        """

        self._percent_complete = percent_complete

    @property
    def time_remaining(self):
        """Gets the time_remaining of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The time_remaining of this InlineObject78.  # noqa: E501
        :rtype: float
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this InlineObject78.

          # noqa: E501

        :param time_remaining: The time_remaining of this InlineObject78.  # noqa: E501
        :type: float
        """

        self._time_remaining = time_remaining

    @property
    def query(self):
        """Gets the query of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The query of this InlineObject78.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this InlineObject78.

          # noqa: E501

        :param query: The query of this InlineObject78.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and query is None:  # noqa: E501
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject78.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject78.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject78.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject78.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject78.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject78.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def complete_after_duration(self):
        """Gets the complete_after_duration of this InlineObject78.  # noqa: E501

          # noqa: E501

        :return: The complete_after_duration of this InlineObject78.  # noqa: E501
        :rtype: int
        """
        return self._complete_after_duration

    @complete_after_duration.setter
    def complete_after_duration(self, complete_after_duration):
        """Sets the complete_after_duration of this InlineObject78.

          # noqa: E501

        :param complete_after_duration: The complete_after_duration of this InlineObject78.  # noqa: E501
        :type: int
        """

        self._complete_after_duration = complete_after_duration

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
        if not isinstance(other, InlineObject78):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject78):
            return True

        return self.to_dict() != other.to_dict()
