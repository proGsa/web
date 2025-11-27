from __future__ import annotations

import logging

from fastapi import HTTPException

from ...shared.models.accommodation import Accommodation
from ...shared.schemas.accommodation import AccommodationCreate
from ...shared.schemas.accommodation import AccommodationResponse
from ...shared.schemas.accommodation import AccommodationUpdate
from core_service.services.accommodation_service import AccommodationService
from core_service.services.city_service import CityService


logger = logging.getLogger(__name__)


class AccommodationController:
    def __init__(self, accommodation_service: AccommodationService, city_service: CityService) -> None:
        self.accommodation_service = accommodation_service
        self.city_service = city_service
        logger.debug("Инициализация AccommodationController")

    async def create_new_accommodation(self, data: AccommodationCreate) -> AccommodationResponse:
        try:
            city = await self.city_service.get_by_id(data.city_id)
            if not city:
                raise ValueError("City not found")
            
            accommodation = Accommodation(
                accommodation_id=1,
                price=data.price,
                address=data.address,
                name=data.name,
                type=data.type,
                rating=data.rating,
                check_in=data.check_in.strftime('%Y-%m-%dT%H:%M'),
                check_out=data.check_out.strftime('%Y-%m-%dT%H:%M'),
                city=city
            )
            accommodation = await self.accommodation_service.add(accommodation)
            logger.info("Проживание успешно создано: %s", accommodation)
            return AccommodationResponse(
                accommodation_id=accommodation.accommodation_id,
                name=accommodation.name,
                city_id=accommodation.city.city_id,
                address=accommodation.address,
                price=accommodation.price,
                type=accommodation.type,
                rating=accommodation.rating,
                check_in=accommodation.check_in,
                check_out=accommodation.check_out,
            )
        except Exception as e:
            logger.error("Ошибка при создании проживания: %s", str(e), exc_info=True)
            raise HTTPException(status_code=400, detail=str(e))
    
    async def update_accommodation(self, accommodation_id: int, data: AccommodationUpdate) -> AccommodationResponse:
        try:
            city = await self.city_service.get_by_id(data.city_id)
            if not city:
                raise ValueError("City not found")
            accommodation = Accommodation(
                accommodation_id=accommodation_id,
                price=data.price,
                address=data.address,
                name=data.name,
                type=data.type,
                rating=data.rating,
                check_in=data.check_in.strftime('%Y-%m-%dT%H:%M'),
                check_out=data.check_out.strftime('%Y-%m-%dT%H:%M'),
                city=city
            )
            new_accommodation = await self.accommodation_service.update(accommodation)
            logger.info("Проживание ID %d успешно обновлено", accommodation_id)
            return AccommodationResponse(
                accommodation_id=new_accommodation.accommodation_id,
                name=new_accommodation.name,
                city_id=new_accommodation.city.city_id,
                address=new_accommodation.address,
                price=new_accommodation.price,
                type=new_accommodation.type,
                rating=new_accommodation.rating,
                check_in=new_accommodation.check_in,
                check_out=new_accommodation.check_out,
            )
        except Exception as e:
            logger.error("Ошибка при обновлении проживания ID %d: %s", accommodation_id, str(e), exc_info=True)
            raise HTTPException(status_code=400, detail=str(e))
    
    async def get_accommodation_details(self, accommodation_id: int) -> AccommodationResponse:
        accommodation = await self.accommodation_service.get_by_id(accommodation_id)
        if not accommodation:
            logger.warning("Проживание ID %d не найдено", accommodation_id)
            raise HTTPException(status_code=404, detail="Accommodation not found")
        return AccommodationResponse(
            accommodation_id=accommodation.accommodation_id,
            name=accommodation.name,
            city_id=accommodation.city.city_id,
            address=accommodation.address,
            price=accommodation.price,
            type=accommodation.type,
            rating=accommodation.rating,
            check_in=accommodation.check_in,
            check_out=accommodation.check_out,
        )

    async def get_all_accommodation(self) -> list[AccommodationResponse]:
        accommodation_list = await self.accommodation_service.get_list()
        return [
            AccommodationResponse(
                accommodation_id=a.accommodation_id,
                name=a.name,
                city_id=a.city.city_id,
                address=a.address,
                price=a.price,
                type=a.type,
                rating=a.rating,
                check_in=a.check_in,
                check_out=a.check_out,
            )
            for a in accommodation_list
        ]

    async def delete_accommodation(self, accommodation_id: int) -> None:
        try:
            await self.accommodation_service.delete(accommodation_id)
            logger.info("Проживание ID %d успешно удалено", accommodation_id)
        except Exception as e:
            logger.error("Ошибка при удалении проживания ID %d: %s", accommodation_id, str(e), exc_info=True)
            raise HTTPException(status_code=400, detail=str(e))
