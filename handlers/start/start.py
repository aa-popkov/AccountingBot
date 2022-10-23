from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import dp
from messages import start_msg


@dp.message_handler(commands=["start"], state="*")
async def start(msg: types.Message, state: FSMContext):
    await msg.answer("👋")
    kb = types.ReplyKeyboardRemove()

    reply = start_msg
    await msg.answer(reply, reply_markup=kb)
