# from typing import Optional, List
# from datetime import datetime
# from pydantic import EmailStr

from fastapi_users import models
from pydantic import validator

# from .base import Base
# from .db import DateTimeModelMixin
# from ...services.users import get_user
# from ...core.mongodb import AsyncIOMotorClient
# from ...core.security import get_password_hash, verify_password
# from app.core.security


class User(models.BaseUser):
    # id - Unique Identifier UUID4
    # email - Validated by email-validator
    # is_active 
    # is_verified - useful for email verification
    # is_superuses - useful for admin 
    pass


class UserCreate(models.BaseUserCreate):
    # Required email and password
    @validator('password')
    def valid_password(self, v: str):
        if len(v) < 6:
            raise ValueError('Password should be atleast 6 characters')
        return v


class UserUpdate(User, models.BaseUserUpdate):
    # optional password field
    pass


class UserDB(User, models.BaseUserDB):
    # adds hashed_password
    pass


# class UserBase(Base):
#     email: EmailStr
#     full_name: Optional[str]


# class UserInDB(DateTimeModelMixin, UserBase):
#     hashed_password: str = ""
#     permissions: List[str] = []

#     def check_password(self, password: str):
#         return verify_password(password, self.hashed_password)

#     def update_password(self, password: str):
#         self.hashed_password = get_password_hash(password)

#     def update_time(self):
#         self.updated_at = datetime.now()


# class User(UserBase):
#     token: str


# class UserLogin(Base):
#     email: EmailStr
#     password: str


# class UserRegister(UserLogin):
#     pass


# class UserUpdate(Base):
#     email: Optional[str]
#     password: Optional[str]
#     full_name: Optional[str]


# class UserInResponse(Base):
#     email: str
#     full_name: Optional[str]
