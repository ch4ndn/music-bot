from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Configuration
api_id = 21285273
api_hash = "0d085c47077cdc89721459a347a96b65"
bot_token = "7915939730:AAF36DTkoeUJ3to3TbGWx-MqTSrSamvvpa4"
session_string = "BQFEyZkAKJQicUNowEQgENHLLUtWd7tI8k5D7anrHGABWJAeiHXNyHErGFdW7dktN38G5axjhnJa4MMO6Qdp7DLBdMY51Jxy1O4vcL-PozLXiwIm3JWig36rzJzHs5TlLvA2499mByZ1vi9lQsI-ODtbTL7nFVnSe-4pCNEVZLO0WWMyZQD5lI4kwsJRd47CJQvHMZMIx6j7ssRkK_xpYROO0Twle0bGJODTrJXmR8_CYV1KkEhMvIXbRiRGSh_B18sQlZXl6skqUsIshth7TsgJJTWj42zTIT_2s2t5whAh6QHAIBWQueZBgibbzAaUNMOmqdecndjVAnFG9NRcRFKBKcItZwAAAAGWibR7AA"

# Initialize bot client
app = Client(
    name="sanatani_music_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    session_string=session_string
)

BOT_IMAGE = "https://res.cloudinary.com/dtjjgiitl/image/upload/q_auto:good,f_auto,fl_progressive/v1752935054/d95megrfotatymyzumq6.jpg"

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_photo(
        photo=BOT_IMAGE,
        caption=(
            "⦿ HEY, I AM SANATANI MUSIC BOT 🎵\n"
            "➻ A Powerful Telegram Streaming Bot\n"
            "─────────────────────────────\n"
            "➻ USAGE: /play | /vplay | /pause | /resume | /help"
        ),
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🌹 OWNER 🌹", url="https://t.me/snxrajput"),
                InlineKeyboardButton("✨ SUPPORT ✨", url="https://t.me/+kTMKvxD4f3s1YmFl")
            ],
            [
                InlineKeyboardButton("😍 ADD ME BABY 😍", url=f"https://t.me/{_.me.username}?startgroup=true")
            ],
            [
                InlineKeyboardButton("🚀 HELP & CMDS 🚀", callback_data="help")
            ],
            [
                InlineKeyboardButton("❄️ SOURCE ❄️", url="https://github.com/"),
                InlineKeyboardButton("☁️ ABOUT ☁️", callback_data="about")
            ]
        ])
    )

@app.on_callback_query(filters.regex("help"))
async def help_menu(_, callback_query):
    await callback_query.message.edit_text(
        "**Available Commands:**\n"
        "/play - Play music\n"
        "/vplay - Play video music\n"
        "/pause - Pause the music\n"
        "/resume - Resume music\n"
        "/skip - Skip current song\n"
        "/stop - Stop playback\n"
        "/auth - Authorize a user\n"
        "/unauth - Unauthorize a user\n"
        "/authusers - List authorized users\n",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ BACK", callback_data="start")]
        ])
    )

@app.on_callback_query(filters.regex("about"))
async def about_menu(_, callback_query):
    await callback_query.message.edit_text(
        "This bot is created by @snxrajput for streaming high quality audio & video in groups and channels.\n\n"
        "Powered by Pyrogram + PyTgCalls.\nEnjoy the beats! 🎶",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ BACK", callback_data="start")]
        ])
    )

@app.on_callback_query(filters.regex("start"))
async def back_to_start(_, callback_query):
    await start(_, callback_query.message)

# Run the app
app.run()
