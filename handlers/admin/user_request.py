import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from bot import dp, ADMIN_ID, bot
from keyboards import menu_keyboard
from states import AuthState
from googlesheets import GoogleSheet
from catalogs import Currency

@dp.callback_query_handler(filters.IDFilter(user_id=ADMIN_ID), text="accept", state="*")
async def accept_auth_request(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.delete_reply_markup()

    # * Получаем ID пользователя запросившего регистрацию
    auth_user_id = str(re.findall(r"user_id - \*([\d]{0,})\*", callback_query.message.text)[0])

    # * Создаем листы в таблице и наполняем базовыми столбцами
    gs = GoogleSheet()

    gs.create_list(tg_id=auth_user_id)
    gs.update_row(user_data=[["Category", "Sum", "Currency", "Date"]], range=f"tg-{auth_user_id}-Data!A1:D1")

    som_formula = gs.som_currency_formula.format(auth_user_id)
    usd_formula = gs.usd_currency_formula.format(auth_user_id)
    rub_formula = gs.rub_currency_formula.format(auth_user_id)
    currency = Currency()
    gs.update_row(
        user_data=[
            [currency.sum, currency.usd, currency.rub],
            [som_formula, usd_formula, rub_formula]],
        range=f"tg-{auth_user_id}-Pivot!A1:C2")

    await callback_query.message.answer(text="Успешно авторизован")

    kb = menu_keyboard()
    await bot.send_message(auth_user_id, text="Ты успешно авторизован🔥\n\nПеревожу в Главное меню", reply_markup=kb)

    st = dp.current_state(user=auth_user_id, chat=auth_user_id)
    await st.set_state(AuthState.accept)


@dp.callback_query_handler(filters.IDFilter(user_id=ADMIN_ID), text="decline", state="*")
async def decline_auth_request(callback_query: types.callback_query, state: FSMContext):
    await callback_query.answer()
    auth_user_id = str(re.findall(r"user_id - \*([\d]{0,})\*", callback_query.message.text)[0])

    await callback_query.answer("Заблокирован")
    await bot.send_message(auth_user_id, "Запрос на авторизацию отклонен😢\n\nЧат заблокирован🔐")
    st = dp.current_state(user=auth_user_id, chat=auth_user_id)
    await st.set_state(AuthState.decline)
