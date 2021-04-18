from pprint import pprint
from typing import List
from fastapi.exceptions import HTTPException

from ..core.mongodb import AsyncIOMotorClient
from ..core.config import NEMWEB_DATABASE_NAME, NEMWEB_COLLECTION_NAME
from ..resources.strings import NEMWEB_UNIT_NOT_FOUND
from ..models.schemas.nemweb import CurrentUnitLoads, UnitLoad


async def get_current_unit_loads(conn: AsyncIOMotorClient, units: List[str]):
    # Building Projection Query
    projection = {"time": 1, "_id": 0}
    for unit in units:
        unit_string = "unit_load." + unit
        projection[unit_string] = 1

    # Querying Database
    documents = conn[NEMWEB_DATABASE_NAME][NEMWEB_COLLECTION_NAME].find(
        sort=[("time", -1)],
        limit=1,
        projection=projection
    )

    # Async Iteration through DB
    for document in await documents.to_list(length=1):
        UnitLoads = []
        if document["unit_load"] == {}:
            raise HTTPException(status_code=404, detail=NEMWEB_UNIT_NOT_FOUND)
        for key, value in document["unit_load"].items():
            UnitLoads.append(UnitLoad(__root__={str(key): float(value)}))

        return CurrentUnitLoads(
            time=document["time"],
            unit_loads=UnitLoads
        )
