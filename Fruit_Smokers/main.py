import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import get_start, call_menu, admins
from os import getenv

# Токен Бота
TOKEN = getenv("BOT_TOKEN")

# Все обработчики должны быть присоединены к Маршрутизатору (или Dispatcher)
dp = Dispatcher()

# Добавления роутеров
dp.include_router(get_start.router1)
dp.include_router(call_menu.router2)
dp.include_router(admins.router3)


async def main() -> None:
    # Инициализация экземпляра бота с режимом парсинга по умолчанию, который будет передаваться во все вызовы API
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
