from time import sleep

from celery import Celery

from app.core.config import REDIS_PORT

celery_app = Celery("tasks", broker=f"redis://redis:{REDIS_PORT}")


@celery_app.task
def test_task(email: str, context: str) -> bool:
    """
    Тестовая функция для Celery
    """

    sleep(5)
    return True

