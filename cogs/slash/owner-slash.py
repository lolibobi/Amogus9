import json

import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import json_manager, checks


class Owner(commands.Cog, name="owner-slash"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="shutdown",
        description="(ownerCommand) выключает нахуи бота",
    )
    @checks.is_owner()
    async def shutdown(self, interaction: ApplicationCommandInteraction) -> None:

        embed = disnake.Embed(
            description="Зачо мене.. Пока! :wave:",
            color=0x9C84EF
        )
        await interaction.send(embed=embed)
        await self.bot.close()

    @commands.slash_command(
        name="say",
        description="(ownerCommand) повторяет то, чо я скажу",
        options=[
            Option(
                name="message",
                description="Сообщение, которое нужно повторить",
                type=OptionType.string,
                required=True
            )
        ],
    )
    @checks.is_owner()
    async def say(self, interaction: ApplicationCommandInteraction, message: str) -> None:

        await interaction.send(message)

    @commands.slash_command(
        name="embed",
        description="(ownerCommand) проверка встроек (почти то же, что и say)",
        options=[
            Option(
                name="message",
                description="Сообщение, которое нужно повторить",
                type=OptionType.string,
                required=True
            )
        ],
    )
    @checks.is_owner()
    async def embed(self, interaction: ApplicationCommandInteraction, message: str) -> None:

        embed = disnake.Embed(
            description=message,
            color=0x9C84EF
        )
        await interaction.send(embed=embed)

    @commands.slash_command(
        name="blacklist",
        description="(ownerCommand) показывает список пидорасов в ЧС",
    )
    @checks.is_owner()
    async def blacklist(self, interaction: ApplicationCommandInteraction) -> None:
        pass

    @blacklist.sub_command(
        base="blacklist",
        name="check",
        description="(ownerCommand) Черный список"
    )
    @checks.is_owner()
    async def blacklist_check(self, interaction: ApplicationCommandInteraction):
        try:
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            embed = disnake.Embed(
                title=f"В настоящее время {len(blacklist['ids'])} занесены в черный список",
                description=f"{', '.join(str(id) for id in blacklist['ids'])}",
                color=0x9C84EF
            )
            await interaction.send(embed=embed)
        except:
            pass

    @blacklist.sub_command(
        base="blacklist",
        name="add",
        description="(ownerCommand) Позволяет добавить пользователя, который не может использовать бота.",
        options=[
            Option(
                name="user",
                description="Имя пидараса",
                type=OptionType.user,
                required=True
            )
        ],
    )
    @checks.is_owner()
    async def blacklist_add(self, interaction: ApplicationCommandInteraction, user: disnake.User = None) -> None:

        try:
            user_id = user.id
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            if user_id in blacklist['ids']:
                embed = disnake.Embed(
                    title="Ашибачка!",
                    description=f"**{user.name}** уже находится в черном списке",
                    color=0xE02B2B
                )
                return await interaction.send(embed=embed)
            json_manager.add_user_to_blacklist(user_id)
            embed = disnake.Embed(
                title="Чел ты... заблокирован",
                description=f"**{user.name}** был успешно дабвален в мой черный список",
                color=0x9C84EF
            )
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            embed.set_footer(
                text=f"Теперь {len(blacklist['ids'])} человек в черном списке"
            )
            await interaction.send(embed=embed)
        except Exception as exception:
            embed = disnake.Embed(
                title="Ошибка!",
                description=f"Произошла неизвестная ошибка при добавлении **{user.name}** в ЧС.",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
            print(exception)

    @blacklist.sub_command(
        base="blacklist",
        name="remove",
        description="(ownerCommand) похоже, что ктото решил через постель выти из ЧС, ну ок, поехоли",
        options=[
            Option(
                name="user",
                description="Имя искупившего вину перед моим членом",
                type=OptionType.user,
                required=True
            )
        ],
    )
    @checks.is_owner()
    async def blacklist_remove(self, interaction: ApplicationCommandInteraction, user: disnake.User = None):

        try:
            json_manager.remove_user_from_blacklist(user.id)
            embed = disnake.Embed(
                title="Пацанчи удален из ЧС",
                description=f"**{user.name}** был успешно удален из моего черного списка!",
                color=0x9C84EF
            )
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            embed.set_footer(
                text=f"Теперь {len(blacklist['ids'])} человек в черном списке"
            )
            await interaction.send(embed=embed)
        except ValueError:
            embed = disnake.Embed(
                title="Ошибко!",
                description=f"**{user.name}** нет в ЧС!",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
        except Exception as exception:
            embed = disnake.Embed(
                title="Ошибка?",
                description=f"Ебать, я вот щас код пишу да, на вряд-ли эта ошибка когда нибудь появится, просто знайте, чо я хочу пельмень. запись 10.05.2022",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
            print(exception)


def setup(bot):
    bot.add_cog(Owner(bot))
