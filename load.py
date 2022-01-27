import asyncio

from aiogram import Bot, Dispatcher

from config import config


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)



bot = Bot(token=config['Telegram']['token'])
dp = Dispatcher(bot=bot)
