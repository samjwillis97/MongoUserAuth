from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import List, Dict

from .db import MongoModel


class Units(BaseModel):
    Units: List[str]


class UnitLoad(BaseModel):
    __root__: Dict[str, float]


class CurrentUnitLoads(BaseModel):
    time: datetime
    unit_loads: List[UnitLoad]
    max: List[UnitLoad]


class UnitTrend(BaseModel):
    start_time: datetime
    end_time: datetime
    delta: timedelta
    length: int
    max: float
    min: float
    unit: str
    values: List[float]
