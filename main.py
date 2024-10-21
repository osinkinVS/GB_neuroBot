import logging
import asyncio
from aiogram import Bot, Dispatcher
import config
from First.handlers import common, cereer_choice

async def main():
    API_TOKEN = config.token

    # Включаем логирование, чтобы видеть сообщения в консоли
    logging.basicConfig(level=logging.INFO)

    # Инициализация бота
    bot = Bot(token=API_TOKEN)
    # Диспетчер
    dp = Dispatcher()

    dp.include_router(cereer_choice.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())