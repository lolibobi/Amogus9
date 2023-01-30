import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks

class Moderation(commands.Cog, name="moderation-normal"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="кик",
        description="Кикает чела из канала",
    )
    @commands.has_permissions(kick_members=True)
    @checks.not_blacklisted()
    async def кик(self, context: Context, member: disnake.Member, *, reason: str = "Донт указаностинк") -> None:
        if member.guild_permissions.administrator:
            embed = disnake.Embed(
                title="ОШИБКА!",
                description="У него права админа блять, АААААААААААААААААААААААААААААА",
                color=0xE02B2B
            )
            await context.send(embed=embed)
        else:
            try:
                embed = disnake.Embed(
                    title="Челикс кикнут!",
                    description=f"**{member}** был кикнут им -> **{context.author}**!",
                    color=0x9C84EF
                )
                embed.add_field(
                    name="Причина:",
                    value=reason
                )
                await context.send(embed=embed)
                await member.kick(reason=reason)
                try:
                    await member.send(
                        f"Ты был кикнут по хотению **{context.author}**!\nПричина: {reason}"
                    )
                except disnake.Forbidden:
                    # Не удалось отправить сообщение в личных сообщениях пользователя
                    pass
            except:
                pass

    @commands.command(
        name="ник",
        description="Меняет ник юзера на сервере",
    )
    @commands.has_permissions(manage_nicknames=True)
    @checks.not_blacklisted()
    async def ник(self, context: Context, member: disnake.Member, *, nickname: str = None) -> None:
        """
        Меняет ник пользователя на сервере.
        :param context: Контекст, в котором была выполнена команда.
        :param member: Участник, у которого должен быть изменен ник.
        :param nickname: Новый ник пользователя. Значение по умолчанию равно None, что приведет к сбросу псевдонима.
        """
        try:
            await member.edit(nick=nickname)
            embed = disnake.Embed(
                title="Ник изменеён!",
                description=f"**{member}'ин** новый ник: **{nickname}**!",
                color=0x9C84EF
            )
            await context.send(embed=embed)
        except:
            embed = disnake.Embed(
                title="Ошибка!",
                description="Произошла ошибка при попытке изменить ник пользователя. Убедись, что моя роль находится выше роли челикса, псевдоним которого ты хочешь изменить.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(
        name="бан",
        description="Банит юзера из сервера",
    )
    @commands.has_permissions(ban_members=True)
    @checks.not_blacklisted()
    async def ban(self, context: Context, member: disnake.Member, *, reason: str = "Потому, что ты пидор епта") -> None:
        if member.guild_permissions.administrator:
            embed = disnake.Embed(
                title="ОШИБКА БЛЯТЬ!",
                description="У него права админа блять, АААААААААААААААААААААААААААААА",
                color=0xE02B2B
            )
            await context.send(embed=embed)
        else:
            try:
                embed = disnake.Embed(
                    title="Челикс забананен",
                    description=f"**{member}** был забанен им -> **{context.author}**!",
                    color=0x9C84EF
                )
                embed.add_field(
                    name="Причина:",
                    value=reason
                )
                await context.send(embed=embed)
                await member.ban(reason=reason)
                try:
                    await member.send(f"Ты был ЗАБАНЕН БЛЯТЬ **{context.author}**!\nПричина: {reason}")
                except disnake.Forbidden:
                    # Не удалось отправить сообщение
                    pass
            except:
                pass

    @commands.command(
        name="варн",
        description="Выдает придупреждение юзеру",
    )
    @commands.has_permissions(manage_messages=True)
    @checks.not_blacklisted()
    async def warn(self, context: Context, member: disnake.Member, *, reason: str = "Донт указаностинк бпрляиать") -> None:
        """
        Предупреждает пользователя в его личных сообщениях.
        :param context: Контекст, в котором была выполнена команда.
        :param member: Участник, которого следует предупредить.
        :param reason: Причина предупреждения. Значение по умолчанию - "Донт указаностинк бпрляиать".
        """
        embed = disnake.Embed(
            title="Предупреждение выдано!",
            description=f"**{member}** получил предупреждение от **{context.author}**!",
            color=0x9C84EF
        )
        embed.add_field(
            name="Предупреждение:",
            value=reason
        )
        await context.send(embed=embed)
        try:
            await member.send("Алло уебище")
            await member.send(f"**{context.author} выдал тебе ПРЕДУПРЕЖДЕНИЕ БЛЯТЬ**!\nПричина: {reason}")
        except disnake.Forbidden:
            # Не удалось отправить сообщение в личных сообщениях пользователя
            await context.send(f"{member.mention}, ты получил предупреждение от **{context.author}**!\nПричина: {reason}")

    @commands.command(
        name="чистка",
        description="Удаляет сообщения",
        aliases = ['cl', 'сд']
    )
    @commands.has_guild_permissions(manage_messages=True)
    @checks.not_blacklisted()
    async def чистка(self, context: Context, amount: int) -> None:
        """
        Удаляет несколько сообщений.
        :param context: Контекст, в котором была выполнена команда.
        :param amount: Количество сообщений, которые должны быть удалены.
        """
        try:
            amount = int(amount)
        except:
            embed = disnake.Embed(
                title="Ошибка!",
                description=f"`{amount}` не правильное число.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        if amount < 1:
            embed = disnake.Embed(
                title="Ошибка!",
                description=f"`{amount}`, чо ты высрал",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        elif amount > 100:
            embed = disnake.Embed(
                title = "Ошибка!",
                description = f"`{amount}` слишкам дахуя",
                color = 0xE02B2B
            )
            await context.send(embed=embed)
            return
        await context.channel.purge(limit=amount + 1)
        embed = disnake.Embed(
            title="Чат почищен!",
            description=f"**{context.author}** удаляет **{amount}** сообщений!",
            color=0x9C84EF
        )
        await context.send(embed=embed, delete_after = 8)

    @commands.command(
        name="хакбан",
        description="Банит чела даже если он не на сервере."
    )
    async def хакбан(self, context: Context, user_id: int, *, reason: str) -> None:
        """
        Bans a user without the user having to be in the server.
        :param context: The context in which the command has been executed.
        :param user_id: The ID of the user that should be banned.
        :param reason: The reason for the ban. Default is "Not specified".
        """
        try:
            await self.bot.http.ban(user_id, context.guild.id, reason=reason)
            user = await self.bot.get_or_fetch_user(user_id)
            embed = disnake.Embed(
                title="Челикс забананен!",
                description=f"**{user} (ID: {user_id}) ** был забанен **{context.author}**!",
                color=0x9C84EF
            )
            embed.add_field(
                name="Причина:",
                value=reason
            )
            await context.send(embed=embed)
        except:
            embed = disnake.Embed(
                title="Ошибка!",
                description="При попытке заблокировать чела произошла ошибка. Убедись, что такое ID существует.",
                color=0xE02B2B
            )
            await context.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
