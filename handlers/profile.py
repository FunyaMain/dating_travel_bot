from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "👤 Мой профиль")
async def profile(message: Message):
    await message.answer("Тут будет твой профиль")
