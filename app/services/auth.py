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
            return user
        if not self.permissions:
            return user
        
        if user.permissions == []:
            raise HTTPException(status_code=403, detail=INCORRECT_PERMS)
        elif (set(user.permissions).intersection(set(self.permissions))) == set():
            raise HTTPException(status_code=403, detail=INCORRECT_PERMS)
        else:
            return user
