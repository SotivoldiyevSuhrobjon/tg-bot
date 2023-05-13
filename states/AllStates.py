from aiogram.dispatcher.filters.state import StatesGroup, State


class Rate_state(StatesGroup):
    name = State()
    oy = State()
    muddat = State()
    narx = State()
    choose = State()
    save = State()


class Save_plan(StatesGroup):
    tarif_name = State()
    tarif_rate = State()
    start_period = State()
    start_period = State()
