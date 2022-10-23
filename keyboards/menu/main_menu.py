from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from catalogs import Accounting, Menu


# * Start keyboard
def menu_keyboard():
    reply = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*Accounting(), Menu().account)
    return reply

