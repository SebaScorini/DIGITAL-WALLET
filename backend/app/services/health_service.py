from app.core.config import get_settings
from app.schemas.health import HealthResponse

settings = get_settings()


def build_health_response() -> HealthResponse:
    response = HealthResponse(
        status="ok",
        service=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
    )
    return response
