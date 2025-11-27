from __future__ import annotations

import logging

from fastapi import HTTPException

from ...shared.models.entertainment import Entertainment
from ...shared.schemas.entertainment import EntertainmentCreate
from ...shared.schemas.entertainment import EntertainmentResponse
from ...shared.schemas.entertainment import EntertainmentUpdate
from core_service.services.city_service import CityService
from core_service.services.entertainment_service import EntertainmentService


logger = logging.getLogger(__name__)


class EntertainmentController:
    def __init__(self, entertainment_service: EntertainmentService, city_service: CityService) -> None:
        self.entertainment_service = entertainment_service
        self.city_service = city_service
        logger.debug("EntertainmentController инициализирован")

    async def create_new_entertainment(self, data: EntertainmentCreate) -> EntertainmentResponse:
        city = await self.city_service.get_by_id(data.city_id)
        if not city:
            raise HTTPException(status_code=404, detail="City not found")
        entertainment = Entertainment(
            entertainment_id=1,
            city=city,
            event_name=data.event_name,
            event_time=data.event_time.replace(tzinfo=None),
            duration=data.duration,
            address=data.address,
        )
        entertainment = await self.entertainment_service.add(entertainment)
        logger.info("Развлечение успешно создано: %s", entertainment)
        return EntertainmentResponse(
            entertainment_id=entertainment.entertainment_id,
            city_id=entertainment.city.city_id,
            event_name=entertainment.event_name,
            event_time=entertainment.event_time,
            duration=entertainment.duration,
            address=entertainment.address,
        )

    async def update_entertainment(self, entertainment_id: int, data: EntertainmentUpdate) -> EntertainmentResponse:
        city = await self.city_service.get_by_id(data.city_id)
        if not city:
            raise HTTPException(status_code=404, detail="City not found")
        data = Entertainment(
            entertainment_id=entertainment_id,
            city=city,
            event_name=data.event_name,
            event_time=data.event_time.replace(tzinfo=None),
            duration=data.duration,
            address=data.address,
        ) 
        entertainment = await self.entertainment_service.update(data)
        logger.info("Развлечение ID %d успешно обновлено", entertainment_id)
        return EntertainmentResponse(
            entertainment_id=entertainment.entertainment_id,
            city_id=entertainment.city.city_id,
            event_name=entertainment.event_name,
            event_time=entertainment.event_time,
            duration=entertainment.duration,
            address=entertainment.address,
        )

    async def get_entertainment_details(self, entertainment_id: int) -> EntertainmentResponse:
        entertainment = await self.entertainment_service.get_by_id(entertainment_id)
        if not entertainment:
            raise HTTPException(status_code=404, detail="Entertainment not found")
        return EntertainmentResponse(
            entertainment_id=entertainment.entertainment_id,
            city_id=entertainment.city.city_id,
            event_name=entertainment.event_name,
            event_time=entertainment.event_time,
            duration=entertainment.duration,
            address=entertainment.address,
        )

    async def get_all_entertainment(self) -> list[EntertainmentResponse]:
        entertainment_list = await self.entertainment_service.get_list()
        return [
            EntertainmentResponse(
                entertainment_id=e.entertainment_id,
                city_id=e.city.city_id,
                event_name=e.event_name,
                event_time=e.event_time,
                duration=e.duration,
                address=e.address,
            )
            for e in entertainment_list
        ]

    async def delete_entertainment(self, entertainment_id: int) -> None:
        try:
            await self.entertainment_service.delete(entertainment_id)
            logger.info("Развлечение ID %d успешно удалено", entertainment_id)
        except Exception as e:
            logger.error("Ошибка при удалении развлечения ID %d: %s", entertainment_id, str(e), exc_info=True)
            raise HTTPException(status_code=400, detail=str(e))
