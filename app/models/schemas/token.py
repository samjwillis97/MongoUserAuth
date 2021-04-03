from typing import Optional

from .base import Base

class TokenData(Base):
    username: Optional[str] = None

class Token(Base):
    access_token: str
    token_type: str