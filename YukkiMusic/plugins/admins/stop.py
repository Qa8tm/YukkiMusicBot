#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from YukkiMusic.plugins.play.filters import command
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Yukki.stop_stream(chat_id)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )


@app.on_message(
    command(["اسكت", "ايقاف"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def endstr(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text("**انا لا اعمل الان 🙂**")
    await Yukki.stop_stream(chat_id)
    await message.reply_text("**تم الايقاف بنجاح 😢♥️**")
