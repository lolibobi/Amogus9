from disnake import ApplicationCommandInteraction
from disnake.ext import commands

from helpers import checks


class Template(commands.Cog, name="template-slash"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command(
        name="testcommand",
        description="Не трож, блять, это моя команда, она тебе не подвластна",
    )
    @checks.not_blacklisted()
    @checks.is_owner()
    async def testcommand(self, interaction: ApplicationCommandInteraction):

        # напиши сда что-то чтобы было не просто чем ничего
        a = 0
        if a == 0:
            await interaction.send("aaaa")

        # Не забудь pass удалить блять, он тут из-за того, что оно ничо не делоет
        # pass

def setup(bot):
    bot.add_cog(Template(bot))
