from typing import Optional, List
from fastapi import Depends
from fastapi.exceptions import HTTPException

from ..models.schemas.users import User
from ..resources.strings import INCORRECT_PERMS
from ..core.jwt import get_current_user

from pprint import pprint

class PermissionChecker:
    def __init__(self, permissions: Optional[List[str]]):
        self.permissions = permissions

    async def __call__(self, user: User = Depends(get_current_user)):
        if user.is_superuser:
            pprint("SUperUser")
            return user
        if not self.permissions:
            pprint("No Perms")
            return user

        pprint((user.permissions))
        pprint((self.permissions))
        pprint(set(user.permissions) & set(self.permissions))
        
        if (set(user.permissions) & set(self.permissions)) is None:
            pprint("Exception")
            raise HTTPException(status_code=403, detail=INCORRECT_PERMS)
        else:
            pprint("Has Perms")
            return user
