import orjson
import uuid

from fastapi import APIRouter, HTTPException

from api.web.schemas.weather import WeatherRequestSchema
# from src.main import redis_client
from src.services.weather_api import transform_weather_response
from src.tasks import process_weather_data

weather_router = APIRouter()


@weather_router.post("/weather")
async def get_weather(weather_request: WeatherRequestSchema):
    cities = weather_request.cities
    task_id = str(uuid.uuid4())
    # await redis_client.set(task_id, orjson.dumps({"status": "running"}).decode())

    results = await process_weather_data(cities)
    transformed_results = ({
        "status": "completed",
        "results": transform_weather_response(results.values())
    })

    # await redis_client.set(task_id, orjson.dumps(transformed_results).decode())
    return transformed_results


# @weather_router.get("/tasks/{task_id}")
# async def get_task_status(task_id: str):
#     task_data = await redis_client.get(task_id)
#     if not task_data:
#         raise HTTPException(status_code=404, detail="Task ID not found")
#     return orjson.loads(task_data).encode()
