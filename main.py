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
    help.add_field(inline=False, name="Extra Commands", value="Use `=clear <number>` to clear a certain number of messages in a channel")



stay_online()
client.run(os.getenv('TOKEN'))