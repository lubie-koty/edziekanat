from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "eDziekanat"
    database_uri: PostgresDsn | None = None

    model_config = SettingsConfigDict(env_file=".env", env_prefix="E_DZIEKANAT_")


settings = Settings()
