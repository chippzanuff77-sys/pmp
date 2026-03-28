from fastapi import FastAPI

from apps.api.routers.health import router as health_router

app = FastAPI(title="Pump Pattern Research & Scanner API", version="0.1.0")
app.include_router(health_router)
