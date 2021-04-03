from typing import Optional

from pydantic import EmailStr

from .base import Base
from .db import DBModelMixin
# from ...services.users import get_user
from ...core.mongodb import AsyncIOMotorClient
from ...core.security import get_password_hash, verify_password
# from app.core.security


class UserBase(Base):
    username: str
    email: Optional[EmailStr]
    full_name: Optional[str]


class UserInDB(DBModelMixin, UserBase):
    hashed_password: str

    def check_password(self, password: str):
        return verify_password(password, self.hashed_password)


class User(UserBase):
    token: str


class UserLogin(Base):
    username: str
    password: str


class UserUpdate(Base):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    full_name: Optional[str]
