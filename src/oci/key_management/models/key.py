# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Key(object):
    """
    Key model.
    """

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "ENABLING"
    LIFECYCLE_STATE_ENABLING = "ENABLING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "ENABLED"
    LIFECYCLE_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "DISABLING"
    LIFECYCLE_STATE_DISABLING = "DISABLING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "DISABLED"
    LIFECYCLE_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    def __init__(self, **kwargs):
        """
        Initializes a new Key object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Key.
        :type compartment_id: str

        :param current_key_version:
            The value to assign to the current_key_version property of this Key.
        :type current_key_version: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Key.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Key.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Key.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Key.
        :type id: str

        :param key_shape:
            The value to assign to the key_shape property of this Key.
        :type key_shape: KeyShape

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Key.
            Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Key.
        :type time_created: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this Key.
        :type time_of_deletion: datetime

        :param vault_id:
            The value to assign to the vault_id property of this Key.
        :type vault_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'current_key_version': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'key_shape': 'KeyShape',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_of_deletion': 'datetime',
            'vault_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'current_key_version': 'currentKeyVersion',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'key_shape': 'keyShape',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_of_deletion': 'timeOfDeletion',
            'vault_id': 'vaultId'
        }

        self._compartment_id = None
        self._current_key_version = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._key_shape = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_of_deletion = None
        self._vault_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Key.
        The OCID of the compartment that contains this key.


        :return: The compartment_id of this Key.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Key.
        The OCID of the compartment that contains this key.


        :param compartment_id: The compartment_id of this Key.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def current_key_version(self):
        """
        **[Required]** Gets the current_key_version of this Key.
        The OCID of the KeyVersion resource used in cryptographic operations. During key rotation, service might be in a transitional state
        where this or a newer KeyVersion are used intermittently. The currentKeyVersion field is updated when the service is guaranteed to
        use the new KeyVersion for all subsequent encryption operations.


        :return: The current_key_version of this Key.
        :rtype: str
        """
        return self._current_key_version

    @current_key_version.setter
    def current_key_version(self, current_key_version):
        """
        Sets the current_key_version of this Key.
        The OCID of the KeyVersion resource used in cryptographic operations. During key rotation, service might be in a transitional state
        where this or a newer KeyVersion are used intermittently. The currentKeyVersion field is updated when the service is guaranteed to
        use the new KeyVersion for all subsequent encryption operations.


        :param current_key_version: The current_key_version of this Key.
        :type: str
        """
        self._current_key_version = current_key_version

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Key.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :return: The defined_tags of this Key.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Key.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :param defined_tags: The defined_tags of this Key.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Key.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this Key.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Key.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Key.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Key.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Key.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Key.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Key.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Key.
        The OCID of the key.


        :return: The id of this Key.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Key.
        The OCID of the key.


        :param id: The id of this Key.
        :type: str
        """
        self._id = id

    @property
    def key_shape(self):
        """
        **[Required]** Gets the key_shape of this Key.

        :return: The key_shape of this Key.
        :rtype: KeyShape
        """
        return self._key_shape

    @key_shape.setter
    def key_shape(self, key_shape):
        """
        Sets the key_shape of this Key.

        :param key_shape: The key_shape of this Key.
        :type: KeyShape
        """
        self._key_shape = key_shape

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Key.
        The key's current state.

        Example: `ENABLED`

        Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Key.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Key.
        The key's current state.

        Example: `ENABLED`


        :param lifecycle_state: The lifecycle_state of this Key.
        :type: str
        """
        allowed_values = ["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Key.
        The date and time the key was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Key.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Key.
        The date and time the key was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Key.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this Key.
        An optional property for the deletion time of the key, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this Key.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this Key.
        An optional property for the deletion time of the key, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this Key.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this Key.
        The OCID of the vault that contains this key.


        :return: The vault_id of this Key.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this Key.
        The OCID of the vault that contains this key.


        :param vault_id: The vault_id of this Key.
        :type: str
        """
        self._vault_id = vault_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
