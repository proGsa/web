from __future__ import annotations

import logging
import json 
from fastapi import FastAPI
# import yaml
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
# from init_monodb.create_mongodb import async_init_mongodb
from logger import setup_logging

from routers.api_v1.accommodation import accommodation_router as accommodation_router_v1
from routers.api_v1.city import city_router as city_router_v1
from routers.api_v1.d_route import d_router as d_router_v1
from routers.api_v1.entertainment import entertainment_router as entertainment_router_v1
from routers.api_v1.route import router as router_v1
from routers.api_v1.travel import travel_router as travel_router_v1
from routers.api_v1.user import user_router as user_router_v1

from routers.api_v2.accommodation import accommodation_router as accommodation_router_v2
from routers.api_v2.city import router as city_router_v2
from routers.api_v2.auth import router as auth_router_v2
from routers.api_v2.d_route import router as d_router_v2
from routers.api_v2.entertainment import entertainment_router as entertainment_router_v2
from routers.api_v2.route import router as router_v2
from routers.api_v2.travel import router as travel_router_v2
from routers.api_v2.user import user_router as user_router_v2
from routers.api_v2.travel_ent import router as tr_ent_router_v2
from routers.api_v2.travel_acc import router as tr_acc_router_v2

templates = Jinja2Templates(directory="templates")

setup_logging()
logger = logging.getLogger(__name__)


# def load_swagger_spec() -> dict[str, Any]:
#     try:
#         with open("swagger_v2.yaml", encoding="utf-8") as file:
#             return yaml.safe_load(file)
#     except FileNotFoundError:
#         logger.warning("swagger.yaml не найден, используется стандартная документация")
#         return None


# Приложение для API v1
app = FastAPI(
    title="TravelGuide API v1",
    description="API v1 для системы TravelGuide",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# # Приложение для API v2  
# app_v2 = FastAPI(
#     title="TravelGuide API v2",
#     description="API v2 для системы TravelGuide", 
#     version="2.0.0",
#     docs_url="/docs",
#     redoc_url="/redoc"
# )

app.include_router(router_v1, prefix="/api/v1")
app.include_router(d_router_v1, prefix="/api/v1")
app.include_router(city_router_v1, prefix="/api/v1")
app.include_router(user_router_v1, prefix="/api/v1")
app.include_router(accommodation_router_v1, prefix="/api/v1")
app.include_router(travel_router_v1, prefix="/api/v1")
app.include_router(entertainment_router_v1, prefix="/api/v1")

app.include_router(router_v2, prefix="/api/v2")
app.include_router(d_router_v2, prefix="/api/v2")
app.include_router(city_router_v2, prefix="/api/v2")
app.include_router(user_router_v2, prefix="/api/v2")
app.include_router(accommodation_router_v2, prefix="/api/v2")
app.include_router(travel_router_v2, prefix="/api/v2")
app.include_router(entertainment_router_v2, prefix="/api/v2")
app.include_router(tr_ent_router_v2, prefix="/api/v2")
app.include_router(tr_acc_router_v2, prefix="/api/v2")
app.include_router(auth_router_v2, prefix="/api/v2")


from fastapi.openapi.utils import get_openapi
import json

@app.get("/openapi/v1.json")
async def get_openapi_v1():
    """Возвращает OpenAPI схему для API v1"""
    # Создаем временное приложение для v1
    temp_app_v1 = FastAPI(
        title="TravelGuide API v1",
        version="1.0.0",
        description="API v1 для системы TravelGuide",
        openapi_url="/openapi.json"
    )
    
    # Подключаем только v1 роутеры
    temp_app_v1.include_router(router_v1, prefix="/api/v1")
    temp_app_v1.include_router(d_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(city_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(user_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(accommodation_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(travel_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(entertainment_router_v1, prefix="/api/v1")
    
    # Получаем схему
    schema = get_openapi(
        title="TravelGuide API v1",
        version="1.0.0",
        description="API v1 для системы TravelGuide",
        routes=temp_app_v1.routes,
    )
    
    # Убеждаемся, что есть обязательные поля
    schema["openapi"] = "3.0.2"
    
    # Исправляем пути - убираем дублирующий /api/v1
    fixed_paths = {}
    for path, methods in schema["paths"].items():
        if path.startswith("/api/v1/api/v1/"):
            # Исправляем дублирование префикса
            fixed_path = path.replace("/api/v1/api/v1/", "/api/v1/")
        elif path.startswith("/api/v1/"):
            fixed_path = path
        else:
            fixed_path = f"/api/v1{path}"
        fixed_paths[fixed_path] = methods
    
    schema["paths"] = fixed_paths
    
    return JSONResponse(schema)

@app.get("/openapi/v2.json")
async def get_openapi_v2():
    """Возвращает OpenAPI схему для API v2"""
    # Создаем временное приложение для v2
    temp_app_v2 = FastAPI(
        title="TravelGuide API v2",
        version="2.0.0", 
        description="API v2 для системы TravelGuide",
        openapi_url="/openapi.json"
    )
    
    # Подключаем только v2 роутеры
    temp_app_v2.include_router(router_v2, prefix="/api/v2")
    temp_app_v2.include_router(d_router_v2, prefix="/api/v2")
    temp_app_v2.include_router(city_router_v2, prefix="/api/v2")
    temp_app_v2.include_router(user_router_v2, prefix="/api/v2")
    temp_app_v2.include_router(accommodation_router_v2, prefix="/api/v2")
    temp_app_v2.include_router(travel_router_v2, prefix="/api/v2")
    temp_app_v2.include_router(entertainment_router_v2, prefix="/api/v2")
    temp_app_v2.include_router(tr_ent_router_v2, prefix="/api/v2")
    temp_app_v2.include_router(tr_acc_router_v2, prefix="/api/v2")
    temp_app_v2.include_router(auth_router_v2, prefix="/api/v2")
    
    # Получаем схему
    schema = get_openapi(
        title="TravelGuide API v2",
        version="2.0.0",
        description="API v2 для системы TravelGuide", 
        routes=temp_app_v2.routes,
    )
    
    # Убеждаемся, что есть обязательные поля
    schema["openapi"] = "3.0.2"
    
    # Исправляем пути - убираем дублирующий /api/v2
    fixed_paths = {}
    for path, methods in schema["paths"].items():
        if path.startswith("/api/v2/api/v2/"):
            # Исправляем дублирование префикса
            fixed_path = path.replace("/api/v2/api/v2/", "/api/v2/")
        elif path.startswith("/api/v2/"):
            fixed_path = path
        else:
            fixed_path = f"/api/v2{path}"
        fixed_paths[fixed_path] = methods
    
    schema["paths"] = fixed_paths
    
    return JSONResponse(schema)

@app.get("/api/v1/docs")
async def swagger_ui_v1():
    """Swagger UI для API v1"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>TravelGuide API v1</title>
        <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3/swagger-ui.css">
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
        <script>
            SwaggerUIBundle({{
                url: '/openapi/v1.json',
                dom_id: '#swagger-ui',
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.SwaggerUIStandalonePreset
                ]
            }});
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html)

@app.get("/api/v2/docs")
async def swagger_ui_v2():
    """Swagger UI для API v2"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>TravelGuide API v2</title>
        <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3/swagger-ui.css">
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
        <script>
            SwaggerUIBundle({{
                url: '/openapi/v2.json',
                dom_id: '#swagger-ui',
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.SwaggerUIStandalonePreset
                ]
            }});
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html)

@app.get("/", response_class=HTMLResponse)
async def serve_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("main.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
async def main_profile_page(request: Request) -> HTMLResponse:
    """Основная страница профиля"""
    return templates.TemplateResponse("profile.html", {"request": request})


@app.exception_handler(Exception)
async def handle_exceptions(request: Request, exc: Exception) -> JSONResponse:
    logger.error(f"Ошибка при обработке запроса: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )

@app.on_event("startup")
async def startup() -> None:
    logger.info("Запуск приложения")
    # await async_init_mongodb()



@app.on_event("shutdown")
async def shutdown() -> None:
    logger.info("Завершение работы приложения")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "OK"}

