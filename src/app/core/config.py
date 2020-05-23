import secrets
from typing import Any, Dict, Optional

from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, PostgresDsn, validator

#PROJECT_NAME = "Vehicles API"
#SECRET_KEY = "080f942c8fd0e4494a2cf3d60d78806e409b210214ebe522c4f61df05cefcbb9"
#ACCESS_TOKEN_EXPIRE_MINUTES = 10


class Settings(BaseSettings):
    ALGORITHM = "HS256"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10
    

    PROJECT_NAME: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
