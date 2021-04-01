from ..db.mongodb import AsyncIOMotorClient
from pydantic import EmailStr

from ..core.config import database_name, user_collection_name
from ..models.schemas.user import UserLogin, UserInDB, UserUpdate

async def get_user(conn: AsyncIOMotorClient, username: str) -> UserInDB:
  row = await conn[database_name][user_collection_name].find_one({"username": username})
  if row:
    return UserInDB(**row)