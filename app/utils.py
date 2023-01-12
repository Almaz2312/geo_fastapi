from bson import ObjectId
from app.models import shop_collection, shop_helper


# Retrieve all shops present in the database
async def get_shops_data():
    shops = []
    async for shop in shop_collection.find():
        shops.append(shop_helper(shop))
    return shops


# Add a new shop into to the database
async def add_shop_data(shop_data: dict) -> dict:
    shop = await shop_collection.insert_one(shop_data)
    new_shop = await shop_collection.find_one({'_id': shop.inserted_id})
    return new_shop


# Retrieve a shop with a matching ID
async def get_shop_data(id: str):
    shop = await shop_collection.find_one({'_id': ObjectId(id)})
    if shop:
        return shop_helper(shop)


# Update a shop with a matching ID
async def update_shop_data(id: str, data: dict):
    if len(data) < 1:
        return False
    shop = await shop_collection.find_one({'_id': ObjectId(id)})
    if shop:
        updated_shop = await shop_collection.update_one(
            {'_id': ObjectId(id)}, {'$set': data}
        )
        if updated_shop:
            return True
        return False


# Delete a student from the database
async def delete_shop_data(id: str):
    shop = await shop_collection.find_one({'_id': ObjectId(id)})
    if shop:
        await shop_collection.delete_one({'_id': ObjectId(id)})
        return True
