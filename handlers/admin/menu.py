from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp, ADMIN_ID, bot
from keyboards import admin_mneu_keyboard
from states import AuthState
from googlesheets import GoogleSheet
from catalogs import Currency


@dp.message_handler(filters.IDFilter(user_id=ADMIN_ID), commands="admin", state="*")
async def admin_menu(msg: types.Message, state: FSMContext):
    kb = admin_mneu_keyboard()
    await msg.answer("😎 Админка 😎", reply_markup=kb)

