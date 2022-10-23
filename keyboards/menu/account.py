from aiogram.types import ReplyKeyboardMarkup

from catalogs import Account, Menu


# * Start keyboard
def account_keyboard():
    reply = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*Account()).row(Menu().main)
    return reply

