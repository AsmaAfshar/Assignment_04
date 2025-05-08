import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Needed for reading messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello there!")

bot.run("MTM2OTk1ODk1ODg5ODYxMDIwNg.GpdvCV.acL4AzHXQi_FKNPfVsnKwIQKIJE-lMtw0F358M")
