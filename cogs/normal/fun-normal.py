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

    @disnake.ui.button(label="Орёль", style=disnake.ButtonStyle.blurple)
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.choice = button.label.lower()
        self.stop()

    @disnake.ui.button(label="Решко", style=disnake.ButtonStyle.blurple)
    async def cancel(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.choice = button.label.lower()
        self.stop()
        
class Names(disnake.ui.Select):
    def __init__(self):
        
        options = [
            disnake.SelectOption(
                label="Алиса"
            ),
            disnake.SelectOption(
                label="Тимур"
            ),
        ]
        
        super().__init__(
            placeholder="Выбирай",
            min_values=1,
            max_values=1,
            options=options,
        )
        
        
    async def callback(self, interaction: disnake.MessageInteraction):
        choices = {
            "Алиса": 0,
            "Тимур": 1,
        }
        user_choice = self.values.lower()
        user_choice_index = choices[user_choice]
        
        result_embed = disnake.Embed(color=0x9C84EF)
        result_embed.set_author(name=interaction.author.display_name, icon_url=interaction.author.avatar.url)
        
        if user_choice_index == 0:
            result_embed.description = f"**Женское имя Алиса**\nЖенское имя Алиса является сокращённой формой имени Adelaide (фр. Adelaide), в свою очередь представляющего собой французский вариант древнегерманского имени Adalheid (Adelheid, Adelheidis). Это сложное слово включает два корня: adal (благородный, знатный) и heid (вид, род, образ). Таким образом, имя Adalheid означает не что иное, как «благородная видом», «благородная происхождением» или же просто «благородство». Такое же значение, с определённой эмоциональной окраской, можно признать и за именем Алиса. Существуют гипотезы о связи имени Алиса с греческим женским именем Каллиста, или с греческим же словом aletheia («истина»)."
            result_embed.colour = 0xF59E42
        elif user_choice_index == 1:
            result_embed.description = f"**Мужское имя Тимур**\nТиму́р (тюрк. Tümür, Demir — «железо») — мужское личное имя тюркского и монгольского происхождения. Это имя означает стойкого, прочного человека. Имя стало знаменитым благодаря полководцу и завоевателю Тимуру (Тамерлану) (1336—1405)."
            result_embed.colour = 0xF59E42
        await interaction.response.defer()
        await interaction.edit_original_message(embed=result_embed, content=None, view=None)
        
class NamesView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Names())
        
class RockPaperScissors(disnake.ui.Select):
    def __init__(self):
        
        options = [
            disnake.SelectOption(
                label="Камень", description="На вид - как твердая пластмасса.", emoji="🪨"
            ),
            disnake.SelectOption(
                label="Бумага", description="Довольно влажный выбор.", emoji="🧻" # ножницы-камень-бумага
            ),
            disnake.SelectOption(
                label="Ножницы", description="Опасненька, можно порезатьс.", emoji="✂"
            ),
        ]

        super().__init__(
            placeholder="Выбирастинк...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        choices = {
            "камень": 0,
            "бумага": 1,
            "ножницы": 2,
        }
        user_choice = self.values[0].lower()
        user_choice_index = choices[user_choice]

        bot_choice = random.choice(list(choices.keys()))
        bot_choice_index = choices[bot_choice]

        result_embed = disnake.Embed(color=0x9C84EF)
        result_embed.set_author(name=interaction.author.display_name, icon_url=interaction.author.avatar.url)

        if user_choice_index == bot_choice_index:
            result_embed.description = f"**Ничья!**\nМы оба выбрали "  ' "' + user_choice + '"'
            result_embed.colour = 0xF59E42
        elif user_choice_index == 0 and bot_choice_index == 2:
            result_embed.description = f"**Блять ты выйграл!**\nТы выбрал {user_choice} а я" ' "' + bot_choice + '"'
            result_embed.colour = 0x9C84EF
        elif user_choice_index == 1 and bot_choice_index == 0:
            result_embed.description = f"**Блять ты выйграл!**\nТы выбрал {user_choice} а я" ' "' + bot_choice + '"'
            result_embed.colour = 0x9C84EF
        elif user_choice_index == 2 and bot_choice_index == 1:
            result_embed.description = f"**Блять ты выйграл!**\nТы выбрал {user_choice} а я" ' "' + bot_choice + '"'
            result_embed.colour = 0x9C84EF
        else:
            result_embed.description = f"**САСАААААААТЬ!**\nТы выбрал {user_choice} а я" ' "' + bot_choice + '"'
            result_embed.colour = 0xE02B2B
        await interaction.response.defer()
        await interaction.edit_original_message(embed=result_embed, content=None, view=None)


class RockPaperScissorsView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(RockPaperScissors())


class Fun(commands.Cog, name="fun-normal"):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(
    #     name="randomfact",
    #     description="Get a random fact."
    # )
    # @checks.not_blacklisted()
    # async def randomfact(self, context: Context):
    #     """
    #     Get a random fact.
    #     :param context: The context in which the command has been executed.
    #     """
    #     # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as request:
    #             if request.status == 200:
    #                 data = await request.json()
    #                 embed = disnake.Embed(
    #                     description=data["text"],
    #                     color=0xD75BF4
    #                 )
    #             else:
    #                 embed = disnake.Embed(
    #                     title="Error!",
    #                     description="Что-та не так с API, пробаните позже",
    #                     color=0xE02B2B
    #                 )
    #             await context.send(embed=embed)

    @commands.command(
        name="монетка",
        description="Бросай манету, но сделай выбор"
    )
    @checks.not_blacklisted()
    async def монетка(self, context: Context) -> None:

        buttons = Choice()
        embed = disnake.Embed(
            description="Твое выборо?",
            color=0x9C84EF
        )
        message = await context.send(embed=embed, view=buttons)
        await buttons.wait()  # Ждем, пока слейвик нажмет на кнопочка
        result = random.choice(["орёль", "решко"])
        if buttons.choice == result:
            # User guessed correctly
            embed = disnake.Embed(
                description=f"Верна ты угадал, эта `{buttons.choice}` я тожа выбирал `{result}`.",
                color=0x9C84EF
            )
        else:
            embed = disnake.Embed(
                description=f"АХАХААХ! ТЫ ПРАЕБАЛ `{buttons.choice}` ДОНТ ПРАВИЛЬНА! `{result}` БЫЛ ВЕРНЫМ ОТВЕТАМ",
                color=0xE02B2B
            )
        await message.edit(embed=embed, view=None)

    @commands.command(
        name="кнб",
        description="Камень-Ножнецы-FatCock"
    )
    @checks.not_blacklisted()
    async def rock_paper_scissors(self, context: Context) -> None:

        view = RockPaperScissorsView()
        await context.send("ОКЕИ БАDDICK, ВЫБИРАЙ СВОЙ ВЫБОР", view=view)
        
    @commands.command(
        name="имя",
        descriotion="Пояснит за тваё имя"
    )
    @checks.not_blacklisted()
    async def names(self, context: Context) -> None:
        
        view = NamesView()
        await context.send("Выбери имя ~~своего краша~~", view=view)
    
def setup(bot):
    bot.add_cog(Fun(bot))
