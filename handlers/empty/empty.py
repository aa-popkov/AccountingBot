from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import dp


@dp.message_handler(state="*")
async def empty_handler(message: types.Message, state: FSMContext):
    await message.answer(f"這清楚嗎?")
