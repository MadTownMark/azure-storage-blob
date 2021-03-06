# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Application
    from ._models_py3 import ApplicationArtifact
    from ._models_py3 import ApplicationDefinition
    from ._models_py3 import ApplicationDefinitionListResult
    from ._models_py3 import ApplicationListResult
    from ._models_py3 import ApplicationPatchable
    from ._models_py3 import ApplicationProviderAuthorization
    from ._models_py3 import ErrorResponse
    from ._models_py3 import GenericResource
    from ._models_py3 import Identity
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import Plan
    from ._models_py3 import PlanPatchable
    from ._models_py3 import Resource
    from ._models_py3 import Sku
except (SyntaxError, ImportError):
    from ._models import Application  # type: ignore
    from ._models import ApplicationArtifact  # type: ignore
    from ._models import ApplicationDefinition  # type: ignore
    from ._models import ApplicationDefinitionListResult  # type: ignore
    from ._models import ApplicationListResult  # type: ignore
    from ._models import ApplicationPatchable  # type: ignore
    from ._models import ApplicationProviderAuthorization  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import GenericResource  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import Plan  # type: ignore
    from ._models import PlanPatchable  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Sku  # type: ignore

from ._application_client_enums import (
    ApplicationArtifactType,
    ApplicationLockLevel,
    ProvisioningState,
)

__all__ = [
    'Application',
    'ApplicationArtifact',
    'ApplicationDefinition',
    'ApplicationDefinitionListResult',
    'ApplicationListResult',
    'ApplicationPatchable',
    'ApplicationProviderAuthorization',
    'ErrorResponse',
    'GenericResource',
    'Identity',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'Plan',
    'PlanPatchable',
    'Resource',
    'Sku',
    'ApplicationArtifactType',
    'ApplicationLockLevel',
    'ProvisioningState',
]
