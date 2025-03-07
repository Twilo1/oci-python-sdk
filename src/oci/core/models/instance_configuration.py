# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfiguration(object):
    """
    An instance configuration is a template that defines the settings to use when creating Compute instances
    as part of an instance pool. For more information about instance pools and instance configurations, see
    `Managing Compute Instances`__.

    __ https://docs.cloud.oracle.com/Content/Compute/Concepts/instancemanagement.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceConfiguration.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this InstanceConfiguration.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this InstanceConfiguration.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InstanceConfiguration.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this InstanceConfiguration.
        :type id: str

        :param instance_details:
            The value to assign to the instance_details property of this InstanceConfiguration.
        :type instance_details: InstanceConfigurationInstanceDetails

        :param deferred_fields:
            The value to assign to the deferred_fields property of this InstanceConfiguration.
        :type deferred_fields: list[str]

        :param time_created:
            The value to assign to the time_created property of this InstanceConfiguration.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'instance_details': 'InstanceConfigurationInstanceDetails',
            'deferred_fields': 'list[str]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'instance_details': 'instanceDetails',
            'deferred_fields': 'deferredFields',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._instance_details = None
        self._deferred_fields = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InstanceConfiguration.
        The OCID of the compartment containing the instance configuration.


        :return: The compartment_id of this InstanceConfiguration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstanceConfiguration.
        The OCID of the compartment containing the instance configuration.


        :param compartment_id: The compartment_id of this InstanceConfiguration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InstanceConfiguration.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstanceConfiguration.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstanceConfiguration.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this InstanceConfiguration.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfiguration.
        A user-friendly name for the instance configuration


        :return: The display_name of this InstanceConfiguration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfiguration.
        A user-friendly name for the instance configuration


        :param display_name: The display_name of this InstanceConfiguration.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstanceConfiguration.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstanceConfiguration.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstanceConfiguration.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this InstanceConfiguration.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstanceConfiguration.
        The OCID of the instance configuration


        :return: The id of this InstanceConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceConfiguration.
        The OCID of the instance configuration


        :param id: The id of this InstanceConfiguration.
        :type: str
        """
        self._id = id

    @property
    def instance_details(self):
        """
        Gets the instance_details of this InstanceConfiguration.

        :return: The instance_details of this InstanceConfiguration.
        :rtype: InstanceConfigurationInstanceDetails
        """
        return self._instance_details

    @instance_details.setter
    def instance_details(self, instance_details):
        """
        Sets the instance_details of this InstanceConfiguration.

        :param instance_details: The instance_details of this InstanceConfiguration.
        :type: InstanceConfigurationInstanceDetails
        """
        self._instance_details = instance_details

    @property
    def deferred_fields(self):
        """
        Gets the deferred_fields of this InstanceConfiguration.
        The required details when using the :func:`launch_instance_configuration` operation.
        These attributes are optional when using the :func:`create_instance_configuration` operation.


        :return: The deferred_fields of this InstanceConfiguration.
        :rtype: list[str]
        """
        return self._deferred_fields

    @deferred_fields.setter
    def deferred_fields(self, deferred_fields):
        """
        Sets the deferred_fields of this InstanceConfiguration.
        The required details when using the :func:`launch_instance_configuration` operation.
        These attributes are optional when using the :func:`create_instance_configuration` operation.


        :param deferred_fields: The deferred_fields of this InstanceConfiguration.
        :type: list[str]
        """
        self._deferred_fields = deferred_fields

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InstanceConfiguration.
        The date and time the instance configuration was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this InstanceConfiguration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstanceConfiguration.
        The date and time the instance configuration was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this InstanceConfiguration.
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
