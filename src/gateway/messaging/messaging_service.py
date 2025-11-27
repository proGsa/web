import aio_pika
import asyncio
import json
import logging
import uuid
from typing import Any

logger = logging.getLogger(__name__)

RABBIT_URL = "amqp://user:pass@rabbitmq:5672/"

class MessagingService:
    def __init__(self, rabbit_url: str = RABBIT_URL):
        self.rabbit_url = rabbit_url
        self.connection = None
        self.channel = None
        self.callback_queue = None
        self.req_exchange = None
        self.resp_exchange = None
        self.futures = {}

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.rabbit_url)
        self.channel = await self.connection.channel()

        # Exchange для отправки запросов в Core
        self.req_exchange = await self.channel.declare_exchange(
            "gw_exchange", aio_pika.ExchangeType.DIRECT, durable=True
        )

        # Exchange для получения ответов от Core
        self.resp_exchange = await self.channel.declare_exchange(
            "core_exchange", aio_pika.ExchangeType.DIRECT, durable=True
        )

        # Временная очередь для ответов
        self.callback_queue = await self.channel.declare_queue(exclusive=True)

        logger.info(f"[GW] Callback queue = {self.callback_queue.name}")

        await self.callback_queue.bind(
            self.resp_exchange, 
            routing_key=self.callback_queue.name
        )
        logger.info(f"[GW] Bound to core_exchange with key {self.callback_queue.name}")

        await self.callback_queue.consume(self.on_response)

    async def on_response(self, message: aio_pika.IncomingMessage):
        async with message.process():
            correlation_id = message.correlation_id
            logger.info(f"[GW] Received response for {correlation_id}")

            if correlation_id in self.futures:
                self.futures[correlation_id].set_result(
                    json.loads(message.body)
                )
                del self.futures[correlation_id]

    async def rpc_call(self, action: str, payload: dict[str, Any], timeout=20):
        correlation_id = str(uuid.uuid4())
        future = asyncio.get_event_loop().create_future()
        self.futures[correlation_id] = future

        body = json.dumps({
            "action": action,
            "payload": payload
        }).encode()

        logger.info(f"[GW] Sending RPC {action} corr={correlation_id}")

        await self.req_exchange.publish(
            aio_pika.Message(
                body=body,
                correlation_id=correlation_id,
                reply_to=self.callback_queue.name
            ),
            routing_key="core_input"
        )

        try:
            return await asyncio.wait_for(future, timeout)
        except asyncio.TimeoutError:
            self.futures.pop(correlation_id, None)
            raise RuntimeError(f"RPC timeout: {action}")
