from __future__ import annotations

import logging
from typing import List, Optional

from fastapi import HTTPException

from models.travel import Travel
from models.entertainment import Entertainment
from models.accommodation import Accommodation
from schemas.travel import TravelCreate, TravelUpdate, TravelResponse
from services.travel_service import TravelService
from services.user_service import UserService
from services.entertainment_service import EntertainmentService
from services.accommodation_service import AccommodationService
from services.city_service import CityService
from schemas.entertainment import EntertainmentCreate, EntertainmentResponse
from schemas.accommodation import AccommodationCreate, AccommodationResponse

logger = logging.getLogger(__name__)


class TravelController:
    def __init__(self, travel_service: TravelService, user_service: UserService,
        ent_service: EntertainmentService, acc_service: AccommodationService, city_service: CityService) -> None:
        self.travel_service = travel_service
        self.user_service = user_service
        self.ent_service = ent_service
        self.acc_service = acc_service
        self.city_service = city_service
        logger.debug("TravelController initialized")

    async def create_travel(self, data: TravelCreate) -> TravelResponse:
        """Создать новое путешествие"""
        try:
            users = [await self.user_service.get_by_id(uid) for uid in data.user_ids]
            entertainments = [await self.ent_service.get_by_id(eid) for eid in data.entertainment_ids]
            accommodations = [await self.acc_service.get_by_id(aid) for aid in data.accommodation_ids]

            travel = Travel(
                travel_id=1,
                status=data.status,
                users=[u for u in users if u],
                entertainments=[e for e in entertainments if e],
                accommodations=[a for a in accommodations if a],
            )
            created = await self.travel_service.add(travel)
            logger.info(f"Создано путешествие ID {created.travel_id}")
            return TravelResponse(
                id=created.travel_id,
                status=created.status,
                user_ids=[u.user_id for u in created.users],
                entertainment_ids=[e.entertainment_id for e in created.entertainments],
                accommodation_ids=[a.accommodation_id for a in created.accommodations],
            )
        except Exception as e:
            logger.error(f"Ошибка при создании путешествия: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Error creating travel")

    async def get_all_travels(self) -> List[TravelResponse]:
        """Получить список всех путешествий"""
        try:
            travels = await self.travel_service.get_all_travels()
            if not travels:
                logger.warning("Путешествия не найдены")
                return []
            return [
                TravelResponse(
                    id=t.travel_id,
                    status=t.status,
                    user_ids=[u.user_id for u in t.users],
                    entertainment_ids=[e.entertainment_id for e in t.entertainments],
                    accommodation_ids=[a.accommodation_id for a in t.accommodations],
                )
                for t in travels
            ]
        except Exception as e:
            logger.error(f"Ошибка при получении списка путешествий: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Error fetching travels")

    async def get_travel_by_id(self, travel_id: int) -> Optional[TravelResponse]:
        """Получить путешествие по ID"""
        try:
            travel = await self.travel_service.get_by_id(travel_id)
            if not travel:
                logger.warning(f"Путешествие ID {travel_id} не найдено")
                return None
            return TravelResponse(
                id=travel.travel_id,
                status=travel.status,
                user_ids=[u.user_id for u in travel.users],
                entertainment_ids=[e.entertainment_id for e in travel.entertainments],
                accommodation_ids=[a.accommodation_id for a in travel.accommodations],
            )
        except Exception as e:
            logger.error(f"Ошибка при получении путешествия ID {travel_id}: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Error fetching travel")

    async def update_travel(self, travel_id: int, data: TravelUpdate) -> Optional[TravelResponse]:
        """Обновить данные путешествия"""
        try:
            existing = await self.travel_service.get_by_id(travel_id)
            if not existing:
                logger.warning(f"Путешествие ID {travel_id} не найдено для обновления")
                return None

            users = (
                [await self.user_service.get_by_id(uid) for uid in data.user_ids]
                if data.user_ids else existing.users
            )
            entertainments = (
                [await self.ent_service.get_by_id(eid) for eid in data.entertainment_ids]
                if data.entertainment_ids else existing.entertainments
            )
            accommodations = (
                [await self.acc_service.get_by_id(aid) for aid in data.accommodation_ids]
                if data.accommodation_ids else existing.accommodations
            )

            travel = Travel(
                travel_id=travel_id,
                status=data.status or existing.status,
                users=[u for u in users if u],
                entertainments=[e for e in entertainments if e],
                accommodations=[a for a in accommodations if a],
            )
            updated = await self.travel_service.update(travel)
            logger.info(f"Путешествие ID {travel_id} обновлено")
            return TravelResponse(
                id=updated.travel_id,
                status=updated.status,
                user_ids=[u.user_id for u in updated.users],
                entertainment_ids=[e.entertainment_id for e in updated.entertainments],
                accommodation_ids=[a.accommodation_id for a in updated.accommodations],
            )
        except Exception as e:
            logger.error(f"Ошибка при обновлении путешествия ID {travel_id}: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Error updating travel")

    async def delete_travel(self, travel_id: int) -> None:
        """Удалить путешествие"""
        try:
            await self.travel_service.delete(travel_id)
            logger.info(f"Путешествие ID {travel_id} удалено")
        except Exception as e:
            logger.error(f"Ошибка при удалении путешествия ID {travel_id}: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Error deleting travel")

    async def complete_travel(self, travel_id: int) -> TravelResponse:
        """Завершить путешествие"""
        try:
            completed = await self.travel_service.complete(travel_id)
            if not completed:
                raise HTTPException(status_code=404, detail="Travel not found")
            logger.info(f"Путешествие ID {travel_id} завершено")
            return TravelResponse(
                id=completed.travel_id,
                status=completed.status,
                user_ids=[u.user_id for u in completed.users],
                entertainment_ids=[e.entertainment_id for e in completed.entertainments],
                accommodation_ids=[a.accommodation_id for a in completed.accommodations],
            )
        except Exception as e:
            logger.error(f"Ошибка при завершении путешествия ID {travel_id}: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Error completing travel")

    async def add_entertainment_to_travel(self, travel_id: int, data: EntertainmentCreate) -> EntertainmentResponse:
        try:
            travel = await self.travel_service.get_by_id(travel_id)
            if not travel:
                logger.warning(f"Путешествие ID {travel_id} не найдено")
                raise KeyError("Travel not found")
            city = await self.city_service.get_by_id(data.city_id)
            if not city:
                raise HTTPException(status_code=404, detail="City not found")
            data = Entertainment(
                entertainment_id=1,
                city=city,
                event_name=data.event_name,
                event_time=data.event_time.replace(tzinfo=None),
                duration=data.duration,
                address=data.address,
            )
            entertainment = await self.ent_service.add(data)
            logger.info(f"Создано развлечение ID {entertainment.entertainment_id}")

            entertainments = await self.travel_service.get_entertainments_by_travel(travel_id)
            ent_ids = [e.entertainment_id for e in entertainments]
            ent_ids.append(entertainment.entertainment_id)
            await self.travel_service.link_entertainments(travel_id, ent_ids)

            return EntertainmentResponse(
                entertainment_id=entertainment.entertainment_id,
                event_name=entertainment.event_name,
                city_id=entertainment.city.city_id,
                duration=entertainment.duration,
                address=entertainment.address,
                event_time=entertainment.event_time,
            )
        except Exception as e:
            logger.error(f"Ошибка при добавлении развлечения к путешествию {travel_id}: {e}", exc_info=True)
            raise

    async def delete_entertainment_from_travel(self, travel_id: int, entertainment_id: int) -> None:
        try:
            travel = await self.travel_service.get_by_id(travel_id)
            if not travel:
                logger.warning(f"Путешествие ID {travel_id} не найдено")
                raise KeyError("Travel not found")

            await self.travel_service.unlink_entertainment(travel_id, entertainment_id)
            logger.info(f"Развлечение ID {entertainment_id} удалено из путешествия ID {travel_id}")
        except Exception as e:
            logger.error(f"Ошибка при удалении развлечения из путешествия {travel_id}: {e}", exc_info=True)
            raise

    
    async def add_accommodation_to_travel(self, travel_id: int, data: AccommodationCreate) -> AccommodationResponse:
        try:
            travel = await self.travel_service.get_by_id(travel_id)
            if not travel:
                logger.warning(f"Путешествие ID {travel_id} не найдено")
                raise KeyError("Travel not found")
            city = await self.city_service.get_by_id(data.city_id)
            if not city:
                raise HTTPException(status_code=404, detail="City not found")
            data = Accommodation(
                accommodation_id=1,
                city=city,
                name=data.name,
                price=data.price,
                check_in=data.check_in.replace(tzinfo=None),
                check_out=data.check_out.replace(tzinfo=None),
                type=data.type,
                rating=data.rating,
                address=data.address,
            )
            accommodation = await self.acc_service.add(data)
            logger.info(f"Создано размещение ID {accommodation.accommodation_id}")

            accommodations = await self.travel_service.get_accommodations_by_travel(travel_id)
            acc_ids = [a.accommodation_id for a in accommodations]
            acc_ids.append(accommodation.accommodation_id)
            await self.travel_service.link_accommodations(travel_id, acc_ids)

            return AccommodationResponse(
                accommodation_id=accommodation.accommodation_id,
                price=accommodation.price,
                city_id=accommodation.city.city_id,
                name=accommodation.name,
                address=accommodation.address,
                type=accommodation.type,
                rating=accommodation.rating,
                check_in=accommodation.check_in,
                check_out=accommodation.check_out
            )
        except Exception as e:
            logger.error(f"Ошибка при добавлении развлечения к путешествию {travel_id}: {e}", exc_info=True)
            raise

    async def delete_accommodation_from_travel(self, travel_id: int, accommodation_id: int) -> None:
        """Удалить развлечение из путешествия"""
        try:
            travel = await self.travel_service.get_by_id(travel_id)
            if not travel:
                logger.warning(f"Путешествие ID {travel_id} не найдено")
                raise KeyError("Travel not found")

            await self.travel_service.unlink_accommodation(travel_id, accommodation_id)
            logger.info(f"Развлечение ID {accommodation_id} удалено из путешествия ID {travel_id}")
        except Exception as e:
            logger.error(f"Ошибка при удалении развлечения из путешествия {travel_id}: {e}", exc_info=True)
            raise