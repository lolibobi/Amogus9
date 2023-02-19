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
        
class Questions(disnake.ui.List):
    def __init__(self):
        
        options = ["Ты сус?", "Я сус?", "Тимур сус?"]
        
    async def callback(self, interaction: disnake.MessageInteraction):
        choices = random.randit(choices)
        
        bot_choice = choices
        bot_choice_index = choices[bot_choice]
        
        result_embed = disnake.Embed(color=0x9C84EF)
        
        if bot_choice_index == options:
            result_embed.description = {bot_choice}
        await interaction.response.defer()
        await interaction.edit_original_message(embed=result_embed, content=None, view=None)
           
class Test(commands.Cog, name="test-normal"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="вопрос",
        descpiption="Амогус задаст тебе вопрос"
    )
    @checks.not_blacklisted()
    async def вопрос(self, context: Context) -> None:
        vopros1 = list( "Тимур сус?", "Амогус сус?" )
        vopros2 = list( "Я сус?", "Алиса сус?" )
        vopros = list( vopros1, vopros2 )
        
        buttons = Choice()
        embed = disnake.Embed(
            title="Вапросик",
            description=vopros,
            color=0x9C84EF
        )
        message = await context.send(embed=embed, view=buttons)
        await buttons.wait()
        result1 = "Ответ верный. Маладец. Держи cockфетку."
        result2 = "Неверный ответ!!! Заебошу тяяяя!"
         
        if vopros == vopros1:
            embed = disnake.Embed(
                title="Вапросик",
                description= result1,
                color=0x5FFC00
            )
        if vopros == vopros2:
            embed = disnake.Embed(
                title="Вапросик",
                description=result1,
                color=0x5FFC00
            )
        else:
            embed = disnake.Embed(
                title="Вапросик",
                description=result2,
                color=0xE02B2B
            )
        await message.edit(embed=embed, content=None, view=None)
            
            
def setup(bot):
    bot.add_cog(Test(bot))
