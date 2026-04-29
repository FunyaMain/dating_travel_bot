import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Каналы
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
CHAT_ID = int(os.getenv("CHAT_ID"))

# Модерация
MOD_CHAT_ID = int(os.getenv("MOD_CHAT_ID"))

# БД (Railway PostgreSQL)
DB_URL = os.getenv("DATABASE_URL")
