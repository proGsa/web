# from __future__ import annotations

# import logging
# import os

# from fastapi import FastAPI

# # import yaml
# from fastapi import Request
# from fastapi.responses import HTMLResponse
# from fastapi.responses import JSONResponse
# from fastapi.templating import Jinja2Templates
# from .service_locator import get_service_locator_v1, get_service_locator_v2

# # from init_monodb.create_mongodb import async_init_mongodb
# from .logger import setup_logging
# from .routers.api_v1.accommodation import accommodation_router as accommodation_router_v1
# from .routers.api_v1.city import city_router as city_router_v1
# from .routers.api_v1.d_route import d_router as d_router_v1
# from .routers.api_v1.entertainment import entertainment_router as entertainment_router_v1
# from .routers.api_v1.route import router as router_v1
# from .routers.api_v1.travel import travel_router as travel_router_v1
# from .routers.api_v1.user import user_router as user_router_v1
# from .routers.api_v2.accommodation import accommodation_router as accommodation_router_v2
# from .routers.api_v2.auth import router as auth_router_v2
# from .routers.api_v2.city import router as city_router_v2
# from .routers.api_v2.d_route import router as d_router_v2
# from .routers.api_v2.entertainment import entertainment_router as entertainment_router_v2
# from .routers.api_v2.route import router as router_v2
# from .routers.api_v2.travel import router as travel_router_v2
# from .routers.api_v2.travel_acc import router as tr_acc_router_v2
# from .routers.api_v2.travel_ent import router as tr_ent_router_v2
# from .routers.api_v2.user import user_router as user_router_v2
# from fastapi.openapi.utils import get_openapi
# import os
# from fastapi import APIRouter



# templates = Jinja2Templates(directory="templates")

# setup_logging()
# logger = logging.getLogger(__name__)

# DB_MODE = os.getenv("DB_MODE", "write")
# NODE_NAME = os.getenv("NODE_NAME", "app_main")

# app = FastAPI(
#     title="TravelGuide API v1",
#     description="API v1 для системы TravelGuide",
#     version="1.0.0",
#     docs_url="/docs",
#     redoc_url="/redoc"
# )
# mirror_api_v1 = APIRouter(prefix="/mirror/api/v1")
# mirror_api_v2 = APIRouter(prefix="/mirror/api/v2")


# @app.middleware("http")
# async def block_write_on_readonly(request: Request, call_next):
#     if DB_MODE == "read" and request.method in ("POST", "PUT", "PATCH", "DELETE"):
#         raise HTTPException(status_code=403, detail="Write operations not allowed on read-only instance")
#     response = await call_next(request)
#     return response

# app.include_router(router_v1, prefix="/api/v1")
# app.include_router(d_router_v1, prefix="/api/v1")
# app.include_router(city_router_v1, prefix="/api/v1")
# app.include_router(user_router_v1, prefix="/api/v1")
# app.include_router(accommodation_router_v1, prefix="/api/v1")
# app.include_router(travel_router_v1, prefix="/api/v1")
# app.include_router(entertainment_router_v1, prefix="/api/v1")

# app.include_router(router_v2, prefix="/api/v2")
# app.include_router(d_router_v2, prefix="/api/v2")
# app.include_router(city_router_v2, prefix="/api/v2")
# app.include_router(user_router_v2, prefix="/api/v2")
# app.include_router(accommodation_router_v2, prefix="/api/v2")
# app.include_router(travel_router_v2, prefix="/api/v2")
# app.include_router(entertainment_router_v2, prefix="/api/v2")
# app.include_router(tr_ent_router_v2, prefix="/api/v2")
# app.include_router(tr_acc_router_v2, prefix="/api/v2")
# app.include_router(auth_router_v2, prefix="/api/v2")


# mirror_api_v1.include_router(router_v1)
# mirror_api_v1.include_router(d_router_v1)
# mirror_api_v1.include_router(city_router_v1)
# mirror_api_v1.include_router(user_router_v1)
# mirror_api_v1.include_router(accommodation_router_v1)
# mirror_api_v1.include_router(travel_router_v1)
# mirror_api_v1.include_router(entertainment_router_v1)

# mirror_api_v2.include_router(router_v2)
# mirror_api_v2.include_router(d_router_v2)
# mirror_api_v2.include_router(city_router_v2)
# mirror_api_v2.include_router(user_router_v2)
# mirror_api_v2.include_router(accommodation_router_v2)
# mirror_api_v2.include_router(travel_router_v2)
# mirror_api_v2.include_router(entertainment_router_v2)
# mirror_api_v2.include_router(tr_ent_router_v2)
# mirror_api_v2.include_router(tr_acc_router_v2)
# mirror_api_v2.include_router(auth_router_v2)

# app.include_router(mirror_api_v1)
# app.include_router(mirror_api_v2)

# @app.get("/openapi/v1.json")
# async def get_openapi_v1():
#     """Возвращает OpenAPI схему для API v1"""
#     temp_app_v1 = FastAPI(
#         title="TravelGuide API v1",
#         version="1.0.0",
#         description="API v1 для системы TravelGuide",
#         openapi_url="/openapi.json"
#     )
    
#     temp_app_v1.include_router(router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(d_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(city_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(user_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(accommodation_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(travel_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(entertainment_router_v1, prefix="/api/v1")
    
#     schema = get_openapi(
#         title="TravelGuide API v1",
#         version="1.0.0",
#         description="API v1 для системы TravelGuide",
#         routes=temp_app_v1.routes,
#     )
    
#     schema["openapi"] = "3.0.2"
#     fixed_paths = {}
#     for path, methods in schema["paths"].items():
#         if path.startswith("/api/v1/api/v1/"):
#             fixed_path = path.replace("/api/v1/api/v1/", "/api/v1/")
#         elif path.startswith("/api/v1/"):
#             fixed_path = path
#         else:
#             fixed_path = f"/api/v1{path}"
#         fixed_paths[fixed_path] = methods
    
#     schema["paths"] = fixed_paths
    
#     return JSONResponse(schema)


# @app.get("/openapi/v2.json")
# async def get_openapi_v2():
#     """Возвращает OpenAPI схему для API v2"""
#     temp_app_v2 = FastAPI(
#         title="TravelGuide API v2",
#         version="2.0.0", 
#         description="API v2 для системы TravelGuide",
#         openapi_url="/openapi.json"
#     )
    
#     temp_app_v2.include_router(router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(d_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(city_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(user_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(accommodation_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(travel_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(entertainment_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(tr_ent_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(tr_acc_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(auth_router_v2, prefix="/api/v2")
    
#     schema = get_openapi(
#         title="TravelGuide API v2",
#         version="2.0.0",
#         description="API v2 для системы TravelGuide", 
#         routes=temp_app_v2.routes,
#     )
    
#     schema["openapi"] = "3.0.2"
#     fixed_paths = {}
#     for path, methods in schema["paths"].items():
#         if path.startswith("/api/v2/api/v2/"):
#             fixed_path = path.replace("/api/v2/api/v2/", "/api/v2/")
#         elif path.startswith("/api/v2/"):
#             fixed_path = path
#         else:
#             fixed_path = f"/api/v2{path}"
#         fixed_paths[fixed_path] = methods
    
#     schema["paths"] = fixed_paths
    
#     return JSONResponse(schema)


# @app.get("/api/v1/docs")
# async def swagger_ui_v1():
#     """Swagger UI для API v1"""
#     html = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>TravelGuide API v1</title>
#         <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3/swagger-ui.css">
#     </head>
#     <body>
#         <div id="swagger-ui"></div>
#         <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
#         <script>
#             SwaggerUIBundle({
#                 url: '/openapi/v1.json',
#                 dom_id: '#swagger-ui',
#                 presets: [
#                     SwaggerUIBundle.presets.apis,
#                     SwaggerUIBundle.SwaggerUIStandalonePreset
#                 ]
#             });
#         </script>
#     </body>
#     </html>
#     """
#     return HTMLResponse(html)


# @app.get("/api/v2/docs")
# async def swagger_ui_v2():
#     """Swagger UI для API v2"""
#     html = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>TravelGuide API v2</title>
#         <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3/swagger-ui.css">
#     </head>
#     <body>
#         <div id="swagger-ui"></div>
#         <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
#         <script>
#             SwaggerUIBundle({
#                 url: '/openapi/v2.json',
#                 dom_id: '#swagger-ui',
#                 presets: [
#                     SwaggerUIBundle.presets.apis,
#                     SwaggerUIBundle.SwaggerUIStandalonePreset
#                 ]
#             });
#         </script>
#     </body>
#     </html>
#     """
#     return HTMLResponse(html)


# @app.get("/mirror/openapi/v1.json")
# async def mirror_get_openapi_v1():
#     """Возвращает OpenAPI схему для API v1"""
#     temp_app_v1 = FastAPI(
#         title="TravelGuide API v1",
#         version="1.0.0",
#         description="API v1 для системы TravelGuide",
#         openapi_url="/openapi.json"
#     )
    
#     temp_app_v1.include_router(router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(d_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(city_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(user_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(accommodation_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(travel_router_v1, prefix="/api/v1")
#     temp_app_v1.include_router(entertainment_router_v1, prefix="/api/v1")
    
#     schema = get_openapi(
#         title="TravelGuide API v1",
#         version="1.0.0",
#         description="API v1 для системы TravelGuide",
#         routes=temp_app_v1.routes,
#     )
    
#     schema["openapi"] = "3.0.2"
#     fixed_paths = {}
#     for path, methods in schema["paths"].items():
#         if path.startswith("/api/v1/api/v1/"):
#             fixed_path = path.replace("/api/v1/api/v1/", "/api/v1/")
#         elif path.startswith("/api/v1/"):
#             fixed_path = path
#         else:
#             fixed_path = f"/api/v1{path}"
#         fixed_paths[fixed_path] = methods
    
#     schema["paths"] = fixed_paths
    
#     return JSONResponse(schema)


# @app.get("/mirror/openapi/v2.json")
# async def mirror_get_openapi_v2():
#     """Возвращает OpenAPI схему для API v2"""
#     temp_app_v2 = FastAPI(
#         title="TravelGuide API v2",
#         version="2.0.0", 
#         description="API v2 для системы TravelGuide",
#         openapi_url="/openapi.json"
#     )
    
#     temp_app_v2.include_router(router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(d_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(city_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(user_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(accommodation_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(travel_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(entertainment_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(tr_ent_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(tr_acc_router_v2, prefix="/api/v2")
#     temp_app_v2.include_router(auth_router_v2, prefix="/api/v2")
    
#     schema = get_openapi(
#         title="TravelGuide API v2",
#         version="2.0.0",
#         description="API v2 для системы TravelGuide", 
#         routes=temp_app_v2.routes,
#     )
    
#     schema["openapi"] = "3.0.2"
#     fixed_paths = {}
#     for path, methods in schema["paths"].items():
#         if path.startswith("/api/v2/api/v2/"):
#             fixed_path = path.replace("/api/v2/api/v2/", "/api/v2/")
#         elif path.startswith("/api/v2/"):
#             fixed_path = path
#         else:
#             fixed_path = f"/api/v2{path}"
#         fixed_paths[fixed_path] = methods
    
#     schema["paths"] = fixed_paths
    
#     return JSONResponse(schema)


# @app.get("/mirror/api/v1/docs")
# async def mirror_swagger_ui_v1():
#     """Swagger UI для API v1"""
#     html = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>TravelGuide API v1</title>
#         <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3/swagger-ui.css">
#     </head>
#     <body>
#         <div id="swagger-ui"></div>
#         <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
#         <script>
#             SwaggerUIBundle({
#                 url: '/mirror/openapi/v1.json',
#                 dom_id: '#swagger-ui',
#                 presets: [
#                     SwaggerUIBundle.presets.apis,
#                     SwaggerUIBundle.SwaggerUIStandalonePreset
#                 ]
#             });
#         </script>
#     </body>
#     </html>
#     """
#     return HTMLResponse(html)


# @app.get("/mirror/api/v2/docs")
# async def mirror_swagger_ui_v2():
#     """Swagger UI для API v2"""
#     html = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>TravelGuide API v2</title>
#         <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3/swagger-ui.css">
#     </head>
#     <body>
#         <div id="swagger-ui"></div>
#         <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
#         <script>
#             SwaggerUIBundle({
#                 url: '/mirror/openapi/v2.json',
#                 dom_id: '#swagger-ui',
#                 presets: [
#                     SwaggerUIBundle.presets.apis,
#                     SwaggerUIBundle.SwaggerUIStandalonePreset
#                 ]
#             });
#         </script>
#     </body>
#     </html>
#     """
#     return HTMLResponse(html)



# @app.get("/", response_class=HTMLResponse)
# async def serve_main_page(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse("main.html", {"request": request})


# @app.get("/login", response_class=HTMLResponse)
# async def login_page(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse("login.html", {"request": request})


# @app.get("/register", response_class=HTMLResponse)
# async def register_page(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse("register.html", {"request": request})


# @app.get("/profile", response_class=HTMLResponse)
# async def main_profile_page(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse("profile.html", {"request": request})


# @app.exception_handler(Exception)
# async def handle_exceptions(request: Request, exc: Exception) -> JSONResponse:
#     logger.error(f"Ошибка при обработке запроса: {exc}", exc_info=True)
#     return JSONResponse(
#         status_code=500,
#         content={"detail": "Internal server error"},
#     )


# @app.on_event("startup")
# async def startup() -> None:
#     global service_locator_v1, service_locator_v2
#     logger.info("Запуск Gateway приложения")
#     service_locator_v1 = await get_service_locator_v1()
#     service_locator_v2 = await get_service_locator_v2()
#     asyncio.create_task(start_consumer())


# @app.on_event("shutdown")
# async def shutdown() -> None:
#     logger.info("Завершение работы приложения")

# @app.get("/api/v1/health")
# async def health_v1():
#     return {"status": "OK", "node": NODE_NAME}

# @app.get("/api/v2/health")
# async def health_v2():
#     return {"status": "OK", "node": NODE_NAME}

from __future__ import annotations

import asyncio
import logging
import os

from fastapi import FastAPI, APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.openapi.utils import get_openapi

from .service_locator import get_service_locator_v1, get_service_locator_v2
from .logger import setup_logging

# V1 routers
from .routers.api_v1.accommodation import accommodation_router as accommodation_router_v1
from .routers.api_v1.city import city_router as city_router_v1
from .routers.api_v1.d_route import d_router as d_router_v1
from .routers.api_v1.entertainment import entertainment_router as entertainment_router_v1
from .routers.api_v1.route import router as router_v1
from .routers.api_v1.travel import travel_router as travel_router_v1
from .routers.api_v1.user import user_router as user_router_v1

# V2 routers
from .routers.api_v2.accommodation import accommodation_router as accommodation_router_v2
from .routers.api_v2.auth import router as auth_router_v2
from .routers.api_v2.city import router as city_router_v2
from .routers.api_v2.d_route import router as d_router_v2
from .routers.api_v2.entertainment import entertainment_router as entertainment_router_v2
from .routers.api_v2.route import router as router_v2
from .routers.api_v2.travel import router as travel_router_v2
from .routers.api_v2.travel_acc import router as tr_acc_router_v2
from .routers.api_v2.travel_ent import router as tr_ent_router_v2
from .routers.api_v2.user import user_router as user_router_v2

setup_logging()
logger = logging.getLogger(__name__)

DB_MODE = os.getenv("DB_MODE", "write")
NODE_NAME = os.getenv("NODE_NAME", "app_main")

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="TravelGuide Gateway",
    version="2.0.0",
    docs_url=None,
    redoc_url=None,
)

# --- Middleware для запрета записи на readonly ---
@app.middleware("http")
async def block_write_on_readonly(request: Request, call_next):
    if DB_MODE == "read" and request.method in ("POST", "PUT", "PATCH", "DELETE"):
        raise HTTPException(status_code=403, detail="Write operations not allowed on read-only instance")
    return await call_next(request)

# --- API V1 ---
api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(router_v1)
api_v1_router.include_router(d_router_v1)
api_v1_router.include_router(city_router_v1)
api_v1_router.include_router(user_router_v1)
api_v1_router.include_router(accommodation_router_v1)
api_v1_router.include_router(travel_router_v1)
api_v1_router.include_router(entertainment_router_v1)

app.include_router(api_v1_router)

# --- API V2 ---
api_v2_router = APIRouter(prefix="/api/v2")
api_v2_router.include_router(router_v2)
api_v2_router.include_router(d_router_v2)
api_v2_router.include_router(city_router_v2)
api_v2_router.include_router(user_router_v2)
api_v2_router.include_router(accommodation_router_v2)
api_v2_router.include_router(travel_router_v2)
api_v2_router.include_router(entertainment_router_v2)
api_v2_router.include_router(tr_ent_router_v2)
api_v2_router.include_router(tr_acc_router_v2)
api_v2_router.include_router(auth_router_v2)

app.include_router(api_v2_router)

# --- Swagger/OpenAPI ---
def create_openapi(app: FastAPI, title: str, version: str, prefix: str):
    temp_app = FastAPI(title=title, version=version, openapi_url="/openapi.json")
    for router in app.router.routes:
        temp_app.routes.append(router)
    schema = get_openapi(title=title, version=version, routes=app.routes, description=f"{title} OpenAPI")
    # фиксируем дублирующиеся префиксы
    fixed_paths = {}
    for path, methods in schema["paths"].items():
        if path.startswith(prefix + prefix):
            fixed_paths[path.replace(prefix + prefix, prefix)] = methods
        else:
            fixed_paths[path] = methods
    schema["paths"] = fixed_paths
    return schema

# @app.get("/openapi/v1.json")
# async def openapi_v1():
#     return JSONResponse(create_openapi(app, "TravelGuide API v1", "1.0.0", "/api/v1"))

# @app.get("/openapi/v2.json")
# async def openapi_v2():
#     return JSONResponse(create_openapi(app, "TravelGuide API v2", "2.0.0", "/api/v2"))

# --- Страницы ---
@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

# --- Exception handler ---
@app.exception_handler(Exception)
async def handle_exceptions(request: Request, exc: Exception):
    logger.error("Ошибка при обработке запроса", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})

# --- Health ---
@app.get("/api/v1/health")
async def health_v1():
    return {"status": "OK", "node": NODE_NAME}

@app.get("/api/v2/health")
async def health_v2():
    return {"status": "OK", "node": NODE_NAME}

# --- Startup/Shutdown ---
service_locator_v1: any = None
service_locator_v2: any = None

@app.on_event("startup")
async def startup():
    global service_locator_v1, service_locator_v2
    logger.info("Запуск Gateway приложения")
    service_locator_v1 = await get_service_locator_v1()
    service_locator_v2 = await get_service_locator_v2()

@app.on_event("shutdown")
async def shutdown():
    logger.info("Завершение работы Gateway приложения")

from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

# def get_openapi_schema(app: FastAPI, title: str, version: str, routers: list[APIRouter]):
#     temp_app = FastAPI(title=title, version=version)
#     for router in routers:
#         temp_app.include_router(router)
#     schema = get_openapi(
#         title=title,
#         version=version,
#         routes=temp_app.routes,
#         description=f"{title} OpenAPI"
#     )
#     schema["openapi"] = "3.0.2"
#     return schema

# @app.get("/openapi/v1.json")
# async def openapi_v1():
#     routers_v1 = [router_v1, d_router_v1, city_router_v1, user_router_v1,
#                   accommodation_router_v1, travel_router_v1, entertainment_router_v1]
#     schema = get_openapi_schema(app, "TravelGuide API v1", "1.0.0", routers_v1)
#     return JSONResponse(schema)

# @app.get("/openapi/v2.json")
# async def openapi_v2():
#     routers_v2 = [router_v2, d_router_v2, city_router_v2, user_router_v2,
#                   accommodation_router_v2, travel_router_v2, entertainment_router_v2,
#                   tr_ent_router_v2, tr_acc_router_v2, auth_router_v2]
#     schema = get_openapi_schema(app, "TravelGuide API v2", "2.0.0", routers_v2)
#     return JSONResponse(schema)


# def swagger_ui_html(openapi_url: str, title: str) -> str:
#     """Генерирует HTML для Swagger UI"""
#     return f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>{title}</title>
#         <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3/swagger-ui.css">
#     </head>
#     <body>
#         <div id="swagger-ui"></div>
#         <script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
#         <script>
#             SwaggerUIBundle({{
#                 url: '{openapi_url}',
#                 dom_id: '#swagger-ui',
#                 presets: [
#                     SwaggerUIBundle.presets.apis,
#                     SwaggerUIBundle.SwaggerUIStandalonePreset
#                 ]
#             }});
#         </script>
#     </body>
#     </html>
#     """

# @app.get("/api/v1/docs", response_class=HTMLResponse)
# async def swagger_ui_v1():
#     return HTMLResponse(swagger_ui_html("/openapi/v1.json", "TravelGuide API v1"))

# @app.get("/api/v2/docs", response_class=HTMLResponse)
# async def swagger_ui_v2():
#     return HTMLResponse(swagger_ui_html("/openapi/v2.json", "TravelGuide API v2"))

@app.get("/openapi/v1.json")
async def get_openapi_v1():
    """Возвращает OpenAPI схему для API v1"""
    temp_app_v1 = FastAPI(
        title="TravelGuide API v1",
        version="1.0.0",
        description="API v1 для системы TravelGuide",
        openapi_url="/openapi.json"
    )
    
    temp_app_v1.include_router(router_v1, prefix="/api/v1")
    temp_app_v1.include_router(d_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(city_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(user_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(accommodation_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(travel_router_v1, prefix="/api/v1")
    temp_app_v1.include_router(entertainment_router_v1, prefix="/api/v1")
    
    schema = get_openapi(
        title="TravelGuide API v1",
        version="1.0.0",
        description="API v1 для системы TravelGuide",
        routes=temp_app_v1.routes,
    )
    
    schema["openapi"] = "3.0.2"
    fixed_paths = {}
    for path, methods in schema["paths"].items():
        if path.startswith("/api/v1/api/v1/"):
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
    temp_app_v2 = FastAPI(
        title="TravelGuide API v2",
        version="2.0.0", 
        description="API v2 для системы TravelGuide",
        openapi_url="/openapi.json"
    )
    
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
    
    schema = get_openapi(
        title="TravelGuide API v2",
        version="2.0.0",
        description="API v2 для системы TravelGuide", 
        routes=temp_app_v2.routes,
    )
    
    schema["openapi"] = "3.0.2"
    fixed_paths = {}
    for path, methods in schema["paths"].items():
        if path.startswith("/api/v2/api/v2/"):
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
    html = """
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
            SwaggerUIBundle({
                url: '/openapi/v1.json',
                dom_id: '#swagger-ui',
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.SwaggerUIStandalonePreset
                ]
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html)


@app.get("/api/v2/docs")
async def swagger_ui_v2():
    """Swagger UI для API v2"""
    html = """
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
            SwaggerUIBundle({
                url: '/openapi/v2.json',
                dom_id: '#swagger-ui',
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.SwaggerUIStandalonePreset
                ]
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html)

