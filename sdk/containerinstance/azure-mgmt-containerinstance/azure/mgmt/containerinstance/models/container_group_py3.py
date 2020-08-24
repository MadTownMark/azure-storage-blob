# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class ContainerGroup(Resource):
    """A container group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource id.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param identity: The identity of the container group, if configured.
    :type identity:
     ~azure.mgmt.containerinstance.models.ContainerGroupIdentity
    :ivar provisioning_state: The provisioning state of the container group.
     This only appears in the response.
    :vartype provisioning_state: str
    :param containers: Required. The containers within the container group.
    :type containers: list[~azure.mgmt.containerinstance.models.Container]
    :param image_registry_credentials: The image registry credentials by which
     the container group is created from.
    :type image_registry_credentials:
     list[~azure.mgmt.containerinstance.models.ImageRegistryCredential]
    :param restart_policy: Restart policy for all containers within the
     container group.
     - `Always` Always restart
     - `OnFailure` Restart on failure
     - `Never` Never restart
     . Possible values include: 'Always', 'OnFailure', 'Never'
    :type restart_policy: str or
     ~azure.mgmt.containerinstance.models.ContainerGroupRestartPolicy
    :param ip_address: The IP address type of the container group.
    :type ip_address: ~azure.mgmt.containerinstance.models.IpAddress
    :param os_type: Required. The operating system type required by the
     containers in the container group. Possible values include: 'Windows',
     'Linux'
    :type os_type: str or
     ~azure.mgmt.containerinstance.models.OperatingSystemTypes
    :param volumes: The list of volumes that can be mounted by containers in
     this container group.
    :type volumes: list[~azure.mgmt.containerinstance.models.Volume]
    :ivar instance_view: The instance view of the container group. Only valid
     in response.
    :vartype instance_view:
     ~azure.mgmt.containerinstance.models.ContainerGroupPropertiesInstanceView
    :param diagnostics: The diagnostic information for a container group.
    :type diagnostics:
     ~azure.mgmt.containerinstance.models.ContainerGroupDiagnostics
    :param network_profile: The network profile information for a container
     group.
    :type network_profile:
     ~azure.mgmt.containerinstance.models.ContainerGroupNetworkProfile
    :param dns_config: The DNS config information for a container group.
    :type dns_config: ~azure.mgmt.containerinstance.models.DnsConfiguration
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'containers': {'required': True},
        'os_type': {'required': True},
        'instance_view': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'ContainerGroupIdentity'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'containers': {'key': 'properties.containers', 'type': '[Container]'},
        'image_registry_credentials': {'key': 'properties.imageRegistryCredentials', 'type': '[ImageRegistryCredential]'},
        'restart_policy': {'key': 'properties.restartPolicy', 'type': 'str'},
        'ip_address': {'key': 'properties.ipAddress', 'type': 'IpAddress'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'volumes': {'key': 'properties.volumes', 'type': '[Volume]'},
        'instance_view': {'key': 'properties.instanceView', 'type': 'ContainerGroupPropertiesInstanceView'},
        'diagnostics': {'key': 'properties.diagnostics', 'type': 'ContainerGroupDiagnostics'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'ContainerGroupNetworkProfile'},
        'dns_config': {'key': 'properties.dnsConfig', 'type': 'DnsConfiguration'},
    }

    def __init__(self, *, containers, os_type, location: str=None, tags=None, identity=None, image_registry_credentials=None, restart_policy=None, ip_address=None, volumes=None, diagnostics=None, network_profile=None, dns_config=None, **kwargs) -> None:
        super(ContainerGroup, self).__init__(location=location, tags=tags, **kwargs)
        self.identity = identity
        self.provisioning_state = None
        self.containers = containers
        self.image_registry_credentials = image_registry_credentials
        self.restart_policy = restart_policy
        self.ip_address = ip_address
        self.os_type = os_type
        self.volumes = volumes
        self.instance_view = None
        self.diagnostics = diagnostics
        self.network_profile = network_profile
        self.dns_config = dns_config