import uuid
import orjson
from fastapi import APIRouter, Depends, HTTPException
from redis.asyncio import Redis

from api.web.schemas.weather import WeatherRequestSchema
from src.redis_tools.tools import get_redis
from src.services.data_cleaner import clean_city_name
from src.services.file_writer import save_to_file, get_file_path
from src.services.weather_api import transform_weather_response
from src.tasks import process_weather_data

weather_router = APIRouter()


@weather_router.post("/weather")
async def get_weather(request: WeatherRequestSchema, redis_client: Redis = Depends(get_redis)):
    task_id = str(uuid.uuid4())
    await redis_client.set(task_id, orjson.dumps({"status": "running"}).decode())

    cities = [await clean_city_name(city) for city in request.cities]
    results = await process_weather_data(cities, task_id, redis_client)

    transformed_results = {
        "status": "completed" if results else "failed",
        "results": transform_weather_response(results.values()).results
    }

    if results:
        file_path = get_file_path(task_id, transformed_results["results"])
        await save_to_file(task_id, transformed_results)
        transformed_results["file_url"] = file_path

    await redis_client.set(task_id, orjson.dumps(transformed_results).decode())
    return transformed_results


@weather_router.get("/tasks/{task_id}")
async def get_task_status(task_id: str, redis_client: Redis = Depends(get_redis)):
    task_data = await redis_client.get(task_id)
    if not task_data:
        raise HTTPException(
            status_code=404,
            detail=f"Task with ID '{task_id}' not found"
        )

    task_info = orjson.loads(task_data)
    response = {
        "status": task_info["status"],
    }
    return response
