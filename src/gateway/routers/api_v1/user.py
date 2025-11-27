# from __future__ import annotations

# import logging

# from typing import Any

# from fastapi import APIRouter
# from fastapi import Depends
# from fastapi import HTTPException
# from fastapi import Request
# from fastapi import status
# from fastapi.responses import HTMLResponse
# from fastapi.responses import JSONResponse
# from fastapi.responses import RedirectResponse
# from fastapi.templating import Jinja2Templates

# from ...service_locator import ServiceLocatorV1
# from ...service_locator import get_service_locator_v1


# logger = logging.getLogger(__name__)

# user_router = APIRouter()

# templates = Jinja2Templates(directory="templates")

# get_sl_dep = Depends(get_service_locator_v1)


# @user_router.get("/profile")
# async def show_profile(request: Request) -> HTMLResponse:
#     try:
#         return templates.TemplateResponse("profile.html", {"request": request})
#     except Exception as e:
#         logger.error("Ошибка при отображении профиля: %s", e)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal server error"
#         )


# @user_router.post("/users", response_class=HTMLResponse)
# async def register_admin(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     try:
#         form_data = await request.form()
#         form_data["is_admin"] = True
        
#         result = await service_locator.get_user_contr().create_new_user(form_data)
        
#         logger.info("Администратор успешно создан: %s", result)
#         return templates.TemplateResponse("user.html", {"request": request})
        
#     except Exception as e:
#         logger.error("Ошибка при создании администратора: %s", e)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal server error"
#         )


# @user_router.put("/users/{user_id}", response_class=HTMLResponse)
# async def update_admin(user_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     try:
#         form_data = await request.form()
        
#         form_data["is_admin"] = True
        
#         result = await service_locator.get_user_contr().update_user(user_id, form_data)
        
#         if not result:
#             raise HTTPException(status_code=404, detail="User not found")
            
#         logger.info("Администратор ID %d успешно обновлен: %s", user_id, result)
#         return RedirectResponse(url="/api/v1/users", status_code=303)
        
#     except HTTPException:
#         raise
#     except Exception as e:
#         logger.error("Ошибка при обновлении администратора: %s", e)
#         raise HTTPException(status_code=400, detail=str(e))


# @user_router.put("/users/{user_id}", response_class=HTMLResponse)
# async def update_user(user_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> Any:
#     try:
#         form_data = await request.form()

#         result = await service_locator.get_user_contr().update_user(user_id, form_data)
        
#         if not result:
#             raise HTTPException(status_code=404, detail="User not found")
            
#         logger.info("Пользователь ID %d успешно обновлен: %s", user_id, result)
#         return RedirectResponse(url="/api/v1/users", status_code=303)
        
#     except HTTPException:
#         raise
#     except Exception as e:
#         logger.error("Ошибка при обновлении пользователя: %s", e)
#         raise HTTPException(status_code=400, detail=str(e))


# @user_router.post("/register")
# async def register_user(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> JSONResponse:
#     try:
#         result = await service_locator.get_user_contr().registrate(request)
#         logger.info("Пользователь успешно зарегистрирован: %s", result)
        
#         return {
#             "access_token": result["access_token"],
#             "user_id": result["user_id"],
#             "message": "Регистрация прошла успешно"
#         }
#     except Exception as e:
#         logger.error("Ошибка при регистрации пользователя: %s", e)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal server error"
#         )


# @user_router.post("/login")
# async def login_user(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
#     try:
#         result = await service_locator.get_user_contr().login(request)
#         logger.info("Результат входа: %s", result)
#         return result
#     except Exception as e:
#         logger.error("Ошибка при входе пользователя: %s", e)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal server error"
#         )


# @user_router.get("/profile_user/{user_id}", response_class=HTMLResponse)
# async def get_user_profile(user_id: int, request: Request, 
#                                         service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     try:
#         profile_data = await service_locator.get_user_contr().get_user_profile(user_id)
#         active_routes = await service_locator.get_route_serv().get_routes_by_user_and_status_and_type(
#             user_id, "В процессе", 'Свои'
#         )
#         completed_routes = await service_locator.get_route_serv().get_routes_by_user_and_status_and_type(
#             user_id, 'Завершен', 'Свои'
#         )
        
#         routes_active_data = []
#         for route in active_routes:
#             transport_cost = route.d_route.cost if route.d_route else 0
#             accommodations = route.travels.accommodations if route.travels else []
#             accommodation_cost = sum(acc.price for acc in accommodations)
#             total_cost = transport_cost + accommodation_cost

#             users = []
#             if route.travels and route.travels.travel_id:
#                 users_raw = await service_locator.get_travel_serv().get_users_by_travel(route.travels.travel_id)
#                 users = [user for user in users_raw if user is not None]

#             route_dict = {
#                 "route_id": route.route_id,
#                 "start_time": route.start_time,
#                 "end_time": route.end_time,
#                 "transport": route.d_route.type_transport if route.d_route else None,
#                 "cost": total_cost,
#                 "destination_city": route.d_route.destination_city.name if route.d_route 
#                                                     and route.d_route.destination_city else None,
#                 "entertainments": route.travels.entertainments if route.travels else [],
#                 "accommodations": route.travels.accommodations if route.travels else [],
#                 "travel_id": route.travels.travel_id if route.travels else None,
#                 "users": users
#             }
#             routes_active_data.append(route_dict)

#         routes_completed_data = []
#         for route in completed_routes:
#             transport_cost = route.d_route.cost if route.d_route else 0
#             accommodations = route.travels.accommodations if route.travels else []
#             accommodation_cost = sum(acc.price for acc in accommodations)
#             total_cost = transport_cost + accommodation_cost

#             users = []
#             if route.travels and route.travels.travel_id:
#                 users_raw = await service_locator.get_travel_serv().get_users_by_travel(route.travels.travel_id)
#                 users = [user for user in users_raw if user is not None]

#             route_dict = {
#                 "route_id": route.route_id,
#                 "start_time": route.start_time,
#                 "end_time": route.end_time,
#                 "transport": route.d_route.type_transport if route.d_route else None,
#                 "cost": total_cost,
#                 "destination_city": route.d_route.destination_city.name if route.d_route 
#                                                     and route.d_route.destination_city else None,
#                 "entertainments": route.travels.entertainments if route.travels else [],
#                 "accommodations": route.travels.accommodations if route.travels else [],
#                 "travel_id": route.travels.travel_id if route.travels else None,
#                 "users": users
#             }
#             routes_completed_data.append(route_dict)

#         return templates.TemplateResponse(
#             "profile_user.html",
#             {
#                 "request": request,
#                 "user": profile_data,
#                 "active_routes": routes_active_data,
#                 "completed_routes": routes_completed_data,
#                 "current_user_id": profile_data["user"]["user_id"]
#             }
#         )
#     except Exception as e:
#         logger.error("Ошибка при получении профиля пользователя: %s", e)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal server error"
#         )


# @user_router.get("/users", response_class=HTMLResponse)
# async def get_all_users(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     try:
#         user_list = await service_locator.get_user_contr().get_all_users()
#         users = user_list.get("users", [])
#         logger.info("Получено %d пользователей", len(users))
#         return templates.TemplateResponse(
#             "user.html",
#             {
#                 "request": request,
#                 "users": users
#             }
#         )
#     except Exception as e:
#         logger.error("Ошибка при получении списка пользователей: %s", e)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal server error"
#         )


# @user_router.delete("/users/{user_id}", response_class=HTMLResponse)
# async def delete_user(user_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
#     try:
#         result = await service_locator.get_user_contr().delete_user(user_id)
#         if not result:
#             raise HTTPException(status_code=404, detail="User not found")
#         logger.info("Пользователь ID %d успешно удален", user_id)
#     except HTTPException:
#         raise
#     except Exception as e:
#         logger.error("Ошибка при удалении пользователя: %s", e)
#         raise HTTPException(status_code=500, detail="Internal server error")
from __future__ import annotations

import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from ...service_locator import ServiceLocatorV1, get_service_locator_v1
from ...shared.schemas.user import UserCreate, UserUpdate

logger = logging.getLogger(__name__)

user_router = APIRouter()
templates = Jinja2Templates(directory="templates")
get_sl_dep = Depends(get_service_locator_v1)


@user_router.get("/profile", response_class=HTMLResponse)
async def show_profile(request: Request) -> HTMLResponse:
    try:
        return templates.TemplateResponse("profile.html", {"request": request})
    except Exception as e:
        logger.error("Ошибка при отображении профиля: %s", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@user_router.post("/users", response_class=HTMLResponse)
async def register_admin(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    try:
        form_data = await request.form()
        user_data = UserCreate(
            password=form_data["password"],
            is_admin=True
        )
        result = await service_locator.get_user_contr().create_new_user(user_data)
        logger.info("Администратор успешно создан: %s", result)
        return templates.TemplateResponse("user.html", {"request": request})
    except Exception as e:
        logger.error("Ошибка при создании администратора: %s", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@user_router.put("/users/{user_id}", response_class=HTMLResponse)
async def update_admin(user_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    try:
        form_data = await request.form()
        user_data = UserUpdate(
            fio=form_data.get("fio"),
            number_password=form_data.get("number_password"),
            email=form_data.get("email"),
            phone_number=form_data.get("phone_number"),
            is_admin=form_data.get("is_admin") == "true"
        )
        result = await service_locator.get_user_contr().update_user(user_id, user_data)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        logger.info("Администратор ID %d успешно обновлен: %s", user_id, result)
        return RedirectResponse(url="/users", status_code=303)
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Ошибка при обновлении администратора: %s", e)
        raise HTTPException(status_code=400, detail=str(e))


@user_router.put("/users/{user_id}/update", response_class=HTMLResponse)
async def update_user(user_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    try:
        form_data = await request.form()
        user_data = UserUpdate(
            fio=form_data.get("fio"),
            number_password=form_data.get("number_password"),
            email=form_data.get("email"),
            phone_number=form_data.get("phone_number"),
            is_admin=form_data.get("is_admin") == "true"
        )
        result = await service_locator.get_user_contr().update_user(user_id, user_data)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        logger.info("Пользователь ID %d успешно обновлен: %s", user_id, result)
        return RedirectResponse(url="/users", status_code=303)
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Ошибка при обновлении пользователя: %s", e)
        raise HTTPException(status_code=400, detail=str(e))


@user_router.post("/register")
async def register_user(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
    try:
        form_data = await request.json()
        user_data = UserCreate(
            password=form_data["password"],
            is_admin=False
        )
        result = await service_locator.get_user_contr().registrate(user_data)
        logger.info("Пользователь успешно зарегистрирован: %s", result)
        return {
            "access_token": result["access_token"],
            "user_id": result["user_id"],
            "message": "Регистрация прошла успешно"
        }
    except Exception as e:
        logger.error("Ошибка при регистрации пользователя: %s", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@user_router.post("/login")
async def login_user(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
    try:
        form_data = await request.json()
        result = await service_locator.get_user_contr().login(form_data["email"], form_data["password"])
        logger.info("Результат входа: %s", result)
        return result
    except Exception as e:
        logger.error("Ошибка при входе пользователя: %s", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@user_router.get("/profile_user/{user_id}", response_class=HTMLResponse)
async def get_user_profile(user_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    try:
        profile_data = await service_locator.get_user_contr().get_user_profile(user_id)
        active_routes = await service_locator.get_route_contr().get_routes_by_user_and_status_and_type(user_id, "В процессе", "Свои")
        completed_routes = await service_locator.get_route_contr().get_routes_by_user_and_status_and_type(user_id, "Завершен", "Свои")
        # Подготовка данных для шаблона
        # ...
        return templates.TemplateResponse("profile_user.html", {"request": request, "user": profile_data})
    except Exception as e:
        logger.error("Ошибка при получении профиля пользователя: %s", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@user_router.get("/users", response_class=HTMLResponse)
async def get_all_users(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    try:
        user_list = await service_locator.get_user_contr().get_all_users()
        return templates.TemplateResponse("user.html", {"request": request, "users": user_list})
    except Exception as e:
        logger.error("Ошибка при получении списка пользователей: %s", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@user_router.delete("/users/{user_id}", response_class=HTMLResponse)
async def delete_user(user_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
    try:
        result = await service_locator.get_user_contr().delete_user(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        logger.info("Пользователь ID %d успешно удален", user_id)
        return RedirectResponse(url="/users", status_code=303)
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Ошибка при удалении пользователя: %s", e)
        raise HTTPException(status_code=500, detail="Internal server error")
