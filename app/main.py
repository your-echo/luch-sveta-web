from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path

from .config import STATIC_DIR, TEMPLATES_DIR, DEBUG
from .routers import health, public, admin
from .db import init_db


# ----------------------------------------------------
#  СОЗДАЕМ ПРИЛОЖЕНИЕ
# ----------------------------------------------------
app = FastAPI(
    title="Луч света — Web API",
    debug=DEBUG,
)

# ----------------------------------------------------
#  CORS (разрешаем всё)
# ----------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # потом можно ограничить
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
#  СТАТИКА И ШАБЛОНЫ
# ----------------------------------------------------
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


# ----------------------------------------------------
#  РОУТЕРЫ
# ----------------------------------------------------
app.include_router(health.router)
app.include_router(public.router)
app.include_router(admin.router)


# ----------------------------------------------------
#  ИНИЦИАЛИЗАЦИЯ БАЗЫ ДАННЫХ
# ----------------------------------------------------
@app.on_event("startup")
async def on_startup():
    await init_db()
    print("📚 Database initialized")


# ----------------------------------------------------
#  Точка входа
#  (при локальном запуске: uvicorn app.main:app --reload)
# ----------------------------------------------------
@app.get("/")
async def root():
    return {"message": "Луч света Web API работает"}

