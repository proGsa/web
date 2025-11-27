# from __future__ import annotations

# import logging

# from datetime import datetime

# from fastapi import APIRouter
# from fastapi import Depends
# from fastapi import Request
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import HTMLResponse
# from fastapi.responses import RedirectResponse
# from fastapi.responses import Response
# from fastapi.templating import Jinja2Templates

# from ...service_locator import ServiceLocatorV1
# from ...service_locator import get_service_locator_v1


# logger = logging.getLogger(__name__)

# travel_router = APIRouter()
# templates = Jinja2Templates(directory="templates")
# get_sl_dep = Depends(get_service_locator_v1)


# @travel_router.post("/travels", response_class=HTMLResponse)
# async def create_travel(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     result = await service_locator.get_travel_contr().create_new_travel(request)
#     logger.info("Путешествие успешно создано: %s", result)
#     return templates.TemplateResponse("travel.html", {"request": request})


# @travel_router.get("/travels", response_class=HTMLResponse)
# async def get_all_travels(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     travel_list = await service_locator.get_travel_contr().get_all_travels()
#     travels = travel_list.get("travels", [])
#     logger.info("Получено %d путешествий", len(travels))
    
#     user_id = travels[0]["users"][0]["user_id"] if travels and travels[0]["users"] else None
#     user = None
#     if user_id is not None:
#         logger.info("Получение данных пользователя ID %s", user_id)
#         user = await service_locator.get_user_contr().get_user_profile(user_id)
#     users = await service_locator.get_user_contr().get_all_users()
#     all_entertainments = await service_locator.get_ent_contr().get_all_entertainment()
#     all_accommodations = await service_locator.get_acc_contr().get_all_accommodation()

#     entertainments = travel_list.get("entertainments", [])
#     for e in all_entertainments["entertainments"]:
#         e['event_time'] = datetime.fromisoformat(e['event_time'])
#     for e in entertainments:
#         e['event_time'] = datetime.fromisoformat(e['event_time'])
#     accommodations = travel_list.get("accommodations", [])
#     for a in accommodations:
#         a['check_in'] = datetime.fromisoformat(a['check_in'])
#         a['check_out'] = datetime.fromisoformat(a['check_out'])
#     for a in all_accommodations["accommodations"]:
#         a['check_in'] = datetime.fromisoformat(a['check_in'])
#         a['check_out'] = datetime.fromisoformat(a['check_out'])

#     for travel in travels:
#         for entertainment in travel["entertainments"]:
#             if isinstance(entertainment.get("city"), dict):
#                 entertainment["city_name"] = entertainment["city"].get("name", "Undefined")
#             elif hasattr(entertainment.get("city"), "name"): 
#                 entertainment["city_name"] = entertainment["city"].name
#             else:
#                 entertainment["city_name"] = "Undefined"

#         # Для размещений
#         for accommodation in travel["accommodations"]:
#             if isinstance(accommodation.get("city"), dict):
#                 accommodation["city_name"] = accommodation["city"].get("name", "Undefined")
#             elif hasattr(accommodation.get("city"), "name"):  # Если это объект модели
#                 accommodation["city_name"] = accommodation["city"].name
#             else:
#                 accommodation["city_name"] = "Undefined"

#     logger.info("Данные о развлечениях и проживании обработаны")
#     return templates.TemplateResponse(
#         "travel.html",
#         {
#             "request": request, 
#             "travels": jsonable_encoder(travels),
#             "user": user['user'] if user else None,
#             "entertainments": entertainments,
#             "accommodations": accommodations,
#             "users": users["users"],
#             "all_entertainments": all_entertainments["entertainments"],
#             "all_accommodations": all_accommodations["accommodations"]
#         },
#     )


# @travel_router.put("/travels/{travel_id}", response_class=HTMLResponse)
# async def update_travel(travel_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     result = await service_locator.get_travel_contr().update_travel(travel_id, request)
#     logger.info("Путешествие ID %d успешно обновлено: %s", travel_id, result)
#     return templates.TemplateResponse("travel.html", {"request": request})


# @travel_router.delete("/travels/{travel_id}", response_class=HTMLResponse)
# async def delete_travel(travel_id: int, request: Request, 
#                                             service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
#     result = await service_locator.get_travel_contr().delete_travel(travel_id)
#     logger.info("Путешествие ID %d успешно удалено: %s", travel_id, result)
#     return RedirectResponse(url="/travel.html", status_code=303)


# @travel_router.patch("/travels/{travel_id}")
# async def complete_travel(travel_id: int, request: Request, 
#                                                 service_locator: ServiceLocatorV1 = get_sl_dep) -> Response:
#     result = await service_locator.get_travel_contr().complete_travel(travel_id)
#     logger.info("Путешествие успешно завершено: %s", result)
#     travel = await service_locator.get_travel_contr().get_travel_details(travel_id)
#     user_id = travel['travel'].get("user_id")
#     if not user_id:
#         logger.error("Не удалось получить user_id для путешествия ID %d", travel_id)
#         return HTMLResponse(content="<h1>Пользователь не найден</h1>", status_code=404)
#     return RedirectResponse(url=f"/profile_user/{user_id}", status_code=303)
from __future__ import annotations

import logging
from datetime import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates

from ...service_locator import ServiceLocatorV1, get_service_locator_v1
from ...shared.schemas.travel import TravelCreate, TravelUpdate

logger = logging.getLogger(__name__)

travel_router = APIRouter()
templates = Jinja2Templates(directory="templates")
get_sl_dep = Depends(get_service_locator_v1)


@travel_router.post("/travels", response_class=HTMLResponse)
async def create_travel(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    form = await request.form()
    travel_data = TravelCreate(
        status=form["status"],
        user_id=form["user_id"],
        entertainment_ids=form["entertainment_ids"],
        accommodation_ids=form["accommodation_ids"],
    )
    result = await service_locator.get_travel_contr().create_new_travel(travel_data)
    logger.info("Путешествие успешно создано: %s", result)
    return templates.TemplateResponse("travel.html", {"request": request})


@travel_router.get("/travels", response_class=HTMLResponse)
async def get_all_travels(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    travels = await service_locator.get_travel_contr().get_all_travels()
    travels_list = [t.dict() for t in travels]

    # Получение первого пользователя для отображения, если есть
    user = None
    if travels_list and travels_list[0].get("user_id"):
        user = await service_locator.get_user_contr().get_user_profile(travels_list[0]["user_id"])
        user = user.dict() if user else None

    users = await service_locator.get_user_contr().get_all_users()
    users_list = users if isinstance(users, list) else []

    all_entertainments = await service_locator.get_ent_contr().get_all_entertainment()
    all_entertainments_list = [e.dict() for e in all_entertainments]

    all_accommodations = await service_locator.get_acc_contr().get_all_accommodations()
    all_accommodations_list = [a.dict() for a in all_accommodations]

    # Обработка дат
    for t in travels_list:
        for ent in t.get("entertainments", []):
            ent["event_time"] = datetime.fromisoformat(ent["event_time"])
            ent["city_name"] = ent.get("city", {}).get("name", "Undefined")
        for acc in t.get("accommodations", []):
            acc["check_in"] = datetime.fromisoformat(acc["check_in"])
            acc["check_out"] = datetime.fromisoformat(acc["check_out"])
            acc["city_name"] = acc.get("city", {}).get("name", "Undefined")

    logger.info("Данные о путешествиях, развлечениях и проживании обработаны")

    return templates.TemplateResponse(
        "travel.html",
        {
            "request": request,
            "travels": jsonable_encoder(travels_list),
            "user": user,
            "users": users_list,
            "entertainments": [e for t in travels_list for e in t.get("entertainments", [])],
            "accommodations": [a for t in travels_list for a in t.get("accommodations", [])],
            "all_entertainments": all_entertainments_list,
            "all_accommodations": all_accommodations_list,
        }
    )


@travel_router.put("/travels/{travel_id}", response_class=HTMLResponse)
async def update_travel(travel_id: int, request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
    form = await request.form()
    travel_data = TravelUpdate(
        status=form["status"],
        user_id=form["user_id"],
        entertainment_ids=form["entertainment_ids"],
        accommodation_ids=form["accommodation_ids"],
    )
    result = await service_locator.get_travel_contr().update_travel(travel_id, travel_data)
    logger.info("Путешествие ID %d успешно обновлено: %s", travel_id, result)
    return templates.TemplateResponse("travel.html", {"request": request})


@travel_router.delete("/travels/{travel_id}", response_class=HTMLResponse)
async def delete_travel(travel_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
    await service_locator.get_travel_contr().delete_travel(travel_id)
    logger.info("Путешествие ID %d успешно удалено", travel_id)
    return RedirectResponse(url="/travel.html", status_code=303)


@travel_router.patch("/travels/{travel_id}/complete")
async def complete_travel(travel_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> Response:
    await service_locator.get_travel_contr().complete_travel(travel_id)
    travel = await service_locator.get_travel_contr().get_travel_details(travel_id)
    user_id = travel.get("user_id") if travel else None
    if not user_id:
        logger.error("Не удалось получить user_id для путешествия ID %d", travel_id)
        return HTMLResponse(content="<h1>Пользователь не найден</h1>", status_code=404)
    logger.info("Путешествие ID %d успешно завершено", travel_id)
    return RedirectResponse(url=f"/profile_user/{user_id}", status_code=303)
