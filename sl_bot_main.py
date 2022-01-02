import os

from dotenv import load_dotenv
from aiogram import Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher


load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp)
