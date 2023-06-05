from discord.ext.commands.errors import MissingRequiredArgument
import requests
from discord.ext import commands, tasks
import discord
import asyncio
from datetime import datetime
import random
import time
from typing import Optional
from discord import Member
import re
import json
from decimal import *
from discord.ext.commands import has_permissions, MissingPermissions, Greedy
import pymongo
from pymongo import MongoClient
import ssl
import os



colors = [0xFF3333, 0x761954, 0xc34a17, 0x005073, 0x146f85, 0xbf4055, 0x40bfaa, 0x674d93, 0xf474d0, 0x278d39, 0x9f1616]

icon_list = ["https://media.discordapp.net/attachments/850445045937209365/852944234674913320/blight_1.png", 'https://media.discordapp.net/attachments/850445045937209365/852944263083589672/blight_2.png', "https://media.discordapp.net/attachments/850445045937209365/852944312379637830/blight_3.png", "https://media.discordapp.net/attachments/850445045937209365/852973375885279272/blight-5.png"]

API_KEY = os.environ["API_KEY"]
mongo = os.environ["mongo"]
channel_list = ["what-to-do", "applications", "verify", "portal", "invite-waiting-list", "rules-｡･", "announcements-｡･", "server-roles-｡･", "absences-｡･", "our-history-｡･", "progression-｡･", "pack-updates-｡･", "thought-of-the-day-｡･", "suggestions-｡･", "giveaways-｡･", "bot-reqs", "main-chat", "totd-discussion", "counting", "time-zones-counting", "face-reveals", "drip-check", "art", "pictures", "meme-shit", "bedwars-team", "skywars-team", "duels-team", "in-call-chat", "bot-commands", "sbs-commands", "mee6-level", "groovy-commands", "staff-chat", "project-exodus", "staff-bot-commands", "staff-announcements", "summaries", "rules", "invite-log", "kick-log", "mee6-logs", "staff-work", "mutes-and-warns", "infractions", "gexp-spreadsheets", "quack", "executive-discussion", "carl-logs", "Demonical-discussion", "cute-gifs"]




class ModerativeCommands(commands.Cog):
    """Moderative Commands"""
    def convert(self, time):
        pos = ["s", "m", "h", "d"]
        time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}
        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]
    

    
    import discord

    
    

        



    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None
    @commands.command(name="spam")
    async def spam(self, ctx, member: discord.Member):
        """Only useable by blazing."""
        if str(ctx.author.id) == "587390710974644311":
            while True:
                await ctx.send(f"{member.mention}")
                await asyncio.sleep(1)
        else:
            await ctx.send(f'{ctx.author.mention} dumbo')
        
     

    @commands.command(name="mute", aliases=["Mute", "tempmute", "Tempmute"])
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")
    async def mute_command(self, ctx, member: discord.Member=None, unconvertedtime=None, reason=None):
        """Only useable by staff, mutes a user"""
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        ascended = ctx.author.guild.premium_subscriber_role
        print(ascended)
        try:
            roleids = []
            if member is None:
                
                    
                embed = discord.Embed(title="Mute Command!", description="The ideal way to use this command is ```b!mute [user] [time] [reason]```", colour = random.choice(colors))
                embed.add_field(name="What it does:",value="Using it like this automatically gives them back their roles once the mute is over.", inline=False)
                embed.add_field(name="Improper Way:.",value="You are also able to use the command with just ```b!mute [user]``` though the muted user will not have a reason and you will have to manually add their roles back.", inline=False)
                await ctx.send(embed=embed)
            elif member.top_role >= ctx.author.top_role:
                embed = discord.Embed(title="Failed!", description="You can only moderate members below your role.", colour=random.choice(colors))
                await ctx.send(f"You can only moderate members below your role")         
                return
            
            elif ascended in member.roles:
                
                if unconvertedtime is None:
                    rolenames = [r.name for r  in member.roles]
                
                
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Mute"]
                    collection = db["Mutes"]
                    post = {"_id": member.id, "roles": rolenames}
                    collection.insert_one(post)
                    embed = discord.Embed(title="Muted!", description=f"{member} has been muted indefinitely.")
                    await ctx.send(embed=embed)
                    await member.edit(roles=[ascended])
                    await member.add_roles(muted)
                elif reason is None:
                    rolenames = [r.name for r  in member.roles]
                
                
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Mute"]
                    collection = db["Mutes"]
                    post = {"_id": member.id, "roles": rolenames}
                    time = self.convert(unconvertedtime)
                    collection.insert_one(post)
                    roles1 = member.roles #save the member roles
                    await member.edit(roles=[]) #remove all member roles
                    
                    await member.add_roles(muted)
                    await asyncio.sleep(time)

                    await member.remove_roles(muted)
                    await member.edit(roles=roles1)
                    embed = discord.Embed(title="Muted!", description=f"{member} has been muted for {time}.")
                    await ctx.send(embed=embed)

                else:
                    rolenames = [r.name for r  in member.roles]
                
                
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Mute"]
                    collection = db["Mutes"]
                    post = {"_id": member.id, "roles": rolenames}
                    time = self.convert(unconvertedtime)
                    collection.insert_one(post)
                    time = self.convert(unconvertedtime)
                    print('oi')
                    roles1 = member.roles #save the member roles
                    await member.edit(roles=[ascended]) #remove all member roles
                    
                    await member.add_roles(muted)
                    await asyncio.sleep(time)
                    collection.delete_one({"_id": member.id})
                    await member.remove_roles(muted)
                    await member.edit(roles=roles1)
                    embed = discord.Embed(title="Muted!", description=f"{member} has been muted for {time}.")
                    await ctx.send(embed=embed)
                


            elif unconvertedtime is None:
                rolenames = [r.name for r  in member.roles]
                
                
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Mute"]
                collection = db["Mutes"]
                post = {"_id": member.id, "roles": rolenames}
                collection.insert_one(post)
                embed = discord.Embed(title="Muted!", description=f"{member} has been muted indefinitely.")
                await ctx.send(embed=embed)
                await member.edit(roles=[])
                await member.add_roles(muted)
            elif reason is None:
                rolenames = [r.name for r  in member.roles]
                
                
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Mute"]
                collection = db["Mutes"]
                post = {"_id": member.id, "roles": rolenames}
                time = self.convert(unconvertedtime)
                collection.insert_one(post)

                roles1 = member.roles #save the member roles
                await member.edit(roles=[]) #remove all member roles
                
                await member.add_roles(muted)
                await asyncio.sleep(time)
                await member.remove_roles(muted)
                collection.delete_one({"_id": member.id})
                await member.edit(roles=roles1)
                embed = discord.Embed(title="Muted!", description=f"{member} has been muted for {time}.")
                await ctx.send(embed=embed)

            

            else:
                rolenames = [r.name for r  in member.roles]
                
                
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Mute"]
                collection = db["Mutes"]
                post = {"_id": member.id, "roles": rolenames}
                time = self.convert(unconvertedtime)
                collection.insert_one(post)

                roles1 = member.roles #save the member roles
                await member.edit(roles=[]) #remove all member roles
                
                await member.add_roles(muted)
                await asyncio.sleep(time)
                collection.delete_one({"_id": member.id})

                await member.remove_roles(muted)
                await member.edit(roles=roles1)
                embed = discord.Embed(title="Muted!", description=f"{member} has been muted for {time} for {reason}.")
                await ctx.send(embed=embed)
        except Exception as e:
            print(e)
    @commands.command(name="unmute", aliases=["Unmute"])
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")
    async def unmute(self, ctx, member: discord.Member):
        """Only useable by staff, unmutes a user."""
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        guest = discord.utils.get(ctx.guild.roles, name="Guest")
        if muted in member.roles:
            try:
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Mute"]
                collection = db["Mutes"]
                results = collection.find_one({"_id": member.id})
                roleids = results["roles"]
                print(roleids)
                del roleids[0]
                i = 0
                print(roleids)
                while i < len(roleids):
                    role = discord.utils.get(ctx.guild.roles, name=str(roleids[i]))
                    await member.add_roles(role)
                    i = i + 1
                collection.delete_one({"_id": member.id})
                await member.remove_roles(muted)
                embed = discord.Embed(title="Succeeded!", description=f"{member.display_name} has been unmuted!", colour = discord.Colour.random())
                await ctx.send(embed=embed)
            except Exception as e:
                print(e)

                await member.remove_roles(muted)
                await member.add_roles(guest)
                staffcommands = discord.utils.get(ctx.guild.channels, name="staff-bot-commands")
                await staffcommands.send(ctx.author.mention, delete_after=0.1)
                embed = discord.Embed(title=f"Please manually give {member.display_name.capitalize()} their roles back.", description="This is because you did not give a time limit so we could not automaticall give his roles back.", colour=random.choice(colors))
                await staffcommands.send(embed=embed)
        else:
            embed = discord.Embed(title="User was not muted.", description="If he is missing roles give them back manually.", colour=random.choice(colors))
            staffcommands = discord.utils.get(ctx.guild.channels, name="staff-bot-commands")
            await staffcommands.send(ctx.author.mention, delete_after=0.1)
            await staffcommands.send(embed=embed)
        
    @commands.command(name="pingg")
    async def pingg(self, ctx: commands.Context):
        """Get the bots current API latency"""
        start_time = time.time()
        message = await ctx.send('Testing ping..')
        end_time = time.time()

        await message.edit(content=(f'Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms'))
    @commands.command(name="kick")
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")
    async def kick(self, ctx, member: discord.Member=None, reason=None):
        """Only useable by staff, kicks a user."""
        try:
            if member is None:
                embed = discord.Embed(title="Kick Command!", description="The ideal way to use this command is ```!kick [user] [reason]```")
                embed.add_field(name="What it does:", value="This command will kick the user and DM them the reason, if there is none it will not include the reason.")
                embed.add_field(name="Improper way:", value="You can also just kick the user with ```!kick [user]``` but it would be much easier if you added in a reason for the staff team.")
                await ctx.send(embed=embed)
            elif member.top_role >= ctx.author.top_role:
                embed = discord.Embed(title="Failed!", description="You can only moderate members below your role.", colour=random.choice(colors))
                await ctx.send(f"You can only moderate members below your role")         
                return
            elif reason is None:
                embed = discord.Embed(title=f"You have been kicked from {ctx.guild.name}.", description="Please avoid breaking the rules if you are allowed back in.")
                await member.send(embed=embed)
                await member.kick()
            else:
                embed = discord.Embed(title=f"You have been kicked from {ctx.guild.name}.", description=f"You have been kicked for the reason: ```{reason}```.\nPlease avoid breaking the rules if you are allowed back in.")
                await member.send(embed=embed)
                await member.kick()
        except Exception as e:
            print(e)
    @commands.command(name="ban")
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")
    async def ban(self, ctx, member: discord.Member=None, reason=None):
        """Only useable by staff, bans a user."""
        try:
            if member is None:
                embed = discord.Embed(title="Ban Command!", description="The ideal way to use this command is ```!ban [user] [reason]```", colour=random.choice(colors))
                embed.add_field(name="What it does:", value="This command will ban the user and DM them the reason, if there is none it will not include the reason.")
                embed.add_field(name="Improper way:", value="The command also works with ```!ban [user]``` but it would be much easier for the staff team if you included a reason for the ban.", )
                await ctx.send(embed=embed)
            elif member.top_role >= ctx.author.top_role:
                embed = discord.Embed(title="Failed!", description="You can only moderate members below your role.", colour=random.choice(colors))
                await ctx.send(f"You can only moderate members below your role")         
                return
            elif reason is None:
                embed=discord.Embed(title=f"You have been banned from {ctx.guild.name}.", description="In the low chance you are allowed back in the server avoid breaking __**any**__ rules.", colour=random.choice(colors))
                await member.send(embed=embed)
                await member.ban()
            else:
                embed = discord.Embed(title=f"You have been banned from {ctx.guild.name}.", description=f"You have been banned for the reason: ```{reason}```.\nIn the low chance you are allowed back in the server avoid breaking __**any**__ rules.", colour=random.choice(colors))
                await member.send(embed=embed)
                await member.ban()
        except Exception as e:
            print(e)
    @commands.command(name="unban")
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="Success!", description=f"Unbanned: {user.mention}", colour=random.choice(colors))
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Failed!", description="This user was not banned?", colour=random.choice(colors))
    
    @commands.command(name="member")
    async def member(self, ctx, member: discord.Member):
        print(member.roles)

    

def setup(bot: commands.Bot):
    bot.add_cog(ModerativeCommands(bot))