# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBackendSetDetails(object):
    """
    The configuration details for updating a load balancer backend set.
    For more information on backend set configuration, see
    `Managing Backend Sets`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingbackendsets.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBackendSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this UpdateBackendSetDetails.
        :type policy: str

        :param backends:
            The value to assign to the backends property of this UpdateBackendSetDetails.
        :type backends: list[BackendDetails]

        :param health_checker:
            The value to assign to the health_checker property of this UpdateBackendSetDetails.
        :type health_checker: HealthCheckerDetails

        :param ssl_configuration:
            The value to assign to the ssl_configuration property of this UpdateBackendSetDetails.
        :type ssl_configuration: SSLConfigurationDetails

        :param session_persistence_configuration:
            The value to assign to the session_persistence_configuration property of this UpdateBackendSetDetails.
        :type session_persistence_configuration: SessionPersistenceConfigurationDetails

        """
        self.swagger_types = {
            'policy': 'str',
            'backends': 'list[BackendDetails]',
            'health_checker': 'HealthCheckerDetails',
            'ssl_configuration': 'SSLConfigurationDetails',
            'session_persistence_configuration': 'SessionPersistenceConfigurationDetails'
        }

        self.attribute_map = {
            'policy': 'policy',
            'backends': 'backends',
            'health_checker': 'healthChecker',
            'ssl_configuration': 'sslConfiguration',
            'session_persistence_configuration': 'sessionPersistenceConfiguration'
        }

        self._policy = None
        self._backends = None
        self._health_checker = None
        self._ssl_configuration = None
        self._session_persistence_configuration = None

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this UpdateBackendSetDetails.
        The load balancer policy for the backend set. To get a list of available policies, use the
        :func:`list_policies` operation.

        Example: `LEAST_CONNECTIONS`


        :return: The policy of this UpdateBackendSetDetails.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this UpdateBackendSetDetails.
        The load balancer policy for the backend set. To get a list of available policies, use the
        :func:`list_policies` operation.

        Example: `LEAST_CONNECTIONS`


        :param policy: The policy of this UpdateBackendSetDetails.
        :type: str
        """
        self._policy = policy

    @property
    def backends(self):
        """
        **[Required]** Gets the backends of this UpdateBackendSetDetails.

        :return: The backends of this UpdateBackendSetDetails.
        :rtype: list[BackendDetails]
        """
        return self._backends

    @backends.setter
    def backends(self, backends):
        """
        Sets the backends of this UpdateBackendSetDetails.

        :param backends: The backends of this UpdateBackendSetDetails.
        :type: list[BackendDetails]
        """
        self._backends = backends

    @property
    def health_checker(self):
        """
        **[Required]** Gets the health_checker of this UpdateBackendSetDetails.

        :return: The health_checker of this UpdateBackendSetDetails.
        :rtype: HealthCheckerDetails
        """
        return self._health_checker

    @health_checker.setter
    def health_checker(self, health_checker):
        """
        Sets the health_checker of this UpdateBackendSetDetails.

        :param health_checker: The health_checker of this UpdateBackendSetDetails.
        :type: HealthCheckerDetails
        """
        self._health_checker = health_checker

    @property
    def ssl_configuration(self):
        """
        Gets the ssl_configuration of this UpdateBackendSetDetails.

        :return: The ssl_configuration of this UpdateBackendSetDetails.
        :rtype: SSLConfigurationDetails
        """
        return self._ssl_configuration

    @ssl_configuration.setter
    def ssl_configuration(self, ssl_configuration):
        """
        Sets the ssl_configuration of this UpdateBackendSetDetails.

        :param ssl_configuration: The ssl_configuration of this UpdateBackendSetDetails.
        :type: SSLConfigurationDetails
        """
        self._ssl_configuration = ssl_configuration

    @property
    def session_persistence_configuration(self):
        """
        Gets the session_persistence_configuration of this UpdateBackendSetDetails.

        :return: The session_persistence_configuration of this UpdateBackendSetDetails.
        :rtype: SessionPersistenceConfigurationDetails
        """
        return self._session_persistence_configuration

    @session_persistence_configuration.setter
    def session_persistence_configuration(self, session_persistence_configuration):
        """
        Sets the session_persistence_configuration of this UpdateBackendSetDetails.

        :param session_persistence_configuration: The session_persistence_configuration of this UpdateBackendSetDetails.
        :type: SessionPersistenceConfigurationDetails
        """
        self._session_persistence_configuration = session_persistence_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
