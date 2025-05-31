# FastAPI main app entry point
from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from .routes import router as routes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("service_host")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Starting Service Host API...")
    yield
    logger.info("🧹 Shutting down Service Host API...")

app = FastAPI(
    title="Service Host API",
    lifespan=lifespan
)

app.include_router(routes)
