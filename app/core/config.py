from starlette.config import Config

config = Config(".env")

REDIS_HOST = config("REDIS_HOST", cast=str)
REDIS_PORT = config("REDIS_PORT", cast=str)
