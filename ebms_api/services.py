from typing import Generic, Type, Optional

from fastapi import Depends
from sqlalchemy import select, ScalarResult
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from common.constants import OriginModelType, InputSchemaType
from database import get_async_session


class BaseService(Generic[OriginModelType, InputSchemaType]):
    def __init__(self, model: Type[OriginModelType], db_session: AsyncSession = Depends(get_async_session)):
        self.model = model
        self.db_session = db_session

    async def get(self, autoid: int) -> Optional[OriginModelType]:
        stmt = select(self.model).where(self.model.autoid == autoid)
        result = await self.db_session.scalars(stmt)
        try:
            return result.one()
        except NoResultFound:
            return None

    async def list(self):
        stmt = select(self.model)
        objs: ScalarResult[OriginModelType] = await self.db_session.scalars(stmt)
        return objs.all()

    async def create(self, obj: InputSchemaType) -> OriginModelType:
        """ Not allowed to create """
        raise NotImplementedError

    async def update(self, autoid: int, obj: InputSchemaType) -> Optional[OriginModelType]:
        """ Not allowed to update """
        raise NotImplementedError

    async def partial_update(self, autoid: int, obj: InputSchemaType) -> Optional[OriginModelType]:
        """ Not allowed to update """
        raise NotImplementedError

    async def delete(self, autoid: int) -> Optional[OriginModelType]:
        """ Not allowed to delete """
        raise NotImplementedError


class TaskService(BaseService[OriginModelType, InputSchemaType]):
    def __init__(self, db_session: AsyncSession = Depends(get_async_session)):
        super().__init__(model=OriginModelType, db_session=db_session)