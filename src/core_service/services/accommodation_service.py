from __future__ import annotations

from datetime import datetime
import logging

from ..abstract_repository.iaccommodation_repository import IAccommodationRepository
from ..abstract_service.accommodation_service import IAccommodationService
from ..shared.models.accommodation import Accommodation
from ..shared.models.city import City

logger = logging.getLogger(__name__)


# class AccommodationService(IAccommodationService):
#     def __init__(self, repository: IAccommodationRepository, publisher) -> None:
#         self.repository = repository
#         self.publisher = publisher
#         logger.debug("AccommodationService инициализирован")

#     async def get_by_id(self, accommodation_id: int) -> Accommodation | None:
#         logger.debug("Получение размещения по ID %d", accommodation_id)
#         return await self.repository.get_by_id(accommodation_id)

#     async def get_list(self) -> list[Accommodation]:
#         logger.debug("Получение списка размещений")
#         return await self.repository.get_list()

#     async def add(self, accommodation: Accommodation) -> Accommodation:
#         try:
#             logger.debug("Добавления размещения с ID %d", accommodation.accommodation_id)
#             accommodation = await self.repository.add(accommodation)
#             await self.publisher.publish(
#                 ACCOMMODATION_CREATED,
#                 accommodation.model_dump(),
#             )
#         except (Exception):
#             logger.error("Размещение c таким ID %d уже существует.", accommodation.accommodation_id)
#             raise ValueError("Размещение c таким ID уже существует.")
#         return accommodation

#     async def update(self, update_accommodation: Accommodation) -> Accommodation:
#         try:
#             logger.debug("Обновление размещения с ID %d", update_accommodation.accommodation_id)
#             await self.repository.update(update_accommodation)
#             await self.publisher.publish(
#                 ACCOMMODATION_UPDATED,
#                 update_accommodation.model_dump(),
#             )
#         except (Exception):
#             logger.error("Размещение c таким ID %d не найдено.", update_accommodation.accommodation_id)
#             raise ValueError("Размещение c таким ID не найдено.")
#         return update_accommodation

#     async def delete(self, accommodation_id: int) -> None:
#         try:
#             logger.debug("Размещение с ID %d успешно удалено", accommodation_id)
#             await self.repository.delete(accommodation_id)
#             await self.publisher.publish(
#                 ACCOMMODATION_DELETED,
#                 {"id": accommodation_id},
#             )
#         except (Exception):
#             logger.error("Размещение c таким ID %d не найдено.", accommodation_id)
#             raise ValueError("Размещение не найдено.")


class AccommodationService(IAccommodationService):
    def __init__(self, rpc_client) -> None:
        self.rpc = rpc_client
        logger.debug("AccommodationService инициализирован")

    async def get_by_id(self, payload) -> Accommodation | None:
        accommodation_id = payload.get("accommodation_id")
        if accommodation_id is None:
            logger.error("accommodation_id не передан в payload")
            return None  
        response = await self.rpc.call("core_accommodation_get", {"id": accommodation_id})
        acc = response.get("result", [])
        accommodation = Accommodation(
                accommodation_id=accommodation_id,
                name=acc["name"],
                city=City(city_id=acc["city"]["city_id"], name=acc["city"]["name"]),
                address=acc["address"],
                price=acc["price"],
                type=acc["type"],
                rating=acc["rating"],
                check_in=datetime.fromisoformat(acc["check_in"]) ,
                check_out=datetime.fromisoformat(acc["check_out"]),
            )
        return {
                **accommodation.model_dump(),
                "check_in": accommodation.check_in.isoformat(),
                "check_out": accommodation.check_out.isoformat(),
            }

    async def get_list(self, payload=None) -> list[Accommodation]:
        logger.debug("RPC: accommodation.get_list")
        items = await self.rpc.call("core_accommodation_get_all", {})
        logger.info(f"Items from DataService: {items}")
        items = items.get("result", [])
        accommodations = [
            Accommodation(
                accommodation_id=acc["accommodation_id"],
                name=acc["name"],
                city=City(city_id=acc["city"]["city_id"], name=acc["city"]["name"]),
                address=acc["address"],
                price=acc["price"],
                type=acc["type"],
                rating=acc["rating"],
                check_in=datetime.fromisoformat(acc["check_in"]) ,
                check_out=datetime.fromisoformat(acc["check_out"]),
            )
            for acc in items
        ]
        return [
            {
                **acc.model_dump(),
                "check_in": acc.check_in.isoformat(),
                "check_out": acc.check_out.isoformat(),
            }
            for acc in accommodations
        ]

    async def add(self, payload) -> Accommodation:
        acc_dict = {
            "accommodation_id": 1,  # или None, если генерируется в Data
            "name": payload["name"],
            "city_id": payload["city_id"],
            "address": payload["address"],
            "price": payload["price"],
            "type": payload["type"],
            "rating": payload["rating"],
            "check_in": payload["check_in"],   # уже строка ISO
            "check_out": payload["check_out"], # уже строка ISO
        }

        response = await self.rpc.call(
            "core_accommodation_create",
            {"accommodation": acc_dict}
        )
        acc = response.get("result", [])
        accommodation = Accommodation(
                accommodation_id=acc["accommodation_id"],
                name=acc["name"],
                city=City(city_id=acc["city"]["city_id"], name=acc["city"]["name"]),
                address=acc["address"],
                price=acc["price"],
                type=acc["type"],
                rating=acc["rating"],
                check_in=datetime.fromisoformat(acc["check_in"]) ,
                check_out=datetime.fromisoformat(acc["check_out"]),
            )
        return {
                **accommodation.model_dump(),
                "check_in": accommodation.check_in.isoformat(),
                "check_out": accommodation.check_out.isoformat(),
            }

    async def update(self, payload) -> Accommodation:
        logger.debug("RPC: accommodation.update %s", accommodation)
        response = await self.rpc.call("accommodation.update", accommodation.model_dump())

        return Accommodation(**response)

    async def delete(self, payload) -> None:
        accommodation_id = payload.get("accommodation_id")
        if accommodation_id is None:
            logger.error("accommodation_id не передан в payload")
            return None 
        res = await self.rpc.call("core_accommodation_delete", {"accommodation_id": accommodation_id})
        items = res.get("result", [])
        return items


