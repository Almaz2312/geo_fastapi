from bson import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorClient
from .models import shop_helper


# Retrieve all shops present in the database
async def get_shops_data(database: AsyncIOMotorClient):
    shops = []
    async for shop in database['shops'].find():
        shops.append(shop_helper(shop))
    return shops


# Add a new shop into to the database
async def add_shop_data(database: AsyncIOMotorClient, shop_data: dict) -> dict:
    shop = await database['shops'].insert_one(shop_data)
    new_shop = await database['shops'].find_one({'_id': shop.inserted_id})
    return shop_helper(new_shop)


# Retrieve a shop with a matching ID
async def get_shop_data(database: AsyncIOMotorClient, id: str):
    shop = await database['shops'].find_one({'_id': ObjectId(id)})
    if shop:
        return shop_helper(shop)


# Update a shop with a matching ID
async def update_shop_data(database: AsyncIOMotorClient, id: str, data: dict):
    if len(data) < 1:
        return False
    shop = await database['shops'].find_one({'_id': ObjectId(id)})
    if shop:
        updated_shop = await database['shops'].update_one(
            {'_id': ObjectId(id)}, {'$set': data}
        )
        if updated_shop:
            return True
        return False


# Delete a student from the database
async def delete_shop_data(database: AsyncIOMotorClient, id: str):
    # Check for validity of ID
    try:
        ObjectId(id)
    except InvalidId:
        return False

    shop = await database['shops'].find_one({'_id': ObjectId(id)})
    if shop:
        await database['shops'].delete_one({'_id': ObjectId(id)})
        return True
    return False
