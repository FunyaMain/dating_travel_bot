from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "💎 Поддержать")
async def support(message: Message):
    await message.answer(
        "Поддержка проекта:\n\nTON: your_wallet\nUSDT: your_wallet"
    )
