from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Registration
from keyboards import confirm_kb

router = Router()

@router.message(Registration.name)
async def set_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.age)
    await message.answer("Возраст?")
