from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import config




# объект бота
bot = Bot(token=config.TOKEN)
#Диспетчер
dp = Dispatcher(bot, storage=MemoryStorage())

