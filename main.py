import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database import connect, init_db

from handlers import start, registration, agreement, profile, anonymous, support

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    await connect()
    await init_db()

    dp.include_router(start.router)
    dp.include_router(agreement.router)
    dp.include_router(registration.router)
    dp.include_router(profile.router)
    dp.include_router(anonymous.router)
    dp.include_router(support.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
