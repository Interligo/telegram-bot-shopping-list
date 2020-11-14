from aiogram import types

from sl_bot_main import bot
from sl_bot_main import dp
import sl_bot_keyboards as kb
import sl_db_functions as db


@dp.callback_query_handler(lambda call: call.data == 'show')
async def callback_show(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.send_message(call.message.chat.id, db.show_sl(), reply_markup=kb.show_markup)
