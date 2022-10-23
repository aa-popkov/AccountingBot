from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from catalogs import Menu


# * Start keyboard
def start_keyboard():
    main_menu = KeyboardButton(Menu().main)
    reply = ReplyKeyboardMarkup(
        resize_keyboard=True).add(main_menu)
    return reply

