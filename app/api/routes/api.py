from fastapi import APIRouter

from . import authentication
from . import users

router = APIRouter()
# router.include_router(authentication, tags=["authentication"], prefix="/users")
# router.include_router(users, tags=["users"], prefix="/user")