from src.services.weather_api import fetch_weather
from src.services.file_writer import save_weather_data
import asyncio
import logging

logging.basicConfig(level=logging.INFO)


async def process_city(city: str, results: dict):
    try:
        weather_data = await fetch_weather(city)
        if weather_data:
            results[city] = weather_data
        else:
            logging.warning(f"No weather data for {city}")
    except Exception as e:
        logging.error(f"Error processing city {city}: {e}")


async def process_weather_data(cities: list):
    results = {}
    tasks = [process_city(city, results) for city in cities]
    await asyncio.gather(*tasks)

    if not results:
        logging.warning("No valid weather data received for any city.")

    await save_weather_data("global", results)
    return results
