"""Central place to register all API routers.

Add new feature routers here, e.g.:
    from app.api.endpoints import users
    api_router.include_router(users.router, prefix="/users", tags=["users"])
"""

from fastapi import APIRouter

from app.api.endpoints import health, hello,tasks

api_router = APIRouter()

api_router.include_router(hello.router)
api_router.include_router(health.router)
api_router.include_router(tasks.router)
