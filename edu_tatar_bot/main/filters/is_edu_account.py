from edu_tatar_bot.classes.EduAccountReg import EduAccountReg
from aiogram.dispatcher.filters import BoundFilter
from edu_tatar_bot.utils.db import User, EduTatarUser
from edu_tatar_bot.main.keyboards.markup import cancel_btn
from aiogram import types


class IsEduAccount(BoundFilter):
    key = 'is_edu_account'

    def __init__(self, is_edu_account: bool):
        self.is_edu_account = is_edu_account

    async def check(self, message: types.Message) -> bool:
        user = User.query.filter(User.chat_id == message.from_user.id).first()

        if user.edu_tatar:
            return True
        else:
            await message.answer(
                "У вас отсутствует привязка к аккаунту edu.tatar.ru! Сейчас начнется процесс регистрации 🤖\n\n"
                "<i>Продолжая пользоваться ботом, вы автоматически соглашаетесь с тем, что данные от вашего "
                "аккаунта edu.tatar.ru будут храниться на нашем сервере</i>")
            await message.answer("Отправьте след. сообщением логин от вашего аккаунта (например, 5100000000):",
                                 reply_markup=cancel_btn())

            await EduAccountReg.ask_login.set()
            return False
