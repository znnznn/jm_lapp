from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from common.models import EBMSBase, DefaultBase
from settings import EBMS_DB, Default_DB


engines = {
    EBMSBase: create_async_engine('mssql+aioodbc://{}:{}@{}:{}/{}?driver=ODBC+Driver+17+for+SQL+Server'.format(
        EBMS_DB.DB_USER, EBMS_DB.DB_PASS, EBMS_DB.DB_HOST, EBMS_DB.DB_PORT, EBMS_DB.DB_NAME), echo=True),
    DefaultBase: create_async_engine('postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
        Default_DB.DB_USER, Default_DB.DB_PASS, Default_DB.DB_HOST, Default_DB.DB_PORT, Default_DB.DB_NAME), echo=True),
}

async_session_maker = async_sessionmaker(binds=engines, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
