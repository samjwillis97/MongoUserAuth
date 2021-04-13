from pydantic import EmailStr
from bson.objectid import ObjectId
from datetime import datetime
from pprint import pprint

from ..core.mongodb import AsyncIOMotorClient
from ..core.config import database_name, user_collection_name
from ..models.schemas.users import UserLogin, UserInDB, UserSuperUpdate, UserRegister


async def get_user(conn: AsyncIOMotorClient, email: str) -> UserInDB:
    row = await conn[database_name][user_collection_name].find_one(
        {"email": email}
    )
    if row:
        pprint(row)
        return UserInDB(**row, id=row["_id"])


async def create_user(conn: AsyncIOMotorClient, user: UserRegister) -> UserInDB:
    dbuser = UserInDB(**user.dict())
    dbuser.update_password(user.password)
    dbuser.created_at = datetime.now()
    dbuser.update_time()

    await conn[database_name][user_collection_name].insert_one(dbuser.dict())

    return dbuser


async def update_user(conn: AsyncIOMotorClient, user: UserInDB, form_data: UserSuperUpdate) -> UserInDB:
    # Get old document using user.email
    # pprint(user)
    await conn[database_name][user_collection_name].update_one(
        {'_id': user.id},
        # {'$set': {k:v for k,v in form_data.items() if v is not None}}
        {'$set': form_data.dict(skip_defaults=True)}
    )
    
    return


async def check_email_is_taken(conn: AsyncIOMotorClient, email: str):
    row = await conn[database_name][user_collection_name].find_one(
        {"email": email}
    )
    if row:
        return True
    return False
