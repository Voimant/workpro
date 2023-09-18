import asyncio
import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers import users_handlers
from create_bot import bot, dp


users_handlers.register_handlers(dp)

#Логгирование, получение событий:
logging.basicConfig(level=logging.INFO)

#модель машины состояний
# class Fsm(StatesGroup):
#     gos_namber = State()
#     vin = State()




# запуск
async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
