from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *


bot = Bot(token=TG_API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())

ADMIN_ID = TG_ADMIN_ID


async def on_startup(dp: Dispatcher):
    print("OK")
    commands = [
        types.BotCommand(command="/start", description="🏁Стартуем!"),
        types.BotCommand(command="/menu", description="🏠Главное меню"),
    ]
    await bot.set_my_commands(commands)
    await bot.send_message(ADMIN_ID, "Бот перезапущен!\n/start")


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)