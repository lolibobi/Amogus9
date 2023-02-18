import random

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks

class Alisa(commands.Cog, name="alisa-normal"):
    def __init__(self, bot):
        self.bot = bot
        

def setup(bot):
    bot.add_cog(Test(bot))
