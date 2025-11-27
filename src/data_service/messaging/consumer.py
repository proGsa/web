# import asyncio
# import aio_pika
# import json
# from .service_locator import get_service_locator

# RABBIT_URL = "amqp://user:pass@rabbitmq:5672/"


# class DataServiceRPCServer:
#     def __init__(self, locator):
#         self.locator = locator
#         self.queue_name = "data_queue"
#         self.connection = None
#         self.channel = None
#         self.action_map = {
#             "get_city": self.get_city,
#             "add_city": self.add_city,

#         }
#     async def connect(self):
#         self.connection = await aio_pika.connect_robust(self.rabbit_url)
#         self.channel = await self.connection.channel()

#         # Очередь для запросов от Core
#         queue = await self.channel.declare_queue(self.queue_name, durable=True)
#         await queue.consume(self.on_message)
#         print("DataService listening...")

#     async def on_message(self, message: aio_pika.IncomingMessage):
#         async with message.process():
#             data = json.loads(message.body)
#             action = data.get("action")
#             payload = data.get("payload", {})

#             if action not in self.action_map:
#                 response = {"error": f"Unknown action {action}"}
#             else:
#                 result = await self.action_map[action](payload)
#                 response = {"result": result}

#             # Отправка ответа обратно Core
#             await self.channel.default_exchange.publish(
#                 aio_pika.Message(
#                     body=json.dumps(response).encode(),
#                     correlation_id=message.correlation_id
#                 ),
#                 routing_key=message.reply_to
#             )
#     async def shutdown(self):
#         if self.queue:
#             await self.queue.cancel()
#         if self.channel:
#             await self.channel.close()
#             print("DataServiceRPCServer channel closed")
#         if self.connection:
#             await self.connection.close()
#             print("DataServiceRPCServer connection closed")
import asyncio
import aio_pika
import json
from ..service_locator import get_service_locator
from ..shared.models.city import City
from ..shared.models.accommodation import Accommodation
from ..shared.models.directory_route import DirectoryRoute
from ..shared.models.entertainment import Entertainment
from ..shared.models.route import Route
from ..shared.models.travel import Travel
from ..shared.models.user import User
import logging

RABBIT_URL = "amqp://user:pass@rabbitmq:5672/"
logger = logging.getLogger(__name__)


class DataServiceRPCServer:
    def __init__(self, locator):
        self.locator = locator
        self.queue_name = "data_queue"
        self.connection = None
        self.channel = None

        self.city_repo = locator.repositories.city_repo
        self.user_repo = locator.repositories.user_repo
        self.acc_repo = locator.repositories.acc_repo
        self.d_route_repo = locator.repositories.d_route_repo
        self.ent_repo = locator.repositories.ent_repo
        self.route_repo = locator.repositories.route_repo
        self.travel_repo = locator.repositories.travel_repo

        self.action_map = {
            # --- CITY ---
            "core_city_get_all": self.get_city_list,
            "core_city_create": self.add_city,
            "core_city_get": self.get_city,
            "core_city_update": self.update_city,
            "core_city_delete": self.delete_city,

            # --- USER ---
            "core_user_create": self.user_repo.add,
            "core_user_update": self.user_repo.update,
            "core_user_delete": self.user_repo.delete,
            "core_user_get_profile": self.user_repo.get_by_id,
            "core_user_get_all": self.user_repo.get_list,

            # auth
            "core_user_register": self.user_repo.add,
            "core_user_login": self.user_repo.get_by_login,

            # --- ACCOMMODATION ---
            "core_accommodation_create": self.acc_repo.add,
            "core_accommodation_get_all": self.get_acc_list,
            "core_accommodation_get": self.acc_repo.get_by_id,
            "core_accommodation_update": self.acc_repo.update,
            "core_accommodation_delete": self.acc_repo.delete,

            # --- D_ROUTE ---
            "core_d_route_create": self.d_route_repo.add,
            "core_d_route_get_all": self.d_route_repo.get_list,
            "core_d_route_get": self.d_route_repo.get_by_id,
            "core_d_route_update": self.d_route_repo.update,
            "core_d_route_delete": self.d_route_repo.delete,

            # --- ENTERTAINMENT ---
            "core_entertainment_create": self.ent_repo.add,
            "core_entertainment_get_all": self.ent_repo.get_list,
            "core_entertainment_get": self.ent_repo.get_by_id,
            "core_entertainment_update": self.ent_repo.update,
            "core_entertainment_delete": self.ent_repo.delete,

            # --- ROUTE ---
            "core_route_create": self.route_repo.add,
            "core_route_get_all": self.route_repo.get_list,
            "core_route_get": self.route_repo.get_by_id,
            "core_route_update": self.route_repo.update,
            "core_route_delete": self.route_repo.delete,
            "core_route_get_parts": self.route_repo.get_route_parts,
            "core_route_change_transport": self.route_repo.change_transport,
            "core_route_delete_city": self.route_repo.delete_city_from_route,
            "core_route_insert_city_after": self.route_repo.insert_city_after,

            # --- TRAVEL ---
            "core_travel_create": self.travel_repo.add,
            "core_travel_get_all": self.travel_repo.get_list,
            "core_travel_get": self.travel_repo.get_by_id,
            "core_travel_update": self.travel_repo.update,
            "core_travel_delete": self.travel_repo.delete,
            "core_travel_complete": self.travel_repo.complete,
        }


    async def connect(self):
        self.connection = await aio_pika.connect_robust(RABBIT_URL)
        self.channel = await self.connection.channel()

        # Core -> Data exchange
        self.req_exchange = await self.channel.declare_exchange(
            "core_to_data_exchange", aio_pika.ExchangeType.DIRECT, durable=True
        )

        # Очередь, которую слушает Data
        self.queue = await self.channel.declare_queue("data_input", durable=True)
        await self.queue.bind(self.req_exchange, routing_key="data_input")

        # Data -> Core exchange (для ответов)
        self.resp_exchange = await self.channel.declare_exchange(
            "data_to_core_exchange", aio_pika.ExchangeType.DIRECT, durable=True
        )

        # Data слушает только data_input
        await self.queue.consume(self.on_message)

        logger.info("DataService RPC ready. Listening on queue: data_input")


    async def on_message(self, message: aio_pika.IncomingMessage):
        async with message.process():
            data = json.loads(message.body)
            action = data["action"]
            payload = data.get("payload", {})

            if action not in self.action_map:
                response = {"error": f"Unknown action {action}"}
            else:
                result = await self.action_map[action](payload)
                response = {"result": result}

            # Ответ Core’у в его callback_queue
            await self.resp_exchange.publish(
                aio_pika.Message(
                    body=json.dumps(response).encode(),
                    correlation_id=message.correlation_id
                ),
                routing_key=message.reply_to
            )


    async def shutdown(self):
        if self.channel:
            await self.channel.close()
            print("DataServiceRPCServer channel closed")
        if self.connection:
            await self.connection.close()
            print("DataServiceRPCServer connection closed")

    # =======================
    # City
    # =======================
    async def get_city_list(self, payload=None):
        items = await self.city_repo.get_list()
        return [{"city_id": c["city_id"], "name": c["name"]} for c in items]

    async def get_city(self, payload):
        city_id = payload.get("city_id")
        city = await self.city_repo.get_by_id(city_id)
        return {"city_id": city.city_id, "name": city.name}

    async def add_city(self, payload):
        city = await self.city_repo.add(City(city_id=1, name=payload.get("name")))
        return {"city_id": city.city_id, "name": city.name}

    async def update_city(self, payload):
        city = City(city_id=payload.get("city_id"), name=payload.get("name"))
        await self.city_repo.update(city)
        updated_city = await self.city_repo.get_by_id(payload.get("city_id"))
        return {"city_id": updated_city.city_id, "name": updated_city.name}

    async def delete_city(self, payload):
        await self.city_repo.delete(payload.get("city_id"))
        return {"status": "ok"}

    # =======================
    # Accommodation
    # =======================
    async def get_acc_list(self, payload=None):
        items = await self.acc_repo.get_list()
        result = []
        for acc in items:
            city_obj = await self.city_repo.get_by_id(acc.city.city_id)
            result.append({
                "accommodation_id": acc.accommodation_id,
                "name": acc.name,
                "city": {
                    "city_id": city_obj.city_id,
                    "name": city_obj.name
                },
                "address": acc.address,
                "price": acc.price,
                "type": acc.type,
                "rating": acc.rating,
                "check_in": acc.check_in.isoformat(),
                "check_out": acc.check_out.isoformat(),
            })
        return result

    async def get_accommodation(self, payload):
        repo = await self.locator.get_acc_repo()
        acc_id = payload.get("id")
        return await repo.get_by_id(acc_id)

    async def add_accommodation(self, payload):
        repo = await self.locator.get_acc_repo()
        acc = Accommodation(**payload)
        return await repo.add(acc)

    async def update_accommodation(self, payload):
        repo = await self.locator.get_acc_repo()
        acc = Accommodation(**payload)
        await repo.update(acc)
        return {"status": "ok"}

    async def delete_accommodation(self, payload):
        repo = await self.locator.get_acc_repo()
        await repo.delete(payload.get("id"))
        return {"status": "ok"}

    # =======================
    # DirectoryRoute
    # =======================
    async def get_d_route(self, payload):
        repo = await self.locator.get_d_route_repo()
        route_id = payload.get("id")
        return await repo.get_by_id(route_id)

    async def add_d_route(self, payload):
        repo = await self.locator.get_d_route_repo()
        route = DirectoryRoute(**payload)
        return await repo.add(route)

    async def update_d_route(self, payload):
        repo = await self.locator.get_d_route_repo()
        route = DirectoryRoute(**payload)
        await repo.update(route)
        return {"status": "ok"}

    async def delete_d_route(self, payload):
        repo = await self.locator.get_d_route_repo()
        await repo.delete(payload.get("id"))
        return {"status": "ok"}

    # =======================
    # Entertainment
    # =======================
    async def get_entertainment(self, payload):
        repo = await self.locator.get_ent_repo()
        ent_id = payload.get("id")
        return await repo.get_by_id(ent_id)

    async def add_entertainment(self, payload):
        repo = await self.locator.get_ent_repo()
        ent = Entertainment(**payload)
        return await repo.add(ent)

    async def update_entertainment(self, payload):
        repo = await self.locator.get_ent_repo()
        ent = Entertainment(**payload)
        await repo.update(ent)
        return {"status": "ok"}

    async def delete_entertainment(self, payload):
        repo = await self.locator.get_ent_repo()
        await repo.delete(payload.get("id"))
        return {"status": "ok"}

    # =======================
    # Route
    # =======================
    async def get_route(self, payload):
        repo = await self.locator.get_route_repo()
        route_id = payload.get("id")
        return await repo.get_by_id(route_id)

    async def add_route(self, payload):
        repo = await self.locator.get_route_repo()
        route = Route(**payload)
        return await repo.add(route)

    async def update_route(self, payload):
        repo = await self.locator.get_route_repo()
        route = Route(**payload)
        await repo.update(route)
        return {"status": "ok"}

    async def delete_route(self, payload):
        repo = await self.locator.get_route_repo()
        await repo.delete(payload.get("id"))
        return {"status": "ok"}

    # =======================
    # Travel
    # =======================
    async def get_travel(self, payload):
        repo = await self.locator.get_travel_repo()
        travel_id = payload.get("id")
        return await repo.get_by_id(travel_id)

    async def add_travel(self, payload):
        repo = await self.locator.get_travel_repo()
        travel = Travel(**payload)
        return await repo.add(travel)

    async def update_travel(self, payload):
        repo = await self.locator.get_travel_repo()
        travel = Travel(**payload)
        await repo.update(travel)
        return {"status": "ok"}

    async def delete_travel(self, payload):
        repo = await self.locator.get_travel_repo()
        await repo.delete(payload.get("id"))
        return {"status": "ok"}

    # =======================
    # User
    # =======================
    async def get_user(self, payload):
        repo = await self.locator.get_user_repo()
        user_id = payload.get("id")
        return await repo.get_by_id(user_id)

    async def add_user(self, payload):
        repo = await self.locator.get_user_repo()
        user = User(**payload)
        return await repo.add(user)

    async def update_user(self, payload):
        repo = await self.locator.get_user_repo()
        user = User(**payload)
        await repo.update(user)
        return {"status": "ok"}

    async def delete_user(self, payload):
        repo = await self.locator.get_user_repo()
        await repo.delete(payload.get("id"))
        return {"status": "ok"}
