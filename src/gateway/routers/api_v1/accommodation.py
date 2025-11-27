# from __future__ import annotations

# import logging

# from datetime import datetime
# from typing import Any

# from fastapi import APIRouter
# from fastapi import Depends
# from fastapi import HTTPException
# from fastapi import Request
# from fastapi.responses import HTMLResponse
# from fastapi.responses import RedirectResponse
# from fastapi.templating import Jinja2Templates

# from ...service_locator import ServiceLocatorV1
# from ...service_locator import get_service_locator_v1


# logger = logging.getLogger(__name__)

# accommodation_router = APIRouter()
# templates = Jinja2Templates(directory="templates")
# get_sl_dep = Depends(get_service_locator_v1)


# @accommodation_router.post("/accommodations", response_class=HTMLResponse)
# async def create_accommodation(request: Request, service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     result = await service_locator.get_acc_contr().create_new_accommodation(request)
#     logger.info("Проживание успешно создано: %s", result)
#     return templates.TemplateResponse("accommodation.html", {"request": request})


# @accommodation_router.get("/accommodations", response_class=HTMLResponse)
# async def get_all_accommodations(request: Request, service_locator: ServiceLocator = get_sl_dep) -> HTMLResponse:
#     accommodation_list = await service_locator.get_acc_contr().get_all_accommodation()
#     accommodations = accommodation_list.get("accommodations", []) 
#     logger.info("Получено %d проживаний", len(accommodations))
#     for a in accommodations:
#         a['check_in'] = datetime.fromisoformat(a['check_in'])
#         a['check_out'] = datetime.fromisoformat(a['check_out'])
#     logger.info("Получение списка городов")
#     cities_list = await service_locator.get_city_contr().get_all_cities()
#     cities = cities_list.get("cities", [])
#     logger.info("Получено %d городов", len(cities))

#     return templates.TemplateResponse(
#         "accommodation.html",
#         {
#             "request": request, 
#             "accommodations": accommodations, 
#             "cities": cities
#         }
#     )


# @accommodation_router.get("/accommodation/get/{accommodation_id}")
# async def get_accommodation(accommodation_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
#     try:
#         acc = await service_locator.get_acc_contr().get_accommodation_details(accommodation_id)
#         if acc is None:
#             logger.warning("Проживание с ID %d не найдено", accommodation_id)
#             raise HTTPException(status_code=404, detail="Accommodation not found")
#         logger.info("Информация о проживании ID %d получена", accommodation_id)
#         return acc
#     except Exception as e:
#         logger.error("Ошибка при получении информации о проживании: %s", str(e), exc_info=True)
#         raise HTTPException(status_code=500, detail=str(e))


# @accommodation_router.put("/accommodations/{accommodation_id}", response_class=HTMLResponse)
# async def update_accommodation(accommodation_id: int, request: Request, 
#                                 service_locator: ServiceLocatorV1 = get_sl_dep) -> HTMLResponse:
#     result = await service_locator.get_acc_contr().update_accommodation(accommodation_id, request)
#     logger.info("Проживание ID %d успешно обновлено: %s", accommodation_id, result)
#     return templates.TemplateResponse("accommodation.html", {"request": request})


# @accommodation_router.post("/accommodation/delete/{accommodation_id}", response_class=HTMLResponse)
# async def delete_accommodation(accommodation_id: int, service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
#     result = await service_locator.get_acc_contr().delete_accommodation(accommodation_id)
#     logger.info("Проживание ID %d успешно удалено: %s", accommodation_id, result)
#     return RedirectResponse(url="/accommodation.html", status_code=303)


# @accommodation_router.delete("/route/accommodation/delete/{accommodation_id}", response_class=HTMLResponse)
# async def delete_accommodation_for_route(accommodation_id: int, route_id: int,
#                                 service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
#     result = await service_locator.get_acc_contr().delete_accommodation(accommodation_id)
#     logger.info("Размещение ID %d успешно удалено: %s", accommodation_id, result)
#     return RedirectResponse(url=f"/route/edit/{route_id}", status_code=303)


# @accommodation_router.post("/accommodation/add/{route_id}", response_class=HTMLResponse)
# async def add_acc_to_route(route_id: int, request: Request,
#                                          service_locator: ServiceLocatorV1 = get_sl_dep) -> RedirectResponse:
#     try:
#         result = await service_locator.get_acc_contr().create_new_accommodation(request)
#         logger.info("Размещение успешно создано: %s", result)
#         travel = await service_locator.get_travel_serv().get_travel_by_route_id(route_id)
#         if not travel:
#             raise ValueError(f"No travel found for route_id={route_id}")
#         ent_ids = []
#         accommodations = await service_locator.get_travel_serv().get_accommodations_by_travel(travel.travel_id)
#         ent_ids = [e.accommodation_id for e in accommodations]
#         ent_ids.append(result["accommodation_id"])

#         await service_locator.get_travel_serv().link_accommodations(travel.travel_id, ent_ids)
#         return RedirectResponse(
#             url=f"/route/edit/{route_id}", 
#             status_code=303
#         )
        
#     except Exception as e:
#         logger.error(f"Error adding accommodation: {e!s}")
#         raise


# @accommodation_router.put("/accommodations/{accommodation_id}")
# async def update_accommodation_dates(accommodation_id: int, request: Request,
#     service_locator: ServiceLocatorV1 = get_sl_dep) -> dict[str, Any]:
#     return await service_locator.get_acc_contr().update_accommodation_dates(accommodation_id, request)
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from ...service_locator import ServiceLocatorV1, get_service_locator_v1
from ...shared.schemas.accommodation import AccommodationCreate, AccommodationUpdate

logger = logging.getLogger(__name__)

accommodation_router = APIRouter()
templates = Jinja2Templates(directory="templates")
get_sl_dep = Depends(get_service_locator_v1)


@accommodation_router.post("/accommodations", response_class=HTMLResponse)
async def create_accommodation(
    request: Request,
    service_locator: ServiceLocatorV1 = get_sl_dep
) -> HTMLResponse:
    form = await request.form()
    acc_data = AccommodationCreate(
        name=form["name"],
        city_id=int(form["city_id"]),
        address=form["address"],
        price=float(form["price"]),
        type=form["type"],
        rating=float(form["rating"]),
        check_in=datetime.fromisoformat(form["check_in"]),
        check_out=datetime.fromisoformat(form["check_out"])
    )
    result = await service_locator.get_acc_contr().create_new_accommodation(acc_data)
    logger.info("Проживание успешно создано: %s", result)
    return templates.TemplateResponse("accommodation.html", {"request": request})


@accommodation_router.get("/accommodations", response_class=HTMLResponse)
async def get_all_accommodations(
    request: Request,
    service_locator: ServiceLocatorV1 = get_sl_dep
) -> HTMLResponse:
    accommodation_list = await service_locator.get_acc_contr().get_all_accommodations()
    accommodations = accommodation_list  # уже список DTO
    for a in accommodations:
        a.check_in = datetime.fromisoformat(a.check_in)
        a.check_out = datetime.fromisoformat(a.check_out)

    cities_list = await service_locator.get_city_contr().get_all_cities()
    cities = cities_list  # список DTO

    logger.info("Получено %d проживаний и %d городов", len(accommodations), len(cities))

    return templates.TemplateResponse(
        "accommodation.html",
        {
            "request": request,
            "accommodations": [a.dict() for a in accommodations],
            "cities": [c.dict() for c in cities]
        }
    )


@accommodation_router.get("/accommodation/get/{accommodation_id}")
async def get_accommodation(
    accommodation_id: int,
    service_locator: ServiceLocatorV1 = get_sl_dep
) -> Any:
    try:
        acc = await service_locator.get_acc_contr().get_accommodation_details(accommodation_id)
        if acc is None:
            logger.warning("Проживание с ID %d не найдено", accommodation_id)
            raise HTTPException(status_code=404, detail="Accommodation not found")
        logger.info("Информация о проживании ID %d получена", accommodation_id)
        return acc.dict()
    except Exception as e:
        logger.error("Ошибка при получении информации о проживании: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@accommodation_router.put("/accommodations/{accommodation_id}", response_class=HTMLResponse)
async def update_accommodation(
    accommodation_id: int,
    request: Request,
    service_locator: ServiceLocatorV1 = get_sl_dep
) -> HTMLResponse:
    form = await request.form()
    acc_data = AccommodationUpdate(
        name=form["name"],
        address=form["address"],
        city_id=int(form["city_id"]),
        price=float(form["price"]),
        type=form["type"],
        rating=float(form["rating"]),
        check_in=datetime.fromisoformat(form["check_in"]),
        check_out=datetime.fromisoformat(form["check_out"])
    )
    result = await service_locator.get_acc_contr().update_accommodation(accommodation_id, acc_data)
    logger.info("Проживание ID %d успешно обновлено: %s", accommodation_id, result)
    return templates.TemplateResponse("accommodation.html", {"request": request})


@accommodation_router.post("/accommodation/delete/{accommodation_id}", response_class=HTMLResponse)
async def delete_accommodation(
    accommodation_id: int,
    service_locator: ServiceLocatorV1 = get_sl_dep
) -> RedirectResponse:
    await service_locator.get_acc_contr().delete_accommodation(accommodation_id)
    logger.info("Проживание ID %d успешно удалено", accommodation_id)
    return RedirectResponse(url="/accommodation.html", status_code=303)


@accommodation_router.delete("/route/accommodation/delete/{accommodation_id}", response_class=HTMLResponse)
async def delete_accommodation_for_route(
    accommodation_id: int,
    route_id: int,
    service_locator: ServiceLocatorV1 = get_sl_dep
) -> RedirectResponse:
    await service_locator.get_acc_contr().delete_accommodation(accommodation_id)
    logger.info("Размещение ID %d успешно удалено", accommodation_id)
    return RedirectResponse(url=f"/route/edit/{route_id}", status_code=303)


@accommodation_router.post("/accommodation/add/{route_id}", response_class=HTMLResponse)
async def add_acc_to_route(
    route_id: int,
    request: Request,
    service_locator: ServiceLocatorV1 = get_sl_dep
) -> RedirectResponse:
    form = await request.form()
    acc_data = AccommodationCreate(
        name=form["name"],
        address=form["address"],
        city_id=int(form["city_id"]),
        price=float(form["price"]),
        type=form["type"],
        rating=float(form["rating"]),
        check_in=datetime.fromisoformat(form["check_in"]),
        check_out=datetime.fromisoformat(form["check_out"])
    )
    result = await service_locator.get_acc_contr().create_new_accommodation(acc_data)
    logger.info("Размещение успешно создано: %s", result)

    travel = await service_locator.get_travel_contr().get_travel_by_route_id(route_id)
    if not travel:
        raise HTTPException(status_code=404, detail=f"No travel found for route_id={route_id}")

    accommodations = await service_locator.get_travel_contr().get_accommodations_by_travel(travel.travel_id)
    ent_ids = [e.accommodation_id for e in accommodations]
    ent_ids.append(result.accommodation_id)

    await service_locator.get_travel_contr().link_accommodations(travel.travel_id, ent_ids)

    return RedirectResponse(url=f"/route/edit/{route_id}", status_code=303)


@accommodation_router.put("/accommodations/{accommodation_id}/dates")
async def update_accommodation_dates(
    accommodation_id: int,
    request: Request,
    service_locator: ServiceLocatorV1 = get_sl_dep
) -> Any:
    form = await request.form()
    acc_data = AccommodationUpdate(
        name=form.get("name", ""),
        address=form.get("address", ""),
        city_id=int(form["city_id"]),
        price=float(form.get("price", 0)),
        type=form.get("type", ""),
        rating=float(form.get("rating", 0)),
        check_in=datetime.fromisoformat(form["check_in"]),
        check_out=datetime.fromisoformat(form["check_out"])
    )
    return await service_locator.get_acc_contr().update_accommodation(accommodation_id, acc_data)
