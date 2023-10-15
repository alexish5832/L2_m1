import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def programist(ctx):
    img_name = random.choice(os.listdir('images_programist'))
    with open(f'images_programist/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTE1ODAxOTQ2MTM3MTEzNDA5Mw.GLSHfA.aR_BOqCw4PdnVvfMgFIvMro1DRBckbZt1wMj6U")
