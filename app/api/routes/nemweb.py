from ...models.schemas.users import User
from ...models.schemas.nemweb import CurrentUnitLoads, UnitTrend, Units
from ...core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ...core.mongodb import AsyncIOMotorClient, get_database
from ...core.jwt import get_current_user
from ...services.auth import PermissionChecker
from ...services.nemweb import get_current_unit_loads, get_unit_load_trend, get_all_units

from fastapi import APIRouter, Depends, HTTPException, status, Body, Response, Query
from typing import List

from pprint import pprint


router = APIRouter()


@router.get(
    "/",
    response_model=Units
)
async def list_all_units(
        db: AsyncIOMotorClient = Depends(get_database)):
    return await get_all_units(db)


@router.get(
    "/current",
    # response_model=CurrentUnitLoads
)
async def get_recent_unit_loads(
        units: List[str] = Query(...),
        db: AsyncIOMotorClient = Depends(get_database)):
    return await get_current_unit_loads(db, units)


@router.get(
    "/trend",
    response_model=UnitTrend
)
async def get_unit_load_over_time(
        unit: str,
        days: int,
        average_period: int,
        db: AsyncIOMotorClient = Depends(get_database)):
    return await get_unit_load_trend(db, unit, days, average_period)
