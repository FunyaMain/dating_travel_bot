from aiogram import Router, F
from aiogram.types import Message
from database import fetchrow
from keyboards import main_menu

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    user = await fetchrow("SELECT * FROM users WHERE user_id=$1", message.from_user.id)

    if not user:
        await message.answer("Привет! Пройди регистрацию.")
    else:
        await message.answer("Добро пожаловать обратно!", reply_markup=main_menu)
