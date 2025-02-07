from fastapi import FastAPI

from api.web.routers.weather import weather_router


def register_routers(app: FastAPI):
    app.include_router(weather_router)


def create_app():
    app = FastAPI()
    register_routers(app)

    return app
