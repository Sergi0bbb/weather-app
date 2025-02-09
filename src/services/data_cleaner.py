import httpx
from src.configs.external.weather import WeatherConfig

weather_config = WeatherConfig()


async def clean_city_name(city: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                weather_config.WEATHER_API_SEARCH_URL,
                params={"key": weather_config.WEATHER_API_KEY, "q": city}
            )
            city_data = response.json()
            return city_data[0]["name"] if city_data else city
        except httpx.RequestError:
            return city
