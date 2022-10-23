from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp, ADMIN_ID
from keyboards import addition_keyboard, costs_keyboard
from catalogs import Currency
from states import AdditionState, CostsState
from messages import currency_type_msg


@dp.message_handler(filters.Text(equals=[*Currency()]), state=AdditionState.currency)
async def addition_currency_menu(msg: types.Message, state: FSMContext):
    """
    Принимает Валюту и статус Доходов\n
    Устанавливаем следуюущий статус\n
    Выводим выбор категории
    """

    user_text = msg.text
    kb = addition_keyboard()

    await AdditionState.next()
    await state.update_data(currency=user_text)

    state_data = await state.get_data()
    acc_type = state_data['account']

    reply = currency_type_msg.format(acc_type, user_text)

    await msg.answer(reply, reply_markup=kb)


@dp.message_handler(filters.Text(equals=[*Currency()]), state=CostsState.currency)
async def costs_currency_menu(msg: types.Message, state: FSMContext):
    """
    Принимает Валюту и статус Доходов\n
    Устанавливаем следуюущий статус\n
    Выводим выбор категории
    """

    user_text = msg.text
    kb = costs_keyboard()

    await CostsState.next()
    await state.update_data(currency=user_text)

    state_data = await state.get_data()
    acc_type = state_data['account']

    reply = currency_type_msg.format(acc_type, user_text)

    await msg.answer(reply, reply_markup=kb)