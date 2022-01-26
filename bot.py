import logging

from dcbot import bot
from config import discord_settings as settings
import handlers


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    bot.run(settings['token'])
