from typing import Optional

from pydantic import EmailStr

from base import Base
from db import DBModelMixin
# from app.core.security

class UserBase(Base):
  username: str
  email: Optional[EmailStr]
  full_name: Optional[str]

class UserInDB(DBModelMixin, UserBase):
  hashed_password: str