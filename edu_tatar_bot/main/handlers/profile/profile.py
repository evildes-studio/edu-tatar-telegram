from aiogram import types
from edu_tatar_bot.main.filters import is_edu_account
from edu_tatar_bot.main.misc import dp, bot, config
from edu_tatar_bot.utils.db import User, session
from aiogram.dispatcher import FSMContext
from edu_tatar_bot.main.keyboards.inline import channel_keyboard


@dp.message_handler(text="Профиль 🖥", is_edu_account=True)
async def profile(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_data()

    await message.answer(f"Ваш профиль:")
