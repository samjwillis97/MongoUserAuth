from pydantic import EmailStr
from bson.objectid import ObjectId
from datetime import datetime
from pprint import pprint
from fastapi.exceptions import HTTPException

from ..resources.strings import USER_NOT_FOUND
from ..core.mongodb import AsyncIOMotorClient
from ..core.security import get_password_hash
from ..core.config import database_name, user_collection_name
from ..models.schemas.users import UserCreate, UserLogin, UserInDB, UserSuperUpdate, UserRegister, User, UserInResponse


async def get_user(conn: AsyncIOMotorClient, email: str) -> UserInDB:
    row = await conn[database_name][user_collection_name].find_one(
        {"email": email}
    )
    if row:
        return UserInDB(**row, id=row["_id"])

async def get_all_users(conn: AsyncIOMotorClient):
    users = []
    user_collection = conn[database_name][user_collection_name]
    
    async for document in user_collection.find({}):
        users.append(UserInResponse(**document))

    return users

async def create_user(conn: AsyncIOMotorClient, user: UserRegister) -> UserInDB:
    dbuser = UserCreate(**user.dict())
    dbuser.update_password(user.password)
    dbuser.created_at = datetime.now()
    dbuser.update_time()

    # create refresh token, hash, store in db??

    await conn[database_name][user_collection_name].insert_one(dbuser.dict())

    return dbuser


async def update_user(conn: AsyncIOMotorClient, user: User, form_data: UserSuperUpdate) -> UserInDB:
    user_to_update = await get_user(conn, user.email)
    user_to_update.update_time()
    
    user_updates = form_data.dict(skip_defaults=True)
    user_updates['hashed_password'] = get_password_hash(user_updates['password'])
    del user_updates['password']

    user_to_update = user_to_update.dict()
    user_to_update_id = user_to_update['id']
    del user_to_update['id']

    updated_user = user_to_update | user_updates

    await conn[database_name][user_collection_name].update_one(
        {'_id': user.id},
        {'$set': updated_user}
    )
    
    updated_user['id'] = user_to_update_id

    return UserInDB(**updated_user)


async def check_email_is_taken(conn: AsyncIOMotorClient, email: str):
    row = await conn[database_name][user_collection_name].find_one(
        {"email": email}
    )
    if row:
        return True
    return False


async def read_user_by_email(conn: AsyncIOMotorClient, email: str):
    row = await conn[database_name][user_collection_name].find_one(
        {"email": email}
    )
    if row:
        pprint(row)
        return UserInResponse(**row)
    else:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)

# return user of 403?
# async def check_superuser(conn:AsyncIOMotorClient, email:str):
#     row = await conn[database_name][user_collection_name].find_one(
#         {"email": email}
#     )
#     return row["is_superuser"]
