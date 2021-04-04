from pydantic import EmailStr
from bson.objectid import ObjectId
from datetime import datetime

from ..core.mongodb import AsyncIOMotorClient
from ..core.config import database_name, user_collection_name
from ..models.schemas.users import UserLogin, UserInDB, UserUpdate, UserRegister


async def get_user(conn: AsyncIOMotorClient, email: str) -> UserInDB:
    row = await conn[database_name][user_collection_name].find_one(
        {"email": email}
    )
    if row:
        return UserInDB(**row)


async def create_user(conn: AsyncIOMotorClient, user: UserRegister) -> UserInDB:
    dbuser = UserInDB(**user.dict())
    dbuser.update_password(user.password)
    dbuser.created_at = datetime.now()
    dbuser.update_time()

    await conn[database_name][user_collection_name].insert_one(dbuser.dict())

    return dbuser


async def check_email_is_taken(conn: AsyncIOMotorClient, email: str):
    row = await conn[database_name][user_collection_name].find_one(
        {"email": email}
    )
    if row:
        return True
    return False
