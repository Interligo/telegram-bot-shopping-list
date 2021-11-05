import os
from dotenv import load_dotenv
from aiogram import types
from aiogram.dispatcher.webhook import SendMessage, SendPhoto
from aiogram.utils.markdown import text

from sl_bot_main import dp
import sl_bot_keyboards as kb


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
valid_ids = os.getenv('ADMIN_ID'), os.getenv('USER_ID'), os.getenv('COLLABORATOR_ID')


@dp.message_handler(commands=['start'])
async def greet_user(message: types.Message):
    if str(message.from_user.id) in valid_ids:
        return SendMessage(message.chat.id, db.show_sl(), reply_markup=kb.show_markup)
    else:
        return SendMessage(message.chat.id, f'Привет, {message.from_user.first_name}! Я тебя не знаю, поэтому мы '
                                            f'можем с тобой немного поговорить, но к большинству функций тебе '
                                            f'доступ закрыт.')


@dp.message_handler(commands=['show'])
async def show_shopping_list(message: types.Message):
    if str(message.from_user.id) in valid_ids:
        return SendMessage(message.chat.id, f'Привет, {message.from_user.first_name}! Рада тебя видеть. '
                                            f'Чем я могу помочь?', reply_markup=kb.start_markup)
    else:
        return SendMessage(message.chat.id, f'Привет, {message.from_user.first_name}! Я тебя не знаю, поэтому мы '
                                            f'можем с тобой немного поговорить, но к большинству функций тебе '
                                            f'доступ закрыт.')


@dp.message_handler(commands=['id'])
async def send_user_id(message: types.Message):
    return SendMessage(message.chat.id,
                       f'{message.from_user.first_name}, я узнала твой ID в Telegram - {message.from_user.id}.')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    return SendMessage(message.chat.id,
                       text('Я - бот-ассистент, могу подсказать некоторые команды:', '/start', '/show', '/cancel', '/id',
                            'Есть ещё парочка секретных команд, но если ты их не знаешь... Тогда обойдемся без них.',
                            'Если остались какие-то вопросы, то можешь 👇',
                            sep='\n'), reply_markup=kb.contact_dev_kb)


@dp.message_handler(commands=['cancel'])
async def cancel_command(message: types.Message):
    return SendMessage(message.chat.id, 'Давай начнем заново :)', reply_markup=kb.start_markup)


@dp.message_handler(commands=['test'])
async def test_command(message: types.Message):
    await message.answer('Это служебная команда для отладки новых функций моим создателем.')


@dp.message_handler(commands=['boobs'])
async def show_boobs(message: types.Message):
    if str(message.from_user.id) == str(os.getenv('ADMIN_ID')):
        boobs_url = "http://img.177pic.info/uploads/2020/07a/a055-210.jpg"
        return SendPhoto(message.chat.id, photo=boobs_url)
    else:
        return SendMessage(message.chat.id, 'Только избранные могут увидеть то, что скрыто!')


@dp.message_handler(regexp='Привет')
async def hello_message_answer(message: types.Message):
    return SendMessage(message.chat.id, f'{message.from_user.first_name}, здравствуй!')


@dp.message_handler(regexp='Пока')
async def bye_message_answer(message: types.Message):
    return SendMessage(message.chat.id, f'{message.from_user.first_name}, пока!')


@dp.message_handler()
async def any_message_answer(message: types.Message):
    return SendMessage(message.chat.id,
                       f'{message.from_user.first_name}, если ты просто хочешь поболтать, '
                       f'то обратись к Алисе или Сири.')
