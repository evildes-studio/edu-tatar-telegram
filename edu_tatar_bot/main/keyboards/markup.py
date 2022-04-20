
from aiogram import types


def start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Дневник 🎓')
    keyboard.row('Статистика 📊', 'Профиль 🖥')
    keyboard.row('О Боте 🤖')

    return keyboard
