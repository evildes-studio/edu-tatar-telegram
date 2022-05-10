from aiogram import types
from edu_tatar_bot.main.misc import dp, bot, config
from edu_tatar_bot.utils.db import User, session
from aiogram.dispatcher import FSMContext
from edu_tatar_bot.main.keyboards.inline import channel_keyboard
import datetime


@dp.message_handler(text="Расписание 📆")
async def schedule(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_data()

    await message.answer(f"Расписание на {datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y')}:")
