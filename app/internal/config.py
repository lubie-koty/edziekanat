from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "eDziekanat"
    database_uri: PostgresDsn | None = None
    jwt_secret_key: str = "secret"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="E_DZIEKANAT_", extra="ignore"
    )


settings = Settings()
