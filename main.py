import discord
from discord.ext import commands
from myserver import server_on

TOKEN = "MTA3NjE2MTgxNDQ2MDY0MTI4MA.GN9vSq.CZZIxM2QJcN-zbLen4X7y7ue9b2D_BJe7fL1K4" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

server_on()
bot.run(TOKEN)
