from __future__ import annotations

import logging

from models.city import City
from schemas.city import CityCreate
from schemas.city import CityResponse
from schemas.city import CityUpdate
from services.city_service import CityService


logger = logging.getLogger(__name__)


class CityController:
    def __init__(self, city_service: CityService) -> None:
        self.city_service = city_service
        logger.debug("CityController initialized")

    async def create_city(self, city_data: CityCreate) -> CityResponse:
        """Создать новый город"""
        try:
            city = City(city_id = 1, name=city_data.name)
            created_city = await self.city_service.add(city)
            logger.info(f"Создан город: {created_city.name}")
            return CityResponse(id=created_city.city_id, name=created_city.name)
        except Exception as e:
            logger.error(f"Ошибка при создании города: {e!s}", exc_info=True)
            raise

    async def get_all_cities(self) -> list[CityResponse]:
        """Получить список всех городов"""
        try:
            cities = await self.city_service.get_all_cities()
            if not cities:
                logger.warning("Города не найдены")
                return []
            return [CityResponse(id=c.city_id, name=c.name) for c in cities]
        except Exception as e:
            logger.error(f"Ошибка при получении списка городов: {e!s}", exc_info=True)
            raise

    async def get_city_by_id(self, city_id: int) -> CityResponse | None:
        """Получить город по ID"""
        try:
            city = await self.city_service.get_by_id(city_id)
            if city is None:
                logger.warning(f"Город ID {city_id} не найден")
                return None
            return CityResponse(id=city.city_id, name=city.name)
        except Exception as e:
            logger.error(f"Ошибка при получении города ID {city_id}: {e!s}", exc_info=True)
            raise

    async def update_city(self, city_id: int, city_data: CityUpdate) -> CityResponse | None:
        """Обновить данные города"""
        try:
            city = City(city_id=city_id, name=city_data.name)
            updated_city = await self.city_service.update(city)
            if updated_city is None:
                logger.warning(f"Не удалось обновить город ID {city_id}")
                return None
            logger.info(f"Город ID {city_id} обновлён")
            return CityResponse(id=updated_city.city_id, name=updated_city.name)
        except Exception as e:
            logger.error(f"Ошибка при обновлении города ID {city_id}: {e!s}", exc_info=True)
            raise

    async def delete_city(self, city_id: int) -> None:
        """Удалить город по ID"""
        try:
            await self.city_service.delete(city_id)
            logger.info(f"Город ID {city_id} успешно удалён")
        except Exception as e:
            logger.error(f"Ошибка при удалении города ID {city_id}: {e!s}", exc_info=True)
            raise
