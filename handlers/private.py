import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/38ca11b0fb33d6d9cf472.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━
🥀 Hᴇʏ,
      I ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ Mᴜsɪᴄ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴏɴ ɢʀᴏᴜᴘ ᴄʜᴀᴛs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ Tᴇʟᴇɢʀᴀᴍ's Vɪᴅᴇᴏ Cʜᴀᴛs...!

┏━━━━━━━━━━━━━━┓
     ᴄʀᴇᴀᴛᴏʀ: VOID  🥀
┗━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Add Void To Your Gc •", url="https://t.me/voidvcbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "✗ ᴄʀᴇᴀᴛᴏʀ ✗", url="https://t.me/voidxtoxic"
                    ),
                    InlineKeyboardButton(
                        "Aɴɪᴍᴇ Cʜᴀᴛ Gʀᴏᴜᴘ", url="https://t.me/horimiya_family"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "• Void Network •", url="https://t.me/horimiya_family"
                    )]
            ]
       ),
    )

@Client.on_message(command(["pin", "repo", "voidvc", "a"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZIiVngACSppiDZZGd6IPFA0TnEuOM3EqFbRxVQACCQMAArU72FSskU3O5FiqcyME")
    await message.reply_text(
        text=f"""» ɪ ᴀᴍ ᴀʟɪᴠᴇ ree !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✗ ᴅᴇᴠᴇʟᴏᴘᴇʀ ✗", url="https://t.me/voidxtoxic")
                  ],[
                    InlineKeyboardButton(
                        "✗ sᴜᴘᴘᴏʀᴛ ✗", url="https://t.me/horimiya_family"
                    ),
                    InlineKeyboardButton(
                        "✗ sᴏᴜʀᴄᴇ ✗", url="https://t.me/horimiya_family"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "✗ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ​​ ✗", url="https://t.me/voidvcbot?startgroup=true"
                    )]
            ]
        ),
    )
