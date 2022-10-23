from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from googlesheets import GoogleSheet
from bot import dp, ADMIN_ID, bot
from keyboards import menu_keyboard, user_auth_keyboard
from states import AuthState


@dp.message_handler(commands=["auth"], state=None)
async def registration_user(msg: types.Message, state: FSMContext):
    wait_msg = await msg.answer("Секунду, проверяю регистрацию⏱\n")

    await state.finish()

    user_id = str(msg.from_user.id)
    gs = GoogleSheet()
    all_list = gs.get_lists()['sheets']
    for gs_list in all_list:
        registred_id = gs_list['properties']['title'].split('-')[1]
        if registred_id == user_id:
            kb = menu_keyboard()
            await bot.delete_message(wait_msg.chat.id, wait_msg.message_id)
            await msg.answer("Похоже ты Авторизован🎉\nПеревожу в главное меню", reply_markup=kb)
            await AuthState.accept.set()
            return

    kb = user_auth_keyboard()
    await AuthState.queue.set()
    reply = "😢 Похоже что ты не авторизован...\n\nОтправить запрос на регистрацию?"
    await msg.answer(reply, reply_markup=kb)
    
