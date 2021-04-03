import os

from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

API_PREFIX = "/api"
VERSION = "1.0.0"

JWT_TOKEN_PREFIX = "Token"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

config = Config("app/.env")

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


SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

PROJECT_NAME: str = config("PROJECT_NAME", default="Fast API Project")

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

database_name = MONGO_DB
user_collection_name = "users"

# Could Add Logging (See FASTAPI RWE)
