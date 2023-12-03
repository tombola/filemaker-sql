from pydantic import Field

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from rich import print


class DatabaseSettings(BaseModel):
    host: str = Field("localhost")
    name: str = Field("")
    user: str = Field("")
    pwd: str = Field("")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="fmsql_",
        env_nested_delimiter="__",
    )
    database: DatabaseSettings
