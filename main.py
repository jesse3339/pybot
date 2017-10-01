import discord
from discord.ext import commands
import os


# Token Handler
token = ""
try:
    f = open("token.priv", "r")
    token = f.readline()
    f.close()
except FileNotFoundError as e:
    f = open("token.priv", "w+")
    in_token = input("Please input your token: ")
    f.write(in_token)
    token = in_token
    f.close()

# bot description and settings
description = "I aM nIg NoG bOt!"
bot = commands.Bot(command_prefix='$', description=description)

# load directories for cogs
startup_ext = os.listdir("./commands")
if "__pycache__" in startup_ext:
    startup_ext.remove("__pycache__")
startup_ext = [ext.replace('.py', '') for ext in startup_ext]
loaded_ext = []


# bot startup
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    for ext in startup_ext:
        try:
            bot.load_extension("commands.{}".format(ext.replace(".py","")))
            loaded_ext.append(ext)

        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("failed to load extension {} -> {}".format(ext, exc))

    print("Successfully loaded {}".format(loaded_ext))

bot.run(token)
