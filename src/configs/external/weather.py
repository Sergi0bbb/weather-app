from src.configs.base import BaseConfig


class WeatherConfig(BaseConfig):
    WEATHER_API_KEY: str
    WEATHER_API_URL: str
    WEATHER_API_SEARCH_URL: str
