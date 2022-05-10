from aiogram import types
from edu_tatar_bot.main.misc import dp, bot, config
from aiogram.dispatcher import FSMContext
from edu_tatar_bot.main.keyboards.markup import diary_keyboard


@dp.message_handler(text="Дневник 🎓", is_edu_account=True)
async def menu(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_data()

    await message.answer(f"Выберите доступные функции для дневника 👇",
                         reply_markup=diary_keyboard())
