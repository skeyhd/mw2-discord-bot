import discord
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv, find_dotenv
import datetime

# Imports gun stat dictionaries
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
    await client.change_presence(activity=discord.Game("!help"))

# User events
@client.event
async def on_message(message):

    # Help
    if message.content.startswith("!help"):
        embed = discord.Embed(
                title="COMMANDS",
                description="Here are all of the commands!",
                colour = 000000,
                timestamp=datetime.datetime.utcnow()
        )

        embed.add_field(
            name = "Help & Support", 
            value = "!help \n!donate",
            inline = False
        )

        embed.add_field(
            name = "S Tier Gun Builds",
            value = "!iso hemlock \n!lachmann sub \n!kv broadside \n!sakin mg38 \n!raal mg",
            inline = True
        )

        embed.add_field(
            name = "A Tier Gun Builds",
            value = "!taq 56 \n!vaznev-9k \n!m4 \n!rpk \n!signal 50 \n!kastov 762 \n!m13b \n!chimera \n!kastov-74u",
            inline = True
        )

        embed.set_author(name="MW2/WZ META", icon_url="https://media.discordapp.net/attachments/1081590091182510220/1081679411104985239/ghost.png")
        await message.channel.send(embed=embed)


    # Donate
    if message.content.startswith("!donate"):
        embed = discord.Embed(
            title="DONATE",
            description = "BTC address : bc1q2slgd0du9tfhh7yyjzfa02pnxdjunw20ldhurt \nETH address : 0x67350aB07FBd1115FF7E480AddEf6DA97873879b",
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Iso Hemlock
    if message.content.startswith("!iso hemlock"):
        stats = ""
        for item in iso_hemlock:
            stats = stats + "{} : {}\n".format(item,iso_hemlock[item])
        
        embed = discord.Embed(
            title="Iso Hemlock",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)
    
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
            
    # TAQ 56
    if message.content.startswith("!taq 56"):
        stats = ""
        for item in taq_56:
            stats = stats + "{} : {}\n".format(item,taq_56[item])
        
        await message.channel.send(stats)

    # Vaznev-9K
    if message.content.startswith("!vaznev-9k"):
        stats = ""
        for item in vaznev_9k:
            stats = stats + "{} : {}\n".format(item,vaznev_9k[item])
        
        await message.channel.send(stats)

    # M4
    if message.content.startswith("!m4"):
        stats = ""
        for item in m4:
            stats = stats + "{} : {}\n".format(item,m4[item])
        
        await message.channel.send(stats)

    # RPK
    if message.content.startswith("!rpk"):
        stats = ""
        for item in rpk:
            stats = stats + "{} : {}\n".format(item,rpk[item])
        
        await message.channel.send(stats)

    # Signal 50
    if message.content.startswith("!signal 50"):
        stats = ""
        for item in signal_50:
            stats = stats + "{} : {}\n".format(item,signal_50[item])
        
        await message.channel.send(stats)

    # Kastov 762
    if message.content.startswith("!kastov 762"):
        stats = ""
        for item in kastov_762:
            stats = stats + "{} : {}\n".format(item,kastov_762[item])
        
        await message.channel.send(stats)

    # M13B
    if message.content.startswith("!m13b"):
        stats = ""
        for item in m13b:
            stats = stats + "{} : {}\n".format(item,m13b[item])
        
        await message.channel.send(stats)

    # Chimera
    if message.content.startswith("!chimera"):
        stats = ""
        for item in chimera:
            stats = stats + "{} : {}\n".format(item,chimera[item])
        
        await message.channel.send(stats)

    # Kastov-74U
    if message.content.startswith("!kastov-74u"):
        stats = ""
        for item in kastov_74U:
            stats = stats + "{} : {}\n".format(item,kastov_74U[item])
        
        await message.channel.send(stats)


# Runs bot
client.run(bot_token)
