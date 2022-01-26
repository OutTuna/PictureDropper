import asyncio

from aiogram import Bot, Dispatcher

import config


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)



bot = Bot(token=config.token)
dp = Dispatcher(bot=bot)
