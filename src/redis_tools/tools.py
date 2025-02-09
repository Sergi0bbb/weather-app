import logging

import orjson
from redis.asyncio import Redis
from src.configs.external.redis import RedisConfig

redis_config = RedisConfig()


async def get_redis() -> Redis:
    return Redis(host=redis_config.REDIS_HOST, port=int(redis_config.REDIS_PORT))


async def store_task_result(redis_client: Redis, task_id: str, data: dict):
    await redis_client.set(task_id, orjson.dumps(data))


async def get_task_status(redis_client: Redis, task_id: str) -> dict:
    task_data = await redis_client.get(task_id)
    if not task_data:
        return {"error": "Task ID not found"}
    return orjson.loads(task_data)
