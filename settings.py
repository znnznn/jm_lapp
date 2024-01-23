from decouple import config
from pydantic import Field
from pydantic_settings import BaseSettings

SECRET_KEY = config("SECRET_KEY", cast=str)

ALGORITHM = "SHA256"
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)


class EBMSDatabase(BaseSettings):
    env_file: str = ".env"
    DB_USER: str = Field(alias="EBMS_DB_USER", default="postgres")
    DB_PASS: str = Field(alias="MSSQL_SA_PASSWORD", default="postgres")
    DB_HOST: str = Field(alias="EBMS_DB_HOST", default="localhost")
    DB_PORT: int = Field(alias="EBMS_DB_PORT", default=1433)
    DB_NAME: str = Field(alias="EBMS_DB_NAME", default="mssql")


class DataBase(BaseSettings):
    env_file: str = ".env"
    DB_USER: str = Field(alias="DB_USER", default="postgres")
    DB_PASS: str = Field(alias="DB_PASS", default="postgres")
    DB_HOST: str = Field(alias="DB_HOST", default="db")
    DB_PORT: int = Field(alias="DB_PORT", default=5432)
    DB_NAME: str = Field(alias="DB_NAME", default="jmlappdb_dev")


EBMS_DB = EBMSDatabase()
Default_DB = DataBase()
