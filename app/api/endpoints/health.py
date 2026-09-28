from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health", summary="Health check")
def health_check() -> dict[str, str]:
    """Liveness probe for orchestrators / load balancers."""
    return {"status": "ok"}
