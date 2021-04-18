from ...models.schemas.users import User
from ...models.schemas.nemweb import CurrentUnitLoads
from ...core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ...core.mongodb import AsyncIOMotorClient, get_database
from ...core.jwt import get_current_user
from ...services.auth import PermissionChecker
from ...services.nemweb import get_current_unit_loads

from fastapi import APIRouter, Depends, HTTPException, status, Body, Response, Query
from typing import List

from pprint import pprint


router = APIRouter()


@router.get(
    "/units",
    # response_model=CurrentUnitLoads
)
async def get_unit_loads(
        units: List[str] = Query(...),
        db: AsyncIOMotorClient = Depends(get_database)):
    return await get_current_unit_loads(db, units)
