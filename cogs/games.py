import json
import random

from discord.ext import commands
import discord
from info import killerInfo

killerNames = sorted(set([i['name'] for i in killerInfo.values()]))[1:]
killerPerks = [i for i in killerInfo.keys()]

"""
with open("JSON/killerperks.json", "r") as f:
    killerInfo = json.load(fp=f)
    killerNames = sorted(set([i['name'] for i in killerInfo.values()]))[1:]
    killerPerks = [i for i in killerInfo.keys()]
"""
with open("JSON/survivorperks.json", "r") as f:
    survivorInfo = json.load(fp=f)
    survivorPerks = [i for i in survivorInfo.keys()]
    
class DBD(commands.Cog):
    """
    A class used to hold DBD discord commands
    
    Attributes
    ----------
    bot = commands.Com
        The bot instance
    
    Methods
    -------
    DBD(self,ctx)
        """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()#aliases=["dbd"])
    async def DBD(self, ctx:commands.Context):
        pf = "$"  # pf = prefix
        em = discord.Embed(title="DBD", color=0x32a852)
        em.add_field(name=f"{pf}survivorperk/{pf}sperk", value="Sends 1 random survivor perk", inline=False)
        em.add_field(name=f"{pf}survivorperks/{pf}sperks", value="Sends 4 random survivor perks", inline=False)
        em.add_field(name=f"{pf}killerperk/{pf}kperk", value="Sends 1 random killer perk", inline=False)
        em.add_field(name=f"{pf}killerperks/{pf}kperks", value="Sends 4 random killer perk", inline=False)
        em.add_field(name=f"{pf}killername/{pf}kname", value="Sends 1 random killer name", inline=False)
        em.add_field(name=f"{pf}kyfsurvivorperk/{pf}kyfsperk", value="DMs a user one random survivor perk", inline=False)
        em.add_field(name=f"{pf}kyfsurvivorperks/{pf}kyfsperks", value="DMs a user 4 random survivor perks", inline=False)
        em.add_field(name=f"{pf}kyfkillerperk/{pf}kyfkperk", value="DMs a user 1 random killer perk", inline=False)
        em.add_field(name=f"{pf}kyfkillerperks/{pf}kyfkperks", value="DMs a user 4 random killer perk", inline=False)
        em.add_field(name=f"{pf}kyfkillername/{pf}kyfkname", value="DMs a user 1 random killer name", inline=False)
        await ctx.send(embed=em)


    # These set of commands are just for DBD KILLERS
    @commands.command(aliases=["kname"])
    async def killername(self, ctx:commands.Context):
        await ctx.message.channel.send(f"Your killer is:\n{random.choice(killerNames)}")

    @commands.command(aliases=["kperks"])
    async def killerperks(self, ctx:commands.Context):
        perks = list(random.sample(killerPerks, 4))
        embed = discord.Embed(title=f"Perks:", color=0xff0000)
        embed.add_field(name="Perk:", value= "{perk}->{killer}".format(perk=perks[0], killer=killerInfo[perks[0]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{killer}".format(perk=perks[1], killer=killerInfo[perks[1]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{killer}".format(perk=perks[2], killer=killerInfo[perks[2]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{killer}".format(perk=perks[3], killer=killerInfo[perks[3]]['name']), inline=False)
        await ctx.message.channel.send(embed= embed)

    @commands.command(aliases=["kperk"])
    async def killerperk(self, ctx:commands.Context):
        perk = random.choice(killerPerks)
        embed = discord.Embed(title=f"{perk}", color=0xff0000)
        embed.add_field(name="From:", value=killerInfo[perk]['name'], inline=False)
        embed.add_field(name="Description:", value=killerInfo[perk]['description'], inline=False)
        embed.set_thumbnail(url=killerInfo[perk]['icon'])
        await ctx.message.channel.send(embed= embed)

    @commands.command(aliases=["krandom"])
    async def killerrandom(self, ctx:commands.Context):
        await ctx.message.channel.send(f'Name:{random.choice(killerNames)}\nPerks:{random.sample(killerPerks, 4)}')

    # DBD survivor

    @commands.command(aliases=["sperks"])
    async def survivorperks(self, ctx:commands.Context):
        perks = list(random.sample(survivorPerks, 4))
        embed = discord.Embed(title=f"Perks:", colour=0x0033ff)
        embed.add_field(name="Perk:", value= "{perk}->{survivor}".format(perk=perks[0], survivor=survivorInfo[perks[0]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{survivor}".format(perk=perks[1], survivor=survivorInfo[perks[1]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{survivor}".format(perk=perks[2], survivor=survivorInfo[perks[2]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{survivor}".format(perk=perks[3], survivor=survivorInfo[perks[3]]['name']), inline=False)
        await ctx.message.channel.send(embed= embed)


    @commands.command(aliases=["sperk"])
    async def survivorperk(self, ctx:commands.Context):
        perk = random.choice(survivorPerks)
        embed = discord.Embed(title=f"{perk}", colour=0x0033ff)
        embed.add_field(name="From:", value=survivorInfo[perk]['name'], inline=False)
        embed.add_field(name="Description:", value=survivorInfo[perk]['description'], inline=False)
        embed.set_thumbnail(url=survivorInfo[perk]['icon'])
        await ctx.message.channel.send(embed= embed)

    # These set of commands are just for DBD kyf KILLERS
    @commands.command(aliases=["kyfkname"])
    async def kyfkillername(self, ctx:commands.Context):
        await ctx.author.send(f"Your killer is:\n{random.choice(killerNames)}")

    @commands.command(aliases=["kyfkperks"])
    async def kyfkillerperks(self, ctx:commands.Context):
        perks = list(random.sample(killerPerks, 4))
        embed = discord.Embed(title=f"Perks:", color=0xff0000)
        embed.add_field(name="Perk:", value= "{perk}->{killer}".format(perk=perks[0], killer=killerInfo[perks[0]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{killer}".format(perk=perks[1], killer=killerInfo[perks[1]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{killer}".format(perk=perks[2], killer=killerInfo[perks[2]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{killer}".format(perk=perks[3], killer=killerInfo[perks[3]]['name']), inline=False)
        await ctx.author.send(embed= embed)

    @commands.command(aliases=["kyfkperk"])
    async def kyfkillerperk(self, ctx:commands.Context):
        perk = random.choice(killerPerks)
        embed = discord.Embed(title=f"{perk}", color=0xff0000)
        embed.add_field(name="From:", value=killerInfo[perk]['name'], inline=False)
        embed.add_field(name="Description:", value=killerInfo[perk]['description'], inline=False)
        embed.set_thumbnail(url=killerInfo[perk]['icon'])
        await ctx.author.send(embed= embed)

    @commands.command(aliases=["kyfkrandom"])
    async def kyfkillerrandom(self, ctx:commands.Context):
        await ctx.author.send(f'Name:{random.choice(killerNames)}\nPerks:{random.sample(killerPerks, 4)}')

    # DBD kyf survivor

    @commands.command(aliases=["kyfsperks"])
    async def kyfsurvivorperks(self, ctx:commands.Context):
        perks = list(random.sample(survivorPerks, 4))
        embed = discord.Embed(title=f"Perks:", colour=0x0033ff)
        embed.add_field(name="Perk:", value= "{perk}->{survivor}".format(perk=perks[0], survivor=survivorInfo[perks[0]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{survivor}".format(perk=perks[1], survivor=survivorInfo[perks[1]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{survivor}".format(perk=perks[2], survivor=survivorInfo[perks[2]]['name']), inline=False)
        embed.add_field(name="Perk:", value= "{perk}->{survivor}".format(perk=perks[3], survivor=survivorInfo[perks[3]]['name']), inline=False)
        await ctx.author.send(embed= embed)


    @commands.command(aliases=["kyfsperk"])
    async def kyfsurvivorperk(self, ctx:commands.Context):
        perk = random.choice(survivorPerks)
        embed = discord.Embed(title=f"{perk}", colour=0x0033ff)
        embed.add_field(name="From:", value=survivorInfo[perk]['name'], inline=False)
        embed.add_field(name="Description:", value=survivorInfo[perk]['description'], inline=False)
        embed.set_thumbnail(url=survivorInfo[perk]['icon'])
        await ctx.author.send(embed= embed)

    @commands.command(aliases=["searchperk"])
    async def perk(self,ctx, *args):
        perkName = "".join(args)
        if perkName in killerPerks:
            embed = discord.Embed(title=f"{perkName}", color=0xff0000)
            embed.add_field(name="From:", value=killerInfo[perkName]['name'], inline=False)
            embed.add_field(name="Description:", value=killerInfo[perkName]['description'], inline=False)
            embed.set_thumbnail(url=killerInfo[perkName]['icon'])
            await ctx.message.channel.send(embed= embed)
        elif perkName in survivorPerks:
            embed = discord.Embed(title=f"{perkName}", colour=0x0033ff)
            embed.add_field(name="From:", value=survivorInfo[perkName]['name'], inline=False)
            embed.add_field(name="Description:", value=survivorInfo[perkName]['description'], inline=False)
            embed.set_thumbnail(url=survivorInfo[perkName]['icon'])
            await ctx.message.channel.send(embed= embed)
        else:
            await ctx.message.channel.send("Invalid perk name")

def setup(bot):
    bot.add_cog(DBD(bot))
