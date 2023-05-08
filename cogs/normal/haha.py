import discord
from discord.ext import commands
import youtube_dl
import asyncio

class Haha(commands.Cog, name="haha"):
    def __init__(self, bot):
        self.bot = bot

# Обработчик команды "!play"
    @bot.command()
    async def play(ctx, url):
        # Проверяем, находится ли автор команды в голосовом канале
        if ctx.author.voice is None:
            await ctx.send("Вы должны находиться в голосовом канале, чтобы использовать эту команду.")
            return

        # Подключаемся к голосовому каналу автора команды
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()

        # Скачиваем аудио из YouTube и воспроизводим
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            voice_client.play(discord.FFmpegPCMAudio(url2))

        # Ожидаем окончания воспроизведения и отключаемся от голосового канала
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()

