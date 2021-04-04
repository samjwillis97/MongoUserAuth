from typing import Optional, List
from datetime import datetime
from pydantic import EmailStr

from .base import Base
from .db import DateTimeModelMixin
# from ...services.users import get_user
from ...core.mongodb import AsyncIOMotorClient
from ...core.security import get_password_hash, verify_password
# from app.core.security


class UserBase(Base):
    email: EmailStr
    full_name: Optional[str]


class UserInDB(DateTimeModelMixin, UserBase):
    hashed_password: str = ""
    permissions: List[str] = []

    def check_password(self, password: str):
        return verify_password(password, self.hashed_password)

    def update_password(self, password: str):
        self.hashed_password = get_password_hash(password)

    def update_time(self):
        self.updated_at = datetime.now()


class User(UserBase):
    token: str


class UserLogin(Base):
    email: EmailStr
    password: str


class UserRegister(UserLogin):
    pass


class UserUpdate(Base):
    email: Optional[str]
    password: Optional[str]
    full_name: Optional[str]


class UserInResponse(Base):
    email: str
    full_name: Optional[str]
