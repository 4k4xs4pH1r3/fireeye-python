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


class InlineObject126(object):
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
        'last_event_at': 'str',
        'alert_type': 'object',
        'classification': 'int',
        'origin_id': 'str',
        'is_tuned': 'bool',
        'is_suppressed': 'bool',
        'emailed_at': 'int',
        'is_hidden': 'bool',
        'first_event_at': 'str',
        'alert_type_details': 'str',
        'id': 'int',
        'confidence': 'str',
        'severity': 'str',
        'closed_reason': 'str',
        'threat_type': 'int',
        'threat_changed_at': 'str',
        'state': 'str',
        'trigger_revision': 'int',
        'alert_threat': 'str',
        'closed_state': 'str',
        'type': 'str',
        'last_sync_ms': 'int',
        'description': 'str',
        'tags': 'list[str]',
        'distinguisher_key': 'str',
        'trigger_id': 'str',
        'distinguishers': 'str',
        'kill_chain': 'list[str]',
        'assigned_at': 'str',
        'info_links': 'list[str]',
        'metaclasses': 'str',
        'risk_order': 'int',
        'search': 'str',
        'message': 'str',
        'mongo_id': 'str',
        'source_revision': 'int',
        'tuning_search': 'str',
        'products': 'str',
        'assigned_to': 'object',
        'external_id': 'str'
    }

    attribute_map = {
        'last_event_at': 'last_event_at',
        'alert_type': 'alert_type',
        'classification': 'classification',
        'origin_id': 'origin_id',
        'is_tuned': 'is_tuned',
        'is_suppressed': 'is_suppressed',
        'emailed_at': 'emailed_at',
        'is_hidden': 'is_hidden',
        'first_event_at': 'first_event_at',
        'alert_type_details': 'alert_type_details',
        'id': 'id',
        'confidence': 'confidence',
        'severity': 'severity',
        'closed_reason': 'closed_reason',
        'threat_type': 'threat_type',
        'threat_changed_at': 'threat_changed_at',
        'state': 'state',
        'trigger_revision': 'trigger_revision',
        'alert_threat': 'alert_threat',
        'closed_state': 'closed_state',
        'type': 'type',
        'last_sync_ms': 'last_sync_ms',
        'description': 'description',
        'tags': 'tags',
        'distinguisher_key': 'distinguisher_key',
        'trigger_id': 'trigger_id',
        'distinguishers': 'distinguishers',
        'kill_chain': 'kill_chain',
        'assigned_at': 'assigned_at',
        'info_links': 'info_links',
        'metaclasses': 'metaclasses',
        'risk_order': 'risk_order',
        'search': 'search',
        'message': 'message',
        'mongo_id': 'mongo_id',
        'source_revision': 'source_revision',
        'tuning_search': 'tuning_search',
        'products': 'products',
        'assigned_to': 'assigned_to',
        'external_id': 'external_id'
    }

    def __init__(self, last_event_at=None, alert_type=None, classification=None, origin_id=None, is_tuned=None, is_suppressed=None, emailed_at=None, is_hidden=None, first_event_at=None, alert_type_details=None, id=None, confidence=None, severity=None, closed_reason=None, threat_type=None, threat_changed_at=None, state=None, trigger_revision=None, alert_threat=None, closed_state=None, type=None, last_sync_ms=None, description=None, tags=None, distinguisher_key=None, trigger_id=None, distinguishers=None, kill_chain=None, assigned_at=None, info_links=None, metaclasses=None, risk_order=None, search=None, message=None, mongo_id=None, source_revision=None, tuning_search=None, products=None, assigned_to=None, external_id=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject126 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_event_at = None
        self._alert_type = None
        self._classification = None
        self._origin_id = None
        self._is_tuned = None
        self._is_suppressed = None
        self._emailed_at = None
        self._is_hidden = None
        self._first_event_at = None
        self._alert_type_details = None
        self._id = None
        self._confidence = None
        self._severity = None
        self._closed_reason = None
        self._threat_type = None
        self._threat_changed_at = None
        self._state = None
        self._trigger_revision = None
        self._alert_threat = None
        self._closed_state = None
        self._type = None
        self._last_sync_ms = None
        self._description = None
        self._tags = None
        self._distinguisher_key = None
        self._trigger_id = None
        self._distinguishers = None
        self._kill_chain = None
        self._assigned_at = None
        self._info_links = None
        self._metaclasses = None
        self._risk_order = None
        self._search = None
        self._message = None
        self._mongo_id = None
        self._source_revision = None
        self._tuning_search = None
        self._products = None
        self._assigned_to = None
        self._external_id = None
        self.discriminator = None

        if last_event_at is not None:
            self.last_event_at = last_event_at
        if alert_type is not None:
            self.alert_type = alert_type
        if classification is not None:
            self.classification = classification
        self.origin_id = origin_id
        if is_tuned is not None:
            self.is_tuned = is_tuned
        if is_suppressed is not None:
            self.is_suppressed = is_suppressed
        if emailed_at is not None:
            self.emailed_at = emailed_at
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if first_event_at is not None:
            self.first_event_at = first_event_at
        if alert_type_details is not None:
            self.alert_type_details = alert_type_details
        if id is not None:
            self.id = id
        self.confidence = confidence
        self.severity = severity
        if closed_reason is not None:
            self.closed_reason = closed_reason
        if threat_type is not None:
            self.threat_type = threat_type
        if threat_changed_at is not None:
            self.threat_changed_at = threat_changed_at
        if state is not None:
            self.state = state
        if trigger_revision is not None:
            self.trigger_revision = trigger_revision
        if alert_threat is not None:
            self.alert_threat = alert_threat
        if closed_state is not None:
            self.closed_state = closed_state
        self.type = type
        if last_sync_ms is not None:
            self.last_sync_ms = last_sync_ms
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if distinguisher_key is not None:
            self.distinguisher_key = distinguisher_key
        if trigger_id is not None:
            self.trigger_id = trigger_id
        if distinguishers is not None:
            self.distinguishers = distinguishers
        if kill_chain is not None:
            self.kill_chain = kill_chain
        if assigned_at is not None:
            self.assigned_at = assigned_at
        if info_links is not None:
            self.info_links = info_links
        if metaclasses is not None:
            self.metaclasses = metaclasses
        if risk_order is not None:
            self.risk_order = risk_order
        if search is not None:
            self.search = search
        self.message = message
        if mongo_id is not None:
            self.mongo_id = mongo_id
        if source_revision is not None:
            self.source_revision = source_revision
        if tuning_search is not None:
            self.tuning_search = tuning_search
        if products is not None:
            self.products = products
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if external_id is not None:
            self.external_id = external_id

    @property
    def last_event_at(self):
        """Gets the last_event_at of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The last_event_at of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._last_event_at

    @last_event_at.setter
    def last_event_at(self, last_event_at):
        """Sets the last_event_at of this InlineObject126.

          # noqa: E501

        :param last_event_at: The last_event_at of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._last_event_at = last_event_at

    @property
    def alert_type(self):
        """Gets the alert_type of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The alert_type of this InlineObject126.  # noqa: E501
        :rtype: object
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this InlineObject126.

          # noqa: E501

        :param alert_type: The alert_type of this InlineObject126.  # noqa: E501
        :type: object
        """

        self._alert_type = alert_type

    @property
    def classification(self):
        """Gets the classification of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The classification of this InlineObject126.  # noqa: E501
        :rtype: int
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this InlineObject126.

          # noqa: E501

        :param classification: The classification of this InlineObject126.  # noqa: E501
        :type: int
        """

        self._classification = classification

    @property
    def origin_id(self):
        """Gets the origin_id of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The origin_id of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._origin_id

    @origin_id.setter
    def origin_id(self, origin_id):
        """Sets the origin_id of this InlineObject126.

          # noqa: E501

        :param origin_id: The origin_id of this InlineObject126.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and origin_id is None:  # noqa: E501
            raise ValueError("Invalid value for `origin_id`, must not be `None`")  # noqa: E501

        self._origin_id = origin_id

    @property
    def is_tuned(self):
        """Gets the is_tuned of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The is_tuned of this InlineObject126.  # noqa: E501
        :rtype: bool
        """
        return self._is_tuned

    @is_tuned.setter
    def is_tuned(self, is_tuned):
        """Sets the is_tuned of this InlineObject126.

          # noqa: E501

        :param is_tuned: The is_tuned of this InlineObject126.  # noqa: E501
        :type: bool
        """

        self._is_tuned = is_tuned

    @property
    def is_suppressed(self):
        """Gets the is_suppressed of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The is_suppressed of this InlineObject126.  # noqa: E501
        :rtype: bool
        """
        return self._is_suppressed

    @is_suppressed.setter
    def is_suppressed(self, is_suppressed):
        """Sets the is_suppressed of this InlineObject126.

          # noqa: E501

        :param is_suppressed: The is_suppressed of this InlineObject126.  # noqa: E501
        :type: bool
        """

        self._is_suppressed = is_suppressed

    @property
    def emailed_at(self):
        """Gets the emailed_at of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The emailed_at of this InlineObject126.  # noqa: E501
        :rtype: int
        """
        return self._emailed_at

    @emailed_at.setter
    def emailed_at(self, emailed_at):
        """Sets the emailed_at of this InlineObject126.

          # noqa: E501

        :param emailed_at: The emailed_at of this InlineObject126.  # noqa: E501
        :type: int
        """

        self._emailed_at = emailed_at

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject126.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject126.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject126.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def first_event_at(self):
        """Gets the first_event_at of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The first_event_at of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._first_event_at

    @first_event_at.setter
    def first_event_at(self, first_event_at):
        """Sets the first_event_at of this InlineObject126.

          # noqa: E501

        :param first_event_at: The first_event_at of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._first_event_at = first_event_at

    @property
    def alert_type_details(self):
        """Gets the alert_type_details of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The alert_type_details of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._alert_type_details

    @alert_type_details.setter
    def alert_type_details(self, alert_type_details):
        """Sets the alert_type_details of this InlineObject126.

          # noqa: E501

        :param alert_type_details: The alert_type_details of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._alert_type_details = alert_type_details

    @property
    def id(self):
        """Gets the id of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The id of this InlineObject126.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineObject126.

          # noqa: E501

        :param id: The id of this InlineObject126.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def confidence(self):
        """Gets the confidence of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The confidence of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this InlineObject126.

          # noqa: E501

        :param confidence: The confidence of this InlineObject126.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and confidence is None:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must not be `None`")  # noqa: E501

        self._confidence = confidence

    @property
    def severity(self):
        """Gets the severity of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The severity of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this InlineObject126.

          # noqa: E501

        :param severity: The severity of this InlineObject126.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and severity is None:  # noqa: E501
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def closed_reason(self):
        """Gets the closed_reason of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The closed_reason of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._closed_reason

    @closed_reason.setter
    def closed_reason(self, closed_reason):
        """Sets the closed_reason of this InlineObject126.

          # noqa: E501

        :param closed_reason: The closed_reason of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._closed_reason = closed_reason

    @property
    def threat_type(self):
        """Gets the threat_type of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The threat_type of this InlineObject126.  # noqa: E501
        :rtype: int
        """
        return self._threat_type

    @threat_type.setter
    def threat_type(self, threat_type):
        """Sets the threat_type of this InlineObject126.

          # noqa: E501

        :param threat_type: The threat_type of this InlineObject126.  # noqa: E501
        :type: int
        """

        self._threat_type = threat_type

    @property
    def threat_changed_at(self):
        """Gets the threat_changed_at of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The threat_changed_at of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._threat_changed_at

    @threat_changed_at.setter
    def threat_changed_at(self, threat_changed_at):
        """Sets the threat_changed_at of this InlineObject126.

          # noqa: E501

        :param threat_changed_at: The threat_changed_at of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._threat_changed_at = threat_changed_at

    @property
    def state(self):
        """Gets the state of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The state of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineObject126.

          # noqa: E501

        :param state: The state of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def trigger_revision(self):
        """Gets the trigger_revision of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The trigger_revision of this InlineObject126.  # noqa: E501
        :rtype: int
        """
        return self._trigger_revision

    @trigger_revision.setter
    def trigger_revision(self, trigger_revision):
        """Sets the trigger_revision of this InlineObject126.

          # noqa: E501

        :param trigger_revision: The trigger_revision of this InlineObject126.  # noqa: E501
        :type: int
        """

        self._trigger_revision = trigger_revision

    @property
    def alert_threat(self):
        """Gets the alert_threat of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The alert_threat of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._alert_threat

    @alert_threat.setter
    def alert_threat(self, alert_threat):
        """Sets the alert_threat of this InlineObject126.

          # noqa: E501

        :param alert_threat: The alert_threat of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._alert_threat = alert_threat

    @property
    def closed_state(self):
        """Gets the closed_state of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The closed_state of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._closed_state

    @closed_state.setter
    def closed_state(self, closed_state):
        """Sets the closed_state of this InlineObject126.

          # noqa: E501

        :param closed_state: The closed_state of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._closed_state = closed_state

    @property
    def type(self):
        """Gets the type of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The type of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineObject126.

          # noqa: E501

        :param type: The type of this InlineObject126.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def last_sync_ms(self):
        """Gets the last_sync_ms of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The last_sync_ms of this InlineObject126.  # noqa: E501
        :rtype: int
        """
        return self._last_sync_ms

    @last_sync_ms.setter
    def last_sync_ms(self, last_sync_ms):
        """Sets the last_sync_ms of this InlineObject126.

          # noqa: E501

        :param last_sync_ms: The last_sync_ms of this InlineObject126.  # noqa: E501
        :type: int
        """

        self._last_sync_ms = last_sync_ms

    @property
    def description(self):
        """Gets the description of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject126.

          # noqa: E501

        :param description: The description of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The tags of this InlineObject126.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject126.

          # noqa: E501

        :param tags: The tags of this InlineObject126.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def distinguisher_key(self):
        """Gets the distinguisher_key of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The distinguisher_key of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._distinguisher_key

    @distinguisher_key.setter
    def distinguisher_key(self, distinguisher_key):
        """Sets the distinguisher_key of this InlineObject126.

          # noqa: E501

        :param distinguisher_key: The distinguisher_key of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._distinguisher_key = distinguisher_key

    @property
    def trigger_id(self):
        """Gets the trigger_id of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The trigger_id of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this InlineObject126.

          # noqa: E501

        :param trigger_id: The trigger_id of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._trigger_id = trigger_id

    @property
    def distinguishers(self):
        """Gets the distinguishers of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The distinguishers of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._distinguishers

    @distinguishers.setter
    def distinguishers(self, distinguishers):
        """Sets the distinguishers of this InlineObject126.

          # noqa: E501

        :param distinguishers: The distinguishers of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._distinguishers = distinguishers

    @property
    def kill_chain(self):
        """Gets the kill_chain of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The kill_chain of this InlineObject126.  # noqa: E501
        :rtype: list[str]
        """
        return self._kill_chain

    @kill_chain.setter
    def kill_chain(self, kill_chain):
        """Sets the kill_chain of this InlineObject126.

          # noqa: E501

        :param kill_chain: The kill_chain of this InlineObject126.  # noqa: E501
        :type: list[str]
        """

        self._kill_chain = kill_chain

    @property
    def assigned_at(self):
        """Gets the assigned_at of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The assigned_at of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._assigned_at

    @assigned_at.setter
    def assigned_at(self, assigned_at):
        """Sets the assigned_at of this InlineObject126.

          # noqa: E501

        :param assigned_at: The assigned_at of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._assigned_at = assigned_at

    @property
    def info_links(self):
        """Gets the info_links of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The info_links of this InlineObject126.  # noqa: E501
        :rtype: list[str]
        """
        return self._info_links

    @info_links.setter
    def info_links(self, info_links):
        """Sets the info_links of this InlineObject126.

          # noqa: E501

        :param info_links: The info_links of this InlineObject126.  # noqa: E501
        :type: list[str]
        """

        self._info_links = info_links

    @property
    def metaclasses(self):
        """Gets the metaclasses of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The metaclasses of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._metaclasses

    @metaclasses.setter
    def metaclasses(self, metaclasses):
        """Sets the metaclasses of this InlineObject126.

          # noqa: E501

        :param metaclasses: The metaclasses of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._metaclasses = metaclasses

    @property
    def risk_order(self):
        """Gets the risk_order of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The risk_order of this InlineObject126.  # noqa: E501
        :rtype: int
        """
        return self._risk_order

    @risk_order.setter
    def risk_order(self, risk_order):
        """Sets the risk_order of this InlineObject126.

          # noqa: E501

        :param risk_order: The risk_order of this InlineObject126.  # noqa: E501
        :type: int
        """

        self._risk_order = risk_order

    @property
    def search(self):
        """Gets the search of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The search of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this InlineObject126.

          # noqa: E501

        :param search: The search of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._search = search

    @property
    def message(self):
        """Gets the message of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The message of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineObject126.

          # noqa: E501

        :param message: The message of this InlineObject126.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def mongo_id(self):
        """Gets the mongo_id of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The mongo_id of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._mongo_id

    @mongo_id.setter
    def mongo_id(self, mongo_id):
        """Sets the mongo_id of this InlineObject126.

          # noqa: E501

        :param mongo_id: The mongo_id of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._mongo_id = mongo_id

    @property
    def source_revision(self):
        """Gets the source_revision of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The source_revision of this InlineObject126.  # noqa: E501
        :rtype: int
        """
        return self._source_revision

    @source_revision.setter
    def source_revision(self, source_revision):
        """Sets the source_revision of this InlineObject126.

          # noqa: E501

        :param source_revision: The source_revision of this InlineObject126.  # noqa: E501
        :type: int
        """

        self._source_revision = source_revision

    @property
    def tuning_search(self):
        """Gets the tuning_search of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The tuning_search of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._tuning_search

    @tuning_search.setter
    def tuning_search(self, tuning_search):
        """Sets the tuning_search of this InlineObject126.

          # noqa: E501

        :param tuning_search: The tuning_search of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._tuning_search = tuning_search

    @property
    def products(self):
        """Gets the products of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The products of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this InlineObject126.

          # noqa: E501

        :param products: The products of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._products = products

    @property
    def assigned_to(self):
        """Gets the assigned_to of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The assigned_to of this InlineObject126.  # noqa: E501
        :rtype: object
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this InlineObject126.

          # noqa: E501

        :param assigned_to: The assigned_to of this InlineObject126.  # noqa: E501
        :type: object
        """

        self._assigned_to = assigned_to

    @property
    def external_id(self):
        """Gets the external_id of this InlineObject126.  # noqa: E501

          # noqa: E501

        :return: The external_id of this InlineObject126.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this InlineObject126.

          # noqa: E501

        :param external_id: The external_id of this InlineObject126.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if not isinstance(other, InlineObject126):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject126):
            return True

        return self.to_dict() != other.to_dict()
