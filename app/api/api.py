from fastapi import APIRouter

from .routes.auth import router as auth_router
from .routes.users import router as users_router

router = APIRouter()

# SEE https://frankie567.github.io/fastapi-users/usage/routes/


### RESET ROUTER
## POST - /forgot-password
# Request: email_address
# Response: Always 202 + Temporary Token
## POST - /reset-password
# Request: Matching token ^ + password
# Response: 200, 400 or 422

### VERIFY ROUTER (Email Verification)
## POST - /request-verify-token
# Request: email address
# Response: 202
## POST - /verify
# Request: token ^
# Response: 200, 422, 400

### USERS ROUTER
## GET - /me
# Response: id? + email + is_active + is_superuser
## PATCH - /me
# Request: Email + Pass
# Response: id? + email + is_active + is_superuse
## GET - /{user_id}
# Response: id? + email + is_active + is_superuser, 401, 403, 404
## PATCH - /{user_id}
# Request: email + password + is_active + is_superuse
# Response: id? + email + is_active + is_superuser, 401, 403, 404
## DELET - /{user_id}
# Response: id? + email + is_active + is_superuser, 401, 403, 404

router.include_router(auth_router, tags=["auth"], prefix="/auth")
router.include_router(users_router, tags=["users"], prefix="/users")
# router.include_router(users, tags=["users"], prefix="/user")