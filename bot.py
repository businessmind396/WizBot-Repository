import os
from discord import Intents, Message
from discord.ext import commands

# Intents
intents = Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Simple command
@bot.command(name='hello', help='Say hello to the bot')
async def hello(ctx: Message):
    await ctx.send(f'Hello {ctx.author.mention}!')

# Run the bot with the token from the environment variable
bot.run(os.environ['BOT_TOKEN'])
