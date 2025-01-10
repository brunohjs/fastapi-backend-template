from fastapi import APIRouter

from src.api.routes import health
from src.api.routes import user


api_router = APIRouter()
api_router.include_router(user.router, tags=["users"])
api_router.include_router(health.router, tags=["health"])
