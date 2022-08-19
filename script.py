import re
import asyncio
import time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from config import API_ID, API_HASH, SESSION_STRING, TEXT, USERNAME

app = Client("my_account", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

async def function(client, message, text):
    time.sleep(6)
    try:
       messages = await message.reply(text)
       check_text = messages.reply_to_message.text
       x = re.match("settings", check_text)
       if x:
         await client.send_message(USERNAME, text)
         username = text.replace('@', '')
         chat = await client.create_channel("Hayırlı olsun", "Channel Description")
         await client.set_chat_username(chat.id, username)
       else:
          pass
    except FloodWait as e:
       print(f"Sleep of {e.value} required by FloodWait ...")
       time.sleep(e.value)
       
@app.on_message(filters.private)
async def check(client, message):
    await function(client, message, text)

app.run()
