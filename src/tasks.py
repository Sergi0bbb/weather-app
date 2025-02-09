from typing import List

import orjson
from redis.asyncio import Redis
from src.services.file_writer import save_to_file
from src.services.weather_api import fetch_weather


async def process_weather_data(cities: List[str], task_id: str, redis_client: Redis):
    results = {}
    for city in cities:
        weather_data = await fetch_weather(city)
        results[city] = weather_data

    data = orjson.loads(await redis_client.get(task_id) or "{}")
    await save_to_file(task_id, data)
    return results
