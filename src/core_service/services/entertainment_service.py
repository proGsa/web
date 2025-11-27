from __future__ import annotations

import logging

from ..abstract_repository.ientertainment_repository import IEntertainmentRepository
from ..abstract_service.entertainment_service import IEntertainmentService
from ..shared.models.entertainment import Entertainment

logger = logging.getLogger(__name__)


# class EntertainmentService(IEntertainmentService):
#     def __init__(self, repository: IEntertainmentRepository, publisher) -> None:
#         self.repository = repository
#         self.publisher = publisher
#         logger.debug("EntertainmentService инициализирован")

#     async def get_by_id(self, entertainment_id: int) -> Entertainment | None:
#         logger.debug("Получение развлечения по ID %d", entertainment_id)
#         return await self.repository.get_by_id(entertainment_id)

#     async def add(self, entertainment: Entertainment) -> Entertainment:
#         try:
#             logger.debug("Добавление развлечения с ID %d", entertainment.entertainment_id)
#             entertainment = await self.repository.add(entertainment)
#             await self.publisher.publish(
#                 ENTERTAINMENT_CREATED,
#                 entertainment.model_dump(),
#             )
#         except (Exception):
#             logger.error("Развлечение c таким ID %d уже существует.", entertainment.entertainment_id)
#             raise ValueError("Размещение c таким ID уже существует.")
#         return entertainment

#     async def update(self, update_entertainment: Entertainment) -> Entertainment:
#         try:
#             logger.debug("Обновление развлечения с ID %d", update_entertainment.entertainment_id)
#             await self.repository.update(update_entertainment)
#             await self.publisher.publish(
#                 ENTERTAINMENT_UPDATED,
#                 update_entertainment.model_dump(),
#             )
#         except (Exception):
#             logger.error("Развлечение с ID %d не найдено.", update_entertainment.entertainment_id)
#             raise ValueError("Размещение не найдено.")
#         return update_entertainment

#     async def delete(self, entertainment_id: int) -> None:
#         try:
#             logger.debug("Удаление развлечения с ID %d", entertainment_id)
#             await self.repository.delete(entertainment_id)
#             await self.publisher.publish(
#                 ENTERTAINMENT_DELETED,
#                 {"id": entertainment_id},
#             )
#         except (Exception):
#             logger.error("Развлечение с ID %d не найдено.", entertainment_id)
#             raise ValueError("Размещение не найдено.")

#     async def get_list(self) -> list[Entertainment]:
#         logger.debug("Получение списка всех развлечений")
#         return await self.repository.get_list()


class EntertainmentService(IEntertainmentService):
    def __init__(self, rpc_client) -> None:
        self.rpc = rpc_client
        logger.debug("EntertainmentService инициализирован")

    async def get_by_id(self, entertainment_id: int) -> Entertainment | None:
        logger.debug("RPC: entertainment.get_by_id %d", entertainment_id)
        response = await self.rpc.call(
            "entertainment.get_by_id",
            {"id": entertainment_id}
        )
        return Entertainment(**response) if response else None

    async def get_list(self) -> list[Entertainment]:
        logger.debug("RPC: entertainment.get_list")
        items = await self.rpc.call("entertainment.get_list", {})
        return [Entertainment(**item) for item in items]

    async def add(self, entertainment: Entertainment) -> Entertainment:
        logger.debug(
            "RPC: entertainment.add %d",
            entertainment.entertainment_id
        )
        response = await self.rpc.call(
            "entertainment.add",
            entertainment.model_dump()
        )

        return Entertainment(**response)

    async def update(self, entertainment: Entertainment) -> Entertainment:
        logger.debug(
            "RPC: entertainment.update %d",
            entertainment.entertainment_id
        )
        response = await self.rpc.call(
            "entertainment.update",
            entertainment.model_dump()
        )
        return Entertainment(**response)

    async def delete(self, entertainment_id: int) -> None:
        logger.debug("RPC: entertainment.delete %d", entertainment_id)

        await self.rpc.call(
            "entertainment.delete",
            {"id": entertainment_id}
        )