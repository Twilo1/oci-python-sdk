# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CrossConnectGroup(object):
    """
    For use with Oracle Cloud Infrastructure FastConnect. A cross-connect group
    is a link aggregation group (LAG), which can contain one or more
    :class:`CrossConnect`. Customers who are colocated with
    Oracle in a FastConnect location create and use cross-connect groups. For more
    information, see `FastConnect Overview`__.

    **Note:** If you're a provider who is setting up a physical connection to Oracle so customers
    can use FastConnect over the connection, be aware that your connection is modeled the
    same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on).

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "PROVISIONED"
    LIFECYCLE_STATE_PROVISIONED = "PROVISIONED"

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new CrossConnectGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CrossConnectGroup.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CrossConnectGroup.
        :type display_name: str

        :param id:
            The value to assign to the id property of this CrossConnectGroup.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CrossConnectGroup.
            Allowed values for this property are: "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param customer_reference_name:
            The value to assign to the customer_reference_name property of this CrossConnectGroup.
        :type customer_reference_name: str

        :param time_created:
            The value to assign to the time_created property of this CrossConnectGroup.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'customer_reference_name': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'customer_reference_name': 'customerReferenceName',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._customer_reference_name = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CrossConnectGroup.
        The OCID of the compartment containing the cross-connect group.


        :return: The compartment_id of this CrossConnectGroup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CrossConnectGroup.
        The OCID of the compartment containing the cross-connect group.


        :param compartment_id: The compartment_id of this CrossConnectGroup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CrossConnectGroup.
        The display name of a user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CrossConnectGroup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CrossConnectGroup.
        The display name of a user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CrossConnectGroup.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this CrossConnectGroup.
        The cross-connect group's Oracle ID (OCID).


        :return: The id of this CrossConnectGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CrossConnectGroup.
        The cross-connect group's Oracle ID (OCID).


        :param id: The id of this CrossConnectGroup.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CrossConnectGroup.
        The cross-connect group's current state.

        Allowed values for this property are: "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CrossConnectGroup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CrossConnectGroup.
        The cross-connect group's current state.


        :param lifecycle_state: The lifecycle_state of this CrossConnectGroup.
        :type: str
        """
        allowed_values = ["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def customer_reference_name(self):
        """
        Gets the customer_reference_name of this CrossConnectGroup.
        A reference name or identifier for the physical fiber connection that this cross-connect
        group uses.


        :return: The customer_reference_name of this CrossConnectGroup.
        :rtype: str
        """
        return self._customer_reference_name

    @customer_reference_name.setter
    def customer_reference_name(self, customer_reference_name):
        """
        Sets the customer_reference_name of this CrossConnectGroup.
        A reference name or identifier for the physical fiber connection that this cross-connect
        group uses.


        :param customer_reference_name: The customer_reference_name of this CrossConnectGroup.
        :type: str
        """
        self._customer_reference_name = customer_reference_name

    @property
    def time_created(self):
        """
        Gets the time_created of this CrossConnectGroup.
        The date and time the cross-connect group was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this CrossConnectGroup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CrossConnectGroup.
        The date and time the cross-connect group was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this CrossConnectGroup.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
