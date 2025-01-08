from datetime import timedelta
from os import scandir

import discord
from discord import app_commands, Forbidden
from discord.ext import commands

import sathya_secrets

token = sathya_secrets.TOKEN
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)


async def preload():
    for cog in scandir("./cogs"):
        if cog.name.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{cog.name[:-3]}')
                print(f'Loaded {cog.name}')
            except Exception as e:
                print(f"{cog.name} failed to load: ", e)


@bot.event
async def setup_hook():
    await preload()

@bot.event
async def on_ready():
    print(f'{bot.user} is now online.')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command(name="bonk")
@commands.is_owner()
async def sync_commands(ctx):
    synced = await ctx.bot.tree.sync()
    print(synced)
    await ctx.send("Hi, I'm Sathya! Commands have been synced!")

@bot.command(name="whack")
@commands.is_owner()
async def reload_extensions(ctx):
    for cog in scandir("./cogs"):
        if cog.name.endswith('.py'):
            try:
                await bot.reload_extension(f'cogs.{cog.name[:-3]}')
                print(f'Loaded {cog.name}')
            except Exception as e:
                print(f"{cog.name} did not reload properly: ", e)
    await ctx.send("Extensions have been reloaded.")

bot.run(token)
