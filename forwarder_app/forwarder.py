import os
import asyncio
import discord
from discord import Intents
from discord.ext import commands
from telegram import Bot
import os
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']


intents = Intents.default()
intents.message_content = True
discord_bot = commands.Bot(command_prefix='!', intents=intents)
telegram_bot = Bot(token=TELEGRAM_TOKEN)
forward_enabled = False
bot_name = ""

@discord_bot.event
async def on_ready():
    global bot_name
    bot_name = discord_bot.user
    print(f'{discord_bot.user} has connected to Discord!')

@discord_bot.event
async def on_message(message):
    print("Message received: " + message.content)
    global forward_enabled
    if forward_enabled:
        chat_id = TELEGRAM_CHAT_ID
        if message.author == discord_bot.user:
            print("User is the author: not forwarding")
            return
        content = f'{message.author}: {message.content}'
        asyncio.create_task(telegram_bot.send_message(chat_id, content))
        print("Sent!")

def start_discord_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(discord_bot.start(DISCORD_TOKEN))
    except KeyboardInterrupt:
        loop.run_until_complete(discord_bot.logout())
    finally:
        loop.close()

def enable_forwarding():
    global forward_enabled
    forward_enabled = True
    print("Bot enabled!")

def disable_forwarding():
    global forward_enabled
    forward_enabled = False
    print("Bot disabled")
