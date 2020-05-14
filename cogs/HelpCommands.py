import discord
from discord.ext import commands



class HelpCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name='helpcmd', invoke_without_command=True)
    async def helpcommand(self, ctx):
        await ctx.channel.send('Base help command = .help. Subcommands: Misc, Fun, Music')

    @helpcommand.command(name='misc')
    async def misc_subcommand(self, ctx):
        await ctx.channel.send('Misc subcommand from help')

    @helpcommand.command(name='fun')
    @commands.has_any_role('Snapchat', 'Youtube', 'Node')
    async def fun_subcommand(self, ctx):
        await ctx.channel.send('Fun subcommand of Help')

    @helpcommand.command(name='music')
    async def music_subcommand(self, ctx, arg1):
        await ctx.channel.send('Music subcommand')
        
def setup(client):
    client.add_cog(HelpCommands(client))
