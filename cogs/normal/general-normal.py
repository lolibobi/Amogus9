import random
import platform

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks



class General(commands.Cog, name="general-normal"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="ботинфо",
        description="Дает немнога (без)полезной инфы о боте",
        aliases=["botinfo","help","хелп","комманды"]
    )
    @checks.not_blacklisted()
    async def ботинфо(self, context: Context) -> None:

        embed = disnake.Embed(
            description="[Алиса](https://heydi-is-sus), здорова",
            color=0x9C84EF
        )
        embed.set_author(
            name="Информацоя обо мене"
        )
        embed.add_field(
            name="Павелител:",
            value="Chisu#4334",
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
        embed.add_field(
            name=f"{self.bot.config['prefix']}ответь",
            value="отвечаю на твои вопрос стопроц точность!",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}серверинфо",
            value="Показывает немного (без)полезной информации о сервере",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}пинг",
            value="Проверка пинга хостинга",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}сервер",
            value="Скидывает ссылку на сервер (Afterlife)",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}биток",
            value="Показывает курс битка",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}амогус",
            value="СУС",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}монетка",
            value="Игра в манетачку палучаеца, проста попробуй",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}кнб",
            value="Камень-Ножнецы-FatCock",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}рандом",
            value="Выдает ~~на лицо~~ рандомное число",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}вы",
            value="писка",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}шип",
            value="Шипперю пацанчей",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}переводчик(тр/т)",
            value=f'Перевод от гугол переводчика: ;т ru/eng (слово)',
            inline=False
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}лемур",
            value=f'показать лемуров',
            inline=True
        )
        embed.set_footer(
            text=f"Вызвал {context.author}"
        )
        await context.send(embed=embed)

    @commands.command(
        name="админ",
        description="Показывает список админ комманд",
    )
    @commands.has_permissions(administrator=True)
    async def админ(self, context: Context) -> None:
        embed = disnake.Embed(
            description="Спиок админ-комманд:",
            color=0x000000
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}кик",
            value="Кикает чела из канала",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}бан",
            value="Банит уебка из сервера",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}ник",
            value="Меняет ник челикса на сервере",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}варн",
            value="Выдает придупреждение пидарасу",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}чистка(сд)",
            value="Удаляет сообщения",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}хакбан",
            value="Банит чела даже если он не на сервере.",
            inline=True
        )
        embed.add_field(
            name="Команды для овнерса",
            value="ниje",
            inline=False
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}офай",
            value="Выключает бота",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}скажи",
            value="бот скажет соже самое",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}встройка",
            value="бот повторит сообщение, но только в embed'e",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}чс",
            value="Показывает ЧС список",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}чс добавить (имя)",
            value="Вносит имя в чс",
            inline=True
        )
        embed.add_field(
            name=f"{self.bot.config['prefix']}чс удалить (имя)",
            value="Удаляет имя в чс",
            inline=True
        )

        embed.set_footer(
            text=f"Вызвал {context.author}"
        )
        await context.send(embed=embed)

    @commands.command(
        name="серверинфо",
        description="Показывает немного (без)полезной информации о сервере",
    )
    @checks.not_blacklisted()
    async def серверинфо(self, context: Context) -> None:

        roles = [role.name for role in context.guild.roles]
        if len(roles) > 50:
            roles = roles[:50]
            roles.append(f">>>> Показать [50/{len(roles)}] Ролей")
        roles = ", ".join(roles)

        embed = disnake.Embed(
            title="**Имя сервера:**",
            description=f"{context.guild}",
            color=0x9C84EF
        )
        embed.set_thumbnail(
            url=context.guild.icon.url
        )
        embed.add_field(
            name="ID Сервера",
            value=context.guild.id
        )
        embed.add_field(
            name="Кол-во геев",
            value=context.guild.member_count
        )
        embed.add_field(
            name="Текстовые/Голосовые Каналы",
            value=f"{len(context.guild.channels)}"
        )
        embed.add_field(
            name=f"Роли ({len(context.guild.roles)})",
            value=roles
        )
        embed.set_footer(
            text=f"Сервар создан: {context.guild.created_at}"
        )
        await context.send(embed=embed)

    @commands.command(
        name="пинг",
        description="Проверка пинга хостинга",
    )
    @checks.not_blacklisted()
    async def пинг(self, context: Context) -> None:

        embed = disnake.Embed(
            title="Хуинг!",
            description=f"Отклик хостинга {round(self.bot.latency * 1000)}ms.",
            color=0x9C84EF
        )
        await context.send(embed=embed)

    @commands.command(
        name="I1VV5D",
        description="Кидает ссылку на приглос бота на свой твой сервер",
    )
    @checks.not_blacklisted()
    async def I1VV5D(self, context: Context) -> None:

        embed = disnake.Embed(
            description=f"Приглоси мене [ссылка](https://discordapp.com/oauth2/authorize?&client_id={self.bot.config['application_id']}&scope=bot+applications.commands&permissions={self.bot.config['permissions']}).",
            color=0xD75BF4
        )
        try:
            await context.author.send(embed=embed)
            await context.send("Код выполнен, сообщение выслано!")
        except disnake.Forbidden:
            await context.send(embed=embed)

    @commands.command(
        name="сервер",
        description="Скидывает ссылку на сервер (Afterlife)",
    )
    @checks.not_blacklisted()
    async def сервер(self, context: Context) -> None:

        embed = disnake.Embed(
            description=f"сам бы блять мог посмотреть, уебище ленивое, вот твоя [ссылка](https://discord.gg/Rm9sqrYDAg) ебучая \n (https://discord.gg/Rm9sqrYDAg)",
            color=0xD75BF4
        )
        try:
            await context.author.send(embed=embed)
            await context.send("Чекой лс")
        except disnake.Forbidden:
            await context.send(embed=embed)

    @commands.command(
        name="ответь",
        description="спроси что-нибудь у мене",
    )
    @checks.not_blacklisted()
    async def ответь(self, context: Context, *, question: str) -> None:

        answersYes = ["Конешна да", "Естествена da", "da", "без сомнений, это так!"]

        answers = ["Конешна да", "Естествена da", "da","Верно", "Так и есть",
                   "Я хз", "Донт знаю", "не ебу", "заебал с вопросоми своими ебучими, позвони бабушке своей, ей будет приятно",
                   "Неа", "Не", "донт.",
                   "пошол нахуи"]
        embed = disnake.Embed(
            title="**Мой ответ:**",
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
            await context.send(embed=susembed)
        # Ответ на обычный вопрос
        else:
            await context.send(embed=embed)

    @commands.command(
        name="биток",
        description="Показывает курс битка",
    )
    @checks.not_blacklisted()
    async def биток(self, context: Context) -> None:

        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json") as request:
                if request.status == 200:
                    data = await request.json(
                        content_type="application/javascript")  # возвращаемое содержимое имеет тип JavaScript
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
                await context.send(embed=embed)
def setup(bot):
    bot.add_cog(General(bot))
