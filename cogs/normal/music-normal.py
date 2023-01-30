# from ast import alias
# import disnake
# from disnake.ext import commands
# from disnake.ext.commands import Context

# from youtube_dl import YoutubeDL

# class Music(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
    
#         #all the music related stuff
#         self.is_playing = False
#         self.is_paused = False

#         # 2d array containing [song, channel]
#         self.music_queue = []
#         self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
#         self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

#         self.vc = None

#      #searching the item on youtube
#     def search_yt(self, item):
#         with YoutubeDL(self.YDL_OPTIONS) as ydl:
#             try: 
#                 info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
#             except Exception: 
#                 return False

#         return {'source': info['formats'][0]['url'], 'title': info['title']}

#     def play_next(self):
#         if len(self.music_queue) > 0:
#             self.is_playing = True

#             #get the first url
#             m_url = self.music_queue[0][0]['source']

#             #remove the first element as you are currently playing it
#             self.music_queue.pop(0)

#             self.vc.play(disnake.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
#         else:
#             self.is_playing = False

#     # infinite loop checking 
#     async def play_music(self, context: Context):
#         if len(self.music_queue) > 0:
#             self.is_playing = True

#             m_url = self.music_queue[0][0]['source']
            
#             #try to connect to voice channel if you are not already connected
#             if self.vc == None or not self.vc.is_connected():
#                 self.vc = await self.music_queue[0][1].connect()

#                 #in case we fail to connect
#                 if self.vc == None:
#                     await context.send("Could not connect to the voice channel")
#                     return
#             else:
#                 await self.vc.move_to(self.music_queue[0][1])
            
#             #remove the first element as you are currently playing it
#             self.music_queue.pop(0)

#             self.vc.play(disnake.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
#         else:
#             self.is_playing = False

#     @commands.command(name="play", aliases=["p","playing"], help="Plays a selected song from youtube")
#     async def play(self, context: Context, *args):
#         query = " ".join(args)
        
#         voice_channel = context.author.voice.channel
#         if voice_channel is None:
#             #you need to be connected so that the bot knows where to go
#             await context.send("Зайди в войс цуукц!")
#         elif self.is_paused:
#             self.vc.resume()
#         else:
#             song = self.search_yt(query)
#             if type(song) == type(True):
#                 await context.send("Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
#             else:
#                 await context.send("Музыка добавлена в очередь")
#                 self.music_queue.append([song, voice_channel])
                
#                 if self.is_playing == False:
#                     await self.play_music(context)

#     @commands.command(name="pause", help="Pauses the current song being played")
#     async def pause(self, context: Context, *args):
#         if self.is_playing:
#             self.is_playing = False
#             self.is_paused = True
#             self.vc.pause()
#         elif self.is_paused:
#             self.vc.resume()

#     @commands.command(name = "resume", aliases=["r"], help="Resumes playing with the discord bot")
#     async def resume(self, context: Context, *args):
#         if self.is_paused:
#             self.vc.resume()

#     @commands.command(name="skip", aliases=["s"], help="Skips the current song being played")
#     async def skip(self, context: Context):
#         if self.vc != None and self.vc:
#             self.vc.stop()
#             #try to play next in the queue if it exists
#             await self.play_music(context)


#     @commands.command(name="queue", aliases=["q"], help="Displays the current songs in queue")
#     async def queue(self, context: Context):
#         retval = ""
#         for i in range(0, len(self.music_queue)):
#             # display a max of 5 songs in the current queue
#             if (i > 4): break
#             retval += self.music_queue[i][0]['title'] + "\n"

#         if retval != "":
#             await context.send(retval)
#         else:
#             await context.send("Донт музыки в очерединк")

#     @commands.command(name="clear", aliases=["c", "bin"], help="Stops the music and clears the queue")
#     async def clear(self, context: Context):
#         if self.vc != None and self.is_playing:
#             self.vc.stop()
#         self.music_queue = []
#         await context.send("музыка в очереди очищена")

#     @commands.command(name="leave", aliases=["disconnect", "l", "d"], help="Kick the bot from VC")
#     async def dc(self, context: Context):
#         self.is_playing = False
#         self.is_paused = False
#         await self.vc.disconnect()

# def setup(bot):
#     bot.add_cog(Music(bot))






































import disnake
from disnake.ext import commands
from disnake.ext.commands import Context


from youtube_dl import YoutubeDL


class Music(commands.Cog, name="music-normal"):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def вход(self, context: Context):
        if context.author.voice is None:
            await context.send('a тя донт там!')
        voice_channel = context.author.voice.channel
        if context.voice_client is None:
            await voice_channel.connect()
        else:
            await context.voice_client.move_to(voice_channel)

    @commands.command()
    async def лив(self, context: Context):
        voice_channel = context.author.voice.channel
        await context.voice_client.disconnect()


    @commands.command()
    async def play(self, context: Context, *, arg):
        YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        vc = context.voice_client


        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in arg:
                info = ydl.extract_info(arg, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]


        url = info['formats'][0]['url']
        source = await disnake.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)

        vc.play(source)


def setup(bot):
    bot.add_cog(Music(bot))