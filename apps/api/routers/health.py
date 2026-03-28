from datetime import datetime, timezone

from fastapi import APIRouter

from packages.core.config import settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "env": settings.app_env,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
