import os

import discord
from aiogram import types
from aiogram.types import ContentType

from load import dp, bot, config
from dcbot import bot as dbot


async def sender(photo: str, username: str):
    if username:
        message = f'Отправлено от: {username}'
    else:
        message = 'У пользователя отсувствует никнейм'
    channel = dbot.get_channel(int(config["Discord"]["channel_id"]))
    picture = discord.File(photo)
    await channel.send(message, file=picture)


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_sender(message: types.Message):
    if not os.path.exists(config["Filesystem"]["path"]): os.mkdir(config["Filesystem"]["path"])

    c = len(message.photo)-1

    filename = message.photo[c].file_id
    full_path = config["Filesystem"]["path"]+filename+".jpg"

    await message.photo[c].download(destination_file=full_path)
    await sender(full_path, message.from_user.username)

    os.remove(full_path)

@dp.message_handler(content_types=[ContentType.VIDEO, ContentType.ANIMATION] )
async def photo_sender(message: types.Message):
    if not os.path.exists(config["Filesystem"]["path"]): os.mkdir(config["Filesystem"]["path"])
    
    if message.video:
        filename = message.video.file_id
        full_path = config["Filesystem"]["path"] + filename + ".mp4"

        await message.video.download(destination_file=full_path)
    else:
        filename = message.animation.file_id
        full_path = config["Filesystem"]["path"] + filename + ".mp4"

        await message.animation.download(destination_file=full_path)

    await sender(full_path, message.from_user.username)

    os.remove(full_path)



@dp.message_handler(content_types=[ContentType.AUDIO])
async def audio_sender(message: types.Message):
    if not os.path.exists(config["Filesystem"]["path"]): os.mkdir(config["Filesystem"]["path"])

    if message.audio:

        filename = message.audio.file_id
        full_path = config["Filesystem"]["path"] + filename + ".mp3"

        await message.audio.download(destination_file=full_path)   

    await sender(full_path, message.from_user.username)
    
    os.remove(full_path)   



@dp.message_handler(content_types=[ContentType.VOICE])
async def audio_sender(message: types.Message):
    if not os.path.exists(config["Filesystem"]["path"]): os.mkdir(config["Filesystem"]["path"])

    if message.voice:

        filename = message.voice.file_id
        full_path = config["Filesystem"]["path"] + filename + ".ogg"

        await message.voice.download(destination_file=full_path)

    await sender(full_path, message.from_user.username)
    
    os.remove(full_path)    
 



@dp.message_handler()
async def test(message):
    await bot.send_message(message.chat.id, "Привет,всё что ты скинешь будет автоматически отправлено в НСФВ канал,Удачки)\nCreated by @fuksys and @OutTuna")
