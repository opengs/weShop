from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from .database import register_db
from .services.cart import register_cart_service

from .routes.cart import router as carts_router

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])

app.include_router(carts_router, prefix="/api/carts", tags=["Cart"])

register_db(app)
register_cart_service(app)