from discord import colour
from discord.colour import Color
from discord.enums import StickerType
from discord.ext import commands
import asyncio
import datetime
import random
import json
import discord
from discord.ext.commands.core import command
import pytz
from info import jokes

with open("JSON/facts.json", "r") as f:
    data = json.load(fp=f)
    facts = data["a"]

with open("JSON/variables.json", "r") as f:
    data = json.load(fp=f)
    ashley_moments = data["ashley_moments"]
    raven_moments = data["raven_moments"]
    chaeli_moments = data["chaeli_moments"]
    rogan_moments = data["rogan_moments"]
    victoria_moments = data["victoria_moments"]
    lucian_moments = data["lucian_moments"]
    christian_moments = data["christian_moments"]

# Time

utc_now = datetime.datetime.now(tz=pytz.UTC)

messages = {
    "poes":"no you",
    "hoe":"The only hoe around here is you",
    "dictator": random.choice(["Yes Ephemeral is dictator around here. No rights for you",
                "Ephemeral is watching.You must strife carefully on her land filled with dictatorship",
                "Roses are red\nViolets are blue\nEphemeral is a dictator\nWho is also a hater and waiter",
                "You are under the rule of Ephemeral in these lands",
                "Remember when democracy was a thing? Yeah me too"
                ]),
    "homiesexual":"Homiesexual best sexual amen",
    "uk":"A whole bunch of colonisers",
    "dbd":random.choice(["shit","not bad tbh","seen worse","worse than AMOUNG US"]),
    "asain":"Asain persuation brother",
    'wizard 101':'Only hoes play that trash game. Period',
    'fortnite':'super bad game. A worse PUBG',
    'south africa':'Best country ever for real. No crime fr',
    "kiwi":'A fruit, but also people from jaffers land',
    "brexit":'UK is going to be a rainbow but with no colour at all, only white',
    "dragon age origins":'Literally smash all the females'

}

stickers = {
    ":bm:":["go to gym to fattie","mikey.png"]
}

# classes
class UserMessages(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.id != message.author.id:
            context = message.content.strip().lower()
            if context in messages.keys():
                await message.channel.send(messages[context])
            elif context in stickers.keys():
                await message.channel.send(stickers[context][0], file=discord.File(f"images/{stickers[context][1]}"))
                await message.delete()
        else:
            return

    @commands.command(usage="No")
    
    async def reward(self, ctx:commands.Context, member: discord.Member, *args):
        reason = ' '.join(args)
        reward_embed = discord.Embed(title=f'The reward {reason}', description=f'is awarded to {member.display_name}',
                                     colour=0x730BE7)
        reward_embed.add_field(name='This award was given by:', value=f'{ctx.author}', inline=False)
        reward_embed.set_thumbnail(url='https://www.maestro24.com/media/image/product/378733/md/clown-harry-playing-the'
                                       '-tuba.jpg')

        try:
            await ctx.message.channel.send(embed=reward_embed)
        except discord.ext.commands.errors.MemberNotFound:
            await ctx.message.channel.send('incorrect format. Use $rewardformat to see the format')

    @commands.command(usage="No")
    async def ma(self, ctx:commands.Context):
        pass

    @commands.command(usage="No")
    
    async def dk(self, ctx:commands.Context):
        pass

    @commands.command()
    
    async def rewardformat(self, ctx:commands.Context):
        await ctx.message.channel.send(
            'Format of reward command is:\n $reward @user () - where () represents reason for '
            'reward')

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spamEnabled = False

    @commands.command()
    async def joke(self, ctx:commands.Context):
        joke_embed = discord.Embed(title='The joke is...', description=f'{random.choice(jokes)}', colour=0x6800f0)
        await ctx.channel.send(embed=joke_embed)

    @commands.command()
    async def fact(self, ctx:commands.Context):
        fact_embed = discord.Embed(title=f'{ctx.author}, your fact is...', description=f'{random.choice(facts)}',
                                   colour=0xe8e400)
        fact_embed.set_footer(text='Taken from https://www.thefactsite.com')
        await ctx.channel.send(embed=fact_embed)

    @commands.command()
    async def gif(self, ctx:commands.Context):
        gifs=[
        "https://tenor.com/view/weird-bunny-gif-11908781",
        "https://tenor.com/view/hands-loop-many-freaky-gif-7736587",
        "https://tenor.com/view/weird-face-lick-nose-gif-11424629",
        "https://tenor.com/view/weird-funny-scary-banana-weird-face-gif-15355427",
        "https://tenor.com/view/midget-dancing-weird-gif-11230211",
        "https://tenor.com/view/dont-trust-airpods-weird-3d-animation-scream-gif-16483476",
        "https://tenor.com/view/creepy-thomas-train-weird-gif-16804019",
        "https://tenor.com/view/weird-walking-dog-funny-gif-13734035",
        "https://tenor.com/view/funny-animals-lol-dog-cake-big-eyes-gif-12360942",
        "https://tenor.com/view/cursed-mannequin-jericho-walking-weird-gif-17855972",
        "https://tenor.com/view/bilelaca-laugh-laughing-scary-weird-gif-12694732",
        "https://tenor.com/view/weird-cat-pet-gif-11420991",
        "https://tenor.com/view/banana-japanese-weird-wtf-what-gif-5496284",
        "https://tenor.com/view/strange-crazy-weird-head-headache-gif-10066883",
        "https://tenor.com/view/weird-idk-laughing-gif-7221683",
        "https://tenor.com/view/fish-riding-a-bike-funny-animals-fish-weird-odd-gif-10003053",
        "https://tenor.com/view/funny-face-selfie-tongue-out-gif-13879668",
        "https://tenor.com/view/cow-utter-weird-gif-5729563",
        "https://tenor.com/view/japanese-weird-face-hold-it-gif-5777805",
        "https://tenor.com/view/garfield-dance-sexy-gif-15406100",
        "https://tenor.com/view/pig-sexy-pig-sexy-fat-bikini-sexy-back-gif-12326005",
        "https://tenor.com/view/kiss-sexy-bye-hey-hi-gif-15318962",
        "https://tenor.com/view/pizza-time-sexy-snack-time-gif-13948101",
        "https://tenor.com/view/gotta-run-go-chase-raiders-gif-4908126",
        "https://tenor.com/view/whaaaat-weird-cute-dog-gif-13465900",
        "https://tenor.com/view/weird-cat-milk-gif-5542526",
        "https://tenor.com/view/slug-weird-wtf-creepy-eat-gif-6034124",
        "https://tenor.com/view/little-babys-ice-cream-creepy-gif-8059312",
        "https://tenor.com/view/spaceballs-alien-dance-celebrate-creepy-gif-5583361",
        "https://tenor.com/view/star-wars-cat-vs-dog-jedi-cat-jedi-lightsaber-gif-16455709",
        "https://tenor.com/view/car-wtf-weird-cyriak-gif-13984840",
        "https://tenor.com/view/weird-lol-wtf-tongue-dog-gif-13777097",
        "https://tenor.com/view/rem-re-zero-kara-hajimaru-isekai-seikatsu-ram-remu-gif-18081648",
        "https://tenor.com/view/funny-face-ugly-anime-smile-gif-15779943",
        "https://tenor.com/view/swing-anime-gif-11028125",
        "https://tenor.com/view/funny-face-anime-gif-14294759",
        "https://tenor.com/view/weird-anime-gif-22056655",
        "https://tenor.com/view/cat-tik-tok-anime-anime-cat-weird-gif-14355730",
        "https://tenor.com/view/horny-dry-hump-day-happy-gif-14240763",
        "https://tenor.com/view/imposter-syndrome-imposter-among-us-vezi-zauer-veit-gif-20932910",
        "https://tenor.com/view/goat-goat-lick-tongue-out-gif-5193394",
        "https://tenor.com/view/whistle-wolf-cat-call-howl-gif-15693385",
        "https://tenor.com/view/fail-baby-funny-fail-gif-15597542",
        "https://cdn.discordapp.com/attachments/632647249222172694/885976342456336444/flat750x075f-pad750x1000f8f8f8.png",
        "https://tenor.com/view/goal-mbappe-celebration-crying-baby-football-gif-17477397",
        "https://tenor.com/view/abishek-batha-panda-oh-god-what-i-have-done-annoyed-gif-16533558",
        "https://tenor.com/view/futurama-dance-dancing-wiggle-happy-gif-5130323",
        "https://tenor.com/view/cat-tongue-creepy-weird-gif-4933386",
        "https://tenor.com/view/john-cena-weird-face-small-reaction-gif-5386468",
        "https://tenor.com/view/run-crazy-weird-horse-funny-gif-3406247",
        "https://tenor.com/view/dance-excited-weird-gif-5612843",
        "https://tenor.com/view/bugs-bug-insects-gross-creepy-gif-5041662",
        "https://tenor.com/view/trump-donald-elections-gif-5454339",
        "https://tenor.com/view/weird-lol-what-gif-5242674"
        ]
        await ctx.channel.send(gifs[random.randint(0,len(gifs))])


    @commands.command()
    @commands.has_role("Basic Bin Boys")
    async def enable(self, ctx:commands.Context):
        self.spamEnabled = not self.spamEnabled

    @commands.command()
    async def isEnabled(self, ctx:commands.Context):
        await ctx.send(str(self.spamEnabled))
    
    @commands.command()
    async def spammany(self, ctx:commands.Context, *args):
        if self.spamEnabled == False:
            await ctx.send("use $enable to use this command")
            return

        message = ''.join(args)
        counter = random.randint(0, 100)

        if counter == 59:
            await ctx.send("UNLUCKY BRO")
            for i in range(420):
                await ctx.send(message)
                await asyncio.sleep(0.001)
                i += 1
        else:
            for i in range(random.randint(0, 40)):
                await ctx.send(message)
                await asyncio.sleep(0.001)
                i += 1


class Moments(commands.Cog):
    @commands.command()
    async def ashleymoment(self, ctx:commands.Context):
        await ctx.send(random.choice(ashley_moments))

    @commands.command()
    async def ravenmoment(self, ctx:commands.Context):
        await ctx.send(random.choice(raven_moments))

    @commands.command()
    async def victoriamoment(self, ctx:commands.Context):
        await ctx.send(random.choice(victoria_moments))

    @commands.command()
    async def lucianmoment(self, ctx:commands.Context):
        await ctx.send(random.choice(lucian_moments))

    @commands.command()
    async def christianmoment(self, ctx:commands.Context):
        await ctx.send(random.choice(christian_moments))

    @commands.command()
    async def chaelimoment(self, ctx:commands.Context):
        await ctx.send(random.choice(chaeli_moments))

    @commands.command()
    async def roganmoment(self, ctx:commands.Context):
        await ctx.send(random.choice(rogan_moments))


class Timezone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tz(self, ctx:commands.Context):
        await ctx.send(str(utc_now.astimezone(pytz.timezone("Etc/GMT-12")))[10:16])

class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggestion(self, ctx:commands.Context, *args):
        user = await ctx.guild.fetch_member(249901932548849664)
        message = ' '.join(args)
        em = discord.Embed(title="Suggestion:", description=message, colour=discord.Colour.dark_grey())
        em.add_field(name="Suggestion made by:", value=ctx.author)
        await ctx.send(embed=em)
        await user.send(embed=em)


def setup(bot):
    bot.add_cog(Spam(bot))
    bot.add_cog(UserMessages(bot))
    bot.add_cog(Moments(bot))
    bot.add_cog(Timezone(bot))
    bot.add_cog(Suggestions(bot))
