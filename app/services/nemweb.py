from pprint import pprint
from typing import List
from fastapi.exceptions import HTTPException
from datetime import datetime, timedelta

from ..core.mongodb import AsyncIOMotorClient
from ..core.config import NEMWEB_DATABASE_NAME, NEMWEB_COLLECTION_NAME
from ..resources.strings import NEMWEB_UNIT_NOT_FOUND
from ..models.schemas.nemweb import CurrentUnitLoads, UnitLoad, UnitTrend, Units

async def get_all_units(conn: AsyncIOMotorClient):
    documents = conn[NEMWEB_DATABASE_NAME][NEMWEB_COLLECTION_NAME].find(
        sort=[("time", 1)],
        limit=1
    )

    units = []
    for document in await documents.to_list(length=1):
        for key in document["unit_load"].keys():
            units.append(key)
    
    return Units(Units=units)


async def get_current_unit_loads(conn: AsyncIOMotorClient, units: List[str]):
    # Building Projection Query, and Aggregation Pipeline
    projection = {"time": 1, "_id": 0}
    max_pipe_group = {"_id": "null"}
    for unit in units:
        unit_string = "unit_load." + unit
        projection[unit_string] = 1
        max_pipe_group[unit] = {"$max": "$" + unit_string}
    max_pipeline = [{"$group": max_pipe_group}]

    # Querying Database
    documents = conn[NEMWEB_DATABASE_NAME][NEMWEB_COLLECTION_NAME].find(
        sort=[("time", 1)],
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

    # Async Iteration for Max Pipeline Aggregation
    async for doc in conn[NEMWEB_DATABASE_NAME][NEMWEB_COLLECTION_NAME].aggregate(max_pipeline):
        UnitMaxs = []
        for key, value in doc.items():
            if key != "_id":
                UnitMaxs.append(UnitLoad(__root__={str(key): float(value)}))

    return CurrentUnitLoads(
        time=document["time"],
        unit_loads=UnitLoads,
        max=UnitMaxs
    )


async def get_unit_load_trend(conn: AsyncIOMotorClient, unit: str, period: int, avg_period: int):
    greater_than_time = datetime.now() - timedelta(days=period)
    buckets = int(24 * period / avg_period)

    pipeline = [
        {
            "$sort": {
                "time": -1
            }
        },
        {
            "$match": {
                "time": {
                    "$gte": greater_than_time
                }
            }
        },
        {
            "$bucketAuto": {
                "groupBy": "$time",
                "buckets": buckets,
                "output": {
                    "average": {
                        "$avg": "$unit_load." + unit
                    }
                }
            }
        }
    ]

    values = []
    start_time = datetime.utcnow()
    end_time = datetime.min

    async for doc in conn[NEMWEB_DATABASE_NAME][NEMWEB_COLLECTION_NAME].aggregate(pipeline):
        ## if doc average != Raise 404
        if doc['average'] is None:
            raise HTTPException(status_code=404, detail=NEMWEB_UNIT_NOT_FOUND)
       
        if doc['_id']['max'] > end_time:
            end_time = doc['_id']['max']

        if doc['_id']['min'] < start_time:
            start_time = doc['_id']['min']

        interval = doc['_id']['max'] - doc['_id']['min']

        values.append(doc['average'])

    return UnitTrend(
        start_time=start_time,
        end_time=end_time,
        delta=interval,
        length=len(values),
        max=max(values),
        min=min(values),
        unit=unit,
        values=values
    )
