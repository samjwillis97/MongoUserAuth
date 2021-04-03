from ...models.schemas.users import UserInResponse, User
from ...core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ...core.mongodb import AsyncIOMotorClient, get_database
from ...core.jwt import get_current_user
from ...services.users import get_user

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm

from pprint import pprint

# retrieve current user
# update current user

router = APIRouter()

@router.get("/me", response_model=UserInResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user