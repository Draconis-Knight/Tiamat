# Tiamat Personal discord bot

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

Prerequisites
Python 3.5.3 or higher is required

To install the library without full voice support, you can just run the following command:

# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
Otherwise to get voice support you should run the following command:

# Linux/macOS
python3 -m pip install -U discord.py[voice]

# Windows
py -3 -m pip install -U discord.py[voice]

Optional Packages
PyNaCl (for voice support)
Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. apt, dnf, etc) before running the above commands:

libffi-dev (or libffi-devel on some systems)
python-dev (e.g. python3.6-dev for Python 3.6)

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('token')


Links
documentation for the python version
https://discordpy.readthedocs.io/en/latest/index.html
Official Discord Server
https://discord.gg/r3sSKJJ
Discord API server
https://discord.gg/discord-api
