from src.configs.base import BaseConfig


class RedisConfig(BaseConfig):
    REDIS_HOST: str
    REDIS_PORT: str
