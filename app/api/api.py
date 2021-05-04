from fastapi import APIRouter

from .routes.auth import router as auth_router
from .routes.users import router as users_router
from .routes.nemweb import router as nemweb_router

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

### Bearing Faults
## GET - / 
# Request: elements, manufacturer, bearing, greater, less
# Response: List[faults]

### TDMS Upload

### Modems
## GET - /
# Request:
# Response:
## POST - /
# Request:
# Response:
## GET - /{modem_id}
# Request:
# Response:
## PATCH - /{modem_id}
# Request: 
# Response:
## DELETE - /{modem_id}
# Request:
# Response:

router.include_router(auth_router, tags=["auth"], prefix="/auth")
router.include_router(users_router, tags=["users"], prefix="/users")
router.include_router(nemweb_router, tags=["nemweb"], prefix="/nemweb")