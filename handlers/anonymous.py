from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Anon

router = Router()

@router.message(F.text == "💌 Анонимное сообщение")
async def anon_start(message: Message, state: FSMContext):
    await state.set_state(Anon.text)
    await message.answer("Напишите сообщение")

@router.message(Anon.text)
async def anon_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Оплатите 15⭐ (заглушка)")
