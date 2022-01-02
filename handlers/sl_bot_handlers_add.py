from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.webhook import SendMessage

from sl_bot_main import bot, dp
from sl_bot_states import OrderProduct
import sl_bot_keyboards as kb
import sl_db_functions as db


@dp.callback_query_handler(lambda call: call.data == 'add')
async def callback_add(call: types.CallbackQuery):
    await OrderProduct.waiting_for_product_name_to_add.set()
    await bot.send_message(call.message.chat.id, f'Что добавим в список?')
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)


@dp.message_handler(state=OrderProduct.waiting_for_product_name_to_add)
async def answer_product_name_to_add(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    # Проверка на существование такой записи в БД.
    data = await state.get_data()
    product_name = data.get("product")
    product_name = product_name.lower()
    if db.search_product_in_sl(product_name):
        await message.answer(f"Ой, {product_name} уже в списке!", reply_markup=kb.select_markup)
        await state.reset_state(with_data=False)
    else:
        await message.answer("Сколько добавить в список?", reply_markup=kb.amount_markup)
        await state.reset_state(with_data=False)


# Обработка if (выбор: увеличить на +1 из answer_product_name_to_add).
@dp.callback_query_handler(lambda call: call.data == 'count_up')
async def callback_count_up(call: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    data = await state.get_data()
    product_name = data.get("product")
    await state.finish()
    return SendMessage(call.message.chat.id, db.count_up_amount_product(product_name),
                       reply_markup=kb.start_markup)


# Обработка if (выбор: отменить ввод) из answer_product_name_to_add.
@dp.callback_query_handler(lambda call: call.data == 'cancel')
async def callback_back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await state.finish()
    return SendMessage(call.message.chat.id, 'Забудем об этом! Давай лучше добавим что-нибудь в список?',
                       reply_markup=kb.start_markup)


# Обработка else из answer_product_name_to_add.
@dp.callback_query_handler(lambda call: call.data in kb.amount_list_callback)
async def callback_amount(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(amount=call.data)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer('В какую категорию запишем?', reply_markup=kb.type_markup)


@dp.callback_query_handler(lambda call: call.data in kb.type_list_callback)
async def callback_type(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(type=call.data)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    data = await state.get_data()
    product_name = data.get('product')
    product_amount = data.get('amount')
    product_type = data.get('type')
    await state.finish()
    return SendMessage(call.message.chat.id, db.add_to_sl(product_name, product_amount, product_type),
                       reply_markup=kb.start_markup)
