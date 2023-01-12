from bson.objectid import ObjectId
from fastapi import APIRouter, status
# from fas
from app.models import shop_collection, shop_helper
from app.schemas import Shop, UpdateShop

from app.utils import (get_shops_data, add_shop_data,
                       update_shop_data, delete_shop_data,
                       get_shop_data)


router = APIRouter()


@router.get('/', tags=['root'])
def home_page():
    return {'message': 'success!!!'}


@router.get('/shops', tags=['shops'])
async def shop_list():
    shops = []
    async for shop in shop_collection.find():
        shops.append(shop_helper(shop))
    return shops


@router.post('/shops', tags=['add_shop'], status_code=status.HTTP_201_CREATED)
async def post_shop(shop_data: Shop):
    shop = await add_shop_data(shop_data.dict())
    return shop


@router.get('/shop/{id}', tags=['shop detail'], status_code=status.HTTP_200_OK)
async def get_shop(id: str):
    shop = await get_shop_data(id)
    if shop:
        return shop
    return {'Message': status.HTTP_400_BAD_REQUEST}


@router.put('/shop/{id}', tags=['update_shop'], status_code=status.HTTP_202_ACCEPTED)
async def update_shop(id: str, shop_data: UpdateShop):
    shop_data = {k: v for k, v in shop_data.dict().items() if v is not None}
    updated_shop = await update_shop_data(id, shop_data)
    if updated_shop:
        return {'message': f'Student with id {id} is successfully updated'}
    return {'message': status.HTTP_400_BAD_REQUEST}


@router.delete('/shop/{id}', tags=['delete shop'], status_code=status.HTTP_202_ACCEPTED)
async def delete_shop(id: str):
    deleted_shop = await delete_shop_data(id)
    if deleted_shop:
        return {'message': f'Shop with id {id} was successfully deleted'}
    return {'message': status.HTTP_400_BAD_REQUEST}
