# from __future__ import annotations

# import logging

# from datetime import datetime
# from typing import Any

# from fastapi import APIRouter
# from fastapi import Depends
# from fastapi import HTTPException
# from fastapi import Request
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import HTMLResponse
# from fastapi.responses import RedirectResponse
# from fastapi.responses import Response
# from fastapi.templating import Jinja2Templates

# from ...service_locator import ServiceLocatorV1
# from ...service_locator import get_service_locator_v1


# logger = logging.getLogger(__name__)

# router = APIRouter()
# templates = Jinja2Templates(directory="templates")
# get_sl_dep = Depends(get_service_locator_v1)


# @router.post("/routes", response_class=HTMLResponse)
# async def create_route(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     result = await service_locator.get_route_contr().create_new_route(request)
#     logger.info("Маршрут успешно создан: %s", result)
#     return templates.TemplateResponse("route.html", {"request": request})


# # @router.post("/routes/new", response_class=HTMLResponse)
# # async def create_route_user(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> JSONResponse:
# #     logger.info("create_route_user\n")
# #     result = await service_locator.get_route_contr().create_new_route_user(request)
# #     logger.info("Маршрут успешно создан: %s", result)
# #     return JSONResponse(content=result)


# # @router.get("/routes/new", response_class=HTMLResponse)
# # async def get_route_page(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
# #     entertainments = await service_locator.get_ent_serv().get_list()
# #     accommodations = await service_locator.get_acc_serv().get_list()
# #     cities = await service_locator.get_city_serv().get_all_cities()
# #     return templates.TemplateResponse(
# #         "new.html",
# #         {
# #             "request": request,
# #             "entertainments": entertainments,
# #             "accommodations": accommodations,
# #             "cities": cities 
# #         }
# #     )


# @router.get("/routes", response_class=HTMLResponse)
# async def get_all_route(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     route_list = await service_locator.get_route_contr().get_all_routes()
#     routes = route_list.get("routes", [])
#     user = None

#     for route in routes:
#         route['start_time'] = datetime.fromisoformat(route['start_time'])
#         route['end_time'] = datetime.fromisoformat(route['end_time'])
        
#         if route.get('travel'):
#             travel = route['travel']
#             serialized_ents = []
#             for ent in travel['entertainments']:
#                 city_name = None
#                 if hasattr(ent.get('city'), 'name'):
#                     city_name = ent['city'].name
#                 elif isinstance(ent.get('city'), dict):
#                     city_name = ent['city'].get('name', 'Не указан')
#                 elif 'city_id' in ent:
#                     city = await service_locator.get_city_serv().get_by_id(ent['city_id'])
#                     city_name = city.name if city else 'Не указан'
#                 else:
#                     city_name = 'Не указан'

#                 serialized_ents.append({
#                     "id": ent.get("id"),
#                     "event_name": ent.get("event_name"),
#                     "address": ent.get("address"),
#                     "duration": ent.get("duration"),
#                     "event_time": ent.get("event_time"),
#                     "city_name": city_name
#                 })
#             travel['entertainments'] = serialized_ents
        
#         if 'accommodations' in travel:
#             serialized_accs = []
#             for acc in travel['accommodations']:
#                 city_name = None
#                 if hasattr(acc.get('city'), 'name'):
#                     city_name = acc['city'].name
#                 elif isinstance(acc.get('city'), dict):
#                     city_name = acc['city'].get('name', 'Не указан')
#                 elif 'city_id' in acc:
#                     city = await service_locator.get_city_serv().get_by_id(acc['city_id'])
#                     city_name = city.name if city else 'Не указан'
#                 else:
#                     city_name = 'Не указан'

#                 serialized_accs.append({
#                     "id": acc.get("id"),
#                     "name": acc.get("name"),
#                     "type": acc.get("type"),
#                     "address": acc.get("address"),
#                     "price": acc.get("price"),
#                     "rating": acc.get("rating"),
#                     "check_in": acc.get("check_in"),
#                     "check_out": acc.get("check_out"),
#                     "city_name": city_name
#                 })
#             travel['accommodations'] = serialized_accs

#     return templates.TemplateResponse(
#         "route.html",
#         {
#             "request": request,
#             "routes": routes,
#             "travels": await service_locator.get_travel_serv().get_all_travels(),
#             "d_routes": await service_locator.get_d_route_serv().get_list(),
#             "user": user
#         }
#     )


# @router.put("/routes/{route_id}", response_class=HTMLResponse)
# async def update_route(route_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     result = await service_locator.get_route_contr().update_route(route_id, request)
#     logger.info("Маршрут ID %d успешно обновлен: %s", route_id, result)
#     return templates.TemplateResponse("route.html", {"request": request})


# @router.post("/routes/{route_id}", response_class=HTMLResponse)
# async def delete_route(route_id: int, request: Request,
#                                         service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
#     result = await service_locator.get_route_contr().delete_route(route_id)
#     logger.info("Маршрут ID %d успешно удален: %s", route_id, result)
#     return RedirectResponse(url="/route.html", status_code=303)


# @router.get("/routes/{route_id}/edit")
# async def edit_page(route_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> Response:
#     route = await service_locator.get_route_serv().get_by_id(route_id)
#     if not route:
#         logger.error("Маршрут с таким ID %s не найден", route_id)
#         return HTMLResponse(content="<h1>Пользователь не найден</h1>", status_code=404)
#     accommodations = route.travels.accommodations if route.travels else []
#     accommodation_cost = sum(acc.price for acc in accommodations)
#     total_cost = accommodation_cost
#     cities_list = await service_locator.get_city_contr().get_all_cities()
#     cities = cities_list.get("cities", [])
#     route_parts = await service_locator.get_route_contr().get_route_parts(route_id)
#     for r in route_parts:
#         total_cost += r["price"]
#     route_dict = {
#         "route_id": route.route_id,
#         "d_route_id": route.d_route.d_route_id if route.d_route else None,
#         "start_time": route.start_time,
#         "end_time": route.end_time,
#         "transport": ", ".join({part['transport'] for part in route_parts}) if route_parts else None,
#         "cost": total_cost,
#         "destination_city": route.d_route.destination_city.name if route.d_route 
#                                             and route.d_route.destination_city else None,
#         "entertainments": route.travels.entertainments if route.travels else [],
#         "accommodations": route.travels.accommodations if route.travels else [],
#         "travel_id": route.travels.travel_id if route.travels else None
#     }
#     logger.info(route_dict["d_route_id"])
#     return templates.TemplateResponse(
#         "edit.html",
#         {
#             "request": request,
#             "route": route_dict,
#             "route_parts": route_parts,
#             "cities": cities
#         }
#     )


# @router.patch("/routes/{route_id}/change_transport")
# async def change_transport(route_id: int, request: Request, 
#                                             service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
    
#     result = await service_locator.get_route_contr().change_transport(route_id, request)
#     logger.info("Транспорт в маршруте успешно изменен: %s", result)
#     return {"route_id": route_id, "d_route_id": result["d_route_id"]}


# @router.delete("/routes/{route_id}/delete_city")
# async def delete_city_from_route(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
#     result = await service_locator.get_route_contr().delete_city_from_route(request)
#     logger.info("Город успешно удален из маршрута: %s", result)
#     return result


# @router.post("/routes/{route_id}/add_city")
# async def add_new_city(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> None:
#     result = await service_locator.get_route_contr().add_new_city(request)
#     logger.info("Город успешно добавлен в маршрут: %s", result)


# @router.patch("/routes/{route_id}/extend")
# async def api_change_travel_duration(route_id: int, request: Request, 
#     service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
#     try:
#         result = await service_locator.get_route_contr().change_travel_duration(route_id, request)
#         if "error" in result:
#             raise HTTPException(status_code=400, detail=result["error"])
        
#         logger.info("Путешествие успешно продлено: %s", result)
#         return result
#     except HTTPException:
#         raise
#     except Exception as e:
#         logger.error("Ошибка в API продления маршрута: %s", str(e), exc_info=True)
#         raise HTTPException(status_code=500, detail=str(e))


# @router.get("/routes/tours", response_class=HTMLResponse)
# async def get_tours(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     routes = await service_locator.get_route_serv().get_routes_by_type('Авторские')
#     routes_data = []
    
#     for route in routes:
#         transport_cost = route.d_route.cost if hasattr(route, 'd_route') and route.d_route else 0
#         accommodation_cost = 0
#         if hasattr(route, 'travels') and route.travels and hasattr(route.travels, 'accommodations'):
#             accommodations = route.travels.accommodations or []
#             accommodation_cost = sum(getattr(acc, 'price', 0) for acc in accommodations)
        
#         accommodations_list = []
#         if hasattr(route, 'travels') and route.travels and hasattr(route.travels, 'accommodations'):
#             for acc in getattr(route.travels, 'accommodations', []):
#                 logger.info("acc: %s", acc)
#                 check_in = getattr(acc, 'check_in', None)
#                 check_out = getattr(acc, 'check_out', None)
                
#                 acc_data = {
#                     "name": getattr(acc, 'name', 'Не указано'),
#                     "type": getattr(acc, 'type', 'Не указан'),
#                     "address": getattr(acc, 'address', 'Не указан'),
#                     "check_in": check_in.strftime('%d.%m.%Y') if check_in else '',
#                     "check_out": check_out.strftime('%d.%m.%Y') if check_out else '',
#                     "rating": getattr(acc, 'rating', 0),
#                     "price": getattr(acc, 'price', 0)
#                 }
#                 accommodations_list.append(acc_data)
        
#         entertainments = []
#         if hasattr(route, 'travels') and route.travels and hasattr(route.travels, 'entertainments'):
#             for ent in getattr(route.travels, 'entertainments', []):
#                 date = getattr(ent, 'event_time', None)
                
#                 ent_data = {
#                     "name": getattr(ent, 'event_name', 'Не указано'),
#                     "address": getattr(ent, 'address', 'Не указан'),
#                     "date": date.strftime('%d.%m.%Y') if date else '',
#                     "duration": getattr(ent, 'duration', 'Не указана'),
#                 }
#                 entertainments.append(ent_data)
        
#         start_time = getattr(route, 'start_time', None)
#         end_time = getattr(route, 'end_time', None)
        
#         route_dict = {
#             "route_id": getattr(route, 'route_id', 0),
#             "departure_city": getattr(getattr(getattr(route, 'd_route', None), 
#                                                       'departure_city', None), 'name', 'Не указан'),
#             "destination_city": getattr(getattr(getattr(route, 'd_route', None), 
#                                                         'destination_city', None), 'name', 'Не указан'),
#             "transport": getattr(getattr(route, 'd_route', None), 'type_transport', 'Не указан'),
#             "start_time": start_time.strftime('%d.%m.%Y') if start_time else '',
#             "end_time": end_time.strftime('%d.%m.%Y') if end_time else '',
#             "cost": transport_cost + accommodation_cost,
#             "accommodations": accommodations_list or [],
#             "entertainments": entertainments or []
#         }
#         logger.info(f"Сформированные данные маршрута: {route_dict}")
#         routes_data.append(route_dict)
    
#     return templates.TemplateResponse(
#         "tours.html",
#         {
#             "request": request,
#             "routes": jsonable_encoder(routes_data)
#         }
#     )

    
# @router.get("/routes/recommended", response_class=HTMLResponse)
# async def get_recommended_tours(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     routes = await service_locator.get_route_serv().get_routes_by_type('Рекомендованные')
#     routes_data = []
    
#     for route in routes:
#         transport_cost = route.d_route.cost if hasattr(route, 'd_route') and route.d_route else 0
#         accommodation_cost = 0
#         if hasattr(route, 'travels') and route.travels and hasattr(route.travels, 'accommodations'):
#             accommodations = route.travels.accommodations or []
#             accommodation_cost = sum(getattr(acc, 'price', 0) for acc in accommodations)
#         if hasattr(route, 'travels') and route.travels and hasattr(route.travels, 'users'):
#             user_ids = [u.user_id for u in route.travels.users if hasattr(u, 'user_id')]
#         accommodations_list = []
#         if hasattr(route, 'travels') and route.travels and hasattr(route.travels, 'accommodations'):
#             for acc in getattr(route.travels, 'accommodations', []):
#                 logger.info("acc: %s", acc)
#                 check_in = getattr(acc, 'check_in', None)
#                 check_out = getattr(acc, 'check_out', None)
                
#                 acc_data = {
#                     "name": getattr(acc, 'name', 'Не указано'),
#                     "type": getattr(acc, 'type', 'Не указан'),
#                     "address": getattr(acc, 'address', 'Не указан'),
#                     "check_in": check_in.strftime('%d.%m.%Y') if check_in else '',
#                     "check_out": check_out.strftime('%d.%m.%Y') if check_out else '',
#                     "rating": getattr(acc, 'rating', 0),
#                     "price": getattr(acc, 'price', 0)
#                 }
#                 accommodations_list.append(acc_data)
        
#         entertainments = []
#         if hasattr(route, 'travels') and route.travels and hasattr(route.travels, 'entertainments'):
#             for ent in getattr(route.travels, 'entertainments', []):
#                 date = getattr(ent, 'event_time', None)
                
#                 ent_data = {
#                     "name": getattr(ent, 'event_name', 'Не указано'),
#                     "address": getattr(ent, 'address', 'Не указан'),
#                     "date": date.strftime('%d.%m.%Y') if date else '',
#                     "duration": getattr(ent, 'duration', 'Не указана'),
#                 }
#                 entertainments.append(ent_data)
        
#         start_time = getattr(route, 'start_time', None)
#         end_time = getattr(route, 'end_time', None)
        
#         route_dict = {
#             "route_id": getattr(route, 'route_id', 0),
#             "departure_city": getattr(getattr(getattr(route, 'd_route', None), 
#                                                       'departure_city', None), 'name', 'Не указан'),
#             "destination_city": getattr(getattr(getattr(route, 'd_route', None), 
#                                                         'destination_city', None), 'name', 'Не указан'),
#             "transport": getattr(getattr(route, 'd_route', None), 'type_transport', 'Не указан'),
#             "start_time": start_time.strftime('%d.%m.%Y') if start_time else '',
#             "end_time": end_time.strftime('%d.%m.%Y') if end_time else '',
#             "cost": transport_cost + accommodation_cost,
#             "accommodations": accommodations_list or [],
#             "entertainments": entertainments or [],
#             "user_ids": user_ids
#         }
#         logger.info(f"Сформированные данные маршрута: {route_dict}")
#         routes_data.append(route_dict)
    
#     return templates.TemplateResponse(
#         "recommended.html",
#         {
#             "request": request,
#             "routes": jsonable_encoder(routes_data)
#         }
#     )


# @router.post("/routes/{route_id}/join")
# async def join_route(route_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
#     logger.info("Присоединяемся к маршруту %d ID", route_id)
#     return await service_locator.get_route_contr().join_to_trip(route_id, request)
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates

from ...service_locator import ServiceLocatorV1, get_service_locator_v1
from ...shared.schemas.route import RouteCreate, RouteUpdate

logger = logging.getLogger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory="templates")
get_sl_dep = Depends(get_service_locator_v1)


@router.post("/routes", response_class=HTMLResponse)
async def create_route(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    form = await request.form()
    route_data = RouteCreate(
        d_route_id=int(form["d_route_id"]),
        travel_id=int(form["travel_id"]),
        start_time=datetime.fromisoformat(form["start_time"]),
        end_time=datetime.fromisoformat(form["end_time"]),
        type=form.get("type", "")
    )
    result = await service_locator.get_route_contr().create_new_route(route_data)
    logger.info("Маршрут успешно создан: %s", result)
    return templates.TemplateResponse("route.html", {"request": request})


@router.get("/routes", response_class=HTMLResponse)
async def get_all_routes(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    route_list = await service_locator.get_route_contr().get_all_routes()
    routes = route_list  # список DTO
    user = None

    for route in routes:
        route.start_time = datetime.fromisoformat(route.start_time)
        route.end_time = datetime.fromisoformat(route.end_time)

        # Сериализация развлечений
        if route.travels and route.travels.entertainments:
            serialized_ents = []
            for ent in route.travels.entertainments:
                city_name = ent.city.name if ent.city else 'Не указан'
                serialized_ents.append({
                    "id": ent.entertainment_id,
                    "event_name": ent.event_name,
                    "address": ent.address,
                    "duration": ent.duration,
                    "event_time": ent.event_time,
                    "city_name": city_name
                })
            route.travels.entertainments = serialized_ents

        # Сериализация проживания
        if route.travels and route.travels.accommodations:
            serialized_accs = []
            for acc in route.travels.accommodations:
                city_name = acc.city.name if acc.city else 'Не указан'
                serialized_accs.append({
                    "id": acc.accommodation_id,
                    "name": acc.name,
                    "type": acc.type,
                    "address": acc.address,
                    "price": acc.price,
                    "rating": acc.rating,
                    "check_in": acc.check_in,
                    "check_out": acc.check_out,
                    "city_name": city_name
                })
            route.travels.accommodations = serialized_accs

    return templates.TemplateResponse(
        "route.html",
        {
            "request": request,
            "routes": [r.dict() for r in routes],
            "travels": [t.dict() for t in await service_locator.get_travel_contr().get_all_travels()],
            "d_routes": [d.dict() for d in await service_locator.get_d_route_contr().get_list()],
            "user": user
        }
    )


@router.put("/routes/{route_id}", response_class=HTMLResponse)
async def update_route(route_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    form = await request.form()
    route_data = RouteUpdate(
        d_route_id=int(form["d_route_id"]),
        travel_id=int(form["travel_id"]),
        start_time=datetime.fromisoformat(form["start_time"]),
        end_time=datetime.fromisoformat(form["end_time"]),
        type=form.get("type", "")
    )
    result = await service_locator.get_route_contr().update_route(route_id, route_data)
    logger.info("Маршрут ID %d успешно обновлен: %s", route_id, result)
    return templates.TemplateResponse("route.html", {"request": request})


@router.post("/routes/{route_id}", response_class=HTMLResponse)
async def delete_route(route_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
    await service_locator.get_route_contr().delete_route(route_id)
    logger.info("Маршрут ID %d успешно удален", route_id)
    return RedirectResponse(url="/route.html", status_code=303)


@router.get("/routes/{route_id}/edit")
async def edit_route_page(route_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> Response:
    route = await service_locator.get_route_contr().get_route_by_id(route_id)
    if not route:
        logger.error("Маршрут с ID %d не найден", route_id)
        return HTMLResponse(content="<h1>Маршрут не найден</h1>", status_code=404)

    accommodations = route.travels.accommodations if route.travels else []
    total_cost = sum(acc.price for acc in accommodations) if accommodations else 0
    route_parts = await service_locator.get_route_contr().get_route_parts(route_id)
    total_cost += sum(part["price"] for part in route_parts)

    cities = [c.dict() for c in await service_locator.get_city_contr().get_all_cities()]

    route_dict = {
        "route_id": route.route_id,
        "d_route_id": route.d_route.d_route_id if route.d_route else None,
        "start_time": route.start_time,
        "end_time": route.end_time,
        "transport": ", ".join({part['transport'] for part in route_parts}) if route_parts else None,
        "cost": total_cost,
        "destination_city": route.d_route.destination_city.name if route.d_route and route.d_route.destination_city else None,
        "entertainments": route.travels.entertainments if route.travels else [],
        "accommodations": accommodations,
        "travel_id": route.travels.travel_id if route.travels else None
    }

    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "route": route_dict, "route_parts": route_parts, "cities": cities}
    )


@router.patch("/routes/{route_id}/change_transport")
async def change_transport(route_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
    form = await request.form()
    transport = form.get("transport", "")
    result = await service_locator.get_route_contr().change_transport(route_id, transport)
    logger.info("Транспорт в маршруте успешно изменен: %s", result)
    return {"route_id": route_id, "d_route_id": result.d_route_id}


@router.delete("/routes/{route_id}/delete_city")
async def delete_city_from_route(route_id: int, city_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
    result = await service_locator.get_route_contr().delete_city_from_route(route_id, city_id)
    logger.info("Город ID %d успешно удален из маршрута ID %d", city_id, route_id)
    return result


@router.post("/routes/{route_id}/add_city")
async def add_new_city(route_id: int, city_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
    result = await service_locator.get_route_contr().add_new_city(route_id, city_id)
    logger.info("Город ID %d успешно добавлен в маршрут ID %d", city_id, route_id)
    return result


@router.patch("/routes/{route_id}/extend")
async def extend_travel_duration(route_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
    form = await request.form()
    extra_days = int(form.get("extra_days", 0))
    result = await service_locator.get_route_contr().extend_travel_duration(route_id, extra_days)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    logger.info("Путешествие успешно продлено: %s", result)
    return result
