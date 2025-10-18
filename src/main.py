from __future__ import annotations

import logging

from fastapi import FastAPI
import yaml
# from fastapi.templating import Jinja2Templates
# from init_monodb.create_mongodb import async_init_mongodb
from logger import setup_logging

from routers.api_v2.accommodation import accommodation_router
from routers.api_v2.city import router as city_router
from routers.api_v2.auth import router as auth_router
from routers.api_v2.d_route import router as d_router
from routers.api_v2.entertainment import entertainment_router
from routers.api_v2.route import router
from routers.api_v2.travel import router as travel_router
from routers.api_v2.user import user_router
from routers.api_v2.travel_ent import router as tr_ent_router
from routers.api_v2.travel_acc import router as tr_acc_router

# templates = Jinja2Templates(directory="templates")

setup_logging()
logger = logging.getLogger(__name__)


def load_swagger_spec() -> dict[str, Any]:
    try:
        with open("swagger_v2.yaml", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logger.warning("swagger.yaml не найден, используется стандартная документация")
        return None


app = FastAPI(
    title="TravelGuide API",
    description="API для системы TravelGuide",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema
    
    # Загружаем кастомную спецификацию
    swagger_spec = load_swagger_spec()
    
    if swagger_spec:
        # Используем спецификацию из YAML
        app.openapi_schema = swagger_spec
    else:
        # Генерируем стандартную документацию
        from fastapi.openapi.utils import get_openapi
        
        app.openapi_schema = get_openapi(
            title="TravelGuide API",
            version="1.0.0",
            description="API для системы TravelGuide",
            routes=app.routes,
        )
    
    return app.openapi_schema


# app.openapi = custom_openapi


app.include_router(router, prefix="/api/v2")
app.include_router(d_router, prefix="/api/v2")
app.include_router(city_router, prefix="/api/v2")
app.include_router(user_router, prefix="/api/v2")
app.include_router(accommodation_router, prefix="/api/v2")
app.include_router(travel_router, prefix="/api/v2")
app.include_router(entertainment_router, prefix="/api/v2")
app.include_router(tr_ent_router, prefix="/api/v2")
app.include_router(tr_acc_router, prefix="/api/v2")
app.include_router(auth_router, prefix="/api/v2")

# @app.get("/", response_class=HTMLResponse)
# async def serve_main_page(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse("main.html", {"request": request})


# @app.get("/login", response_class=HTMLResponse)
# async def login_page(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse("login.html", {"request": request})


# @app.get("/register", response_class=HTMLResponse)
# async def register_page(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse("register.html", {"request": request})


# @app.exception_handler(Exception)
# async def handle_exceptions(request: Request, exc: Exception) -> JSONResponse:
#     logger.error(f"Ошибка при обработке запроса: {exc}", exc_info=True)
#     return JSONResponse(
#         status_code=500,
#         content={"detail": "Internal server error"},
#     )


# @app.on_event("startup")
# async def startup() -> None:
#     logger.info("Запуск приложения")
#     # await async_init_mongodb()


# @app.on_event("shutdown")
# async def shutdown() -> None:
#     logger.info("Завершение работы приложения")


# @app.get("/health")
# async def health_check() -> dict[str, str]:
#     return {"status": "OK"}


# @app.get("/openapi.json", include_in_schema=False)
# async def get_openapi_json() -> dict[str, Any]:
#     return custom_openapi()


# @app.get("/swagger.yaml", include_in_schema=False)
# async def get_swagger_yaml() -> Response:
#     with open("swagger.yaml", encoding="utf-8") as file:
#         return Response(content=file.read(), media_type="application/x-yaml")