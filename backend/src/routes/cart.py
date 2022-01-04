from fastapi.routing import APIRoute, APIRouter

from ..services.cart import get_cart as get_cart_service, CartModel

router = APIRouter()

@router.get(
    "/cart",
    response_model=CartModel
)
async def get_cart():
    '''Get cart information'''
    return await get_cart_service("DEFAULT")