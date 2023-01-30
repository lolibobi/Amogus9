import platform
import random

import aiohttp
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks


class General(commands.Cog, name="general-slash"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="botinfo",
        description="Инфа о боте и ево cumМАНДАх",
    )
    @checks.not_blacklisted()
    async def botinfo(self, interaction: ApplicationCommandInteraction) -> None:

        embed = disnake.Embed(
            description="[Тимур](https://heydi-is-sus), здорова",
            color=0x9C84EF
        )
        embed.set_author(
            name="Информацоя обо мене"
        )
        embed.add_field(
            name="Павелител:",
            value="lolibobi#1235",
            inline=True
        )
        embed.add_field(
            name="Версия Python:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Префеxы:",
            value=f"/ (Слеш команды) или {self.bot.config['prefix']} для обычных команд",
            inline=False
        )
        embed.set_footer(
            text=f"Вызвал {interaction.author}"
        )
        await interaction.send(embed=embed)

    @commands.slash_command(
        name="serverinfo",
        description="Гринч инфа о сервере",
    )
    @checks.not_blacklisted()
    async def serverinfo(self, interaction: ApplicationCommandInteraction) -> None:
        """
        Get some useful (or not) information about the server.
        :param interaction: The application command interaction.
        """
        roles = [role.name for role in interaction.guild.roles]
        if len(roles) > 50:
            roles = roles[:50]
            roles.append(f">>>> Показать [50/{len(roles)}] Ролей")
        roles = ", ".join(roles)

        embed = disnake.Embed(
            title="**Имя сервера:**",
            description=f"{interaction.guild}",
            color=0x9C84EF
        )
        embed.set_thumbnail(
            url=interaction.guild.icon.url
        )
        embed.add_field(
            name="ID Сервера",
            value=interaction.guild.id
        )
        embed.add_field(
            name="Кол-во геев",
            value=interaction.guild.member_count
        )
        embed.add_field(
            name="Текстовые/Голосовые Каналы",
            value=f"{len(interaction.guild.channels)}"
        )
        embed.add_field(
            name=f"Роли ({len(interaction.guild.roles)})",
            value=roles
        )
        embed.set_footer(
            text=f"Сервар создан: {interaction.guild.created_at}"
        )
        await interaction.send(embed=embed)

    @commands.slash_command(
        name="ping",
        description="Проверка наеба хостинга на мои грощи(хотя я наверн фри хост юзаю)",
    )
    @checks.not_blacklisted()
    async def ping(self, interaction: ApplicationCommandInteraction) -> None:
        """
        Check if the bot is alive.
        :param interaction: The application command interaction.
        """
        embed = disnake.Embed(
            title="Хуинг!",
            description=f"Отклик хостинга {round(self.bot.latency * 1000)}ms.",
            color=0x9C84EF
        )
        await interaction.send(embed=embed)

    # @commands.slash_command(
    #     name="invite",
    #     description="Get the invite link of the bot to be able to invite it.",
    # )
    # @checks.not_blacklisted()
    # async def invite(self, interaction: ApplicationCommandInteraction) -> None:
    #     """
    #     Get the invite link of the bot to be able to invite it.
    #     :param interaction: The application command interaction.
    #     """
    #     embed = disnake.Embed(
    #         description=f"Invite me by clicking [here](https://discordapp.com/oauth2/authorize?&client_id={self.bot.config['application_id']}&scope=bot+applications.commands&permissions={self.bot.config['permissions']}).",
    #         color=0xD75BF4
    #     )
    #     try:
    #         # To know what permissions to give to your bot, please see here: https://discordapi.com/permissions.html and remember to not give Administrator permissions.
    #         await interaction.author.send(embed=embed)
    #         await interaction.send("I sent you a private message!")
    #     except disnake.Forbidden:
    #         await interaction.send(embed=embed)

    # @commands.slash_command(
    #     name="server",
    #     description="Get the invite link of the discord server of the bot for some support.",
    # )
    # @checks.not_blacklisted()
    # async def server(self, interaction: ApplicationCommandInteraction) -> None:
    #     """
    #     Get the invite link of the discord server of the bot for some support.
    #     :param interaction: The application command interaction.
    #     """
    #     embed = disnake.Embed(
    #         description=f"Join the support server for the bot by clicking [here](https://discord.gg/mTBrXyWxAF).",
    #         color=0xD75BF4
    #     )
    #     try:
    #         await interaction.author.send(embed=embed)
    #         await interaction.send("I sent you a private message!")
    #     except disnake.Forbidden:
    #         await interaction.send(embed=embed)

    @commands.slash_command(
        name="8ball",
        description="Отвечу на lubeые твое сокровенные вопросы",
        options=[
            Option(
                name="question",
                description="Твой вопрос",
                type=OptionType.string,
                required=True
            )
        ],
    )
    @checks.not_blacklisted()
    async def eight_ball(self, interaction: ApplicationCommandInteraction, question: str) -> None:

        answersYes = ["Конешна да", "Естествена da", "da", "без сомнений, это так!"]

        answers = ["Верно", "Так и есть", "Конешна да", "Естествена da", "da",
                   "Я хз", "Донт знаю", "не ебу", "заебал с вопросоми своими ебучими, позвони бабушке своей, ей будет приятно",
                   "Неа", "Не", "донт.","Это не так!", "донт, конечно",
                   "пошол нахуи"]
        embed = disnake.Embed(
            title="**Ответ:**",
            description=f"{random.choice(answers)}",
            color=0x9C84EF
        )
        embed.set_footer(
            text=f"Вопрос: {question}"
        )
        # Положительный ответ, если вопрос был о sus'ничестве алисы, Алиса, ты мне нравишьс <3
        if any(i in question for i in ["хеуди сус", "хеуди sus",
            "heydi sus", "heydi sys", "heydi sis", "heudi is sus", "is heudi sus",
            "алиса сус", "алиса sus"]):
            susembed = disnake.Embed(
                title="**Ответ:**",
                description=f"{random.choice(answersYes)}",
                color=0x9C84EF
                )
            susembed.set_footer(
                text=f"Вопрос: {question}"
                )
            await interaction.send(embed=susembed)
        # Ответ на обычный вопрос
        else:
            await interaction.send(embed=embed)

    @commands.slash_command(
        name="bitcoin",
        description="Мониторим курс биточка!",
    )
    @checks.not_blacklisted()
    async def bitcoin(self, interaction: ApplicationCommandInteraction) -> None:

        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json") as request:
                if request.status == 200:
                    data = await request.json(
                        content_type="application/javascript")  # For some reason the returned content is of type JavaScript
                    embed = disnake.Embed(
                        title="Bitcoin price",
                        description=f"Фиксируем прибыль, курс биточка {data['bpi']['USD']['rate']} долларс :dollar:",
                        color=0x9C84EF
                    )
                else:
                    embed = disnake.Embed(
                        title="Ошибка!",
                        description="API-шке хуева, перезвоните позже",
                        color=0xE02B2B
                    )
                await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
