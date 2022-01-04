from fastapi import FastAPI

from typing import List, Union
from pydantic import BaseModel, Field, parse_obj_as

from ..database import DB

class CartModel(BaseModel):
    uuid: str = Field(..., description="Cart UUID")
    products: List[str] = Field([], description="List of products waiting for realization")
    realized: List[str] = Field([], description="List of products already realized")

async def create_cart() -> CartModel:
    '''Create cart'''
    cart = CartModel(uuid="DEFAULT")
    await DB.Carts.insert_one(cart.dict())
    return cart

async def get_cart(cart_uuid: str) -> Union[CartModel, None]:
    cart = await DB.Carts.find_one({"uuid": cart_uuid})
    return None if cart == None else parse_obj_as(CartModel, cart)

async def add_product(cart_uuid: str, product: str):
    '''Add product to the cart list'''
    await DB.Carts.update_one({"uuid": cart_uuid}, {"$addToSet": { "products": product }})

async def remove_product(cart_uuid: str, product: str):
    '''Remove product from the cart list'''
    await DB.Carts.update_one({"uuid": cart_uuid}, {"$pull": { "products": product }})

async def realize_product(cart_uuid: str, product: str, realize: bool):
    '''Make product realized (puted in cart or not)'''
    if realize:
        await DB.Carts.update_one({"uuid": cart_uuid}, {"$pull": { "products": product }, "$addToSet": { "realized": product }})
    else:
        await DB.Carts.update_one({"uuid": cart_uuid}, {"$addToSet": { "products": product }, "$pull": { "realized": product }})

def register_cart_service(app: FastAPI):
    async def on_startup():
        #ensure indexes    
        indexes = await DB.Carts.index_information()
        if "unique_uuid" not in indexes:
            await DB.Carts.create_index([("uuid", 1)], unique=True, name="unique_uuid")

        #Create default cart

        await DB.Carts.update_one(
                {"uuid": "DEFAULT"},
                {"$setOnInsert": CartModel(uuid="DEFAULT").dict()},
                upsert=True
            )

    app.add_event_handler("startup", on_startup)