import discord
from discord.ext import commands

class AdminCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name='ban', aliases=['banuser'])
    @commands.has_any_role('Twilight')
    async def ban(self, ctx, arg1):
        await ctx.channel.send('Banned {}'.format(arg1))

    @commands.command(name='unban', aliases=['unbanuser'])
    @commands.has_any_role('Twilight')
    async def unban(self, ctx, arg1):
        await ctx.channel.send('Unbanned {}'.format(arg1))

    #@commands.command(name='clear', aliases=['purge'])
    #@commands.has_any_role('Twilight')
    #async def clear(self, ctx, amount=10):
        #await ctx.channel.purge(limit=amount)




def setup(client):
    client.add_cog(AdminCommands(client))
