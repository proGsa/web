from __future__ import annotations

import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from ...shared.schemas.route import InsertCityRequest
from ...shared.schemas.route import RouteCreate
from ...shared.schemas.route import RouteResponse
from ...shared.schemas.route import RoutesResponse
from ...shared.schemas.route import RouteUpdate
from ...service_locator import ServiceLocatorV2
from ...service_locator import get_service_locator_v2


logger = logging.getLogger(__name__)
router = APIRouter(prefix="/routes", tags=["routes"])
get_sl_dep = Depends(get_service_locator_v2)


@router.post(
    "/",
    response_model=RouteResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Неверный запрос"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def create_route(route: RouteCreate, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        return await service_locator.get_route_contr().create_route(route)
    except ValueError as e:
        logger.error("Ошибка создания маршрута: %s", e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Внутренняя ошибка при создании маршрута: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/",
    response_model=RoutesResponse,
    responses={
        404: {"description": "Маршруты не найдены"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_all_routes(service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        routes = await service_locator.get_route_contr().get_all_routes()
        if not routes:
            raise HTTPException(status_code=404, detail="Routes not found")
        return {"routes": routes}
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Ошибка получения списка маршрутов: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/{route_id}",
    response_model=RouteResponse,
    responses={
        404: {"description": "Маршрут не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_route(route_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        route = await service_locator.get_route_contr().get_route_by_id(route_id)
        if route is None:
            raise HTTPException(status_code=404, detail="Route not found")
        return route
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Ошибка получения маршрута ID %d: %s", route_id, e, exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put(
    "/{route_id}",
    response_model=RouteResponse,
    responses={
        400: {"description": "Неверный запрос"},
        404: {"description": "Маршрут не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def update_route(route_id: int, route: RouteUpdate, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        updated = await service_locator.get_route_contr().update_route(route_id, route)
        if updated is None:
            raise HTTPException(status_code=404, detail="Route not found")
        return updated
    except ValueError as e:
        logger.error("Ошибка обновления маршрута ID %d: %s", route_id, e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Внутренняя ошибка при обновлении маршрута ID %d: %s", route_id, e, exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete(
    "/{route_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Маршрут не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def delete_route(route_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        await service_locator.get_route_contr().delete_route(route_id)
    except ValueError as e:
        logger.error("Ошибка удаления маршрута ID %d: %s", route_id, e)
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error("Внутренняя ошибка при удалении маршрута ID %d: %s", route_id, e, exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post(
    "/cities/{city_id}",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Город успешно добавлен"},
        400: {"description": "Неверные данные запроса"},
        404: {"description": "Маршрут или город не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def insert_city_into_route(travel_id: int, city_id: int, request: InsertCityRequest, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        await service_locator.get_route_contr().insert_city_after(travel_id, city_id, request)
        return {"message": "Город успешно добавлен"}
    except ValueError as e:
        logger.error("Ошибка вставки города: %s", e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Внутренняя ошибка при вставке города: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/cities/{city_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Город успешно удален из маршрута"},
        400: {"description": "Неверные данные запроса"},
        404: {"description": "Маршрут или город не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def delete_city_from_route(travel_id: int, city_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        controller = service_locator.get_route_contr()
        await controller.delete_city_from_route(travel_id, city_id)
    except ValueError as e:
        logger.error("Ошибка удаления города: %s", e)
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error("Внутренняя ошибка при удалении города: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")