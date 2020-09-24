from aiogram import types
from aiogram.dispatcher.webhook import SendMessage, SendPhoto
from aiogram.utils.markdown import text
# Импорт файлов с настройками
from sl_bot_main import dp
from sl_bot_settings import ADMIN_ID
import sl_bot_keyboards as kb


@dp.message_handler(commands=['start'])
async def greet_user(message: types.Message):
    # Проверка ID пользователя
    if str(message.from_user.id) in ADMIN_ID:
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
                       text('Я - бот-ассистент, могу подсказать некоторые команды:', '/start', '/cancel' '/id',
                            'Есть ещё парочка секретных команд, но если ты их не знаешь... Тогда обойдемся без них.',
                            'Если остались какие-то вопросы, то можешь 👇',
                            sep='\n'), reply_markup=kb.contact_dev_kb)


# Отменяет любые состояния
@dp.message_handler(commands=['cancel'])
async def cancel_command(message: types.Message):
    return SendMessage(message.chat.id, 'Давай начнем заново :)', reply_markup=kb.start_markup)


# Обработчик команды test
@dp.message_handler(commands=['test'])
async def test_command(message: types.Message):
    await message.answer('Это служебная команда для отладки новых функций моим создателем.')


# Показывает свои сиськи избранным
# TODO: Залить картинку на свой сервер и заменить URL, чтобы бот брал картинку с моего сервера
@dp.message_handler(commands=['boobs'])
async def show_boobs(message: types.Message):
    if str(message.from_user.id) in ADMIN_ID:
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


# Обработчик любых сообщений от пользователя
@dp.message_handler()
async def any_message_answer(message: types.Message):
    return SendMessage(message.chat.id,
                       f'{message.from_user.first_name}, если ты просто хочешь поболтать, то обратись к Алисе или Сири.')
