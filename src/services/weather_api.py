import logging

import httpx

from api.web.schemas.weather import WeatherResponseSchema, WeatherDetailSchema
from src.configs.external.weather import WeatherConfig
from src.models.api.weather import WeatherApiModel

logging.basicConfig(level=logging.INFO)


async def fetch_weather(city: str):
    weather_config = WeatherConfig()
    params = {"key": weather_config.WEATHER_API_KEY, "q": city}
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(weather_config.WEATHER_API_URL, params=params)
        response.raise_for_status()

        return WeatherApiModel.model_validate(response.json())

    except httpx.HTTPStatusError as e:
        logging.error(f"API error for {city}: {e}")
    except httpx.RequestError as e:
        logging.error(f"Request error for {city}: {e}")
    except ValueError as e:
        logging.error(f"Invalid JSON response for {city}, {e}")
    return None


def transform_weather_response(original_response: list):
    return WeatherResponseSchema(
        results={
            response.location.region: [
                WeatherDetailSchema(
                    city=response.location.name,
                    temperature=response.current.temperature,
                    description=response.current.condition_text
                )
            ]
            for response in original_response
        }
    )





