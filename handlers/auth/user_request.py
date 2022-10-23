from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp, ADMIN_ID, bot
from keyboards import admin_auth_keyboard
from states import AuthState
from catalogs import UserAuth
from messages import user_request_msg


@dp.message_handler(text=[UserAuth().send], state=AuthState.queue)
async def send_auth_request(msg: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    kb_admin = admin_auth_keyboard()

    user_id = msg.from_user.id
    user_username = msg.from_user.username
    user_firstname = msg.from_user.first_name
    user_chat_id = msg.chat.id

    admin_reply = user_request_msg.format(user_id, user_chat_id, user_username, user_firstname)

    await bot.send_message(ADMIN_ID, admin_reply, reply_markup=kb_admin)
    await msg.answer("Запрос успешно отправлен🎈\nОжидайте от меня обратной связи🙋‍♂️", reply_markup=kb)
    


@dp.message_handler(text=[UserAuth().decline], state=AuthState.queue)
async def decline_auth_request(msg: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await msg.answer("Авторизация отменена😢\nЖду тебя снова🙋‍♂️", reply_markup=kb)
