from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import dp
from states import AuthState


@dp.message_handler(state=[AuthState.queue])
async def queue_handler(message: types.Message, state: FSMContext):
    await message.answer("Похоже что твой запрос еще в очереди на авторизацию😢")


@dp.message_handler(state=[AuthState.decline])
async def decline_handler(message: types.Message, state: FSMContext):
    await message.answer("Похоже что твой запрос на авторизацию отклонен")
