from pydantic import BaseModel
from typing import Optional, List


class Fault(BaseModel):
    name: str
    value: float

class Bearing(BaseModel):
    manufacturer: str
    bearing: str
    elements: int
    faults: List[Fault]