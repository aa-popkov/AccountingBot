from aiogram.types import ReplyKeyboardMarkup

from catalogs import AdminMenu


def admin_mneu_keyboard():
    reply = ReplyKeyboardMarkup(resize_keyboard=True).add(*AdminMenu())
    return reply

