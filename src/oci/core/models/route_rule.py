# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RouteRule(object):
    """
    A mapping between a destination IP address range and a virtual device to route matching
    packets to (a target).
    """

    #: A constant which can be used with the destination_type property of a RouteRule.
    #: This constant has a value of "CIDR_BLOCK"
    DESTINATION_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the destination_type property of a RouteRule.
    #: This constant has a value of "SERVICE_CIDR_BLOCK"
    DESTINATION_TYPE_SERVICE_CIDR_BLOCK = "SERVICE_CIDR_BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new RouteRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this RouteRule.
        :type cidr_block: str

        :param destination:
            The value to assign to the destination property of this RouteRule.
        :type destination: str

        :param destination_type:
            The value to assign to the destination_type property of this RouteRule.
            Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type destination_type: str

        :param network_entity_id:
            The value to assign to the network_entity_id property of this RouteRule.
        :type network_entity_id: str

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'destination': 'str',
            'destination_type': 'str',
            'network_entity_id': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'destination': 'destination',
            'destination_type': 'destinationType',
            'network_entity_id': 'networkEntityId'
        }

        self._cidr_block = None
        self._destination = None
        self._destination_type = None
        self._network_entity_id = None

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this RouteRule.
        Deprecated. Instead use `destination` and `destinationType`. Requests that include both
        `cidrBlock` and `destination` will be rejected.

        A destination IP address range in CIDR notation. Matching packets will
        be routed to the indicated network entity (the target).


        Example: `0.0.0.0/0`


        :return: The cidr_block of this RouteRule.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this RouteRule.
        Deprecated. Instead use `destination` and `destinationType`. Requests that include both
        `cidrBlock` and `destination` will be rejected.

        A destination IP address range in CIDR notation. Matching packets will
        be routed to the indicated network entity (the target).


        Example: `0.0.0.0/0`


        :param cidr_block: The cidr_block of this RouteRule.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def destination(self):
        """
        Gets the destination of this RouteRule.
        Conceptually, this is the range of IP addresses used for matching when routing
        traffic. Required if you provide a `destinationType`.

        Allowed values:

          * IP address range in CIDR notation. For example: `192.168.1.0/24`

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a route rule for traffic destined for a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.


        :return: The destination of this RouteRule.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this RouteRule.
        Conceptually, this is the range of IP addresses used for matching when routing
        traffic. Required if you provide a `destinationType`.

        Allowed values:

          * IP address range in CIDR notation. For example: `192.168.1.0/24`

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a route rule for traffic destined for a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.


        :param destination: The destination of this RouteRule.
        :type: str
        """
        self._destination = destination

    @property
    def destination_type(self):
        """
        Gets the destination_type of this RouteRule.
        Type of destination for the rule. Required if you provide a `destination`.

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).

        Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The destination_type of this RouteRule.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this RouteRule.
        Type of destination for the rule. Required if you provide a `destination`.

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).


        :param destination_type: The destination_type of this RouteRule.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "SERVICE_CIDR_BLOCK"]
        if not value_allowed_none_or_none_sentinel(destination_type, allowed_values):
            destination_type = 'UNKNOWN_ENUM_VALUE'
        self._destination_type = destination_type

    @property
    def network_entity_id(self):
        """
        **[Required]** Gets the network_entity_id of this RouteRule.
        The OCID for the route rule's target. For information about the type of
        targets you can specify, see
        `Route Tables`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm


        :return: The network_entity_id of this RouteRule.
        :rtype: str
        """
        return self._network_entity_id

    @network_entity_id.setter
    def network_entity_id(self, network_entity_id):
        """
        Sets the network_entity_id of this RouteRule.
        The OCID for the route rule's target. For information about the type of
        targets you can specify, see
        `Route Tables`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm


        :param network_entity_id: The network_entity_id of this RouteRule.
        :type: str
        """
        self._network_entity_id = network_entity_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
