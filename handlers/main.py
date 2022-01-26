import os
import datetime
from traceback import print_tb

import discord
from aiogram import types
from aiogram.types import ContentType

from load import dp, bot
from dcbot import bot as dbot
import config


async def sender(photo):
    channel = dbot.get_channel(config.discord_settings["channel_id"])
    picture = discord.File(photo)
    await channel.send(file=picture)


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_sender(message: types.Message):
    if not os.path.exists(config.path): os.mkdir(config.path)

    c = len(message.photo)-1

    filename = message.photo[c].file_id
    full_path = config.path+filename+".jpg"

    await message.photo[c].download(destination_file=full_path)
    await sender(full_path)

    os.remove(full_path)


@dp.message_handler()
async def test(message):
    await bot.send_message(message.chat.id, "Привет,всё что ты скинешь будет автоматически отправлено в НСФВ канал,Удачки)\nCreated by @fuksys and @OutTuna")
