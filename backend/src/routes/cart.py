from fastapi.routing import APIRouter
from fastapi import Body, Depends
from pydantic import BaseModel, Field

from ..services.cart import (
    get_cart as get_cart_service,
    add_product as add_product_service,
    remove_product as remove_product_service,
    CartModel
)

router = APIRouter()

@router.get(
    "/cart",
    response_model=CartModel
)
async def get_cart():
    '''Get cart information'''
    return await get_cart_service("DEFAULT")

class PutProductRequest(BaseModel):
    name: str = Field(..., description="Name of the product")

@router.put(
    "/product"
)
async def add_product(data: PutProductRequest = Body(...)):
    await add_product_service("DEFAULT", data.name)

class DeleteProductRequest(BaseModel):
    name: str = Field(..., description="Name of the product")

@router.delete(
    "/product"
)
async def remove_product(data: DeleteProductRequest = Depends()):
    await remove_product_service("DEFAULT", data.name)