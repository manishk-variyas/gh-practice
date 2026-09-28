from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import api_router


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    # Place startup logic here (DB connections, caches, etc.)
    yield
    # Place shutdown logic here (cleanup, close connections, etc.)


def create_app() -> FastAPI:
    app = FastAPI(
        title="git-learn API",
        summary="Minimal FastAPI hello-world with good practices.",
        version="0.1.0",
        lifespan=lifespan,
    )
    app.include_router(api_router)
    return app


app = create_app()
