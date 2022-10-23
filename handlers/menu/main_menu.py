from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp, ADMIN_ID
from keyboards import menu_keyboard
from catalogs import Menu
from messages import main_menu_msg
from states import AuthState, AdditionState, CostsState, AccountState


@dp.message_handler(
    filters.Text(equals=[Menu().main, '/menu']),
    state=[AdditionState, CostsState, AccountState, AuthState.accept])
async def main_menu(msg: types.Message, state: FSMContext):
    kb = menu_keyboard()
    reply = main_menu_msg.format(Menu().main)
    await AuthState.accept.set()
    await msg.answer(reply, reply_markup=kb)
