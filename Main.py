import discord
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import asyncio
import time
import json
import os
import random

client = commands.Bot(command_prefix='.')
status = cycle(['?help',
                'aldoer ekess wer jimosiig',
                'doegeir ihk wer hrrac',
                'majakir naam',
                'natorkir vrelveli',
                f'{len(client.guilds)} servers',
                f'Playing with {len(set(client.users))} users'])


messages = joined = 0


def read_token():
    for filename in os.listdir('.\database'):
        with open(r'C:\Users\Draconis\IdeaProjects\Tiamat\database\token.json', 'r') as f:
            lines = f.readlines()
            return lines[0].strip()


token = read_token()


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('.\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    change_status.start()
    print(client.user.name)
    print(client.user.id)
    print (f'Playing with {len(client.users)} users')
    print (f'Playing with {len(client.guilds)} servers')


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count('member') > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick='Name already exists')


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == 'Welcome':
            await client.channel.send(f'''Welcome to the server {member.mention}''')
            role = discord.utils.get(member.guild.roles, id='584566079855001640')
            await member.add_roles(role)


@client.event
async def on_member_remove(member):
    print(f'(member) wer jimosiig tepohaic woari vi sepa.')


@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(52839423435341824)
    channels = ['tiamat']
    if str(message.channel) in channels and message.content.find('hello') != -1:
                    await message.channel.trigger_typing()
                    await message.channel.send('svabol shilta wer jimosiig dask tir ihk wux vrak')
                    await client.process_commands(message)

@client.command()
#@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

##last_string = 0
@tasks.loop(seconds=10)
async def change_status():
    # Update the member count string
##    list[str_member_index] = f'Playing with {len(set(client.users))} users'
##    status_str = list[last_string]
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))#change to status_str and remove next
##    last_string += 1
##    if last_string == len(list):
##        last_string = 0



client.run(token)
