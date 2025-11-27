from __future__ import annotations

import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from ...shared.schemas.entertainment import EntertainmentCreate
from ...shared.schemas.entertainment import EntertainmentResponse
from ...shared.schemas.entertainment import EntertainmentsResponse
from ...shared.schemas.entertainment import EntertainmentUpdate
from ...service_locator import ServiceLocatorV2
from ...service_locator import get_service_locator_v2


logger = logging.getLogger(__name__)

entertainment_router = APIRouter(prefix="/entertainments", tags=["entertainments"])
get_sl_dep = Depends(get_service_locator_v2)


@entertainment_router.post(
    "/", response_model=EntertainmentResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Неверный запрос"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def create_entertainment(entertainment: EntertainmentCreate, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        return await service_locator.get_ent_contr().create_new_entertainment(entertainment)
    except ValueError as e:
        logger.error(f"Ошибка создания развлечение: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при создании развлечение: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@entertainment_router.get(
    "/", response_model=EntertainmentsResponse,
    responses={
        404: {"description": "Развлечения не найдены"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_all_entertainments(service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_ent_contr().get_all_entertainment()
        if not result:
            raise HTTPException(status_code=404, detail="Entertainments not found")
        return {"entertainments": result}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка получения списка развлечений: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@entertainment_router.get(
    "/{entertainment_id}",
    response_model=EntertainmentResponse,
    responses={
        404: {"description": "Развлечение не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_entertainment(entertainment_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_ent_contr().get_entertainment_details(entertainment_id)
        if not result:
            raise HTTPException(status_code=404, detail="Entertainment not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка получения развлечения ID {city_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@entertainment_router.put(
    "/{entertainment_id}",
    response_model=EntertainmentResponse,
    responses={
        400: {"description": "Неверный запрос"},
        404: {"description": "Развлечение не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def update_entertainment(entertainment_id: int, entertainment: EntertainmentUpdate,
    service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        result = await service_locator.get_ent_contr().update_entertainment(entertainment_id, entertainment)
        if result is None:
            raise HTTPException(status_code=404, detail="Entertainment not found")
        return result
    except ValueError as e:
        logger.error(f"Ошибка обновления развлечения ID {city_id}: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при обновлении развлечения ID {city_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@entertainment_router.delete(
    "/{entertainment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Развлечение не найдено"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def delete_entertainment(entertainment_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        await service_locator.get_ent_contr().delete_entertainment(entertainment_id)
    except ValueError as e:
        logger.error(f"Ошибка удаления развлечения ID {city_id}: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Внутренняя ошибка при удалении развлечения ID {city_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

