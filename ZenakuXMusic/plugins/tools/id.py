from ZenakuXMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        button = InlineKeyboardButton(" ᴄʟᴏsᴇ ", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            f"**Your ID**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**Chat ID**: `{message.chat.id}'",
            reply_markup=markup
        )
    else:
        button = InlineKeyboardButton(" ᴄʟᴏsᴇ ", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply(
           f"**Your id**: `{message.from_user.id}`\n**chat id**: `{message.chat.id}`",
           reply_markup=markup
        )
