from fastapi import APIRouter

from .routes.token import router as token_router
# from .routes.users import router as users_router

router = APIRouter()
router.include_router(token_router, tags=["authentication"], prefix="/token")
# router.include_router(users, tags=["users"], prefix="/user")