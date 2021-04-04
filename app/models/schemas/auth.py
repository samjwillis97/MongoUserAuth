from typing import Optional, List

from .base import Base

class TokenData(Base):
    email: Optional[str] = None
    scopes: List[str] = []

class Token(Base):
    access_token: str
    token_type: str