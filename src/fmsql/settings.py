from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict
from rich import print


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="fmsql_")

    database_host: str = Field("localhost", alias="host")
    fmsql_database_name: str = Field("")
    database_user: str = Field("")
    database_pwd: str = Field("")
