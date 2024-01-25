from typing import TypeVar

from pydantic import BaseModel

from common.models import DefaultBase, EBMSBase

ModelType = TypeVar("ModelType", bound=DefaultBase)
OriginModelType = TypeVar("OriginModelType", bound=EBMSBase)
InputSchemaType = TypeVar("InputSchemaType", bound=BaseModel)