from datetime import datetime
from sys import version_info
from time import time

from config.config import ALIVE_IMG, ELNQYB
from config.config import LOG_GROUP_ID as log
from YukkiMusic.plugins.play.filters import command, other_filters
from pyrogram import Client, filters
from strings import get_command, get_string
from YukkiMusic import app
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1
__version__ = "0.0.5"

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)



@app.on_message(
    command(["alive", "معلومات", "سورس", "السورس"]) & filters.group & ~filters.edited
)
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Group", url=f"https://t.me/barelnqyb"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/elnqyb"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm Alived **\n\n🧑🏼‍💻 My Master: [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)\n👾 Bot Version: `v{__version__}`\n🔥 Pyrogram Version: `{pyrover}`\n🐍 Python Version: `{__python_version__}`\n✨ PyTgCalls Version: `{pytover.__version__}`\n🆙 Uptime Status: `{uptime}`\n\n❤ **Thanks for Adding me here, for playing video & music on your Group's video chat**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@app.on_message(command(["ping", "بنج"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@app.on_message(command(["uptime", "وقت التشغيل"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )


@app.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await app.send_text(log, f"New Group : {m.chat_username}")
            return await m.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption="""**مرحباً بك \n
⌁ ⁞  بوت تشغيل الأغاني والفيديو  في المكالمه ' المرئية
 البوت قيد التشغيل الان ...... ⚡♥️
⌁ ⁞ my developer [𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶](https://t.me/ahmedelnqyb)
⌁ ⁞  قم بإضافة البوت اللي مجموعتك واستمع إلى الموسيقى ومشاهدة الفيديوهات ♥️""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Channel", url=f"https://t.me/elnqyb"),
                            InlineKeyboardButton("Support", url=f"https://t.me/barelnqyb")
                        ],
                        [
                            InlineKeyboardButton("اضف البوت الى مجموعتك", url=f"https://t.me/{app.username}?startgroup=true")
                        ]
                    ]
                )
            )


@app.on_message(
    command(["ahmedelnqyb"]) & filters.group & ~filters.edited
)
async def starttt_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"𝗦𝗲𝗹𝗹𝗰𝘁 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲 𝘁𝗼 𝗹𝗲𝗮𝗿𝗻 𝗺𝗼𝗿𝗲",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("اللغة العربية 🇪🇬", callback_data="arbic")
                        ],
                        [   
                            InlineKeyboardButton("English language 🇺🇲", callback_data="english")
                        ],
                        [
                            InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", url=f"https://t.me/ahmedelnqyb")
                        ]
                    ]
                )
            )

@app.on_message(command(["/help", "الاوامر"]) & filters.group & ~filters.edited)
async def starhelp(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"𝗦𝗲𝗹𝗹𝗰𝘁 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲 𝘁𝗼 𝗹𝗲𝗮𝗿𝗻 𝗺𝗼𝗿𝗲",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("اللغة العربية 🇪🇬", callback_data="arbic")
                        ],
                        [   
                            InlineKeyboardButton("English language 🇺🇲", callback_data="english")
                        ],
                        [
                            InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", url=f"https://t.me/ahmedelnqyb")
                        ]
                    ]
                )
            )

@app.on_message(command(["المطور", "النقيب"]) & filters.group & ~filters.edited)
async def dev(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{ELNQYB}",
        caption=f"**My Developer : @ahmedelnqyb**",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", url=f"https://t.me/ahmedelnqyb")
                        ]
                    ]
                )
            )

@app.on_message(command(["تست", "بوت", "البوت"]) & filters.group & ~filters.edited)
async def bott(client: Client, message: Message):
    await message.reply_text(" البوت قيد التشغيل الان ⚡",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𝗧𝗲𝗺 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", url=f"https://t.me/barelnqyb")
                        ]
                    ]
                )
            )
