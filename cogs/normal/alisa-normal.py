import random

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks

class Names(disnake.ui.Select):
    def __init__(self):
        
        options = [
            disnake.SelectOption(label="Акылбек"),
            disnake.SelectOption(label="Александр"),
            disnake.SelectOption(label="Алиса"),
            disnake.SelectOption(label="Анастасия"),
            disnake.SelectOption(label="Андрей"),
            disnake.SelectOption(label="Владимир"),
            disnake.SelectOption(label="Владислав"),
            disnake.SelectOption(label="Даниил"),
            disnake.SelectOption(label="Денис"),
            disnake.SelectOption(label="Егор"),
            disnake.SelectOption(label="Леонид"),
            disnake.SelectOption(label="Олег"),
            disnake.SelectOption(label="Темирхан"),
        ]
        
        super().__init__(
            placeholder="Выбирай",
            min_values=1,
            max_values=1,
            options=options,
        )
        
        
    async def callback(self, interaction: disnake.MessageInteraction):
        choices = {
            "акылбек": 0,
            "александр": 1,
            "алиса": 2,
            "анастасия": 3,
            "андрей": 4,
            "владимир": 5,
            "владислав": 6,
            "даниил": 7,
            "денис": 8,
            "егор": 9,
            "леонид": 10,
            "олег": 11,
            "темирхан": 12,
        }
        user_choice = self.values[0].lower()
        user_choice_index = choices[user_choice]
        
        result_embed = disnake.Embed(color=0x9C84EF)
        result_embed.set_author(name="Значение этого кокного имени")
        
        if user_choice_index == 0:
            result_embed.description = "**Мужское имя Акылбек**\nХарактер имени Акылбек определяется \
коммуникативными способностями, которые имеют для них первостепенное значение. Акылбек - творческая \
личность, очень одаренная в самовыражении, легко делится инновационными и новаторскими концепциями с \
помощью искусства, ораторства. Их работа вдохновляет, мотивирует и возвышает других, и Акылбек находит \
огромную радость, заставляя других улыбаться и быть счастливыми. Из недостатков можно отметить капризность, \
вспыльчивость и обидчивость. Эти негативные черты могут нивилироваться практикой мирного воображения для того, \
чтобы находить моменты тишины, сбросить все ненужное, восстановиться и зарядиться позитивной энергией."
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 1:
            result_embed.description = "**Мужское имя Александр**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 2:
            result_embed.description = "**Женское имя Алиса**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 3:
            result_embed.description = "**Женское имя Анастасия**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 4:
            result_embed.description = "**Мужское имя Андрей**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 5:
            result_embed.description = "**Мужское имя Владимир**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 6:
            result_embed.description = "**Мужское имя Владислав**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 7:
            result_embed.description = "**Мужское имя Даниил**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 8:
            result_embed.description = "**Мужское имя Денис**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 9:
            result_embed.description = "**Мужское имя Егор**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 10:
            result_embed.description = "**Мужское имя Леонид**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 11:
            result_embed.description = "**Мужское имя Леонид**\n"
            result_embed.colour = 0xFFFF00
        elif user_choice_index == 12:
            result_embed.description = "**Мужское имя Темирхан**\n"
            result_embed.colour = 0xFFFF00
        await interaction.response.defer()
        await interaction.edit_original_message(embed=result_embed, content=None, view=None)
        
class NamesView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Names())
        
    @commands.command(
        name="имя",
        descriotion="Пояснит за тваё имя"
        )
    @checks.not_blacklisted()
    async def names(self, context: Context) -> None:
        
        view = NamesView()
        await context.send("Выбери имя ~~своего краша~~", view=view)
    

class Alisa(commands.Cog, name="alisa-normal"):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Alisa(bot))
