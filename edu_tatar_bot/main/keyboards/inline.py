from edu_tatar_bot.main.misc import config
from aiogram import types


def channel_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(f'Перейти в канал', url=config["bot"]["channel_url"])
    )
    
    return keyboard
