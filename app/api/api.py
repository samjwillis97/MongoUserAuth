from fastapi import APIRouter

from .routes import token
from .routes import users

router = APIRouter()
router.include_router(token, tags=["authentication"], prefix="/token")
# router.include_router(users, tags=["users"], prefix="/user")