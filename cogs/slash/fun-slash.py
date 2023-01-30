import random

import aiohttp
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands

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


class RockPaperScissors(disnake.ui.Select):
    def __init__(self):

        options = [
            disnake.SelectOption(
                label="Камень", description="На вид - как твердая пластмасса.", emoji="🪨"
            ),
            disnake.SelectOption(
                label="Бумага", description="Довольно влажный выбор.", emoji="🧻"
            ),
            disnake.SelectOption(
                label="Ножницы", description="Опасненька, можно порезать член", emoji="✂"
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
            result_embed.description = "**Ничья!**\nМы оба выбрали "  '"' + user_choice + '"'
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


class Fun(commands.Cog, name="fun-slash"):
    def __init__(self, bot):
        self.bot = bot

    # @commands.slash_command(
    #     name="randomfact",
    #     description="Get a random fact."
    # )
    # @checks.not_blacklisted()
    # async def randomfact(self, interaction: ApplicationCommandInteraction) -> None:
    #     """
    #     Get a random fact.
    #     :param interaction: The application command interaction.
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
    #             await interaction.send(embed=embed)

    @commands.slash_command(
        name="coinflip",
        description="Орёль и Ешка"
    )
    @checks.not_blacklisted()
    async def coinflip(self, interaction: ApplicationCommandInteraction) -> None:

        buttons = Choice()
        embed = disnake.Embed(
            description="Твое выборо?",
            color=0x9C84EF
        )
        await interaction.send(embed=embed, view=buttons)
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
        await interaction.edit_original_message(embed=embed, view=None)

    @commands.slash_command(
        name="rps",
        description="Кам-нож-глеб-кабиков. поспорьте кто посрет первым в этот раз"
    )
    @checks.not_blacklisted()
    async def rock_paper_scissors(self, interaction: ApplicationCommandInteraction) -> None:

        view = RockPaperScissorsView()
        await interaction.send("ОКЕИ БАDDICK, ВЫБИРАЙ СВОЙ ВЫБОР", view=view)


def setup(bot):
    bot.add_cog(Fun(bot))
