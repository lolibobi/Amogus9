import random

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks


           
class Test(commands.Cog, name="test-normal"):
    def __init__(self, bot):
        self.bot = bot
        
class Button(disnake.Button)  

@commands.command(
    name="тест",
    description="aaaa"
)
@checks.not_blacklisted()
async Button(url="https://www.youtube.com/") -> None:
    await context.send("Ссылочка на юбубер")
    

def setup(bot):
    bot.add_cog(Test(bot))
