import asyncio
import aio_pika
import json
from ..services.city_service import CityService
from ..services.user_service import UserService, AuthService
from ..services.accommodation_service import AccommodationService
from ..services.directory_route_service import DirectoryRouteService
from ..services.entertainment_service import EntertainmentService
from ..services.route_service import RouteService
from ..services.travel_service import TravelService
import logging
import uuid

RABBIT_URL = "amqp://user:pass@rabbitmq:5672/"
logger = logging.getLogger(__name__)

class CoreRPCServer:
    def __init__(
        self,
        rabbit_url: str = "amqp://user:pass@rabbitmq:5672/",
        city_service: CityService = None,
        user_service: UserService = None,
        acc_service: AccommodationService = None,
        d_route_service: DirectoryRouteService = None,
        ent_service: EntertainmentService = None,
        route_service: RouteService = None,
        travel_service: TravelService = None,
        auth_service: AuthService = None
    ):
        self.rabbit_url = rabbit_url
        self.connection = None
        self.channel = None
        self.queue_name = "core_input"

        self.city_service = city_service
        self.user_service = user_service
        self.accommodation_service = acc_service
        self.d_route_service = d_route_service
        self.ent_service = ent_service
        self.route_service = route_service
        self.travel_service = travel_service
        self.auth_service = auth_service
        # --- ✔ Action Map остаётся без изменений ---
        self.action_map = {
            "core_city_get_all": self.city_service.get_all_cities,
            "core_city_create": self.city_service.add,
            "core_city_get": self.city_service.get_by_id,
            "core_city_update": self.city_service.update,
            "core_city_delete": self.city_service.delete,

            "core_user_create": self.user_service.add,
            "core_user_update": self.user_service.update,
            "core_user_delete": self.user_service.delete,
            "core_user_get_profile": self.user_service.get_by_id,
            "core_user_get_all": self.user_service.get_list,
            "core_user_register": self.auth_service.registrate,
            "core_user_login": self.auth_service.authenticate,

            "core_accommodation_create": self.accommodation_service.add,
            "core_accommodation_get_all": self.accommodation_service.get_list,
            "core_accommodation_get": self.accommodation_service.get_by_id,
            "core_accommodation_update": self.accommodation_service.update,
            "core_accommodation_delete": self.accommodation_service.delete,
            # "core_travel_link_accommodations": self.accommodation_service.link_to_travel,
            # "core_travel_add_accommodation": self.accommodation_service.add_to_travel,
            # "core_travel_delete_accommodation": self.accommodation_service.delete_from_travel,

            "core_d_route_create": self.d_route_service.add,
            "core_d_route_get_all": self.d_route_service.get_list,
            "core_d_route_get": self.d_route_service.get_by_id,
            "core_d_route_update": self.d_route_service.update,
            "core_d_route_delete": self.d_route_service.delete,
            # "core_d_route_partial_update": self.d_route_service.partial_update_d_route,

            "core_entertainment_create": self.ent_service.add,
            "core_entertainment_get_all": self.ent_service.get_list,
            "core_entertainment_get": self.ent_service.get_by_id,
            "core_entertainment_update": self.ent_service.update,
            "core_entertainment_delete": self.ent_service.delete,
            # "core_entertainment_update_dates": self.ent_service.update_dates,
            # "core_travel_add_entertainment": self.ent_service.add_to_travel,
            # "core_travel_delete_entertainment": self.ent_service.delete_from_travel,

            "core_route_create": self.route_service.add,
            "core_route_get_all": self.route_service.get_all_routes,
            "core_route_get": self.route_service.get_by_id,
            "core_route_update": self.route_service.update,
            "core_route_delete": self.route_service.delete,
            "core_route_get_parts": self.route_service.get_route_parts,
            "core_route_change_transport": self.route_service.change_transport,
            "core_route_delete_city": self.route_service.delete_city_from_route,
            # "core_route_add_city": self.route_service.add_city,
            # "core_route_extend_duration": self.route_service.extend_duration,
            "core_route_insert_city_after": self.route_service.insert_city_after,

            "core_travel_create": self.travel_service.add,
            "core_travel_get_all": self.travel_service.get_all_travels,
            "core_travel_get": self.travel_service.get_by_id,
            "core_travel_update": self.travel_service.update,
            "core_travel_delete": self.travel_service.delete,
            "core_travel_complete": self.travel_service.complete,
        }

        # При подключении
    async def connect(self):
        logger.info("CoreRPCServer connecting...")

        self.connection = await aio_pika.connect_robust(self.rabbit_url)
        self.channel = await self.connection.channel()

        # Exchange для приёма запросов (от Gateway)
        self.req_exchange = await self.channel.declare_exchange(
            "gw_exchange", aio_pika.ExchangeType.DIRECT, durable=True
        )

        # Exchange для ответов (в Gateway)
        self.resp_exchange = await self.channel.declare_exchange(
            "core_exchange", aio_pika.ExchangeType.DIRECT, durable=True
        )

        # Core input queue
        self.queue = await self.channel.declare_queue("core_input", durable=True)
        await self.queue.bind(self.req_exchange, routing_key="core_input")

        await self.queue.consume(self.on_message)

        logger.info("CoreRPCServer ready and listening on core_input")

    async def on_message(self, message: aio_pika.IncomingMessage):
        async with message.process():
            try:
                data = json.loads(message.body)
                action = data["action"]
                payload = data.get("payload")

                logger.info(f"[Core] Received action={action}, payload={payload}")

                if action not in self.action_map:
                    response = {"error": f"Unknown action {action}"}
                else:
                    result = await self.action_map[action](payload)
                    logger.info("result: %s", result)
                    response = result
            except Exception as e:
                logger.exception("Core RPC error")
                response = {"error": str(e)}

            # ответ Gateway
            await self.resp_exchange.publish(
                aio_pika.Message(
                    body=json.dumps(response).encode(),
                    correlation_id=message.correlation_id
                ),
                routing_key=message.reply_to
            )
            logger.info(f"[Core] Received message: {message.body.decode()}")
            logger.info(f"[Core] Available actions: {list(self.action_map.keys())}")

    # async def connect(self):
    #     self.connection = await aio_pika.connect_robust(RABBIT_URL)
    #     self.channel = await self.connection.channel()

    #     # Exchanges
    #     self.req_exchange = await self.channel.declare_exchange(
    #         "gw_exchange", aio_pika.ExchangeType.DIRECT, durable=True
    #     )
    #     self.resp_exchange = await self.channel.declare_exchange(
    #         "core_exchange", aio_pika.ExchangeType.DIRECT, durable=True
    #     )

    #     # Queue
    #     self.queue = await self.channel.declare_queue(self.queue_name, durable=True)
    #     await self.queue.bind(self.req_exchange, routing_key=self.queue_name)
    #     await self.queue.consume(self.on_message)

    #     print("CoreRPCServer: Listening for RPC requests...")

    # async def on_message(self, message: aio_pika.IncomingMessage):
    #     async with message.process():
    #         try:
    #             data = json.loads(message.body)
    #             action = data.get("action")
    #             payload = data.get("payload", {})

    #             if action not in self.action_map:
    #                 response = {"error": f"Unknown action: {action}"}
    #             else:
    #                 method = self.action_map[action]

    #                 # Если payload пустой, вызываем без аргументов
    #                 if payload:
    #                     response_data = await method(payload)
    #                 else:
    #                     response_data = await method()
                    
    #                 response = {"result": response_data}

    #         except Exception as e:
    #             response = {"error": str(e)}

    #         # Отправляем ответ в core_exchange
    #         await self.resp_exchange.publish(
    #             aio_pika.Message(
    #                 body=json.dumps(response).encode(),
    #                 correlation_id=message.correlation_id
    #             ),
    #             routing_key=message.reply_to
    #         )


class CoreRPCClient:
    def __init__(self, rabbit_url: str, queue_name="data_input"):
        self.rabbit_url = rabbit_url
        self.queue_name = queue_name
        self.connection = None
        self.channel = None
        self.callback_queue = None
        self.futures = {}  

    async def connect(self):
        logger.info("CoreRPCClient connecting...")

        self.connection = await aio_pika.connect_robust(self.rabbit_url)
        self.channel = await self.connection.channel()

        # Exchange куда отправляем запросы
        self.req_exchange = await self.channel.declare_exchange(
            "core_to_data_exchange", aio_pika.ExchangeType.DIRECT, durable=True
        )

        # Привязываем очередь к core_exchange (Core → Gateway)
        resp_exchange = await self.channel.declare_exchange(
            "data_to_core_exchange", aio_pika.ExchangeType.DIRECT, durable=True
        )
        self.callback_queue = await self.channel.declare_queue(exclusive=True)

        await self.callback_queue.bind(
            resp_exchange,
            routing_key=self.callback_queue.name
        )

        await self.callback_queue.consume(self.on_response)

        logger.info("CoreRPCClient ready.")

    async def on_response(self, message: aio_pika.IncomingMessage):
        async with message.process():
            corr = message.correlation_id
            if corr in self.futures:
                fut = self.futures.pop(corr)
                fut.set_result(json.loads(message.body))

    async def call(self, action: str, payload: dict, timeout=10):
        correlation_id = str(uuid.uuid4())
        fut = asyncio.get_running_loop().create_future()
        self.futures[correlation_id] = fut

        msg = aio_pika.Message(
            body=json.dumps({"action": action, "payload": payload}).encode(),
            correlation_id=correlation_id,
            reply_to=self.callback_queue.name
        )

        # Отправляем в Core → gw_exchange
        await self.req_exchange.publish(msg, routing_key="data_input")
        logger.info("call core_rpc_client")
        return await fut