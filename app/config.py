import os
from pathlib import Path

# ----------------------------------------------------
# БАЗОВЫЕ ПУТИ
# ----------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DB_PATH = DATABASE_DIR / "knowledge.db"

# ----------------------------------------------------
# АДМИНЫ (по Telegram ID)
# ----------------------------------------------------
# Можно оставить жёстко, можно делать через ENV.
ADMINS = {1325524621}  # Марк

# ----------------------------------------------------
# Cloudflare R2 настройки
# ----------------------------------------------------
# Эти переменные ПРИ ОБЯЗАТЕЛЬНО задаются в Render Environment:
# R2_ACCESS_KEY_ID
# R2_SECRET_ACCESS_KEY
# R2_ENDPOINT_URL
# R2_BUCKET_NAME

R2_ACCESS_KEY_ID = os.getenv("R2_ACCESS_KEY_ID", "")
R2_SECRET_ACCESS_KEY = os.getenv("R2_SECRET_ACCESS_KEY", "")
R2_ENDPOINT_URL = os.getenv("R2_ENDPOINT_URL", "")
R2_BUCKET_NAME = os.getenv("R2_BUCKET_NAME", "luch-sveta")

# Опционально — публичный URL, если сделаешь Custom Domain
R2_PUBLIC_BASE_URL = os.getenv("R2_PUBLIC_BASE_URL", "")

# ----------------------------------------------------
# ПРОЧЕЕ
# ----------------------------------------------------
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

# Статические файлы / шаблоны
TEMPLATES_DIR = BASE_DIR / "app" / "templates"
STATIC_DIR = BASE_DIR / "app" / "static"

