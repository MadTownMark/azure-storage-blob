# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import DnsManagementClientConfiguration
from .operations import RecordSetsOperations
from .operations import ZonesOperations
from .operations import DnsResourceReferenceOperations
from .. import models


class DnsManagementClient(object):
    """The DNS Management Client.

    :ivar record_sets: RecordSetsOperations operations
    :vartype record_sets: azure.mgmt.dns.v2018_05_01.aio.operations.RecordSetsOperations
    :ivar zones: ZonesOperations operations
    :vartype zones: azure.mgmt.dns.v2018_05_01.aio.operations.ZonesOperations
    :ivar dns_resource_reference: DnsResourceReferenceOperations operations
    :vartype dns_resource_reference: azure.mgmt.dns.v2018_05_01.aio.operations.DnsResourceReferenceOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Specifies the Azure subscription ID, which uniquely identifies the Microsoft Azure subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DnsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.record_sets = RecordSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.zones = ZonesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dns_resource_reference = DnsResourceReferenceOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DnsManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
