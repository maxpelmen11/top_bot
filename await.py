 import discord
from discord.ext import commands
import os
import random
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
@bot.command()
async def school(ctx):
    print(os.listdir('school'))
    img_name = random.choice(school)
# А вот так можно подставить имя файла из переменной!
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)\
            await ctx.send(file=picture)
@bot.command()
async def animals(ctx):
    print(os.listdir('animals'))
    img_name = random.choice(animals)
# А вот так можно подставить имя файла из переменной!
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
            

bot.run("ТMTA5NzE5OTg3ODMxNDE0Mzc2NA.G2wBNA.uZfOkNYnwBaPlaKkzOhBkslqvPAKma95_mFNWE")
