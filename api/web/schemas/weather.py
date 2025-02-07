from typing import Annotated

from pydantic import Field

from api.web.schemas.base import BaseModelSchema


class WeatherRequestSchema(BaseModelSchema):
    cities: Annotated[list[str], Field(description="add here list of cities to find weather")]


class WeatherDetailSchema(BaseModelSchema):
    city: Annotated[str, Field()]
    temperature: Annotated[float, Field()]
    description: Annotated[str, Field()]


class WeatherResponseSchema(BaseModelSchema):
    results: Annotated[dict[str, list[WeatherDetailSchema]], Field()]

