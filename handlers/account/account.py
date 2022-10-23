from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp, bot
from keyboards import account_keyboard, menu_keyboard
from catalogs import Menu, Account
from states import AuthState, AccountState
from messages import balance_msg
from googlesheets import GoogleSheet


@dp.message_handler(filters.Text(equals=[Menu().account, '/account']), state=[AuthState.accept])
async def account_menu(msg: types.Message, state: FSMContext):
    kb = account_keyboard()
    await AccountState.account.set()
    await msg.answer("Пока здесь можно посмотреть только Баланс по счетам\n\nВыбери Баланс или вернись в Главное меню", reply_markup=kb)


@dp.message_handler(filters.Text(equals=[Account().balance]), state=[AccountState.account])
async def check_balance(msg: types.Message, state: FSMContext):
    wait_msg = await msg.answer("Секунду, проверяю данные⏱")

    user_id = msg.from_user.id

    gs = GoogleSheet()
    user_balance = gs.get_data(f"tg-{user_id}-Pivot")
    user_balance = [j for i in user_balance for j in i]

    kb = menu_keyboard()

    reply = balance_msg.format(*user_balance)

    await bot.delete_message(wait_msg.chat.id, wait_msg.message_id)

    await AuthState.accept.set()
    await msg.answer(reply, reply_markup=kb)
