from __future__ import annotations

import logging
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.travel import TravelCreate, TravelResponse, TravelUpdate, TravelsResponse
from service_locator import ServiceLocator, get_service_locator

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/travels", tags=["travels"])
get_sl_dep = Depends(get_service_locator)


@router.post(
    "/",
    response_model=TravelResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Неверный запрос"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def create_travel(travel: TravelCreate, service_locator: ServiceLocator = get_sl_dep):
    """
    Создать новое путешествие с пользователями, развлечениями и размещениями
    """
    try:
        result = await service_locator.get_travel_contr().create_travel(travel)
        logger.info("Путешествие успешно создано: %s", result)
        return result
    except ValueError as e:
        logger.error(f"Ошибка создания путешествия: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при создании путешествия: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/",
    response_model=TravelsResponse,
    responses={
        404: {"description": "Путешествия не найдены"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_all_travels(service_locator: ServiceLocator = get_sl_dep):
    """
    Получить список всех путешествий
    """
    try:
        travels = await service_locator.get_travel_contr().get_all_travels()
        if not travels:
            raise HTTPException(status_code=404, detail="Travels not found")
        return {"travels" : travels}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка получения списка путешествий: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/{travel_id}",
    response_model=TravelResponse,
    responses={
        404: {"description": "Путешествие не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_travel(travel_id: int, service_locator: ServiceLocator = get_sl_dep):
    """
    Получить путешествие по ID
    """
    try:
        travel = await service_locator.get_travel_contr().get_travel_by_id(travel_id)
        if travel is None:
            raise HTTPException(status_code=404, detail="Travel not found")
        return travel
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка получения путешествия ID {travel_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put(
    "/{travel_id}",
    response_model=TravelResponse,
    responses={
        400: {"description": "Неверный запрос"},
        404: {"description": "Путешествие не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def update_travel(travel_id: int, travel: TravelUpdate, service_locator: ServiceLocator = get_sl_dep):
    """
    Обновить существующее путешествие
    """
    try:
        updated = await service_locator.get_travel_contr().update_travel(travel_id, travel)
        if updated is None:
            raise HTTPException(status_code=404, detail="Travel not found")
        logger.info("Путешествие ID %d успешно обновлено", travel_id)
        return updated
    except ValueError as e:
        logger.error(f"Ошибка обновления путешествия ID {travel_id}: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при обновлении путешествия ID {travel_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete(
    "/{travel_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Путешествие не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def delete_travel(travel_id: int, service_locator: ServiceLocator = get_sl_dep):
    """
    Удалить путешествие по ID
    """
    try:
        await service_locator.get_travel_contr().delete_travel(travel_id)
        logger.info("Путешествие ID %d успешно удалено", travel_id)
    except ValueError as e:
        logger.error(f"Ошибка удаления путешествия ID {travel_id}: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при удалении путешествия ID {travel_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch(
    "/{travel_id}",
    response_model=TravelResponse,
    responses={
        404: {"description": "Путешествие не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def complete_travel(travel_id: int, service_locator: ServiceLocator = get_sl_dep):
    try:
        completed = await service_locator.get_travel_contr().complete_travel(travel_id)
        if completed is None:
            raise HTTPException(status_code=404, detail="Travel not found")
        logger.info("Путешествие ID %d успешно завершено", travel_id)
        return completed
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка завершения путешествия ID {travel_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
