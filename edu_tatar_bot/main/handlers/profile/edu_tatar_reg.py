from aiogram import types
from edu_tatar_bot.main.misc import dp, bot, config
from edu_tatar_bot.utils.db import User, session, EduTatarUser
from aiogram.dispatcher import FSMContext
from edu_tatar_bot.main.keyboards.markup import cancel_btn, validate_keyboard, start_keyboard
from edu_tatar_bot.classes.EduTatar import EduTatar
from edu_tatar_bot.classes.Parser import Parser
from edu_tatar_bot.classes.EduAccountReg import EduAccountReg


@dp.message_handler(state=EduAccountReg.ask_login)
async def set_login(message: types.Message, state: FSMContext):
    if len(message.text.strip()) == 10 and message.text.strip().isnumeric():
        await state.update_data(login=message.text.strip())
        await message.answer("Введите пароль от аккаунта:")
        await EduAccountReg.ask_password.set()

    else:
        await message.answer("Введенные вами данные имеют неверный формат! Попробуйте еще раз, либо нажмите Отмена:",
                             reply_markup=cancel_btn())
        await EduAccountReg.ask_login.set()


@dp.message_handler(state=EduAccountReg.ask_password)
async def set_password(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text.strip())
    user_data = await state.get_data()
    message_ = await message.answer("Происходит процесс авторизации... Ожидайте")

    edu_tatar = EduTatar(user_data['login'], user_data['password'])
    session_ = edu_tatar.auth()

    parser = Parser(session_)
    user_info = parser.get_user_info()
    session_.close()

    if user_info:
        await message_.edit_text(f"<b>ФИО:</b> <i>{user_info['name']}</i>\n"
                                 f"<b>Школа:</b> <i>{user_info['school']}</i>")
        await message.answer("Данные значения совпадают с владельцем аккаунта?", reply_markup=validate_keyboard())
        await state.update_data(user_info=user_info)
        await EduAccountReg.validation.set()
    else:
        await message_.edit_text("Аккаунт не найден! Пройдите процедуру привязки аккаунта снова, либо нажмите Отмена")
        await message.answer("Введите логин от аккаунта edu.tatar.ru :")
        await EduAccountReg.ask_login.set()


@dp.message_handler(state=EduAccountReg.validation, text="Все верно ✅")
async def validation_ok(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_info = user_data["user_info"]
    user = User.query.filter(User.chat_id == message.chat.id).first()
    user.edu_tatar.append(EduTatarUser(login=user_data["login"], password=user_data["password"],
                                       name=user_info["name"], school=user_info["school"]))
    session.commit()

    await state.finish()
    await message.answer("Аккаунт успешно привязан! Теперь для вас доступны все функции бота 🔥",
                         reply_markup=start_keyboard())
