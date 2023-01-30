from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks


class Template(commands.Cog, name="template-normal"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="testcommand",
        description="Это тест команда, которая делает (всё)ничего",
    )
    @checks.not_blacklisted()
    @checks.is_owner()
    async def testcommand(self, context: Context) -> None:

        # напиши сда что-то чтобы было не просто чем ничего

        # Не забудь pass удалить блять, он тут из-за того, что оно ничо не делоет
        pass

def setup(bot):
    bot.add_cog(Template(bot))
