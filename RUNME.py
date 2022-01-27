#!/usr/bin/env python
import logging

from dcbot import bot
from load import config
import handlers


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    bot.run(config['Discord']['token'])
