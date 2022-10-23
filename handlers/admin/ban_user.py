from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp, ADMIN_ID, bot
from keyboards import ban_user_keyboard
from states import AuthState
from googlesheets import GoogleSheet
from catalogs import AdminMenu


@dp.message_handler(filters.IDFilter(user_id=ADMIN_ID), filters.Text(equals=AdminMenu().ban), state="*")
async def ban_user(msg: types.Message, state: FSMContext):
    wait_msg = await msg.answer("Секунду, собираю данные⏱")

    gs = GoogleSheet()
    all_list = gs.get_lists()['sheets']
    user_list = set()
    for gs_list in all_list:
        registred_id = gs_list['properties']['title'].split('-')[1]
        user_list.add(registred_id)

    reply = "User list:\n"
    for user in user_list:
        reply += f"<code>{user}</code>\n"
    
    kb = ban_user_keyboard()

    await bot.delete_message(wait_msg.chat.id, wait_msg.message_id)

    await msg.answer(reply, reply_markup=kb, parse_mode="HTML")


