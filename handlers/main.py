import os
import io
import datetime

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

    filename = datetime.datetime.strftime(datetime.datetime.now(), "%d%m%Y%H%M%S")
    full_path = config.path+filename+".jpg"

    await message.photo[-1].download(destination_file=full_path)

    await sender(full_path)
    
    os.remove(full_path)


@dp.message_handler()
async def test(message):
    await bot.send_message(message.chat.id, "Привет,всё что ты скинешь будет автоматически отправлено в НСФВ канал,Удачки)\nCreated by @fuksys and @OutTuna")
