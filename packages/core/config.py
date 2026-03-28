from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str = Field(default="dev", alias="APP_ENV")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8080, alias="API_PORT")

    database_url: str = Field(default="postgresql+psycopg://postgres:postgres@localhost:5432/pmp", alias="DATABASE_URL")
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")

    scan_universe_limit: int = Field(default=800, alias="SCAN_UNIVERSE_LIMIT")
    min_dollar_volume: float = Field(default=1_000_000, alias="MIN_DOLLAR_VOLUME")
    min_price: float = Field(default=1.0, alias="MIN_PRICE")

    pump_multiplier: float = Field(default=2.0, alias="PUMP_MULTIPLIER")
    pump_lookahead_min_days: int = Field(default=5, alias="PUMP_LOOKAHEAD_MIN_DAYS")
    pump_lookahead_max_days: int = Field(default=30, alias="PUMP_LOOKAHEAD_MAX_DAYS")


settings = Settings()
