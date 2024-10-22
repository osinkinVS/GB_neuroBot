from aiogram import Router, types, F
from aiogram.filters.command import Command
from First.utils.Photo import fox
from First.keyboards.keyboards import kb1, kb2


router = Router()

# Команда Старт
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Hello, {name}", reply_markup=kb1)

# Команда Инфо
@router.message(F.text == 'Информация')
@router.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Я бот - твой друг и товарищ ")

# Команда Стоп
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Goodbye tmok, {name}")

# Хэндлер на сообщения

@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)

@router.message(F.text)
async def msq_echo(message: types.Message):
    msq_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msq_user:
        await message.answer(f'Привет, {name}')
    elif 'пока' == msq_user:
        await message.answer(f'Пока, {name}')
    elif 'лиса' in msq_user:
        await message.answer(f'Смотри, что есть',  reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')
