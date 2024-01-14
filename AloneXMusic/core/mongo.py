from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database Gandu ...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("Ho Gya cennect Mongo Database Madrchod .....")
except:
    LOGGER(__name__).error("Kya ma chuda rha hain Mongo Database connect nahi hua hain gandu .")
    exit()
