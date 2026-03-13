from fastapi import FastAPI

from app.core.config import get_settings
from app.routers import health_router

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(health_router)
