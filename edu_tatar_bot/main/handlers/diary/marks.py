from aiogram import types
from edu_tatar_bot.main.misc import dp, bot, config
from edu_tatar_bot.utils.db import User, session
from aiogram.dispatcher import FSMContext
from edu_tatar_bot.main.keyboards.inline import diary_keyboard
from edu_tatar_bot.classes.EduTatar import EduTatar
from edu_tatar_bot.classes.Parser import Parser
from datetime import datetime
from datetime import timedelta


@dp.message_handler(text="Оценки 🧾")
async def marks(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_data()

    message_ = await message.answer("Происходит запрос... Ожидайте")
    await show_diary(message_, datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))


@dp.callback_query_handler(text_contains="diary")
async def marks_date(callback: types.CallbackQuery):
    await callback.message.edit_text("Происходит запрос... Ожидайте")
    await show_diary(callback.message, datetime.utcfromtimestamp(int(callback.data.split(":")[-1])))


async def show_diary(message: types.Message, date):
    user = User.query.filter(User.chat_id == message.chat.id).first()
    edu_tatar = EduTatar(user.edu_tatar[-1].login, user.edu_tatar[-1].password)
    session_ = edu_tatar.auth()

    parser = Parser(session_)
    marks = parser.get_marks(date=date, mark_info=True)
    formatted_marks = []
    for subject in marks:
        marks_ = list(map(lambda x: str(x["value"]), subject["marks"]))
        formatted_marks.append(f'<b>{subject["subject"]}:</b> {"/".join(marks_)}')

    await message.edit_text(f"Оценки за {datetime.strftime(date, '%d.%m.%Y')}:\n\n" +
                            "\n".join(formatted_marks),
                            reply_markup=diary_keyboard(int(datetime.timestamp(date - timedelta(days=1))),
                                                        int(datetime.timestamp(date + timedelta(days=1)))
                                                        )
                            )
