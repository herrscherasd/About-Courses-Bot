from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import logging
import os

from keys import button

load_dotenv('.env')

bot = Bot(os.environ.get('TOKEN'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.answer("Приветствую! Я бот который предоставит вам базовую информацию об IT-курсах в Geeks.")
    await message.answer('Существуют 5 направлений. Для подробной информации о каждом нажмите на соответствующую кнопку.', reply_markup=button)

@dp.callback_query_handler(lambda call:call)
async def inline(call):

    if call.data == 'backend':
        await back(call.message)
    elif call.data == 'frontend':
        await front(call.message)
    elif call.data == 'uxui':
        await uxui(call.message)
    elif call.data == 'android':
        await android(call.message)
    elif call.data == 'ios':
        await ios(call.message)

@dp.message_handler(commands=['backend'])
async def back(message:types.Message):
    await message.answer('Бэкенд – это внутренняя, скрытая от пользователя начинка сайта или веб-приложения. Другими словами, это часть сервиса, которая работает на удаленном сервере, а не в браузере или персональном компьютере.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 5 месяцев.')

@dp.message_handler(commands=['frontend'])
async def front(message:types.Message):
    await message.answer('Фронтенд-разработка — это создание пользовательского интерфейса на клиентской стороне веб‑сайта или приложения. Это всё, что видит пользователь, когда открывает веб-страницу, и с чем он взаимодействует: кнопки, баннеры и анимация.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 5 месяцев.')

@dp.message_handler(commands=['uxui'])
async def uxui(message:types.Message):
    await message.answer('UX/UI-дизайнер ― одна из самых востребованных сегодня профессий на рынке. В этом материале мы подробно разбираем, кто такой UX/UI-дизайнер и почему UX/UI-дизайн ― не только про графику.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 3 месяцев.')

@dp.message_handler(commands=['android'])
async def android(message:types.Message):
    await message.answer('Андроид-разработчик создаёт приложения и поддерживает их работу, продумывает интерфейс и логику, изучает пользовательские пожелания и делает обновления.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 7 месяцев.')

@dp.message_handler(commands=['ios'])
async def ios(message:types.Message):
    await message.answer('Разработка приложений для iOS — это процесс создания мобильных приложений для оборудования Apple, включая iPhone, iPad и iPod Touch. Программное обеспечение написано на языке программирования Swift, а затем развернуто в App Store для загрузки пользователями.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 7 месяцев.')

@dp.message_handler()
async def nothing(message:types.Message):
    await message.answer('')
    



executor.start_polling(dp)