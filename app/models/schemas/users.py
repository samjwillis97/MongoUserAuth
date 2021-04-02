from typing import Optional

from pydantic import EmailStr

from base import Base
from db import DBModelMixin
from ...core.security import get_password_hash, verify_password
# from app.core.security


class UserBase(Base):
    username: str
    email: Optional[EmailStr]
    full_name: Optional[str]


class UserInDB(DBModelMixin, UserBase):
    hashed_password: str


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
