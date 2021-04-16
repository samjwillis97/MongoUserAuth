from ...models.schemas.auth import Token
from ...models.schemas.users import UserRegister, UserBase
from ...core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ...core.mongodb import AsyncIOMotorClient, get_database
from ...core.jwt import create_access_token
from ...services.users import get_user, check_email_is_taken, create_user
from ...resources import strings

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

# AUTH ROUTER
# POST - /login
# Request: Login Form (User + Pass)
# Response: access_token + token_type

# REGISTER ROUTER
# POST - /register
# Request: Login (User + Pass)
# Response: id? + email + is_active + is_superuser


@router.post("/login", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: AsyncIOMotorClient = Depends(get_database)):
    user = await get_user(db, form_data.username)
    if not user or not user.check_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=strings.INCORRECT_LOGIN,
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

# @router.post("/refresh-token", response_model=Token)
# async def refresh_token(
#     request
# )

# Would prefer to return new token


@router.post("/register", status_code=201, response_model=UserBase)
async def register_user(
        form_data: UserRegister,
        db: AsyncIOMotorClient = Depends(get_database)):
    if await check_email_is_taken(db, form_data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.EMAIL_TAKEN,
        )
    user = await create_user(db, form_data)
    return user
