from aiogram import types
from edu_tatar_bot.main.misc import dp, bot, config
from edu_tatar_bot.utils.db import User, session
from aiogram.dispatcher import FSMContext
from edu_tatar_bot.main.keyboards.inline import channel_keyboard
import datetime


@dp.message_handler(text="О Боте 🤖")
async def about(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_data()

    open_date = datetime.datetime.strptime(config['bot']['open_date'], "%d.%m.%Y")
    users = User.query.all()

    await message.answer(f"Наш бот функционирует уже <b>{(datetime.datetime.now() - open_date).days}</b> дней!\n\n"
                         f"📌 За это время у нас собралась такая статистика:\n"
                         f"— в нем зарегистрировалось - <b>{len(users)}</b> людей\n"
                         f"— уведомлений об оценках отправлено - <b></b>\n"
                         f"— общее кол-во оценок, увиденных с помощью нашего бота - <b></b>\n\n"
                         f"Подпишись на наш телеграмм-канал, чтобы быть вкурсе новых проектов 👇",
                         reply_markup=channel_keyboard())
