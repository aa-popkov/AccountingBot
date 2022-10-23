from aiogram.types import ReplyKeyboardMarkup

from catalogs import UserAuth


def user_auth_keyboard():
    reply = ReplyKeyboardMarkup(resize_keyboard=True).add(*UserAuth())
    return reply

