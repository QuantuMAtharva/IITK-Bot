import discord
from discord.ext import commands
import os
import asyncio
from stay_online import stay_online

client = discord.Client()
client = commands.Bot(status=discord.Status.dnd, command_prefix= "=", intents = discord.Intents.all())

client.remove_command("help")

# Login prompt for the Bot and varying Rich Presence
@client.event
async def on_ready():
    print('{0.user} is now up and running!'.format(client))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name = "HelloIITK Lectures :) | =help"))
        await asyncio.sleep(20)

        await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name = f"students of {len(client.guilds)} IITK servers get dassa | =help"))
        await asyncio.sleep(20)

        await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name = f"{sum([len(guild.members) for guild in client.guilds])} students get a dassa | =help"))
        await asyncio.sleep(20)

        await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name = "Online Convocation | =help"))
        await asyncio.sleep(20)

# Main Help Command
@client.group(invoke_without_command=True)
async def help(ctx):
    help=discord.Embed(title="IITK Bot Help", color=0x00ff00, description="My prefix is `=`, and commands are to be run as `=<command name>`. Here goes a list of my commands. Use `=help <command name>` to know more about a specific command")
    help.set_author(name="IITK Bot", url="https://github.com/QuantuMAtharva/IITK-Bot", icon_url="https://media.discordapp.net/attachments/864451366327549963/865133614776451072/9k.png")
    help.set_footer(text="Powered by mooKIT", icon_url="https://cdn.discordapp.com/attachments/864451366327549963/865132951251451914/2Q.png")
    help.set_thumbnail(url="https://cdn.discordapp.com/attachments/864451366327549963/865132277620539402/iitk_logo.jpg")
    help.add_field(inline=False, name="Utility Commands", value="1. `iitk` : Gives important official websites related to IITK\n2. `snt` : Gives Server links for all SnT Clubs, with few other details\n3. `mnc` : Gives links related to MnC Clubs\n4. `acads` : Gives important links related to Academic things, like Grade Calculator Website, Course Resorces Links etc.")
    help.add_field(inline=False, name="Enabling IITK Email Verfication for the server", value="Coming soon...")
    help.add_field(inline=False, name="Extra Commands", value="1. `=clear <number>` : To clear a certain number of messages in a channel **[NOTE: Requires user to have Manage Messages Permission]**\n2. `=invite` : Get invite link for the Bot in your DM")
    await ctx.send(embed = help)

# Subcommands under the main help command
@help.command()
async def iitk(ctx):
    iitk = discord.Embed(title="`=iitk` Command", color=0x00ff00, description="Gives out links for IITK website, DoAA, DoSA, IITK Alumni Association, SIIC and much more...")
    await ctx.send(embed=iitk)

@help.command()
async def snt(ctx):
    snt = discord.Embed(title="`=snt` Command", color=0x00ff00, description="Gives out links for all SnT Club servers, websites etc along with much more details")

@help.command()
async def mnc(ctx):
    mnc = discord.Embed(title="`=mnc` Command", color=0x00ff00, description="Gives out links for MnC Club servers, handles etc along with much more details")

@help.command()
async def acads(ctx):
    acads = discord.Embed(title="`=acads` Command", color=0x00ff00, description="Gives out important links related to Academic things, like Grade Calculator Website, Course Resorces Links, Previous Batches Course Grades Stats etc.")

@help.command()
async def clear(ctx, number):
    clear= discord.Embed(title="`=clear <number>` Command", color=0x00ff00, description="Clears a certain number of messages in a channel.\nUsage: `clear 2` clears 2 latest messages\n**[NOTE: Requires user to have Manage Messages Permission]**")

# Other Custom Commands
@client.command()
async def iitk(ctx):
    iitk_links=discord.Embed(title="Links related to IITK", color=0x00ff00, description="1. [IITK Website](https://www.iitk.ac.in)\n2. [IITK Alumni Association](https://iitkalumni.org/)\n3. [SIIC](https://siicincubator.com/)")
    await ctx.send(embed=iitk_links)

@client.command()
async def snt(ctx):
    snt_links=discord.Embed(title="Links related to SnT", color=0x00ff00, description="1. [SnT Website](https://www.sntiitk.in)\n2. [SnT Discord Server](https://discord.gg/ChYB82A49Y)")

@client.command()
async def mnc(ctx):
    mnc_links=discord.Embed(title="Links related to MnC", color=0x00ff00, description="1. [MnC Website](https://students.iitk.ac.in/mnc/)")

@client.command()
async def acads(ctx):
    acads_links=discord.Embed(title="Links related to Academic", color=0x00ff00, description="1. [CPI/SPI Calculator](https://cpi-spi-calculator.herokuapp.com/)\n2. [Course Resorces Links (**More coming soon**)](https://examvault.github.io)\n3. [Faculty Wise Past Grades](https://incog-nahito.github.io/grades/faculty/)\n[Course Wise Past Grades](https://grades-card.github.io/)")

@client.command()
async def invite(ctx):
    invite_link = discord.Embed(title="Hi! I hope ||Chill Hai|| :slight_smile:.\nWant to invite me to your server?", color=0x00ff00, description="[Click Here](https://discord.com/api/oauth2/authorize?client_id=864761267687653416&permissions=8&scope=bot) to Invite me!")
    await ctx.author.send(embed=invite_link)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, num=2):
  await ctx.channel.purge(limit = num+1)




stay_online()
client.run(os.getenv('TOKEN'))