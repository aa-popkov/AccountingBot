from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from catalogs import AdditionCategory, CostsCategory, Menu


# * Start keyboard
def addition_keyboard():
    reply = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True, row_width=2).add(*AdditionCategory()).row(Menu().main)
    return reply


def costs_keyboard():
    reply = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True, row_width=2).add(*CostsCategory()).row(Menu().main)
    return reply