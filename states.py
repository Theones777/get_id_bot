from aiogram.dispatcher.filters.state import StatesGroup, State


class Ids(StatesGroup):
    waiting_for_name = State()
    waiting_for_id = State()

