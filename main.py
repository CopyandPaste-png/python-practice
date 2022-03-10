import discord
from discord.ext import commands

from config import config
from musicbot.audiocontroller import AudioController
from musicbot.settings import Settings
from musicbot.utils import guild_to_audiocontroller, guild_to_settings

import os
from dotenv import load_dotenv
initial_extensions = ["cogs.text","cogs.games","cogs.helpcommand",
                      "musicbot.commands.general","musicbot.commands.music"]


# Loads the .env file
load_dotenv('config.env')


class Exception(Exception):
    pass
    """Raise for my specific kind of exception"""


# Intents
intentsBOT = discord.Intents.all()


bot = commands.Bot(command_prefix="$",
                   help_command=None, intents=intentsBOT)

bot.intents.members=True


class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.creator = 249901932548849664

    @commands.Cog.listener()
    async def on_ready(self):
        print(config.STARTUP_MESSAGE)
        await bot.change_presence(status=discord.Status.online,activity=discord.Game(name="No sleep simulator, type $help"))

        for guild in bot.guilds:
            await register(guild)
            print("Joined {}".format(guild.name))

        print(config.STARTUP_COMPLETE_MESSAGE)



    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        print(f"Joined {guild.name}")

        await register(guild)
            

    @commands.Cog.listener()
    async def on_connect(self):
        
        '''
        This event is called when the bot is connected to discord, this doesn't necessary means that
        the bot is ready. Use `on_ready` for indication that the bot is fully prepared.

        Parameters
        ----------
        No parameters required

        '''
        config.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
        config.COOKIE_PATH = config.ABSOLUTE_PATH + config.COOKIE_PATH

        if config.BOT_TOKEN == "":
            print("Error: No bot token!")
            exit

        for extension in initial_extensions:
            try:
                bot.load_extension(extension)
                print(extension+" loaded")
            except Exception as e:
                print(e)

    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"Left {guild.name}")

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(894512400613666856)
        if channel is not None:
            await member.send("Welcome to BruteForce Gaming! Please read #welcome and enjoy your stay")
            await channel.send(f"{member.display_name} has joined")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(894512400613666856)
        if channel is not None:
            await channel.send(f"{member.display_name} has left")

    @commands.command()
    async def cogunload(self,ctx,cog):
        if cog in initial_extensions and ctx.author.id == self.creator:
            bot.unload_extension(cog)
        else:
            ctx.send("Not a cog")

    @commands.command()
    async def cogload(self,ctx,cog):
        if cog in initial_extensions and ctx.author.id == self.creator:
            bot.load_extension(cog)
        else:
            await ctx.send("Not a cog")

    @commands.command()
    async def cogreload(self,ctx,cog):
        if cog in initial_extensions and ctx.author.id == self.creator:       
            bot.unload_extension(cog)
            bot.load_extension(cog)
        else:
            await ctx.send("Not a cog")

    @commands.command()
    async def cogs(self,ctx):
        if ctx.author.id == self.creator:
            await ctx.send(initial_extensions)


async def register(guild):

    guild_to_settings[guild] = Settings(guild)
    guild_to_audiocontroller[guild] = AudioController(bot, guild)

    sett = guild_to_settings[guild]

    await guild.me.edit(nick=sett.get('default_nickname'))

    if config.GLOBAL_DISABLE_AUTOJOIN_VC == True:
        return

    vc_channels = guild.voice_channels

    if sett.get('vc_timeout') == False:
        if sett.get('start_voice_channel') == None:
            try:
                await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
            except Exception as e:
                print(e)

        else:
            for vc in vc_channels:
                if vc.id == sett.get('start_voice_channel'):
                    try:
                        await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                    except Exception as e:
                        print(e)



bot.add_cog(Startup(bot=bot))

TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(TOKEN)
