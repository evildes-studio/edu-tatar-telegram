from aiogram import types
from edu_tatar_bot.main.misc import dp
from aiogram.dispatcher import FSMContext
from edu_tatar_bot.main.keyboards.markup import start_keyboard


@dp.message_handler(state="*", text="Отмена")
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_data()
    await message.answer("Вы отменили действие!", reply_markup=start_keyboard())
