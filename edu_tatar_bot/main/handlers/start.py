
from aiogram import types
from misc import dp, bot, config
# from edu_tatar_bot.utils.db import
# from keyboards.markup.markup import main_menu
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup


@dp.message_handler(text="")
async def start(message: types.Message):
    pass
