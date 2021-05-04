import os

from typing import List

# from functools import lru_cache
# from pydantic import BaseSettings

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

# class Settings (BaseSettings):
#     class Config:
#         env_file = ".env"

# @lru_cache
# def get_settings():
#     return Settings()

API_PREFIX = "/api"
VERSION = "1.0.0"

JWT_TOKEN_PREFIX = "Token"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

config = Config(".env")

MAX_CONNECTIONS_COUNT: int = config(
    "MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config(
    "MIN_CONNECTIONS_COUNT", cast=int, default=10)

DEBUG: bool = config("DEBUG", cast=bool, default=False)

# deploying without docker-compose
MONGODB_URL: str = config("MONGODB_URL", default=None)
if not MONGODB_URL:
    MONGO_HOST: str = config("MONGO_HOST", default="localhost")
    MONGO_PORT: int = config("MONGO_PORT", cast=int, default=27017)
    MONGO_USER: str = config("MONGO_USER", default="admin")
    MONGO_PASS: str = config("MONGO_PASSWORD", default="markqiu")
    MONGO_DB: str = config("MONGO_DB", default="fastapi")

    MONGODB_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"


SECRET_KEY: Secret = config("SECRET_KEY", cast=str)

PROJECT_NAME: str = config("PROJECT_NAME", default="Fast API Project")

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

USER_DATABASE_NAME: str = config("USER_DATABASE_NAME", default="fastapi")
USER_COLLECTION_NAME: str = config("USER_COLLECTION_NAME", default="users")

NEMWEB_DATABASE_NAME: str = config("NEMWEB_DATABASE_NAME", default="testing")
NEMWEB_COLLECTION_NAME: str = config("NEMWEB_COLLECTION_NAME", default="nemweb")

BEARING_DATABASE_NAME: str = config("BEARING_DATABASE_NAME", default="fastapi")
BEARING_COLLECTION_NAME: str = config("BEARING_COLLECTION_NAME", default="bearings")

# Could Add Logging (See FASTAPI RWE)
