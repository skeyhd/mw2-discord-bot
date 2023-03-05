import discord
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
            value = "!taq 56 \n!vaznev-9k \n!m4 \n!rpk \n!signal 50 \n!kastov 762 \n!m13b \n!chimera \n!basilisk \n!kastov-74u \n!pdsw 528 \n!rapp h",
            inline = True
        )

        embed.add_field(
            name = "B Tier Gun Builds",
            value = "!mcpr-300 \n!fennec 45 \n!lachmann 762",
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
        
        embed = discord.Embed(
            title="Lachmann Sub",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # KV Broadside
    if message.content.startswith("!kv broadside"):
        stats = ""
        for item in kv_broadside:
            stats = stats + "{} : {}\n".format(item,kv_broadside[item])
        
        embed = discord.Embed(
            title="KV Broadside",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)
    
    # Sakin MG38
    if message.content.startswith("!sakin mg38"):
        stats = ""
        for item in sakin_mg38:
            stats = stats + "{} : {}\n".format(item,sakin_mg38[item])
        
        embed = discord.Embed(
            title="Sakin MG38",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)
    
    # Raal MG
    if message.content.startswith("!raal mg"):
        stats = ""
        for item in raal_mg:
            stats = stats + "{} : {}\n".format(item,raal_mg[item])
        
        embed = discord.Embed(
            title="Raal MG",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)
            
    # TAQ 56
    if message.content.startswith("!taq 56"):
        stats = ""
        for item in taq_56:
            stats = stats + "{} : {}\n".format(item,taq_56[item])
        
        embed = discord.Embed(
            title="TAQ 56",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Vaznev-9K
    if message.content.startswith("!vaznev-9k"):
        stats = ""
        for item in vaznev_9k:
            stats = stats + "{} : {}\n".format(item,vaznev_9k[item])
        
        embed = discord.Embed(
            title="Vaznev 9K",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # M4
    if message.content.startswith("!m4"):
        stats = ""
        for item in m4:
            stats = stats + "{} : {}\n".format(item,m4[item])
        
        embed = discord.Embed(
            title="M4",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # RPK
    if message.content.startswith("!rpk"):
        stats = ""
        for item in rpk:
            stats = stats + "{} : {}\n".format(item,rpk[item])
        
        embed = discord.Embed(
            title="RPK",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Signal 50
    if message.content.startswith("!signal 50"):
        stats = ""
        for item in signal_50:
            stats = stats + "{} : {}\n".format(item,signal_50[item])
        
        embed = discord.Embed(
            title="Signal 50",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Kastov 762
    if message.content.startswith("!kastov 762"):
        stats = ""
        for item in kastov_762:
            stats = stats + "{} : {}\n".format(item,kastov_762[item])
        
        embed = discord.Embed(
            title="Kastov 762",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # M13B
    if message.content.startswith("!m13b"):
        stats = ""
        for item in m13b:
            stats = stats + "{} : {}\n".format(item,m13b[item])
        
        embed = discord.Embed(
            title="M13B",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Chimera
    if message.content.startswith("!chimera"):
        stats = ""
        for item in chimera:
            stats = stats + "{} : {}\n".format(item,chimera[item])
        
        embed = discord.Embed(
            title="Chimera",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Basilisk
    if message.content.startswith("!basilisk"):
        stats = ""
        for item in basilisk:
            stats = stats + "{} : {}\n".format(item,basilisk[item])
        
        embed = discord.Embed(
            title="Basilisk",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Kastov-74U
    if message.content.startswith("!kastov-74u"):
        stats = ""
        for item in kastov_74U:
            stats = stats + "{} : {}\n".format(item,kastov_74U[item])
        
        embed = discord.Embed(
            title="Kastov-74u",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # PDSW 528
    if message.content.startswith("!pdsw 528"):
        stats = ""
        for item in pdsw_528:
            stats = stats + "{} : {}\n".format(item,pdsw_528[item])
        
        embed = discord.Embed(
            title="PDSW 528",
            description=stats,
            colour = 000000
        )

    # Rapp H
    if message.content.startswith("!rapp h"):
        stats = ""
        for item in rapp_h:
            stats = stats + "{} : {}\n".format(item,rapp_h[item])
        
        embed = discord.Embed(
            title="Rapp H",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # MCPR-300
    if message.content.startswith("!mcpr-300"):
        stats = ""
        for item in mcpr_300:
            stats = stats + "{} : {}\n".format(item,mcpr_300[item])
        
        embed = discord.Embed(
            title="MCPR-300",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Fennec 45
    if message.content.startswith("!fennec 45"):
        stats = ""
        for item in fennec_45:
            stats = stats + "{} : {}\n".format(item,fennec_45[item])
        
        embed = discord.Embed(
            title="Fennec 45",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

    # Lachmann-762
    if message.content.startswith("!lachmann 762"):
        stats = ""
        for item in lachmann_762:
            stats = stats + "{} : {}\n".format(item,lachmann_762[item])
        
        embed = discord.Embed(
            title="Lachmann 762",
            description=stats,
            colour = 000000
        )

        await message.channel.send(embed=embed)

# Runs bot
client.run(bot_token)

        
