from aiogram.dispatcher.filters.state import StatesGroup, State


class Rate_state(StatesGroup):
    name = State()
    oy = State()
    muddat = State()
    narx = State()
    save = State()
