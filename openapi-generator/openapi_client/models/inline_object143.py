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


class InlineObject143(object):
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
        'is_enabled': 'bool',
        'repeat': 'str',
        'email_recipients': 'list[str]',
        'run_at': 'str',
        'dashboard': 'str',
        'email_password': 'str',
        'repeat_on': 'list[str]',
        'email_pdf': 'bool'
    }

    attribute_map = {
        'is_enabled': 'is_enabled',
        'repeat': 'repeat',
        'email_recipients': 'email_recipients',
        'run_at': 'run_at',
        'dashboard': 'dashboard',
        'email_password': 'email_password',
        'repeat_on': 'repeat_on',
        'email_pdf': 'email_pdf'
    }

    def __init__(self, is_enabled=None, repeat=None, email_recipients=None, run_at=None, dashboard=None, email_password=None, repeat_on=None, email_pdf=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject143 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_enabled = None
        self._repeat = None
        self._email_recipients = None
        self._run_at = None
        self._dashboard = None
        self._email_password = None
        self._repeat_on = None
        self._email_pdf = None
        self.discriminator = None

        if is_enabled is not None:
            self.is_enabled = is_enabled
        if repeat is not None:
            self.repeat = repeat
        if email_recipients is not None:
            self.email_recipients = email_recipients
        self.run_at = run_at
        self.dashboard = dashboard
        if email_password is not None:
            self.email_password = email_password
        if repeat_on is not None:
            self.repeat_on = repeat_on
        if email_pdf is not None:
            self.email_pdf = email_pdf

    @property
    def is_enabled(self):
        """Gets the is_enabled of this InlineObject143.  # noqa: E501

          # noqa: E501

        :return: The is_enabled of this InlineObject143.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this InlineObject143.

          # noqa: E501

        :param is_enabled: The is_enabled of this InlineObject143.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def repeat(self):
        """Gets the repeat of this InlineObject143.  # noqa: E501

          # noqa: E501

        :return: The repeat of this InlineObject143.  # noqa: E501
        :rtype: str
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """Sets the repeat of this InlineObject143.

          # noqa: E501

        :param repeat: The repeat of this InlineObject143.  # noqa: E501
        :type: str
        """

        self._repeat = repeat

    @property
    def email_recipients(self):
        """Gets the email_recipients of this InlineObject143.  # noqa: E501

          # noqa: E501

        :return: The email_recipients of this InlineObject143.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_recipients

    @email_recipients.setter
    def email_recipients(self, email_recipients):
        """Sets the email_recipients of this InlineObject143.

          # noqa: E501

        :param email_recipients: The email_recipients of this InlineObject143.  # noqa: E501
        :type: list[str]
        """

        self._email_recipients = email_recipients

    @property
    def run_at(self):
        """Gets the run_at of this InlineObject143.  # noqa: E501

          # noqa: E501

        :return: The run_at of this InlineObject143.  # noqa: E501
        :rtype: str
        """
        return self._run_at

    @run_at.setter
    def run_at(self, run_at):
        """Sets the run_at of this InlineObject143.

          # noqa: E501

        :param run_at: The run_at of this InlineObject143.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and run_at is None:  # noqa: E501
            raise ValueError("Invalid value for `run_at`, must not be `None`")  # noqa: E501

        self._run_at = run_at

    @property
    def dashboard(self):
        """Gets the dashboard of this InlineObject143.  # noqa: E501

          # noqa: E501

        :return: The dashboard of this InlineObject143.  # noqa: E501
        :rtype: str
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """Sets the dashboard of this InlineObject143.

          # noqa: E501

        :param dashboard: The dashboard of this InlineObject143.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dashboard is None:  # noqa: E501
            raise ValueError("Invalid value for `dashboard`, must not be `None`")  # noqa: E501

        self._dashboard = dashboard

    @property
    def email_password(self):
        """Gets the email_password of this InlineObject143.  # noqa: E501

          # noqa: E501

        :return: The email_password of this InlineObject143.  # noqa: E501
        :rtype: str
        """
        return self._email_password

    @email_password.setter
    def email_password(self, email_password):
        """Sets the email_password of this InlineObject143.

          # noqa: E501

        :param email_password: The email_password of this InlineObject143.  # noqa: E501
        :type: str
        """

        self._email_password = email_password

    @property
    def repeat_on(self):
        """Gets the repeat_on of this InlineObject143.  # noqa: E501

          # noqa: E501

        :return: The repeat_on of this InlineObject143.  # noqa: E501
        :rtype: list[str]
        """
        return self._repeat_on

    @repeat_on.setter
    def repeat_on(self, repeat_on):
        """Sets the repeat_on of this InlineObject143.

          # noqa: E501

        :param repeat_on: The repeat_on of this InlineObject143.  # noqa: E501
        :type: list[str]
        """

        self._repeat_on = repeat_on

    @property
    def email_pdf(self):
        """Gets the email_pdf of this InlineObject143.  # noqa: E501

          # noqa: E501

        :return: The email_pdf of this InlineObject143.  # noqa: E501
        :rtype: bool
        """
        return self._email_pdf

    @email_pdf.setter
    def email_pdf(self, email_pdf):
        """Sets the email_pdf of this InlineObject143.

          # noqa: E501

        :param email_pdf: The email_pdf of this InlineObject143.  # noqa: E501
        :type: bool
        """

        self._email_pdf = email_pdf

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
        if not isinstance(other, InlineObject143):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject143):
            return True

        return self.to_dict() != other.to_dict()
