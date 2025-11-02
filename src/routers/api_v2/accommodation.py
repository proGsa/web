from __future__ import annotations
import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from service_locator import ServiceLocatorV2, get_service_locator_v2
from schemas.accommodation import (
    AccommodationCreate,
    AccommodationUpdate,
    AccommodationResponse,
    AccommodationsResponse
)

logger = logging.getLogger(__name__)

accommodation_router = APIRouter(prefix="/accommodations", tags=["accommodations"])
get_sl_dep = Depends(get_service_locator_v2)


@accommodation_router.post(
    "/",
    response_model=AccommodationResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Неверный запрос"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def create_accommodation(
    accommodation: AccommodationCreate, service_locator: ServiceLocatorV2 = get_sl_dep
):
    try:
        result = await service_locator.get_acc_contr().create_new_accommodation(accommodation)
        return result
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error("Ошибка при создании размещения: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@accommodation_router.get(
    "/",
    response_model=AccommodationsResponse,
    responses={
        404: {"description": "Размещения не найдены"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_all_accommodations(service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_acc_contr().get_all_accommodation()
        if not result:
            raise HTTPException(status_code=404, detail="Cities not found")
        return {"accommodations" : result}
    except Exception as e:
        logger.error("Ошибка при получении списка размещений: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@accommodation_router.get(
    "/{accommodation_id}",
    response_model=AccommodationResponse,
    responses={
        404: {"description": "Размещение не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_accommodation(accommodation_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_acc_contr().get_accommodation_details(accommodation_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Accommodation not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка получения размещения ID {city_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@accommodation_router.put(
    "/{accommodation_id}",
    response_model=AccommodationResponse,
    responses={
        400: {"description": "Неверный запрос"},
        404: {"description": "Размещение не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def update_accommodation(
    accommodation_id: int, accommodation: AccommodationUpdate, service_locator: ServiceLocatorV2 = get_sl_dep
):
    try:
        result = await service_locator.get_acc_contr().update_accommodation(accommodation_id, accommodation)
        if result is None:
            raise HTTPException(status_code=404, detail="Accommodation not found")
        return result
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error("Ошибка при обновлении размещения: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@accommodation_router.delete(
    "/{accommodation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Размещение не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def delete_accommodation(accommodation_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        await service_locator.get_acc_contr().delete_accommodation(accommodation_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    except Exception as e:
        logger.error("Ошибка при удалении размещения: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
