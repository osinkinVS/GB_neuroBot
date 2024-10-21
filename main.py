import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
import config

API_TOKEN = config.token

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Hello, {name}")


@dp.message(F.text == 'Информация')
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Я бот - твой друг и товарищ ")

# Команда Стоп
@dp.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Goodbye tmok, {name}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())