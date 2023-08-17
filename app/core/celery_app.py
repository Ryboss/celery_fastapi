from time import sleep

from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379")


@celery_app.task
def test_task() -> bool:
    """
    Тестовая функция для Celery
    """
    sleep(5)
    return True

