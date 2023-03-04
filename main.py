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

    if message.content.startswith("!help"):
        help_command = "!iso hemlock \n!lachmann sub \n!kv broadside \n!sakin mg38 \n!raal mg"
        
        await message.channel.send(help_command)


    # Iso Hemlock
    if message.content.startswith("!iso hemlock"):
        stats = ""
        for item in iso_hemlock:
            stats = stats + "{} : {}\n".format(item,iso_hemlock[item])
        
        await message.channel.send(stats)
    
    # Lachmann Sub
    if message.content.startswith("!lachmann sub"):
        stats = ""
        for item in lachmann_sub:
            stats = stats + "{} : {}\n".format(item,lachmann_sub[item])
        
        await message.channel.send(stats)
    
    # KV Broadside
    if message.content.startswith("!kv broadside"):
        stats = ""
        for item in kv_broadside:
            stats = stats + "{} : {}\n".format(item,kv_broadside[item])
        
        await message.channel.send(stats)
    
    # Sakin MG38
    if message.content.startswith("!sakin mg38"):
        stats = ""
        for item in sakin_mg38:
            stats = stats + "{} : {}\n".format(item,sakin_mg38[item])
        
        await message.channel.send(stats)
    
    # Raal MG
    if message.content.startswith("!raal mg"):
        stats = ""
        for item in raal_mg:
            stats = stats + "{} : {}\n".format(item,raal_mg[item])
        
        await message.channel.send(stats)
            

client.run(bot_token)
