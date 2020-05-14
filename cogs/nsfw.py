import aiohttp
from discord.ext import commands


class NSFW(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def r34(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://rule34.xxx/index.php?page=post&s=/get') as resp:
                print(resp.status)
                print(await resp.text())
                await session.post('https://rule34.xxx/index.php?page=post&s=/post', data=b'data')




def setup(client):
    client.add_cog(NSFW(client))