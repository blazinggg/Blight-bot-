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

token = os.environ["token"]

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.message_content = True
activities = [
    discord.Game(name="Playing with Blight nons"),
    discord.Activity(type=discord.ActivityType.watching,
                     name="Watching Blight non")
]
activity = random.choice(activities)

bot = commands.Bot(command_prefix="b!",
                   intents=intents)


class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)


bot.help_command = MyNewHelp()

bot.load_extension("Error")

bot.load_extension("leaderboards")

bot.load_extension("somecommands")

bot.load_extension("hypixelcommands")

bot.load_extension("moderativecommands")

bot.load_extension("Image")

keep()
print("Check")

bot.run(token)
