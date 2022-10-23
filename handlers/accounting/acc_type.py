from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp
from keyboards import currency_keyboard
from catalogs import Accounting
from states import AdditionState, CostsState, AuthState
from messages import acc_type_msg


@dp.message_handler(filters.Text(equals=[*Accounting()]), state=AuthState.accept)
async def accounting_menu(msg: types.Message, state: FSMContext):
    """
    Принимает тип Расходов/Доходов\n
    Устанавливаем статус, в зависимости от типа\n
    Выводим выбор валюты
    """
    await state.finish()

    user_text = msg.text

    addition = Accounting().addition
    costs = Accounting().costs
    kb = currency_keyboard()

    if user_text == addition:
        await AdditionState.currency.set()
    else:
        await CostsState.currency.set()

    await state.update_data(account=user_text)
    
    reply = acc_type_msg.format(user_text)

    await msg.answer(reply, reply_markup=kb)
