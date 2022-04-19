
from aiogram import types


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(f'', callback_data=f"")
    )
    
    return keyboard
