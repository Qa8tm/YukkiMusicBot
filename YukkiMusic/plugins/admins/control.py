import asyncio
import os
import random
from asyncio import QueueEmpty

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery

from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.decorators import AdminRightsCheck
from config import get_queue
from YukkiMusic import app
from YukkiMusic.misc import db as db_mem
from YukkiMusic.core import Queues
from YukkiMusic.utils.database.memorydatabase import (add_active_chat, is_active_chat,
                                  is_music_playing, music_off, music_on,
                                  remove_active_chat)



@app.on_callback_query(
    filters.regex(pattern=r"^(pausecb|skipcb|stopcb|resumecb)$")
)
async def admin_risghts(_, CallbackQuery):
    global get_queue
    command = CallbackQuery.matches[0].group(1)
    if not await is_active_chat(CallbackQuery.message.chat.id):
        return await CallbackQuery.answer(
            "Nothing is playing on voice chat.", show_alert=True
        )
    chat_id = CallbackQuery.message.chat.id
    if command == "pausecb":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "Music is already Paused", show_alert=True
            )
        await music_off(chat_id)
        await Yukki.pause_stream(chat_id)
        await CallbackQuery.answer(
                "تم ايقاف التشغيل موقتا ☕🍀", show_alert=True
            )
    if command == "resumecb":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "Music is already Resumed.", show_alert=True
            )
        await music_on(chat_id)
        await Yukki.resume_stream(chat_id)
        await CallbackQuery.answer("تم استكمال التشغيل ☕🍀", show_alert=True)
    if command == "stopcb":
        if CallbackQuery.message.chat.id not in db_mem:
            db_mem[CallbackQuery.message.chat.id] = {}
        wtfbro = db_mem[CallbackQuery.message.chat.id]
        try:
            Queues.clear(chat_id)
        except QueueEmpty:
            pass
        await Yukki.stop_stream(chat_id)
        await CallbackQuery.answer(
                "تم انهاء التشغيل بنجاح ⚡", show_alert=True
            )
