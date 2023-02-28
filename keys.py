from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
    InlineKeyboardButton('Backend', callback_data='backend'),
    InlineKeyboardButton('Frontend', callback_data='frontend'),
    InlineKeyboardButton('Ux/Ui', callback_data='uxui'),
    InlineKeyboardButton('Android-разработка', callback_data='android'),
    InlineKeyboardButton('IOS-разработка', callback_data='ios'),
]
button = InlineKeyboardMarkup().add(*buttons)