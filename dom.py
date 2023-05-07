import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def spisok(ctx):
    await ctx.send(f'Привет! пользуйся многоразовой посудой, перерабатывай ненужные вещи и заботся о природе ведь она очень красива. и я задолбался с этим дискорд ботом!')

@bot.command()
async def o(ctx):
    images = os.listdir('bio')
    img_name = random.choice(o)
    with open(f'bio/{img_name}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

bot.run("")
