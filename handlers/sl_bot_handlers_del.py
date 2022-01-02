from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.webhook import SendMessage

from sl_bot_main import bot
from sl_bot_main import dp
from sl_bot_states import OrderProduct
import sl_bot_keyboards as kb
import sl_db_functions as db


@dp.callback_query_handler(lambda call: call.data == 'del')
async def callback_del(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, 'Выбери, что хочешь удалить.', reply_markup=kb.del_prev_any_markup)


# Обработка callback (удалить последний введенный продукт).
@dp.callback_query_handler(lambda call: call.data == 'del_previous')
async def callback_del_previous(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    product_name = db.search_last_product_in_sl()
    await bot.send_message(call.message.chat.id, db.delete_from_sl(product_name), reply_markup=kb.start_markup)


# Обработка callback (удалить продукт).
@dp.callback_query_handler(lambda call: call.data == 'del_any')
async def callback_del_any_product(call: types.CallbackQuery):
    await OrderProduct.waiting_for_product_name_to_del.set()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, 'Что будем удалять?')


@dp.message_handler(state=OrderProduct.waiting_for_product_name_to_del)
async def answer_product_name_to_del(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await state.reset_state(with_data=False)
    data = await state.get_data()
    product_name = data.get('product')
    product_name = product_name.capitalize()
    if not db.search_product_in_sl(product_name):
        await message.answer(f'{product_name} нет в списке в списке. Продолжим?', reply_markup=kb.start_markup)
        await state.reset_state(with_data=False)
    else:
        return SendMessage(message.chat.id, db.delete_from_sl(product_name), reply_markup=kb.start_markup)
