from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "📜 О нас / Соглашение")
async def agreement(message: Message):
    await message.answer(
        "📜 Соглашение:\n\n"
        "Используя бота, вы принимаете правила сервиса."
    )
