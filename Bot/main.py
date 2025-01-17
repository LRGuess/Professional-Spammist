import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
universal_footer = "Bot by @BigSaltyBeans, ;)"

spam_requests = {}

@bot.tree.command(name='spamuser', description='Ping a user a set amount of times')
async def ping(ctx: discord.Interaction, *, user: discord.User, amount: int):
    await ctx.response.defer()
    mention = user.id
    spam_requests[user.id] = False

    for i in range(amount):
        if spam_requests.get(user.id):
            break
        await ctx.channel.send(f'<@{mention}>')

    embed = discord.Embed(title='Spam Complete', description=f'Successfully pinged {user.mention}!', color=0x00ff00)
    embed.set_footer(text=universal_footer)
    await ctx.followup.send(embed=embed)

@bot.tree.command(name='stop', description='Stop your own spam')
async def stop(ctx: discord.Interaction):
    spam_requests[ctx.user.id] = True
    embed = discord.Embed(title='Spam Stopped', description='Your spam has been stopped.', color=0xff0000)
    embed.set_footer(text=universal_footer)
    await ctx.response.send_message(embed=embed)

@bot.tree.command(name='about', description='About the bot')
async def about(ctx: discord.Interaction):
    await ctx.response.defer()
    embed = discord.Embed(title='About', description='A simple spam-ping bot to annoy people! \n Please use wisely \n \n Made by BigSaltyBeans \n Source Code: [GitHub](https://github.com/LRGuess/Professional-Spammist) \n Support Server: [K-Bean Studios](https://discord.gg/D4WUX7r3)', color=0x00ff00)
    embed.set_footer(text=universal_footer)
    await ctx.followup.send(embed=embed)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')

bot.run(DISCORD_TOKEN)    