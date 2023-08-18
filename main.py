from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware

from app.core.config import REDIS_HOST
from app.endpoints import test_task

app = FastAPI(title="Celery Test", description="Тестовое использование Celery для фоновых задач", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_task.router)


@app.on_event("startup")
async def startup():
    """
    Запуск приложения
    """

    try:
        redis = aioredis.from_url(f"redis://{REDIS_HOST}", encoding="utf-8", decode_responses=True)

        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cash")
    except Exception:
        return "Не удавлось подключиться к редис"
