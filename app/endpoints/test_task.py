from typing import Self
from time import sleep

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi_cache.decorator import cache

from app.core.celery_app import test_task

router = APIRouter(prefix="/api/v1/celery/tasks", tags=["v1", "Celery"])


class MailMessage:
    """
    Модель письма
    """

    def __init__(self: Self, email: str, content: str) -> None:
        email_split = email.split("@")

        if "gmail" in email_split or "mail" in email_split or "yandex" in email_split:
            self.email = email
            self.content = content
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Низя")


async def check_mail(email: str, content: str) -> str:
    """
    Проверка почты на gmail, mail, yandex
    """

    email_split = email.split("@")

    if "gmail" in email_split or "mail" in email_split or "yandex" in email_split:
        return email
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Низя")


@router.get("/send_email_with_class")
@cache(expire=90)
async def send_email_class(
) -> bool:
    """
    ОТправка письма
    """

    sleep(5)
    return True


@router.post("/send_email_with_func")
# @cache(expire=90)
async def send_email_func(
    email: str = Depends(check_mail),
) -> bool:
    """
    ОТправка письма
    """

    return True


@router.post("/celery_send_mail")
async def celery_send_mail(
    email: MailMessage = Depends(MailMessage),
) -> bool:
    """
    Отправка письма с помощью Celery
    """

    test_task.delay(email=email.email, context=email.content)
    return True
