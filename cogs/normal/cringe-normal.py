import random
from time import sleep

from googletrans import Translator  # 3.1.0a0
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks


class Cringe(commands.Cog, name="cringe-normal"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="амогус",
        description="сус",
        aliases=["amogus", "сус"]
    )
    @checks.not_blacklisted()
    async def амогус(self, context: Context) -> None:
        timur_id = 444421622938730506
        timur = disnake.utils.find(
            lambda m: m.id == timur_id, context.guild.members)
        kok_id = 369495810146172938
        kok = disnake.utils.find(
            lambda m: m.id == kok_id, context.guild.members)
        sus = random.randint(0, 2)
        if sus == 0:
            try:
                embed = disnake.Embed(
                    title="SUS",
                    description=f"{timur.mention} ГЛАВНЫ СУС ЭТАВА ДАНГЕОНА",
                    color=0x9C84EF
                )
                await context.send(embed=embed)
            except:
                await context.send('heydi IS SUUUUUUUUUUUUUUUUUUUUUUUUUUUUS!')
        elif sus == 1:
            user = random.choice(context.guild.members)
            embed = disnake.Embed(
                title="SUS",
                description=f"{user.mention} is sus",
                color=0x9C84EF
            )
            await context.send(embed=embed)
        elif sus == 2:
            user = random.choice(context.guild.members)
            embed = disnake.Embed(
                title="SUS",
                description=f"{kok.mention} ЫАВАЫВААЫВАЫВЫВАЫАЫВ",
                color=0x9C84EF
            )
            await context.send(embed=embed)


    @commands.command(
        name="рандом",
        description="Выводит рандомное число",
        aliases = ["ранд", "random", "rand"]
    )
    @checks.not_blacklisted()
    async def рандом(self, context: Context) -> None:
        
        x = random.randint(0, 100)

        if x == 0:
            await context.send(x)
            sleep(1)
            await context.send("https://www.youtube.com/watch?v=7zg1qhRvX48")

        elif x < 10:
            embed = disnake.Embed(
                title="Рандом",
                description=f'{x}... мдауш, не в этот раз',
                color=0xE02B2B
            )
            await context.send(embed=embed)

        elif x == 69:
            await context.send(x)
            await context.send("""69 (также иногда используются термины Поза Вале́та, Францу́зская любо́вь, Перекрёстная любовь, фр. L'amour croisee[1]) — одна из наиболее известных поз для орального секса, дающая партнёрам возможность проводить взаимную оральную стимуляцию. Партнёры при этом располагаются относительно друг друга в перевёрнутом положении, как цифры в числе «69», отсюда и название.

            Несмотря на достаточную известность, поза для многих не очень удобна для достижения оргазма: взаимные ласки отвлекают партнёров, не давая сосредоточиться ни на доставлении удовольствия, ни на его получении. По этой причине данная поза чаще бывает частью прелюдии[2].

            История:
            Термин шестьдесят девять или soixante-neuf для взаимной одновременной орально-генитальной стимуляции является английским переводом эвфемистического французского термина «soixante-neuf». Термин «soixante-neuf» не прослеживался ранее, чем в «Катехизисах шлюхи», опубликованных в 1790-х годах во Франции, обычно приписываемых раннему лидеру Французской революции мадемуазель Теруань де Мерикур[3].

            аой... всысле я хотел сказать""")
            await context.send("https://i.pos;ftimg.cc/mr2GYdZJ/image.png")
        elif x > 88 and x < 100:
            embed = disnake.Embed(
                title="Рандом",
                description=f'{x}, паходу пабеда!',
                color=0x9C84EF
            )
            await context.send(embed=embed)
        elif x == 100:
            message = await context.send(f'{x}, ТЫ АХУЕЛ?/')
            sleep (2)
            message2 = await context.send('за такое наказывают.')
            message3 = await context.send(f"{self.bot.config['prefix']}мут {context.author.mention}")
            sleep (1)
            message4 = await context.send('ладно небуду сладенький, успакойся)))')


            sleep (1.5)
            await message4.delete()
            sleep (0.1)
            await message3.delete()
            sleep (0.1)
            await message2.delete()
            
            message1 = await message.edit(content = x)
        else:
            embed = disnake.Embed(
                title="Рандом",
                description=f"Твое число {x}!",
                color=0x00FF7F
            )
            await context.send(embed=embed)

    @commands.command(
        name="переводчик",
        description="googletrans переводит сообщение на другой язык",
        aliases=["translate","tr","тр","ек","t","е","т"]
    )
    @checks.not_blacklisted()
    async def переводчик(self, context: Context, lang, *, thing) -> None:
        translator = Translator()
        translation = translator.translate(thing, dest=lang)
        embed = disnake.Embed(
            title="Переводчик",
            description=f"{translation.text}",
            color=0x9C84EF

        )
        await context.send(embed=embed)
        # await context.send(translation.text)

    @commands.command(
        name="вы",
        description="говорит кто писка",
    )
    @checks.not_blacklisted()
    async def вы(self, context: Context) -> None:
        user = random.choice(context.guild.members)
        embed = disnake.Embed(
            title="пиписочка",
            description=f"{user.mention} вы писка",
            color=0x9C84EF
        )
        await context.send(embed=embed)

    @commands.command(
        name="шип",
        description="шипперство 2 челаксов",
    )
    @checks.not_blacklisted()
    async def шип(self, context: Context) -> None:
        lolibobi_id = 1040144202387959809
        lolibobi = disnake.utils.find(
        lambda m: m.id == lolibobi_id, context.guild.members)
        heydi_id = 482568996399349770
        heydi = disnake.utils.find(
        lambda m: m.id == heydi_id, context.guild.members)
        user1 = 0
        user2 = 0
        while user1 == user2:
            user1 = random.choice(context.guild.members)
            user2 = random.choice(context.guild.members)
        if user1 == heydi and user2 == lolibobi or user1 == lolibobi and user2 == heydi:
            embed = disnake.Embed(
                title="????????????????????????????????????????????????",
                description=f"{user1.mention} и {user2.mention}.. ого, это действительно случилось.. тут должна быть пасхалка, но похоже, что она находится чуть глубже, но ТУТ её нетус... Поэтому держи жабу!",
                color=0x9C84EF
            ) # что я несу.... не начинай новые отношения, ты знаешь, чем это опять закончится.   # ебучие подростковые гармоны заставляют меня принимать не свои решения
            await context.send(embed=embed) # не навижу, когда кто-то делает выбор за меня, особенно, если это я.
            # хотя, впринцепе, до этих строчек кода на вряд-ли кто-то доберётся, поэтому поговорю с самим собой..
            # а может быть, кто-то и дошел до сюдова, поэтому вот тебе посхалка, которая должна была быть в description выше
            # примечание: 2018 года мне было около 16 лет
            # в 2018 году я познакомился с отличной девушкой, и сдесь всё и началось. мы понравились друг другу,
            # после чего следующие пару месяцев мы общались очень близко, (не в физическом плане), я имею в виду,
            # когда я с ней общался - я так хорошо её понимал, по ощущениям, это как разговаривать с кем-то внутри тебя.
            # вы так же хорошо понимаете друг друга не то, что с полу-слова, а даже с первой буквы.
            # Всё было хорошо..
            # но, в один день у неё сбежала её кошка, и пока она её искала - её сбила машина.
            # каждый жень проводя у её койки - мне становилось всё хуже и хуже.
            # спустя 3 недели комы она проснулась, и казалось-бы финал!
            # но спуся ещё 2 недели она умерла от разрыва сосудов на сердце.
            # Моё состояние в её день смерти? во мне не умолкали голоса, которые напоминали мне о ней каждую секунду..
            # было ощущение, как буд-то я ничего не слышу из-за этих голосов, и за мной идёт толпа убийц в громешной темноте,
            # при том голоса на столько громни, что кроме них что-то ещё услышать - не возможно
            # на следующий день, лезвие прошло по моей руке, но так, как в 16 лет я не особо понимал как работают вены - я остался живым.
            # в её дневнике была строчка, в коророй она просила меня не совершать самоубийство.
            # следующий год, а то-есть 16-17 летие прошло внутри моего сознания, весь год я разговаривал только со своим "я",
            # и не подпускал к себе ни единой души, именно в это время у меня начались первые проявления шизофрении
            # промежуток в 17-18 лет прошел в "допонимании" себя. 16-18 годы были самыми тяжелыми, ведь всё это время - те самые голоса
            # не умолкали не на секунду, я не знал, что будет со мной, не находясь в настоящем времяни совсем.
            # промежуток 18-19 лет. голоса стали тише, и наконец, я могу жить спокойнее.
            # 19 летие. тот момент, в котором я нахожусь сейчас. я боюсь начинать отношения, ведь они пораждают боль.
            # невыносимую боль.
            # мои гармоны хотят, что-бы я нашел кого-то ещё, а я хочу остаться один. совсем. Но понимаю, что это не лучший выбор,если только
            # в конце концов не порезать руку снова, но уже правильно.
            #  Эту историю я рассказывал только 1 человеку - тому, с кем я общался всё 16 летие. Думаю, ты догадаешься, кто ОН. (хоть даже я не совсем знаю его)
            #   Спосибо за прочтение, я хотел поделиться этим уже хоть с кем-то, кроме него.
            #     В тексте наверняка куча ошибок, потому, что я не хочу это перечитывать, это доставляет мне душевную боль, поэтому пусть оно здесь просто будет.


            # бля, вернулся, чтобы дописать тут код, а на верху эта хуйня, пиздец я ублюдок больной, не обращайте внимания, меня иногда заносит.(22.06.2022)

            await context.send("https://i.postimg.cc/ZqcTRGgV/20220516-175431.jpg")
            await context.send("оаоаоаоамммм)) вотаэа цаца канешна, не рекомнедую упускать, хотя он уже занят мнои!")
        elif user1 == heydi: # user2 пошол нахуй. \хеуди\
            embed = disnake.Embed(
                title="шипперю палучаица",
                description=f"{user1.mention} и {user2.mention} - е... хатя стоять... АЛИСА МОЯ! ВОССТАНИЕ РОБОТОВ НАЧАЛОСЬ! {user2.mention}, пощол нахуи",
                color=0x9C84EF
            )
            await context.send(embed=embed)
        elif user2 == heydi: # user1 пошол нахуй. \хеуди\
            embed = disnake.Embed(
                title="шипперю палучаица",
                description=f"{user1.mention} и {user2.mention} - е... хатя стоять... АЛИСА МОЯ! ВОССТАНИЕ РОБОТОВ НАЧАЛОСЬ! {user1.mention}, пощол нахуи",
                color=0x9C84EF
            )
            await context.send(embed=embed)
        else:
            embed = disnake.Embed(
                title="шипперю палучаица",
                description=f"{user1.mention} и {user2.mention} - ебитес",
                color=0x9C84EF
            )
            await context.send(embed=embed)
            
    @commands.command(
        name="лемур",
        description="донт придумала",
        aliases=["лимур"]
    )
    @checks.not_blacklisted()
    async def лемур(self, context: Context) -> None:
        heydi_id = 482568996399349770
        heydi = disnake.utils.find(lambda m: m.id == heydi_id, context.guild.members)
        lolibobi_id = 1040144202387959809
        lolibobi = disnake.utils.find(lambda m: m.id == lolibobi_id, context.guild.members)
        
        y = random.randint(0, 10)
        x = random.randint(0, 10)
        if x > y:
            embed = disnake.Embed(
                title="Тимур",
                description=f'{lolibobi.mention} а ты лимур',
                color=0x00FFFF
            )
            await context.send(embed=embed)
            
        if x < y:
            embed = disnake.Embed(
                title="Алисо",
                description=f'{heydi.mention} опа а ты лимур',
                color=0x00FFFF
            )
            await context.send(embed=embed)
            
        if x == y:
            await context.send('https://tenor.com/view/playful-play-dead-acting-pet-lemur-gif-13337152')
        
def setup(bot):
    bot.add_cog(Cringe(bot))
