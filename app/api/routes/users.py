from ...models.schemas.users import UserInResponse, User, UserUpdate, UserSuperUpdate
from ...core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ...core.mongodb import AsyncIOMotorClient, get_database
from ...core.jwt import get_current_user
from ...services.users import get_user, update_user, get_all_users
from ...services.auth import PermissionChecker

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import List

from pprint import pprint


# USERS ROUTER
# GET - /me
# Response: id? + email + is_active + is_superuser
# PATCH - /me (if email change, logout, re login)
# Request: Email + Pass
# Response: id? + email + is_active + is_superuse
# GET - /{user_id}
# Response: id? + email + is_active + is_superuser, 401, 403, 404
# PATCH - /{user_id}
# Request: email + password + is_active + is_superuse
# Response: id? + email + is_active + is_superuser, 401, 403, 404
# DELET - /{user_id}
# Response: id? + email + is_active + is_superuser, 401, 403, 404

router = APIRouter()

permChecker = PermissionChecker(["super"])

# Get users/ for super


@router.get(
    "/",
    # response_model=List[UserInResponse]
)
def read_all_users(current_user: User = Depends(permChecker)):
    users = get_all_users
    return users


@router.get("/me", response_model=UserInResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch(
    "/me",
    response_model=UserInResponse
)
async def update_current_user(
        form_data: UserUpdate,
        current_user: User = Depends(get_current_user),
        db: AsyncIOMotorClient = Depends(get_database)):
    updated_user = await update_user(db, current_user, UserSuperUpdate(**form_data.dict()))
    return updated_user
