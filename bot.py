import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import hashlib
from webinfo import ipInfo, toIp

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} has connected to Discord! They have connected to the following server: '
        f'{guild.name}(id: {guild.id})')
    channels = list(discord.utils.get(bot.guilds, name=GUILD).channels)
    channel = discord.utils.get(channels, name="général")
    await channel.send("I'm up and running !")

@bot.command(name='webinfo', help='Get information about a website')
async def webinfo(ctx, url):
    data = ipInfo(toIp(url))
    string = ""
    for k, v in data.items():
        string += f"{k} : {v}\n"
    await ctx.send(string)

@bot.command(name='ipinfo', help='Get information about an IP address')
async def ipinfo(ctx, addr):
    data = ipInfo(addr)
    string = ""
    for k, v in data.items():
        string += f"{k} : {v}\n"
    await ctx.send(string)

@bot.command(name="hash", help="Returns the hash of the given string (do not contains spaces) in the given algorithm (sha256 by default)")
async def hash(ctx, string, method="sha256"):
    if method in ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_128", "shake_256"]:
        hash = hashlib.new(method)
        hash.update(string.encode())
        await ctx.send("Hashing with " + method + " : " + hash.hexdigest())

bot.run(TOKEN)
