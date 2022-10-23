from datetime import datetime

from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp, ADMIN_ID, bot
from states import AdditionState, CostsState
from messages import insert_msg
from keyboards import addition_keyboard, costs_keyboard
from googlesheets import GoogleSheet


@dp.message_handler(state=AdditionState.insert_data)
async def addition_insert(msg: types.Message, state: FSMContext):
    """
    Принимает сообщение с суммой\n
    Возвраает на выбор категории\n
    Выводим выбор категории
    """

    wait_msg = await msg.answer("Секунду, проверяю данные⏱")

    user_text = msg.text
    user_data = user_text.split(" ")
    user_id = msg.from_user.id

    summa = user_data[0]
    user_date = datetime.now().strftime("%d.%m.%Y")

    validate_user_data = True

    if len(user_data) > 1:
        try:
            user_date = datetime.strptime(user_data[1], "%d.%m.%Y").strftime("%d.%m.%Y")
        except ValueError as e:
            validate_user_data = False

    if not summa.isdigit() or int(summa) < 1:
        validate_user_data = False
    

    if not validate_user_data:
        await bot.delete_message(wait_msg.chat.id, wait_msg.message_id)
        await msg.answer("Херню написал")
        return

    kb = addition_keyboard()

    state_data = await state.get_data()
    acc_type = state_data['account']
    category = state_data['category']
    currency = state_data['currency']

    gs = GoogleSheet()
    gs.append_row(user_data=[[category, summa, currency, user_date]], range=f"tg-{user_id}-Data!A2:D4")

    reply = insert_msg.format(summa, currency, category, user_date, acc_type)

    await bot.delete_message(wait_msg.chat.id, wait_msg.message_id)
    await AdditionState.previous()
    await msg.answer(reply, reply_markup=kb)


@dp.message_handler(state=CostsState.insert_data)
async def costs_insert(msg: types.Message, state: FSMContext):
    """
    Принимает Валюту и статус Доходов\n
    Устанавливаем следуюущий статус\n
    Выводим выбор категории
    """
    wait_msg = await msg.answer("Секунду, проверяю данные⏱")

    user_text = msg.text
    user_data = user_text.split(" ")
    user_id = msg.from_user.id

    summa = user_data[0]
    user_date = datetime.now().strftime("%d.%m.%Y")

    validate_user_data = True

    if len(user_data) > 1:
        try:
            user_date = datetime.strptime(user_data[1], "%d.%m.%Y").strftime("%d.%m.%Y")
        except ValueError as e:
            validate_user_data = False

    if not summa.isdigit() or int(summa) < 1:
        validate_user_data = False
    
    if not validate_user_data:
        await bot.delete_message(wait_msg.chat.id, wait_msg.message_id)
        await msg.answer("Херню написал")
        return

    kb = costs_keyboard()

    state_data = await state.get_data()
    acc_type = state_data['account']
    category = state_data['category']
    currency = state_data['currency']

    gs = GoogleSheet()
    gs.append_row(user_data=[[category, int(summa)*-1, currency, user_date]], range=f"tg-{user_id}-Data!A2:D4")

    reply = insert_msg.format(summa, currency, category, user_date, acc_type)

    await bot.delete_message(wait_msg.chat.id, wait_msg.message_id)
    await CostsState.previous()
    await msg.answer(reply, reply_markup=kb)