from typing import Annotated

from pydantic import BaseModel, Field


class WeatherLocationModel(BaseModel):
    name: Annotated[str, Field()]
    region: Annotated[str, Field(alias="tz_id")]


class WeatherTemperatureModel(BaseModel):
    temperature: Annotated[float, Field(alias="temp_c")]
    description: Annotated[dict, Field(alias="condition", description="Weather condition")]

    @property
    def condition_text(self) -> str:
        return self.description["text"] if isinstance(self.description, dict) else self.description


class WeatherApiModel(BaseModel):
    location: Annotated[WeatherLocationModel, Field()]
    current: Annotated[WeatherTemperatureModel, Field()]
