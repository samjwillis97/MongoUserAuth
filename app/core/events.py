import logging

from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db


async def connect_to_mongo():
    logging.info("Opening Connection ...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logging.info("Connetion Opened")


async def close_mongo_connection():
    logging.info("Closing Connection ...")
    db.client.close()
    logging.info("Connection Closed")