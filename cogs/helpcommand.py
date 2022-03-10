import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pf = "$"

    @commands.group(invoke_without_command=True)
    async def help(self, ctx:commands.Context):
        """A custom help command

        Parameters
        _________
        None

        NB:
        a @commands.group() decorator is required to make this custom help command work.
        Basically it allows for subcommands(@helpfor.command()) to be called and invoked through
        $helpfor <command_name>, similar to how the default help command works.
        """

        # guild_prefix queries the database (main.GUILDS) to get the prefix for the guild
        em = discord.Embed(title="COMMANDS")

        
        em.add_field(name=f"DBD", value=f"{self.pf}help DBD", inline=False)
        em.add_field(name=f"Text commands", value=f"{self.pf}help text", inline=False)
        em.add_field(name=f"Music commands", value=f"{self.pf}help music", inline=False)
        await ctx.send(embed=em)

    # GAMES COG
    #DEAD BY DAYLIGHT
    @help.command()
    async def DBD(self, ctx:commands.Context):
        
        fields = {
                "(survivorperk/sperk)":"Sends 1 random survivor perk",
                "(survivorperks/sperks)":"Sends 4 random survivor perks",
                "(killerperk/kperk)":"Sends 1 random killer perk",
                "(killerperks/kperks)":"Sends 4 random killer perk",
                "(killername/kname)":"Sends 1 random killer name",
                "(kyfsurvivorperk/kyfsperk)":"DMs a user one random survivor perk",
                "(kyfsurvivorperks/kyfsperks)":"DMs a user 4 random survivor perks",
                "(kyfkillerperk/kyfkperk)":"DMs a user 1 random killer perk",
                "(kyfkillerperks/kyfkperks)":"DMs a user 4 random killer perk",
                "(kyfkillername/kyfkname)":"DMs a user 1 random killer name"

        }
        
        em = discord.Embed(title="DBD", color=0x32a852)
       
        for i,j in fields.items():
            em.add_field(name=f"{self.pf}{i}", value=f"{j}", inline=False)

        await ctx.send(embed=em)


    @help.command(aliases=["kname"])
    async def killername(self, ctx:commands.Context):
        """
        Explains how the $killername command works
        
        """

        em = discord.Embed(title=f"{self.pf}killername", color=0xff0000)
        em.add_field(name="Usage:", value="Sends the user 1 random killer name")
        em.add_field(name="Format:", value=f"{self.pf}killername", inline=False)
        em.add_field(name="Example:", value=f"{self.pf}killername -> Bot will then DM you", inline=False)
        await ctx.send(embed=em)


    @help.command(aliases=["sperks"])
    async def survivorperks(self, ctx:commands.Context):
        """
        Explains how the $survivorperks command works
        """
        pf = "$"  # pf = prefix
        em = discord.Embed(title=f"{self.pf}survivorperks")
        em.add_field(name="Usage:", value="Sends the user 4 random survivor perks")
        em.add_field(name="Format:", value=f"{self.pf}surviorperks", inline=False)
        em.add_field(name="Example:", value=f"{self.pf}surivorperks -> Bot will then DM you", inline=False)
        await ctx.send(embed=em)


    @help.command(aliases=["sperk"])
    async def survivorperk(self, ctx:commands.Context):
        """
        Explains how the $survivorperk command works
        """
        em = discord.Embed(title=f"{self.pf}survivorperk")
        em.add_field(name="Usage:", value="Sends the user 1 random survivor perks")
        em.add_field(name="Format:", value=f"{self.pf}survivorperk", inline=False)
        em.add_field(name="Example:", value=f"{self.pf}survivorperk -> Bot will then DM you", inline=False)
        await ctx.send(embed=em)


    @help.command(aliases=["kperk"])
    async def killerperk(self, ctx:commands.Context):
        """
        Explains how the $killerperk command works
        """
        em = discord.Embed(title=f"{self.pf}killerperk", color=0xff0000)
        em.add_field(name="Usage:", value="Sends the user 1 random killer perks")
        em.add_field(name="Format:", value=f"{self.pf}killerperk", inline=False)
        em.add_field(name="Example:", value=f"{self.pf}killerperk -> Bot will then DM you", inline=False)
        await ctx.send(embed=em)


    @help.command(aliases=["kperks"])
    async def killerperks(self, ctx:commands.Context):
        """
        Explains how the $killerperks command works
        """
        em = discord.Embed(title=f"{self.pf}killerperks", color=0xff0000)
        em.add_field(name="Usage:", value="Sends the user 4 random killer perks")
        em.add_field(name="Format:", value=f"{self.pf}killerperks", inline=False)
        em.add_field(name="Example:", value=f"{self.pf}killerperks -> Bot will then DM you", inline=False)
        await ctx.send(embed=em)

    @help.command()
    async def text(self, ctx:commands.Context):
        em = discord.Embed(title="Text")
        em.add_field(name=f"{self.pf}gif", value="Sends one random gif", inline=False)
        em.add_field(name=f"{self.pf}joke", value="Sends one random joke", inline=False)
        em.add_field(name=f"{self.pf}fact", value="Sends one random fact", inline=False)
        em.add_field(name=f"{self.pf}suggestion", value="Send a suggestion for a command/bot improvement", inline=False)
        em.add_field(name=f"{self.pf}enable", value="Enables spam command", inline=False)
        em.add_field(name=f"{self.pf}isEnabled", value="Checks if spam command is enabled", inline=False)
        await ctx.send(embed=em)

    @help.command()
    async def music(self, ctx:commands.Context):
        em = discord.Embed(title="Music")

        fields = {"play <link/name>":"plays a song.It accepts either links or an inputted name",
                  "loop" :"loops current playing song", "shuffle" :"shuffles upcoming songs",
                  "pause" :"pause current playback", "queue <song>" :"add a song to the queue",
                  "stop" :"Bot stops playing music", "skip" :"skips the current song",
                  "clear" :"clears the queue", "prev" :"plays the previous song",
                  "resume" :"resumes the playback if paused",
                  "songinfo" :"information about the song currently played",
                  "history" :"lists the songs played by the bot in the current session",
                  "volume <number>" :"sets volume of the bot"
        }

        for i,j in fields.items():
            em.add_field(name=f"{self.pf}{i}", value=f"{j}", inline=False)

        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(HelpCommand(bot))
