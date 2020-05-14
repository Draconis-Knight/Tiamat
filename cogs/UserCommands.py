from discord.ext import commands
import random

class UserCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        await ctx.channel.trigger_typing()
        responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.trigger_typing()
        await ctx.send(f'{round(self.client.latency * 1000)}ms')

   # @commands.command(name='role', aliases=['r', 'rolldice', 'rdice'])
    #async def roll_dice_command(self, ctx):
        #await ctx.channel.trigger_typing()

        #await ctx.channel.send('Roll dice command works.')

def setup(client):
    client.add_cog(UserCommands(client))
