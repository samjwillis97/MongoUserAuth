from typing import Optional, List
from datetime import datetime
from pydantic import EmailStr, Field
from bson.objectid import ObjectId

from .base import Base
from .db import DateTimeModelMixin, MongoModel, OID
from ...core.security import get_password_hash, verify_password


class UserBase(MongoModel):
    id: OID = Field()
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    permissions: List[str] = []


class UserInDB(DateTimeModelMixin, UserBase):
    hashed_password: str = ""

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
    email: Optional[EmailStr]
    password: Optional[str]

class UserSuperUpdate(Base):
    email: Optional[EmailStr]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    permissions: Optional[List[str]]
    password: Optional[str]


class UserInResponse(UserBase):
    pass
