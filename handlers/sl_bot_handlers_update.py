from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.webhook import SendMessage
# Импорт файлов с настройками
from sl_bot_main import bot
from sl_bot_main import dp
from sl_bot_states import OrderProduct
import sl_bot_keyboards as kb
import sl_db_functions as db


@dp.callback_query_handler(lambda call: call.data == 'update')
async def callback_update(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    return SendMessage(call.message.chat.id, 'Выбери, что хочешь изменить.', reply_markup=kb.update_prev_any_markup)


# Обработка callback (изменить последний введенный продукт)
@dp.callback_query_handler(lambda call: call.data == 'update_previous')
async def callback_update_previous(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    product_name = db.search_last_product_in_sl()
    await bot.send_message(call.message.chat.id, f'Будем исправлять: {product_name}.',
                           reply_markup=kb.update_prev_markup)


# Начало блока обработки функции update_prev_product
# Включает МС и считывает ввод пользователя
@dp.callback_query_handler(lambda call: call.data == 'update_prev_product')
async def callback_update_prev_name(call: types.CallbackQuery):
    await OrderProduct.waiting_for_product_name_to_update_prev.set()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, 'Напиши мне верное название и я все исправлю.')

# Записывает наименование продукта, просит ввести новое наименование продукта и переходит в другой State
@dp.message_handler(state=OrderProduct.waiting_for_product_name_to_update_prev)
async def answer_product_name_to_update_prev(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    # Получаем данные из МС и ждем ответ от функции
    product_name = db.search_last_product_in_sl()
    data = await state.get_data()
    new_product_name = data.get("product")
    # Завершает работу с МС
    await state.finish()
    return SendMessage(message.chat.id, db.update_name_product(product_name, new_product_name),
                       reply_markup=kb.start_markup)
# Конец блока обработки функции update_prev_product

# Начало блока обработки функции update_prev_amount
@dp.callback_query_handler(lambda call: call.data == 'update_prev_amount')
async def callback_update_amount_prev(call: types.CallbackQuery):
    await OrderProduct.waiting_for_product_amount_to_update_prev.set()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, 'Хорошо, давай изменим количество. Сколько нужно внести в список?')

# Записывает новое количество продукта и передает данные в функцию для записи в БД
@dp.message_handler(state=OrderProduct.waiting_for_product_amount_to_update_prev)
async def answer_product_amount_to_update_prev(message: types.Message, state: FSMContext):
    await state.update_data(amount=message.text)
    # Получаем данные из МС и ждем ответ от функции
    product_name = db.search_last_product_in_sl()
    data = await state.get_data()
    product_amount = data.get('amount')
    # Завершает работу с МС
    await state.finish()
    return SendMessage(message.chat.id, db.update_amount_product(product_name, product_amount),
                       reply_markup=kb.start_markup)
# Конец блока обработки функции update_prev_amount

# Начало блока обработки функции update_prev_type
@dp.callback_query_handler(lambda call: call.data == 'update_prev_type')
async def callback_update_type_prev(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(f'Давай выберем новую категорию.', reply_markup=kb.type_markup_to_update_prev)

# Ловил callback и записывает категорию продукта и передает данные в функцию для записи в БД
@dp.callback_query_handler(lambda call: call.data in kb.type_list_callback_to_update_prev)
async def callback_type(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(type=call.data)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # Получаем данные из МС и ждем ответ от функции
    product_name = db.search_last_product_in_sl()
    data = await state.get_data()
    product_type = data.get("type")
    product_type = product_type[:-1]  # Убираем лишний символ для унификации категорий
    # Завершает работу с состояниями
    await state.finish()
    return SendMessage(call.message.chat.id, db.update_type_product(product_name, product_type),
                       reply_markup=kb.start_markup)
# Конец блока обработки функции update_prev_amount


# Обработка callback (изменить другой продукт)
@dp.callback_query_handler(lambda call: call.data == 'update_any')
async def callback_update_any(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await OrderProduct.waiting_for_product_name_to_update.set()
    await bot.send_message(call.message.chat.id, 'Какой продукт будем исправлять?')

# Записывает наименование продукта и проверяет есть ли он в списке
@dp.message_handler(state=OrderProduct.waiting_for_product_name_to_update)
async def answer_product_name_to_update(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    data = await state.get_data()
    product_name = data.get("product")
    if not db.search_product_in_sl(product_name):
        product_name = product_name.capitalize()
        await message.answer(f'{product_name} ещё нет в списке!', reply_markup=kb.choice_markup)
        await state.reset_state(with_data=False)
    else:
        await bot.send_message(message.chat.id, 'Что изменим?', reply_markup=kb.update_markup)
        await state.reset_state(with_data=False)

# Обработка if (add_product)
@dp.callback_query_handler(lambda call: call.data == 'add_product')
async def callback_new_product_add(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer("Сколько добавить в список?", reply_markup=kb.amount_markup)

# Обработка if (cancel_add)
@dp.callback_query_handler(lambda call: call.data == 'cancel_adding')
async def callback_back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # await state.finish()
    return SendMessage(call.message.chat.id, 'Забудем об этом! Давай лучше добавим что-нибудь в список?',
                       reply_markup=kb.start_markup)

# Обработка else
# Начало блока обработки функции update_product
@dp.callback_query_handler(lambda call: call.data == 'update_product')
async def callback_update_name(call: types.CallbackQuery):
    await OrderProduct.waiting_for_product_new_name_to_update.set()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, 'Поняла. Напиши мне новое название.')

# Записывает новое наименование продукта и передает данные в функцию для записи в БД
@dp.message_handler(state=OrderProduct.waiting_for_product_new_name_to_update)
async def answer_product_new_name_to_update(message: types.Message, state: FSMContext):
    await state.update_data(new_product_name=message.text)
    # Получает данные из МС
    data = await state.get_data()
    product_name = data.get("product")
    new_product_name = data.get("new_product_name")
    # Завершает работу с МС
    await state.finish()
    return SendMessage(message.chat.id, db.update_name_product(product_name, new_product_name),
                       reply_markup=kb.start_markup)
# Конец блока обработки функции update_product

# Начало блока обработки функции update_amount
@dp.callback_query_handler(lambda call: call.data == 'update_amount')
async def callback_update_amount(call: types.CallbackQuery):
    await OrderProduct.waiting_for_product_amount_to_update.set()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, 'Укажи, пожалуйста, новое количество.')

# Записывает новое количество продукта
@dp.message_handler(state=OrderProduct.waiting_for_product_amount_to_update)
async def answer_product_amount_to_update(message: types.Message, state: FSMContext):
    await state.update_data(amount=message.text)
    # Получает данные из МС
    data = await state.get_data()
    product_name = data.get('product')
    product_amount = data.get('amount')
    # Завершает работу с МС
    await state.finish()
    return SendMessage(message.chat.id, db.update_amount_product(product_name, product_amount),
                       reply_markup=kb.start_markup)
# Конец блока обработки функции update_amount

# Начало блока обработки функции update_type
@dp.callback_query_handler(lambda call: call.data == 'update_type')
async def callback_update_type(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(f'Давай выберем новую категорию.', reply_markup=kb.type_markup_to_update)

# Ловил callback и записывает категорию продукта и передает данные в функцию для записи в БД
@dp.callback_query_handler(lambda call: call.data in kb.type_list_callback_to_update)
async def callback_type(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(type=call.data)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # Получает сохраненные состояния
    data = await state.get_data()
    product_name = data.get("product")
    product_type = data.get("type")
    # Завершает работу с состояниями
    await state.finish()
    return SendMessage(call.message.chat.id, db.update_type_product(product_name, product_type),
                       reply_markup=kb.start_markup)
# Конец блока обработки функции update_amount
