import discord
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv, find_dotenv

# Imports gun dictionaries
from mw2_guns import *

# Discord Intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Discord Token
load_dotenv(find_dotenv())
bot_token = os.getenv('TOKEN')

# Startup event
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# User events
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!iso hemlock"):
        stats = ""
        for item in iso_hemlock:
            stats = stats + "{} : {}\n".format(item,iso_hemlock[item])
        
        await message.channel.send(stats)
            

client.run(bot_token)

        #await message.channel.send("{} : {}".format(item,iso_hemlock[item]))
        
