from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from ..main import templates

router = APIRouter()


# ----------------------------------------------------
#  Корневая страница
# ----------------------------------------------------
@router.get("/")
async def root():
    return {"message": "Луч света Web API активен"}


# ----------------------------------------------------
#  Основная страница приложения "ЗНАНИЯ"
# ----------------------------------------------------
@router.get("/app")
async def app_page(request: Request, user_id: int | None = None):
    """
    Главная страница, которая будет открываться
    из Telegram-бота.
    """
    return templates.TemplateResponse(
        "app.html",
        {
            "request": request,
            "user_id": user_id,  # понадобится позже для авторизации
        }
    )

