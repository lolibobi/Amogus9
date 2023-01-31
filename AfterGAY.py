import json
import os
import platform
import random
import sys

import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context

import exceptions

if not os.path.isfile("config.json"):
    sys.exit("'config.json' НЕ НАЙДЕН! добавь обратно, и попробуй снова братиши епта...")
else:
    with open("config.json") as file:
        config = json.load(file)

"""	
Установлены бот интесты (events restrictions)
инфа об интестах:
https://docs.disnake.dev/en/latest/intents.html
https://docs.disnake.dev/en/latest/intents.html#privileged-intents


Default Intents:
intents.bans = True
intents.dm_messages = True
intents.dm_reactions = True
intents.dm_typing = True
intents.emojis = True
intents.emojis_and_stickers = True
intents.guild_messages = True
intents.guild_reactions = True
intents.guild_scheduled_events = True
intents.guild_typing = True
intents.guilds = True
intents.integrations = True
intents.invites = True
intents.messages = True # `message_content` is required to get the content of the messages
intents.reactions = True
intents.typing = True
intents.voice_states = True
intents.webhooks = True

Privileged Intents
intents.members = True
intents.message_content = True
intents.presences = True
"""

intents = disnake.Intents.default()
intents.members = True

bot = Bot(command_prefix=config["prefix"], intents=intents, help_command=None)

"""
Создал переменную бота для доступа к конфигу в cogs, чтобы не импортировать его каждый раз

конфиг использует следующий код:
- bot.config # В этом файле
- self.bot.config # В когах
"""
bot.config = config


@bot.event
async def on_ready() -> None:
    """
    код, который выполняется при запуске бота
    """
    print(f"Залогинелся как: {bot.user.name}")
    print(f"disnake API Версия: {disnake.__version__}")
    print(f"Версия Python: {platform.python_version()}")
    print(f"Запущен на: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    status_task.start()


@tasks.loop(minutes=1.0)
async def status_task() -> None:
    """
    Установить статус игры
    """
    statuses = ["пездец", "хуню", "Heydi is SUS!", "Трах нест",
    "амосус", "сус", "гей пати", "чин чан чон чи", "смысл бытия",
    "жизнь", "доме", "сарае", "докторку", "блять что еще написать сюда",
    "лан все, я заебался"]
    #await bot.change_presence(activity=disnake.Game(random.choice(statuses)))
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name=random.choice(statuses)))


def load_commands(command_type: str) -> None:
    for file in os.listdir(f"./cogs/{command_type}"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{command_type}.{extension}")
                print(f"Загружен ког '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Ошибка при загрузке кога {extension}\n{exception}")


if __name__ == "__main__":
    """
    Это автоматически загрузит команды косой черты и обычные команды, расположенные в соответствующей папке.

    тут можна офнуть слеш/обычные команды    
    """
    load_commands("slash")
    load_commands("normal")
 
 

@bot.event
async def on_message(message: disnake.Message) -> None:
    """
    без split лфуауафтерслейв - БОТ НЕ ОТВЕЧАЕТ фуау афтерслейв - ОТВЕЧАЕТ
    без lower = Автерслейв - БОТ НЕ ОТВЕЧАЕТ автерслейв - ОТВЕЧАЕТ
    Код в этом событии выполняется каждый раз, когда кто-то отправляет сообщение, с префиксом или без него
    """


    if message.author == bot.user or message.author.bot:
        return
    
    if 'хуйня' in message.content.lower().split():
        await message.channel.send('Согласен.')
    if 'афтерслейв' in message.content.lower().split():
        await message.channel.send('нани?')
    if 'гм' in message.content.lower().split():
        await message.channel.send('https://tenor.com/view/arthas-%D0%BF%D0%B0%D0%BF%D0%B8%D1%87-axe-gif-22493188')
    if 'мяу' in message.content.lower().split():
        await message.channel.send('КТО МЯУКАЕТ???')
    if 'спокойной ночи' in message.content.lower():
        await message.channel.send('Споки! мяу')
    heydi_id = 482568996399349770
    heydi = disnake.utils.find(lambda m: m.id == heydi_id, message.guild.members)
    if {heydi.mention} in message.content.lower().split():
        await message.channel.send('УРА У ТЯ ПОЛУЧИЛАСЬ СУСИК')

    await bot.process_commands(message)

#@bot.event
#async def on_message(message: disnake.Message) -> None:
    
    
    
@bot.event
async def on_member_join(member):

    # chanSend = 774511321777438740
    # roleJoin = 479532966486212610

    channel = bot.get_channel(723509261522436208)

    role = disnake.utils.get(member.guild.roles, id = 723515028262879292)
    await member.add_roles(role)
    embed = disnake.Embed(
        title = 'Присоединился',
        description = f'Кокоита {member.mention} прилетел в эту качалку',
        color = 0x6600FF
    )
    embed.set_author(
        name=member.name,
        icon_url= member.avatar.url
    )

    await channel.send(embed = embed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(723509261522436208)
    
    embed = disnake.Embed(
        title = 'Вышел',
        description = f'{member.mention} наконец-то понял, что он попал не в комнату кожанного ремесла',
        color = 0x6600FF
    )
    embed.set_author(
        name=member.name,
        icon_url= member.avatar.url
    )

    await channel.send(embed = embed)


@bot.event
async def on_slash_command(interaction: ApplicationCommandInteraction) -> None:
    """
    Код в этом событии выполняется каждый раз, когда команда косой черты была *успешно* выполнена
    :параметр взаимодействия: Команда косой черты, которая была выполнена.
    """
    print(
        f"Выполнена {interaction.data.name} команда в {interaction.guild.name} (ID: {interaction.guild.id}) by {interaction.author} (ID: {interaction.author.id})")


@bot.event
async def on_slash_command_error(interaction: ApplicationCommandInteraction, error: Exception) -> None:
    """
    Код в этом событии выполняется каждый раз, когда допустимая команда косой черты выдает ошибку
    :param interaction: The slash command that failed executing.
    :param error: The error that has been faced.
    """
    if isinstance(error, exceptions.UserBlacklisted):
        """
        Приведенный здесь код будет выполняться только в том случае, если ошибка является экземпляром 'UserBlacklisted', что может возникнуть при использовании
        проверка @checks.is_owner() в этой команде, или я могу вызвать ошибку самостоятельно.
        
        'hidden=True' сделает так, чтобы только пользователь, выполняющий команду, мог видеть сообщение
        """
        embed = disnake.Embed(
            title="Ошибка!",
            description="Ты в моем black списке ",
            color=0xE02B2B
        )
        print("Чел из ЧС пытается попытался написать команду")
        return await interaction.send(embed=embed, ephemeral=True)
    elif isinstance(error, commands.errors.MissingPermissions):
        embed = disnake.Embed(
            title="ОПААА!",
            description="Нихуя себя дядя, ненада дядя, дядя, не нада! у тя нет прав> `" + ", ".join(
                error.missing_permissions) + "` для осуществления твоих корыстных желаний!",
            color=0xE02B2B
        )
        print("Пользователь, внесенный в черный список, попытался выполнить команду.")
        return await interaction.send(embed=embed, ephemeral=True)
    raise error


@bot.event
async def on_command_completion(context: Context) -> None:
    """
    Код в этом событии выполняется каждый раз, когда обычная команда была *успешно* выполнена
    :контекст параметра: Контекст команды, которая была выполнена.
    """
    full_command_name = context.command.qualified_name
    split = full_command_name.split(" ")
    executed_command = str(split[0])
    print(
        f"Выполнена {executed_command} команда в {context.guild.name} (ID: {context.message.guild.id}) by {context.message.author} (ID: {context.message.author.id})")


@bot.event
async def on_command_error(context: Context, error) -> None:
    """
    Код в этом событии выполняется каждый раз, когда обычная допустимая команда обнаруживает ошибку
    :параметр context: Обычная команда, выполнение которой завершилось неудачей.
    :параметр error: Ошибка, с которой пришлось столкнуться.
    """
    if isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24
        embed = disnake.Embed(
            title="Эбля, притормози челикс!",
            description=f"Ты можешь использовать эту команду через {f'{round(hours)} часов' if round(hours) > 0 else ''} {f'{round(minutes)} минут' if round(minutes) > 0 else ''} {f'{round(seconds)} секунд' if round(seconds) > 0 else ''}.",
            color=0xE02B2B
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = disnake.Embed(
            title="Ошибка!",
            description="тЕ прав донт хватастинк `" + ", ".join(
                error.missing_permissions) + "` для выполнения этой команды ",
            color=0xE02B2B
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = disnake.Embed(
            title="Ошибка!",
            # Нам нужно использовать заглавную букву, потому что аргументы команды в коде не имеют заглавной буквы.
            #description=str(error).capitalize(),
            description="Норма ты така придумал, сталкир, а где аргументы блять",
            color=0xE02B2B
        )
        await context.send(embed=embed)
    raise error


bot.run(config["token"])
