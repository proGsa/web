from __future__ import annotations

import asyncio
import logging

from dataclasses import dataclass
from typing import Any

from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from .abstract_repository.iaccommodation_repository import IAccommodationRepository
from .abstract_repository.icity_repository import ICityRepository
from .abstract_repository.idirectory_route_repository import IDirectoryRouteRepository
from .abstract_repository.ientertainment_repository import IEntertainmentRepository
from .abstract_repository.iroute_repository import IRouteRepository
from .abstract_repository.itravel_repository import ITravelRepository
from .abstract_repository.iuser_repository import IUserRepository
from .repository.accommodation_repository import AccommodationRepository
from .repository.city_repository import CityRepository
from .repository.directory_route_repository import DirectoryRouteRepository
from .repository.entertainment_repository import EntertainmentRepository
from .repository.route_repository import RouteRepository
from .repository.travel_repository import TravelRepository
from .repository.user_repository import UserRepository
from .repository_mongodb.accommodation_repository import AccommodationRepository as MongoAccommodationRepository
from .repository_mongodb.city_repository import CityRepository as MongoCityRepository
from .repository_mongodb.directory_route_repository import DirectoryRouteRepository as MongoDirectoryRouteRepository
from .repository_mongodb.entertainment_repository import EntertainmentRepository as MongoEntertainmentRepository
from .repository_mongodb.route_repository import RouteRepository as MongoRouteRepository
from .repository_mongodb.travel_repository import TravelRepository as MongoTravelRepository
from .repository_mongodb.user_repository import UserRepository as MongoUserRepository
from .settings import settings


logger = logging.getLogger(__name__)

_mongo_client: AsyncIOMotorClient[Any] | None = None
_async_session_maker = None


@dataclass
class Repositories:
    def __init__(
            self,
            acc_repo: IAccommodationRepository,
            city_repo: ICityRepository,
            d_route_repo: IDirectoryRouteRepository,
            ent_repo: IEntertainmentRepository,
            route_repo: IRouteRepository,
            travel_repo: ITravelRepository,
            user_repo: IUserRepository
        ):
        self.acc_repo = acc_repo
        self.city_repo = city_repo
        self.d_route_repo = d_route_repo
        self.ent_repo = ent_repo
        self.route_repo = route_repo
        self.travel_repo = travel_repo
        self.user_repo = user_repo
        
class DataServiceLocator:
    def __init__(self, repositories: Repositories):
        self.repositories = repositories

    def get_acc_repo(self) -> IAccommodationRepository:
        return self.repositories.acc_repo

    def get_city_repo(self) -> ICityRepository:
        return self.repositories.city_repo

    def get_d_route_repo(self) -> IDirectoryRouteRepository:
        return self.repositories.d_route_repo

    def get_ent_repo(self) -> IEntertainmentRepository:
        return self.repositories.ent_repo

    def get_route_repo(self) -> IRouteRepository:
        return self.repositories.route_repo

    def get_travel_repo(self) -> ITravelRepository:
        return self.repositories.travel_repo

    def get_user_repo(self) -> IUserRepository:
        return self.repositories.user_repo

    
async def get_sessionmaker(max_retries: int = 5, delay: int = 2) -> Any: 
    global _async_session_maker
    if _async_session_maker is not None:
        return _async_session_maker
    engine = create_async_engine(
        settings.DATABASE_URL_ASYNC,
        connect_args={
            "server_settings": {
                "search_path": "travel_db" 
            }
        },
        echo=True,
        pool_pre_ping=True
    )   
    for attempt in range(max_retries):
        try:
            return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        except OperationalError as e:
            logger.error(f"Ошибка подключения к БД: {e}")
            if attempt < max_retries - 1:
                logger.info(f"Повторная попытка подключения через {delay} секунд...")
                await asyncio.sleep(delay)
            else:
                raise RuntimeError("Не удалось подключиться к базе данных после нескольких попыток.")
    return None

class DataServiceLocator:
    def __init__(self):
        self._repositories: Repositories | None = None

    async def init_repositories(self):
        global _mongo_client, _async_session_maker
        
        db_type = "mongo" if "mongo" in settings.DATABASE_URL_ASYNC else "postgres"
        
        if db_type == "mongo":
            if _mongo_client is None:
                _mongo_client = AsyncIOMotorClient(settings.DATABASE_URL_ASYNC)
            mongo_client: AsyncIOMotorClient[Any] = _mongo_client
            city_repo = MongoCityRepository(mongo_client)
            d_route_repo = MongoDirectoryRouteRepository(mongo_client, city_repo)
            acc_repo = MongoAccommodationRepository(mongo_client, city_repo)
            ent_repo = MongoEntertainmentRepository(mongo_client, city_repo)
            user_repo = MongoUserRepository(mongo_client)
            travel_repo = MongoTravelRepository(mongo_client, user_repo, ent_repo, acc_repo)
            route_repo = MongoRouteRepository(mongo_client, d_route_repo, travel_repo)
        else:
            if _async_session_maker is None:
                _async_session_maker = await get_sessionmaker()
            async with _async_session_maker() as session:
                city_repo = CityRepository(session)
                d_route_repo = DirectoryRouteRepository(session, city_repo)
                acc_repo = AccommodationRepository(session, city_repo)
                ent_repo = EntertainmentRepository(session, city_repo)
                user_repo = UserRepository(session)
                travel_repo = TravelRepository(session, user_repo, ent_repo, acc_repo)
                route_repo = RouteRepository(session, d_route_repo, travel_repo)

        self._repositories = Repositories(
            acc_repo, city_repo, d_route_repo, ent_repo, route_repo, travel_repo, user_repo
        )

    @property
    def repositories(self) -> Repositories:
        if self._repositories is None:
            raise RuntimeError("Repositories not initialized. Call 'init_repositories()' first.")
        return self._repositories

    # Геттеры для репозиториев
    async def get_acc_repo(self) -> IAccommodationRepository:
        return self.repositories.acc_repo

    async def get_city_repo(self) -> ICityRepository:
        return self.repositories.city_repo

    async def get_d_route_repo(self) -> IDirectoryRouteRepository:
        return self.repositories.d_route_repo

    async def get_ent_repo(self) -> IEntertainmentRepository:
        return self.repositories.ent_repo

    async def get_route_repo(self) -> IRouteRepository:
        return self.repositories.route_repo

    async def get_travel_repo(self) -> ITravelRepository:
        return self.repositories.travel_repo

    async def get_user_repo(self) -> IUserRepository:
        return self.repositories.user_repo


_service_locator: DataServiceLocator | None = None

async def get_service_locator() -> DataServiceLocator:
    global _service_locator
    if _service_locator is None:
        _service_locator = DataServiceLocator()
        await _service_locator.init_repositories()
    return _service_locator