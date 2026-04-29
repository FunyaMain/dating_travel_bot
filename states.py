from aiogram.fsm.state import StatesGroup, State

class Registration(StatesGroup):
    name = State()
    age = State()
    city = State()
    gender = State()
    search = State()
    about = State()
    photo = State()
    confirm = State()

class Anon(StatesGroup):
    text = State()
