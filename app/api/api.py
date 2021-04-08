from fastapi import APIRouter

from .routes.auth import router as auth_router
from .routes.users import router as users_router

router = APIRouter()

# SEE https://frankie567.github.io/fastapi-users/usage/routes/

router.include_router(auth_router, tags=["auth"], prefix="/auth")
router.include_router(users_router, tags=["users"], prefix="/users")
# router.include_router(users, tags=["users"], prefix="/user")