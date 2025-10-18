# src/routers/api_v2_cities.py
from __future__ import annotations

import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from schemas.city import CityCreate
from schemas.city import CityResponse
from schemas.city import CityUpdate, CitiesResponse
from service_locator import ServiceLocator
from service_locator import get_service_locator


logger = logging.getLogger(__name__)
router = APIRouter(prefix="/cities", tags=["cities"])
get_sl_dep = Depends(get_service_locator)


@router.post(
    "/",
    response_model=CityResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Неверный запрос"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def create_city(city: CityCreate, service_locator: ServiceLocator = get_sl_dep):
    try:
        return await service_locator.get_city_contr().create_city(city)
    except ValueError as e:
        logger.error(f"Ошибка создания города: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при создании города: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/",
    response_model=CitiesResponse,
    responses={
        404: {"description": "Города не найдены"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_all_cities(service_locator: ServiceLocator = get_sl_dep):
    try:
        cities = await service_locator.get_city_contr().get_all_cities()
        if not cities:
            raise HTTPException(status_code=404, detail="Cities not found")
        return {"cities": cities}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка получения списка городов: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/{city_id}",
    response_model=CityResponse,
    responses={
        404: {"description": "Город не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_city(city_id: int, service_locator: ServiceLocator = get_sl_dep):
    try:
        city = await service_locator.get_city_contr().get_city_by_id(city_id)
        if city is None:
            raise HTTPException(status_code=404, detail="City not found")
        return city
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка получения города ID {city_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put(
    "/{city_id}",
    response_model=CityResponse,
    responses={
        400: {"description": "Неверный запрос"},
        404: {"description": "Город не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def update_city(city_id: int, city: CityUpdate, service_locator: ServiceLocator = get_sl_dep):
    try:
        updated = await service_locator.get_city_contr().update_city(city_id, city)
        if updated is None:
            raise HTTPException(status_code=404, detail="City not found")
        return updated
    except ValueError as e:
        logger.error(f"Ошибка обновления города ID {city_id}: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при обновлении города ID {city_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete(
    "/{city_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Город не найден"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def delete_city(city_id: int, service_locator: ServiceLocator = get_sl_dep):
    try:
        await service_locator.get_city_contr().delete_city(city_id)
    except ValueError as e:
        logger.error(f"Ошибка удаления города ID {city_id}: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при удалении города ID {city_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
