import logging
from fastapi import FastAPI
from ..config import MONGO_CONNECTION_STRING

from pydantic.json import ENCODERS_BY_TYPE
from pydantic import BaseModel, Field

from bson.objectid import ObjectId
from bson.decimal128 import Decimal128
from motor.motor_asyncio import AsyncIOMotorGridFSBucket, AsyncIOMotorClient
from motor.core import AgnosticClient, Database, Collection

from ..logger import create_logger

_logger = create_logger("database")

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return v
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

ENCODERS_BY_TYPE[ObjectId] = str

class TranslationString(BaseModel):
    en: str = Field(..., alias="en", description="English")
    pl: str = Field(None, alias="pl", description="Polski")
    ua: str = Field(None, alias="ua", description="Українська")
    ru: str = Field(None, alias="ru", description="Русский")

class MoneyField(BaseModel):
    value: int = Field(...)
    currency: str = Field(...)


client: AgnosticClient = None
db: Database = None

class DB():
    Carts: Collection = None

async def _startup():
    global client, db
    _logger.info("Start connecting")
    client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
    db = client.cybertap

    DB.Carts = db['carts']

    _logger.info("Connection established")

async def _shutdown():
    global client
    client.close()
    _logger.info("Connection closed")

def register_db(app: FastAPI):
    app.add_event_handler("startup", _startup)
    app.add_event_handler("shutdown", _shutdown)