import asyncio
from discord import message
from discord.abc import GuildChannel
from discord.ext import commands, tasks
import discord
from discord.guild import Guild
import requests
import time
from datetime import datetime
from discord.utils import get
from time import sleep
from discord.ext import commands
from discord.utils import get
import os
from discord.ext.commands import bot, has_permissions, MissingPermissions
import json
import random
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from itertools import cycle
from discord.ext.commands import Bot
import random

quoteids = ["587390710974644311", "244542234895187979"]




token = os.environ["token"]

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
activities = [discord.Game(name="Playing with Blight nons"),
discord.Activity(type=discord.ActivityType.watching, name="Watching Blight non")]
activity = random.choice(activities)

bot = commands.Bot(command_prefix="b!",
                   intents=intents,
                   activity=activity,
                   status=discord.Status.dnd)








snipe_list = []

colors = [0xFF3333, 0x761954, 0xc34a17, 0x005073, 0x146f85, 0xbf4055, 0x40bfaa, 0x674d93, 0xf474d0, 0x278d39, 0x9f1616]




class Cool(commands.Cog):
    

    """A couple of simple commands"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")
    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bots current API latency"""
        start_time = time.time()
        message = await ctx.send('Testing ping..')
        end_time = time.time()

        await message.edit(content=(f'Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms'))
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        blight = self.bot.get_guild(payload.guild_id)
        member = payload.member
        channel = discord.utils.get(blight.channels, name="quote-book")
        subchannel = discord.utils.get(blight.channels, name="quote-book-submissions")
                    
        
        
        (payload.message_id)
        emoji = "\u2705"
        emoji1 = "\u274c"
        if int(payload.channel_id) == int(879531057932795924):
            message = await subchannel.fetch_message(payload.message_id)
            content = message.content
            if str(member.id) == "850128850213011496":
                return
            elif str(payload.user_id) in quoteids:
                message = await subchannel.fetch_message(payload.message_id)
                print(payload.message_id)
                content = message.content
                print(payload.emoji)
                if '✅' == str(payload.emoji):

                    try:
                        await channel.send(content)
                    except HTTPException:
                        image = message.attachments[0].url
                        await channel.send(image)
                    await message.delete()
                elif '❌' == str(payload.emoji):
                    await message.delete()
                else:
                    await message.remove_reaction(payload.emoji, member)
            elif str(payload.emoji) != '✅' and str(payload.emoji) != '❌' or member.id not in quoteids:
                await message.remove_reaction(payload.emoji, member)
            
                
            else:
                await message.remove_reaction(payload.emoji, member)


    
    @commands.Cog.listener()
    async def on_message(self, message):
        emoji = "\u2705"
        emoji1 = "\u274c"
        if str(message.channel) == "applications":
            await message.delete()
        elif str(message.channel) == "quote-book-submissions":
            await message.add_reaction(emoji)
            await message.add_reaction(emoji1)
    @commands.command(name="mango")
    async def mango(self, ctx):
        """Mango."""
        files = ["./Files/heshmum.mp4", "./Files/mangoo.mov"]
        choice = random.choice(files)
        if str(ctx.author.id) == "587390710974644311":
            await ctx.send("Mango...")
            await ctx.send(file=
            discord.File(choice))
        elif str(ctx.author.id) == "326360408053252108":
            await ctx.send("Mango... UwU")
            await ctx.send(file=discord.File(choice))
        elif str(ctx.author.id) == "649697579424153643":
            await ctx.send("Mango...")
            await ctx.send(file=discord.File(choice))
        elif str(ctx.author.id) == "825552339728334849":
            await ctx.send("no")
        else:
            await ctx.send("Mango...")
            await ctx.send(file=discord.File(choice))
    

    


    @commands.command(name="status")
    @commands.has_role("Bloozing")
    async def status(self, ctx: commands.Context, *, text : str):

      
        """Only useable by blazing."""
        await self.bot.change_presence(activity=discord.Game(name=text))
    #@commands.Cog.listener()
    #async def on_member_join(self, member: discord.Member):
        #print('idk')
        #channel = discord.utils.get(member.guild.channels, name="portal-｡･")
        #print(channel)
        #backgroundimage = Image.open('Blight.png').convert('RGB')
        #draw = ImageDraw.Draw(backgroundimage)
        
        #font = ImageFont.truetype("Snow+White.ttf", 50)
        #text = f"Welcome {member.name.capitalize()}!"
        #draw.text((230,350), text, (255, 255, 255), font=font)
        #backgroundimage.save('text.png')
        #await channel.send(file = discord.File("text.png"))
        #Unverified_role = discord.utils.get(member.guild.roles, name="Unverified")
        #await member.add_roles(Unverified_role)
        #if channel is None:
            #print("none?")
            #return
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        Unverified_role = discord.utils.get(member.guild.roles, name="Unverified")
        await member.add_roles(Unverified_role)

    
    
            
            
        
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message
    @commands.command(name="snipe")
    async def snipe(self, ctx: commands.Context):
        
        """A command to snipe deleted msgs"""
        if not self.last_msg:
            await ctx.send('There is no message to snipe!')
            return
        
        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title=f"Message from {author}", description = content)
        await ctx.send(embed=embed)
        
        snipe_list.append(content)
        print(snipe_list)

    



    



    




        
    

   


        

def setup(bot: commands.Bot):
    bot.add_cog(Cool(bot))




    


