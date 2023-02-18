import random

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks


class Choice(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.choice = None
        
    @disnake.ui.button(label="Да", style=disnake.ButtonStyle.blurple)
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.choice = button.label.lower()
        self.stop()
        
    @disnake.ui.button(label="Нет", style=disnake.ButtonStyle.blurple)
    async def cancel(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.choice = button.label.lower()
        self.stop()
        
class Questions(disnake.ui.Select):
    def __init__(self):
        
        options = ["Ты сус?", "Я сус?", "Тимур сус?"]
        
    async def callback(self, interaction: disnake.MessageInteraction):
        choices = random.options
        
        bot_choice = choices
        bot_choice_index = choices[bot_choice]
        
        result_embed = disnake.Embed(color=0x9C84EF)
        
        if bot_choice_index == options:
            result_embed.description = {bot_choice}
        await interaction.response.defer()
        await interaction.edit_original_message(embed=result_embed, content=None, view=None)
           
class Test(commands.Cog, name="test-slash"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="вопрос"
        descpiption="Амогус задаст тебе вопрос"
    )
    @checks.not_blacklisted()
    async def questions(self, context: Context) -> None:
        
        await context.send({bot_choice})
        
def setup(bot):
    bot.add_cog(Test(bot))
