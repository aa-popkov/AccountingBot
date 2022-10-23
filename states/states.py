from aiogram.dispatcher.filters.state import StatesGroup, State


class AuthState(StatesGroup):
    queue = State()
    accept = State()
    decline = State()


class AccountState(StatesGroup):
    account = State()


class AdditionState(StatesGroup):
    currency = State()
    category = State()
    insert_data = State()


class CostsState(StatesGroup):
    currency = State()
    category = State()
    insert_data = State()
