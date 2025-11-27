from __future__ import annotations

import logging

from ..abstract_repository.icity_repository import ICityRepository
from ..abstract_service.city_service import ICityService
from ..shared.models.city import City

logger = logging.getLogger(__name__)


# class CityService(ICityService):
#     def __init__(self, repository: ICityRepository, publisher) -> None:
#         self.repository = repository
#         self.publisher = publisher
#         logger.debug("CityService инициализирован")

#     async def get_by_id(self, city_id: int) -> City | None:
#         logger.debug("Получение города по ID %d", city_id)
#         return await self.repository.get_by_id(city_id)

#     async def get_all_cities(self) -> list[City]:
#         logger.debug("Получение списка всех городов")
#         return await self.repository.get_list() 

#     async def add(self, city: City) -> City:
#         try:
#             logger.debug("Добавление города с ID %d", city.city_id)
#             city = await self.repository.add(city)
#             await self.publisher.publish(
#                 CITY_CREATED,
#                 city.model_dump(),
#             )
#         except (Exception):
#             logger.error("Город c таким ID %s уже существует.", city.city_id)
#             raise ValueError("Город c таким ID уже существует.")
#         return city

#     async def update(self, updated_city: City) -> City:
#         try:
#             logger.debug("Обновление города с ID %d", updated_city.city_id)
#             await self.repository.update(updated_city)
#             await self.publisher.publish(
#                 CITY_UPDATED,
#                 updated_city.model_dump(),
#             )
#         except (Exception):
#             logger.error("Город с ID %d не найден.", updated_city.city_id)
#             raise ValueError("Город не найден.")
#         return updated_city

#     async def delete(self, city_id: int) -> None:
#         try:
#             logger.debug("Удаление города с ID %d", city_id)
#             await self.repository.delete(city_id)
#             await self.publisher.publish(
#                 CITY_DELETED,
#                 {"id": city_id},
#             )
#         except (Exception):
#             logger.error("Город с ID %d не найден.", city_id)
#             raise ValueError("Город не найден.")

class CityService(ICityService):
    def __init__(self, rpc_client) -> None:
        self.rpc = rpc_client

    async def get_by_id(self, payload) -> City | None:
        logger.info(f"Payload received in DataService: {payload}")
        city_id = payload.get("city_id")
        if city_id is None:
            logger.error("city_id не передан в payload")
            return None  
        items = await self.rpc.call("core_city_get", {"city_id": city_id})
        items = items.get("result", [])
        city = City(**items)
        return city.model_dump()

    async def get_all_cities(self, payload=None) -> list[City]:
        logger.info("Received city_get_list RPC call сервис!")
        items = await self.rpc.call("core_city_get_all", {})
        logger.info(f"Items from DataService: {items}")
        items = items.get("result", [])

        cities = [City(**city) for city in items]
        return [city.model_dump() for city in cities]

    async def add(self, payload) -> City:
        name = payload.get("name")
        if name is None:
            logger.error("name не передан в payload")
            return None  
        items = await self.rpc.call("core_city_create",  {"name": name})
        items = items.get("result", [])
        city = City(**items)
        return city.model_dump()

    async def update(self, payload) -> City:
        city_id = payload.get("city_id")
        name = payload.get("name")
        if name is None or city_id is None:
            logger.error("name/city_id не передан в payload")
            return None  
        items = await self.rpc.call("core_city_update", {"city_id": city_id, "name": name})
        items = items.get("result", [])
        city = City(**items)
        return city.model_dump()


    async def delete(self, payload) -> None:
        city_id = payload.get("city_id")
        if city_id is None:
            logger.error("city_id не передан в payload")
            return None 
        res = await self.rpc.call("core_city_delete", {"city_id": city_id})
        items = res.get("result", [])
        return items
