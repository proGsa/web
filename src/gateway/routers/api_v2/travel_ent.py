from __future__ import annotations

import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from ...shared.schemas.entertainment import EntertainmentCreate
from ...shared.schemas.entertainment import EntertainmentResponse
from ...service_locator import ServiceLocatorV2
from ...service_locator import get_service_locator_v2


logger = logging.getLogger(__name__)
router = APIRouter(prefix="/travels", tags=["travel-entertainments"])
get_sl_dep = Depends(get_service_locator_v2)


@router.post(
    "/{travel_id}/entertainments",
    response_model=EntertainmentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Добавить развлечение к маршруту",
    description="Создает новое развлечение и добавляет его к указанному путешествию",
    responses={
        400: {"description": "Неверный запрос"},
        404: {"description": "Путешествие не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def add_entertainment_to_travel(
    travel_id: int,
    entertainment: EntertainmentCreate,
    service_locator: ServiceLocatorV2 = get_sl_dep,
):
    """
    Создать развлечение и добавить его к путешествию
    """
    try:
        result = await service_locator.get_travel_contr().add_entertainment_to_travel(travel_id, entertainment)
        logger.info("Развлечение '%s' добавлено к путешествию ID %d", entertainment.event_name, travel_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except KeyError:
        raise HTTPException(status_code=404, detail="Travel not found")
    except Exception as e:
        logger.error(f"Ошибка при добавлении развлечения к путешествию: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete(
    "/{travel_id}/entertainments/{entertainment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить развлечение из путешествия",
    description="Удаляет развлечение из указанного путешествия",
    responses={
        404: {"description": "Развлечение или путешествие не найдены"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def delete_entertainment_from_travel(
    travel_id: int,
    entertainment_id: int,
    service_locator: ServiceLocatorV2 = get_sl_dep,
):
    """
    Удалить развлечение из путешествия
    """
    try:
        await service_locator.get_travel_contr().delete_entertainment_from_travel(travel_id, entertainment_id)
        logger.info("Развлечение ID %d удалено из путешествия ID %d", entertainment_id, travel_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Travel or entertainment not found")
    except Exception as e:
        logger.error(f"Ошибка при удалении развлечения из путешествия: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
