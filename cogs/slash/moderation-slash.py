import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks


class Moderation(commands.Cog, name="moderation-slash"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="kick",
        description="Исключить юзера из сервера.",
        options=[
            Option(
                name="user",
                description="Пользователь, которого нужно кикнуть.",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="Причина исключения",
                type=OptionType.string,
                required=False
            )
        ]
    )
    @commands.has_permissions(kick_members=True)
    @checks.not_blacklisted()
    async def kick(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                   reason: str = "Донт указаностинк") -> None:
        """
        Kick a user out of the server.
        :param interaction: The application command interaction.
        :param user: The user that should be kicked from the server.
        :param reason: The reason for the kick. Default is "Not specified".
        """
        member = await interaction.guild.get_or_fetch_member(user.id)
        if member.guild_permissions.administrator:
            embed = disnake.Embed(
                title="ОШИБКА!",
                description="У него права админа блять, АААААААААААААААААААААААААААААА",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
        else:
            try:
                embed = disnake.Embed(
                    title="Челикс кикнут",
                    description=f"**{member}** был кикнут им -> **{interaction.author}**!",
                    color=0x9C84EF
                )
                embed.add_field(
                    name="Причина:",
                    value=reason
                )
                await interaction.send(embed=embed)
                await member.kick(reason=reason)
                try:
                    await member.send(
                        f"Ты был кикнут по хотению **{interaction.author}**!\nПричина: {reason}"
                    )
                except disnake.Forbidden:
                    # Не удалось отправить сообщение в личных сообщениях пользователя
                    pass
            except:
                pass

    @commands.slash_command(
        name="nick",
        description="Ну давай, поменяй ник кому-нибудь, блять, ты хочешь.",
        options=[
            Option(
                name="user",
                description="Имя того, кому не повезло в жизни.",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="nickname",
                description="Новый новое имя бедолаги.",
                type=OptionType.string,
                required=False
            )
        ],
    )
    @commands.has_permissions(manage_nicknames=True)
    @checks.not_blacklisted()
    async def nick(self, interaction: ApplicationCommandInteraction, user: disnake.User, nickname: str = None) -> None:
        """
        Change the nickname of a user on a server.
        :param interaction: The application command interaction.
        :param user: The user that should have its nickname changed.
        :param nickname: The new nickname of the user. Default is None, which will reset the nickname.
        """
        member = await interaction.guild.get_or_fetch_member(user.id)
        try:
            await member.edit(nick=nickname)
            embed = disnake.Embed(
                title="Ник изменеён!",
                description=f"**{member}'ин** новый ник: **{nickname}**!",
                color=0x9C84EF
            )
            await interaction.send(embed=embed)
        except:
            embed = disnake.Embed(
                title="Ошибка!",
                description="Произошла ошибка при попытке изменить ник пользователя. Убедись, что моя роль находится выше роли челикса, псевдоним которого ты хочешь изменить.",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)

    @commands.slash_command(
        name="ban",
        description="Бан челикса из сервера нахуи.",
        options=[
            Option(
                name="user",
                description="Имя отщепенца.",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="Причина банана.",
                type=OptionType.string,
                required=False
            )
        ],
    )
    @commands.has_permissions(ban_members=True)
    @checks.not_blacklisted()
    async def ban(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                  reason: str = "Потому, что ты пидор епта") -> None:
        """
        Bans a user from the server.
        :param interaction: The application command interaction.
        :param user: The user that should be banned from the server.
        :param reason: The reason for the ban. Default is "Not specified".
        """
        # await interaction.send(embed=embed)
        member = await interaction.guild.get_or_fetch_member(user.id)

        if member.guild_permissions.administrator:
            embed = disnake.Embed(
                title="ОШИБКА БЛЯТЬ!",
                description="У него права админа блять, АААААААААААААААААААААААААААААА",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
        else:
            try:
                embed = disnake.Embed(
                    title="Челикс забананен",
                    description=f"**{member}** был забанен им -> **{interaction.author}**!",
                    color=0x9C84EF
                )
                embed.add_field(
                    name="Причина:",
                    value=reason
                )
                await interaction.send(embed=embed)
                await member.ban(reason=reason)
                try:
                    await member.send(f"Ты был ЗАБАНЕН БЛЯТЬ **{interaction.author}**!\nПричина: {reason}")
                except disnake.Forbidden:
                    # Не удалось отправить сообщение
                    pass
            except:
                pass

    @commands.slash_command(
        name="warn",
        description="Высылает предупреждение пидарасу.",
        options=[
            Option(
                name="user",
                description="Челикс, который нарушил закон моего dungeon.",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="и какой же закон он нарешил.",
                type=OptionType.string,
                required=False
            )
        ],
    )
    @commands.has_permissions(manage_messages=True)
    @checks.not_blacklisted()
    async def warn(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                   reason: str = "Донт указаностинк бпрляиать") -> None:
        """
        Warns a user in his private messages.
        :param interaction: The application command interaction.
        :param user: The user that should be warned.
        :param reason: The reason for the warn. Default is "Not specified".
        """
        member = await interaction.guild.get_or_fetch_member(user.id)
        embed = disnake.Embed(
            title="Предупреждение выдано!",
            description=f"**{member}** получил предупреждение от **{interaction.author}**!",
            color=0x9C84EF
        )
        embed.add_field(
            name="Предупреждение:",
            value=reason
        )
        await interaction.send(embed=embed)
        try:
            await member.send("Алло уебище")
            await member.send(f"**{interaction.author} выдал тебе ПРЕДУПРЕЖДЕНИЕ БЛЯТЬ**!\nПричина: {reason}")
        except disnake.Forbidden:
            # Не удалось отправить сообщение в личных сообщениях пользователя
            await context.send(f"{member.mention}, ты получил предупреждение от **{interaction.author}**!\nПричина: {reason}")

    @commands.slash_command(
        name="clean",
        description="Чистит гавно.",
        options=[
            Option(
                name="amount",
                description="Колличество удаляемых сообщений (1-100)",
                type=OptionType.integer,
                required=True,
                min_value=1,
                max_value=100
            )
        ],
    )
    @commands.has_guild_permissions(manage_messages=True)
    @checks.not_blacklisted()
    async def clean(self, interaction: ApplicationCommandInteraction, amount: int) -> None:
        """
        Delete a number of messages.

        :param interaction: The application command interaction.
        :param amount: The number of messages that should be deleted.
        """
        await interaction.channel.purge(limit=amount)
        embed = disnake.Embed(
            title="Чат почищен!",
            description=f"**{interaction.author}** удаляет **{amount}** сообщений!",
            color=0x9C84EF
        )
        await interaction.send(embed=embed, delete_after = 8)

    @commands.slash_command(
        name="hackban",
        description="Банит чела даже если он не на сервере.",
        options=[
            Option(
                name="user_id",
                description="ID челикса, которому над выдать бананку.",
                type=OptionType.string,
                required=True
            ),
            Option(
                name="reason",
                description="Прична траха.",
                type=OptionType.string,
                required=False
            )
        ]
    )
    @commands.has_permissions(ban_members=True)
    @checks.not_blacklisted()
    async def hackban(self, interaction: ApplicationCommandInteraction, user_id: str,
                      reason: str = "Пидарас") -> None:
        """
        Bans a user without the user having to be in the server.
        :param interaction: The application command interaction.
        :param user_id: The ID of the user that should be banned.
        :param reason: The reason for the ban. Default is "Not specified".
        """
        try:
            await self.bot.http.ban(user_id, interaction.guild.id, reason=reason)
            user = await self.bot.get_or_fetch_user(int(user_id))
            embed = disnake.Embed(
                title="Челикс забананен!",
                description=f"**{user} (ID: {user_id}) ** был забанен **{interaction.author}**!",
                color=0x9C84EF
            )
            embed.add_field(
                name="Причина:",
                value=reason
            )
            await interaction.send(embed=embed)
        except Exception as e:
            embed = disnake.Embed(
                title="Ошибка!",
                description="При попытке заблокировать чела произошла ошибка. Убедись, что такое ID существует.",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
            print(e)


def setup(bot):
    bot.add_cog(Moderation(bot))
