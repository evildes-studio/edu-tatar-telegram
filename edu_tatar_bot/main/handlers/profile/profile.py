from aiogram import types
from edu_tatar_bot.main.filters import is_edu_account
from edu_tatar_bot.main.misc import dp, bot, config
from edu_tatar_bot.utils.db import User, session
from aiogram.dispatcher import FSMContext
from edu_tatar_bot.main.keyboards.inline import channel_keyboard
from edu_tatar_bot.classes.EduTatar import EduTatar
from edu_tatar_bot.classes.Parser import Parser
import datetime


@dp.message_handler(text="Профиль 🖥", is_edu_account=True)
async def profile(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_data()

    message_ = await message.answer("Происходит запрос... Ожидайте")

    user = User.query.filter(User.chat_id == message.chat.id).first()
    edu_tatar = EduTatar(user.edu_tatar[-1].login, user.edu_tatar[-1].password)
    session_ = edu_tatar.auth()

    parser = Parser(session_)
    marks = parser.get_marks(term=2)
    all_marks = sum(list(map(lambda x: x["marks"], marks)), [])

    now_date = datetime.datetime.now()
    end_date = datetime.datetime.strptime(f"30.05.{now_date.year}", "%d.%m.%Y")
    days_left = (end_date - now_date).days + 1

    await message_.edit_text(f"👨🏼‍💻 Ваш профиль:\n\n"
                             f"Telegram ID: <code>{message.chat.id}</code>\n"
                             f"ФИО: <code>{user.edu_tatar[-1].name}</code>\n"
                             f"Класс: <b>{parser.get_grade()}</b>\n"
                             f"Дней до окончания учебного года: <b>{days_left}</b>\n"
                             f"Общее кол-во оценок за четверть: <b>{len(all_marks)}</b>\n"
                             f"Общий GPA за текущую четверть/полугодие: <b>{round(sum(all_marks) / len(all_marks), 2)}</b>")
