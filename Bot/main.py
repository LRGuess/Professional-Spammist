import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
universal_footer = "Bot by @BigSaltyBeans, ;)"

@bot.tree.command(name='spamuser', description='Ping a user a set amount of times')
async def ping(ctx: discord.Interaction, *, user: discord.User, amount: int):
    ctx.response.defer()
    mention = user.id

    for i in range(amount):
        await ctx.channel.send(f'<@{mention}>')

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')

bot.run(DISCORD_TOKEN)    