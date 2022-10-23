from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from aiogram.types import ReplyKeyboardRemove


from bot import dp, ADMIN_ID
from catalogs import AdditionCategory, CostsCategory
from states import AdditionState, CostsState
from messages import category_msg


@dp.message_handler(filters.Text(equals=[*AdditionCategory()]), state=AdditionState.category)
async def addtion_menu(msg: types.Message, state: FSMContext):
    """
    Принимает тип Доходы\n
    Устанавливаем категорию в статус\n
    """

    user_text = msg.text
    kb = ReplyKeyboardRemove()

    await AdditionState.next()
    await state.update_data(category=user_text)

    state_data = await state.get_data()
    acc_type = state_data['account']
    select_currency = state_data['currency']

    reply = category_msg.format(acc_type, select_currency, user_text)

    await msg.answer(reply, parse_mode="HTML", reply_markup=kb)


@dp.message_handler(filters.Text(equals=[*CostsCategory()]), state=CostsState.category)
async def costs_menu(msg: types.Message, state: FSMContext):
    """
    Принимает тип Расходы\n
    Устанавливаем категорию в статус\n
    """

    user_text = msg.text
    kb = ReplyKeyboardRemove()

    await CostsState.next()
    await state.update_data(category=user_text)
    
    state_data = await state.get_data()
    acc_type = state_data['account']
    select_currency = state_data['currency']

    reply = category_msg.format(acc_type, select_currency, user_text)

    await msg.answer(reply, reply_markup=kb, parse_mode="HTML")
