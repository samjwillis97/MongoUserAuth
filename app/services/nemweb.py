from pprint import pprint
from typing import List
from fastapi.exceptions import HTTPException

from ..core.mongodb import AsyncIOMotorClient
from ..core.config import NEMWEB_DATABASE_NAME, NEMWEB_COLLECTION_NAME


async def get_current_unit_loads(conn: AsyncIOMotorClient, units: List[str]):
    pass
