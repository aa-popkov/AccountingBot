from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from catalogs import Currency, Menu


# * Currency keyboard
def currency_keyboard():
    reply = ReplyKeyboardMarkup(
        resize_keyboard=True, row_width=3).add(*Currency(), Menu().main)
    return reply

