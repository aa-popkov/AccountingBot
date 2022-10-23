from aiogram.types import ReplyKeyboardMarkup

from catalogs import BanUser


def ban_user_keyboard():
    reply = ReplyKeyboardMarkup(resize_keyboard=True).add(*BanUser())
    return reply

