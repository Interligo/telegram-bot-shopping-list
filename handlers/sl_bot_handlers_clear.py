from aiogram import types
from aiogram.dispatcher.webhook import SendMessage

from sl_bot_main import bot
from sl_bot_main import dp
import sl_db_functions as db


@dp.callback_query_handler(lambda call: call.data == 'clean')
async def callback_clear(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    return SendMessage(call.message.chat.id, db.clear_sl())
