from fastapi import APIRouter

from bezum.endpoints.auth import router as auth_router
from bezum.endpoints.user import router as user_router

routers = APIRouter()

api_routers = APIRouter(prefix="/api")
api_routers.include_router(user_router, tags=["User"])
api_routers.include_router(auth_router, tags=["Auth"])

routers.include_router(api_routers)
