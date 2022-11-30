# generated by datamodel-codegen:
#   filename:  confluent-cloud-api.spec.json
#   timestamp: 2022-11-30T11:44:44+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra

from . import ApiVersion, Id, Kind, ResourceMetadata


class Spec(BaseModel):
    class Config:
        extra = Extra.forbid

    api_version: Optional[ApiVersion] = None
    id: Optional[Id] = None
    kind: Optional[Kind] = None
    metadata: Optional[ResourceMetadata] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
