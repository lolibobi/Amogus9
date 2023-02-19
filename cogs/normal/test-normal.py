import random

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks


           
class Test(commands.Cog, name="test-normal"):
    def __init__(self, bot):
        self.bot = bot
        
        
@commands.command(
    name="тест",
    description="aaaa"
)
@checks.not_blacklisted()
async disnake.Button(url="https://www.youtube.com/"):
    await context.send("Ссылочка на юбубер")
    

def setup(bot):
    bot.add_cog(Test(bot))
