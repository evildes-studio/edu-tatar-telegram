from aiogram.dispatcher.filters.state import State, StatesGroup


class EduAccountReg(StatesGroup):
    ask_login = State()
    ask_password = State()
    validation = State()