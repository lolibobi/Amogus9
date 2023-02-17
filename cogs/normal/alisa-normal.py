import random

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks

def setup(bot):
    bot.add_cog(alisa(bot))
