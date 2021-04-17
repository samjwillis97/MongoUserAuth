from ...models.schemas.users import UserInResponse, User, UserUpdate, UserSuperUpdate
from ...core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ...core.mongodb import AsyncIOMotorClient, get_database
from ...core.jwt import get_current_user
from ...services.users import get_user, update_user, get_all_users, read_user_by_email, delete_user_by_email
from ...services.auth import PermissionChecker
from ...resources.strings import USER_DELETED

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Body, Response
from fastapi.security import OAuth2PasswordRequestForm
from typing import List

from pprint import pprint


# USERS ROUTER
# PATCH - /{user_id}
# Request: email + password + is_active + is_superuse
# Response: id? + email + is_active + is_superuser, 401, 403, 404

router = APIRouter()

superUserCheck = PermissionChecker(["superuser"])


@router.get(
    "/",
    response_model=List[UserInResponse]
)
async def read_all_users(
        current_user: User = Depends(superUserCheck),
        db: AsyncIOMotorClient = Depends(get_database)):
    users = await get_all_users(db)
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
    updated_user = await update_user(db, current_user.email, UserSuperUpdate(**form_data.dict()))
    return updated_user


@router.delete(
    "/me",
    status_code=204,
    response_class=Response
)
async def delete_current_user(
        current_user: User = Depends(get_current_user),
        db: AsyncIOMotorClient = Depends(get_database)):
    await delete_user_by_email(db, current_user.email)
    return


@router.get(
    "/{email}",
    response_model=UserInResponse
)
async def get_a_user(
        email: str,
        current_user: User = Depends(superUserCheck),
        db: AsyncIOMotorClient = Depends(get_database)):
    return await read_user_by_email(db, email)


@router.patch(
    "/{email}",
    response_model=UserInResponse
)
async def update_a_user(
        email: str,
        form_data: UserSuperUpdate,
        current_user: User = Depends(superUserCheck),
        db: AsyncIOMotorClient = Depends(get_database)):
    updated_user = await update_user(db, email, form_data)
    return updated_user


@router.delete(
    "/{email}",
    status_code=204,
    response_class=Response
)
async def delete_a_user(
        email: str,
        current_user: User = Depends(superUserCheck),
        db: AsyncIOMotorClient = Depends(get_database)):
    await delete_user_by_email(db, email)
    return
