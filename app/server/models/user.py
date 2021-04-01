from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
  username: str,
  full_name: Optional[str],
  email: Optional[EmailStr]

class UserCreate(User):
  password: str