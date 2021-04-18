from datetime import datetime
from pydantic import BaseModel
from typing import List, Dict

from .db import MongoModel


class UnitLoad(BaseModel):
    __root__: Dict[str, float]


class CurrentUnitLoads(BaseModel):
    time: datetime
    unit_loads: List[UnitLoad]
