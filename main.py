#Importing - Does not require explanation
from discord.ext import commands
import discord
import requests
from discord.ext import commands, tasks
import discord
import asyncio
from datetime import datetime
import random
import time
from pprint import pprint
import re
import json
from discord.ext.commands import Bot
from discord.ext import tasks
import os
from flask import Flask
from keep_alive import keep
import dns
import pprint

#Getting token and creating bot
token = os.environ["token"]

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
activities = [
    discord.Game(name="Playing with Blight nons"),
    discord.Activity(type=discord.ActivityType.watching,
                     name="Watching Blight non")
]
activity = random.choice(activities)

bot = commands.Bot(command_prefix="b!",
                   intents=intents,
                   status=discord.Status.online)




#Setting help command
class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)

#Loading cogs
cogs = ['Error', 'leaderboards', 'somecommands', 'hypixelcommands', 'moderativecommands', 'Image']

for cog in cogs:
  try:
    bot.load_extension(cog)
  except:
    print(f'Failed to log {cog}')

#Some code that does something   
keep()
print("Check")

#Running bot
bot.run(token)
