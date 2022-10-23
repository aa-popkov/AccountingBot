from typing import NamedTuple


class UserAuth(NamedTuple):
    send: str = "📩 Отправить"
    decline: str = "❌ Отменить"


class Menu(NamedTuple):
    main: str = "🏠 Главное меню"
    account: str = "📃 Счёт"


class AdminMenu(NamedTuple):
    ban: str = "💥 Ban User"
    send_msg: str = "✉ Send Message"


class BanUser(NamedTuple):
    accept: str = "💥 Ban"
    decline: str = "❌ Decline"


class Account(NamedTuple):
    balance: str = "🏧 Баланс"


class Accounting(NamedTuple):
    addition: str = "🤑 Доходы"
    costs: str = "💳 Расходы"


class Currency(NamedTuple):
    rub: str = "🇷🇺 RUB"
    usd: str = "🇺🇸 USD"
    sum: str = "🇺🇿 SUM"


class AdditionCategory(NamedTuple):
    zp: str = "💰Зарплата"
    cashback: str = "💳Кешбек"
    gifts: str = "🎁Подарки"


class CostsCategory(NamedTuple):
    products: str = "🍜Продукты"
    house: str = "🏡Квартира"
    transport: str = "🚗Транспорт"
    web: str = "🌍Интернет/Связь"
    taback: str = "🚬Табак"
    alchogol: str = "🍺Алкоголь"
    food: str = "⚒Обеды/Кофе"
    gifts: str = "🎁Подарки"
    funs: str = "🎉Развлечения"
    clothes: str = "👔Одежда/Обувь"
    travel: str = "🚄Поездки"
