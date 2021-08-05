import discord
from discord.ext import commands
import os
import asyncio

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