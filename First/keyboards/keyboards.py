from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='Информация')
button3 = types.KeyboardButton(text='покажи лису')
button4 = types.KeyboardButton(text='/stop')

keyboard1 = [
    [button1, button2],
    [button3, button4],
]

keyboard2 = [
    [button3, button4]
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)