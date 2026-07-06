from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.config import settings
from app.models import init_db
from app.services.orchestrator import orchestrator


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await orchestrator.close()


app = FastAPI(
    title=settings.app_name,
    description="AI-powered comedy platform for conspiracy theories and debunking",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "AI Conspiracy Generator API", "docs": "/docs"}
