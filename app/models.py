import os
from dotenv import load_dotenv
from pathlib import Path

import motor.motor_asyncio

env_path = Path('.') / '.envs' / '.env'
load_dotenv(dotenv_path=env_path)

MONGODB_URL = os.getenv('MONGO_INITDB_DATABASE')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.mongo_db

shop_collection = database['shops']


def shop_helper(shop) -> dict:
    return {
        "id": str(shop["_id"]),
        "name": shop["name"],
        'latitude': shop['latitude'],
        'longitude': shop['longitude'],
        'address': shop['address'],
        'city': shop['city']
    }

# 63bfb893756e96700d8ea536