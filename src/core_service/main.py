from __future__ import annotations
import logging
from fastapi import FastAPI

from .logger import setup_logging
from .service_locator import get_service_locator
from .settings import settings


setup_logging("core")
logger = logging.getLogger("core")

service_locator = None

app = FastAPI(docs_url=None, redoc_url=None)
NODE_NAME = "core_main"

@app.on_event("startup")
async def startup():
    global service_locator
    logger.info("Core Service стартует")

    service_locator = await get_service_locator()



@app.on_event("shutdown")
async def shutdown():
    logger.info("Core Service завершает работу")


@app.get("/health")
async def health():
    rabbitmq_status = "connected"
    return {
        "status": "OK",
        "node": NODE_NAME,
        "rabbitmq": rabbitmq_status
    }
