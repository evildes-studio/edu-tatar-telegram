from edu_tatar_bot.main.misc import config
from aiogram import types
from datetime import datetime


def channel_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(f'Перейти в канал', url=config["bot"]["channel_url"])
    )

    return keyboard


def diary_keyboard(prev_date, next_date):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        *[types.InlineKeyboardButton(datetime.utcfromtimestamp(date).strftime('%d.%m.%Y'),
                                     callback_data=f"diary:{date}")
          for date in [prev_date, next_date]]
    )

    return keyboard
