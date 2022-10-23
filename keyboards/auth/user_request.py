from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def admin_auth_keyboard():
    accept = InlineKeyboardButton(text="✔", callback_data="accept")
    decline = InlineKeyboardButton(text="❌", callback_data="decline")

    return InlineKeyboardMarkup(row_width=2).add(accept, decline)

