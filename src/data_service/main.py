from fastapi import FastAPI
import logging
import asyncio

from .logger import setup_logging
from .settings import settings
from .service_locator import get_service_locator
from .messaging.consumer import DataServiceRPCServer

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Data Service API", version="1.0.0")

service_locator = None
rpc_server: DataServiceRPCServer | None = None

@app.on_event("startup")
async def startup():
    logger.info("Data Service стартует")
    global service_locator, rpc_server
    service_locator = await get_service_locator()
    rpc_server = DataServiceRPCServer(service_locator)
    asyncio.create_task(rpc_server.connect())
    logger.info("Data Service готов")

@app.on_event("shutdown")
async def shutdown():
    global rpc_server
    if rpc_server:
        await rpc_server.shutdown()


@app.get("/health")
async def health():
    return {"status": "OK"}
