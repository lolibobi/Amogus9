import json

import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import json_manager, checks


class Owner(commands.Cog, name="owner-normal"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="офай",
        description="Выключает бота",
    )
    @checks.is_owner()
    async def офай(self, context: Context):

        embed = disnake.Embed(
            description="Зачо мене.. Пока! :wave:",
            color=0x9C84EF
        )
        await context.send(embed=embed)
        await self.bot.close()

    @commands.command(
        name="скажи",
        description="бот скажет соже самое",
    )
    @checks.is_owner()
    async def скажи(self, context: Context, *, message: str):

        await context.send(message)

    @commands.command(
        name="встройка",
        description="бот повторит сообщение, но только в embed'e",
    )
    @checks.is_owner()
    async def встройка(self, context: Context, *, message: str):

        embed = disnake.Embed(
            description=message,
            color=0x9C84EF
        )
        await context.send(embed=embed)

    @commands.group(
        name="чс"
    )
    async def чс(self, context: Context):

        if context.invoked_subcommand is None:
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            embed = disnake.Embed(
                title=f"В настоящее время {len(blacklist['ids'])} занесены в черный список",
                description=f"{', '.join(str(id) for id in blacklist['ids'])}",
                color=0x9C84EF
            )
            await context.send(embed=embed)

    @чс.command(
        name="добавить"
    )
    async def чс_добавить(self, context: Context, member: disnake.Member = None):

        try:
            user_id = member.id
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            if user_id in blacklist['ids']:
                embed = disnake.Embed(
                    title="Ашибачка!",
                    description=f"**{member.name}** уже находится в черном списке",
                    color=0xE02B2B
                )
                return await context.send(embed=embed)
            json_manager.add_user_to_blacklist(user_id)
            embed = disnake.Embed(
                title="Чел ты... заблокирован",
                description=f"**{member.name}** был успешно дабвален в мой черный список",
                color=0x9C84EF
            )
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            embed.set_footer(
                text=f"Теперь {len(blacklist['ids'])} человек в черном списке"
            )
            await context.send(embed=embed)
        except:
            embed = disnake.Embed(
                title="Ошибка!",
                description=f"Произошла неизвестная ошибка при добавлении **{member.name}** в ЧС",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @чс.command(
        name="удалить"
    )
    async def чс_удалить(self, context, member: disnake.Member = None):

        try:
            user_id = member.id
            json_manager.remove_user_from_blacklist(user_id)
            embed = disnake.Embed(
                title="Пацанчи удален из ЧС",
                description=f"**{member.name}** был успешно удален из моего черного списка!",
                color=0x9C84EF
            )
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            embed.set_footer(
                text=f"Теперь {len(blacklist['ids'])} человек в черном списке"
            )
            await context.send(embed=embed)
        except:
            embed = disnake.Embed(
                title="Ошибко!",
                description=f"**{member.name}** нет в ЧС!",
                color=0xE02B2B
            )
            await context.send(embed=embed)


def setup(bot):
    bot.add_cog(Owner(bot))
