import discord
from discord.ext import commands


class MiscCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='assignrole', aliases=['addrole'])
    async def add_role_command(self, ctx, arg1):
        print(arg1)

    @commands.command(name='removerole', aliases=['removerole'])
    async def remove_role_command(self, ctx, arg1):
        await ctx.channel.send('Removing role')


def setup(client):
    client.add_cog(MiscCommands(client))
