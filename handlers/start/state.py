from aiogram.fsm.state import StatesGroup, State


class RegStatesGroup(StatesGroup):
    lang = State()
    region = State()
    phone_number = State()
    full_name = State()
