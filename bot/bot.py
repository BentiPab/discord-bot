import os
from dotenv import load_dotenv
import discord
from discord.ext.commands import Bot
import requests

url = 'https://ws.geeklab.com.ar/dolar/get-dolar-json.php'

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = Bot(intents=intents, command_prefix="!")


@bot.command(name="dolarblue")
async def dolarBlue(ctx):
    userName = ctx.author.global_name
    res = requests.get(url)
    data = res.json()
    blue = data['blue']
    await ctx.send(f"Hola {userName}! La cotización del dólar blue argentino: {blue} USD")


@bot.event
async def on_message(ctx):
    if (ctx.author == 'iwallas'):
        await ctx.send("Deja de mandar mensajes Waldo come verga")
    await bot.process_commands(ctx)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

bot.run(os.environ.get("DISCORD_TOKEN"))