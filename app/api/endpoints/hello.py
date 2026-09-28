from fastapi import APIRouter

router = APIRouter(tags=["hello"])


@router.get("/", summary="Hello World")
def hello_world() -> dict[str, str]:
    """Return a simple hello world message."""
    return {"message": "Hello, World!"}
