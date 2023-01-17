from fastapi import APIRouter, status, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from .models import get_db
from .schemas import Shop, UpdateShop

from .utils import (get_shops_data, add_shop_data,
                    update_shop_data, delete_shop_data,
                    get_shop_data)

router = APIRouter()


@router.get('/shops', tags=['shops'])
async def shop_list(db: AsyncIOMotorClient = Depends(get_db)):
    shops = await get_shops_data(database=db)
    return shops


@router.post('/shops', tags=['add_shop'], status_code=status.HTTP_201_CREATED)
async def post_shop(shop_data: Shop, db: AsyncIOMotorClient = Depends(get_db)):
    shop = await add_shop_data(shop_data=shop_data.dict(), database=db)
    return shop


@router.get('/shop/{id}', tags=['shop detail'], status_code=status.HTTP_200_OK)
async def get_shop(id: str, db: AsyncIOMotorClient = Depends(get_db)):
    shop = await get_shop_data(id=id, database=db)
    if shop:
        return shop
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Shop with id {id} was not found')


@router.put('/shop/{id}', tags=['update_shop'], status_code=status.HTTP_202_ACCEPTED)
async def update_shop( id: str, shop_data: UpdateShop, db: AsyncIOMotorClient = Depends(get_db)):
    shop_data = {k: v for k, v in shop_data.dict().items() if v is not None}
    updated_shop = await update_shop_data(id=id, data=shop_data, database=db)
    if updated_shop:
        return {'message': f'Student with id {id} is successfully updated'}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.delete('/shop/{id}', tags=['delete shop'], status_code=status.HTTP_202_ACCEPTED)
async def delete_shop(id: str, db: AsyncIOMotorClient = Depends(get_db)):
    deleted_shop = await delete_shop_data(id=id, database=db)
    if deleted_shop:
        return {'message': f'Shop with id {id} was successfully deleted'}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Shop with id {id} is not found')
