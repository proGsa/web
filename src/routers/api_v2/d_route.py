from __future__ import annotations

import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from service_locator import ServiceLocatorV2, get_service_locator_v2
from schemas.directory_route import (
    DirectoryRouteCreate,
    DirectoryRouteUpdate,
    DirectoryRouteResponse,
    DirectoryRoutePartialUpdate,
    DirectoryRouteResponseOut,
    DirectoryRoutesResponse
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/directory_routes", tags=["directory-routes"])
get_sl_dep = Depends(get_service_locator_v2)


@router.post(
    "/",
    response_model=DirectoryRouteResponseOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Неверный запрос"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def create_d_route(d_route: DirectoryRouteCreate, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        return await service_locator.get_d_route_contr().create_new_d_route(d_route)
    except ValueError as e:
        logger.error(f"Ошибка создания справочного маршрута: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при создании справочного маршрута: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/",
    response_model=DirectoryRoutesResponse,
    responses={
        404: {"description": "Справочники маршрута не найдены"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_all_d_routes(service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_d_route_contr().get_all_d_routes()
        if not result:
            raise HTTPException(status_code=404, detail="DirectoryRoutes not found")
        return {"d_routes" : result}
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Ошибка при получении списка маршрутов: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{d_route_id}",
    response_model=DirectoryRouteResponseOut,
    responses={
        404: {"description": "Справочник маршрута не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_d_route(d_route_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_d_route_contr().get_d_route_details(d_route_id)
        if not result:
            raise HTTPException(status_code=404, detail="Directory route not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Ошибка при получении справочника маршрута ID %d: %s", d_route_id, str(e), exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{d_route_id}",
    response_model=DirectoryRouteResponseOut,
    responses={
        400: {"description": "Неверный запрос"},
        404: {"description": "Справочник маршрута не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def update_d_route(d_route_id: int, d_route: DirectoryRouteUpdate, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_d_route_contr().update_d_route(d_route_id, d_route)
        if not result:
            raise HTTPException(status_code=404, detail="Directory route not found")
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Ошибка при обновлении справочника маршрута ID %d: %s", d_route_id, str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{d_route_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Справочник маршрута не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def delete_d_route(d_route_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        await service_locator.get_d_route_contr().delete_d_route(d_route_id)
    except ValueError as e:
        logger.error(f"Ошибка удаления справочника маршрута ID {city_id}: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при удалении справочника маршрута ID {city_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/{d_route_id}",
    response_model=DirectoryRouteResponseOut,
    responses={
        400: {"description": "Неверный запрос"},
        404: {"description": "Справочник маршрута не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def partial_update_d_route(d_route_id: int, d_route: DirectoryRoutePartialUpdate, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_d_route_contr().partial_update_d_route(d_route_id, d_route)
        if not result:
            raise HTTPException(status_code=404, detail="Directory route not found")
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Ошибка при частичном обновлении маршрута ID %d: %s", d_route_id, str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
