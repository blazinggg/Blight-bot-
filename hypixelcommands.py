#Importing
from re import T
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE
import os
from discord.ext import commands
import discord
import asyncio
from datetime import datetime
from discord import Member
import random
from decimal import *
from discord.ext.commands import has_permissions, MissingPermissions
import aiohttp
import math

from hypixel import get_data, get_uuid, get_level, get_reqs, check_reqs
import requests

pingdeny = "a"


colors = [0xFF3333, 0x761954, 0xc34a17, 0x005073, 0x146f85, 0xbf4055, 0x40bfaa, 0x674d93, 0xf474d0, 0x278d39, 0x9f1616]


icon_list = ["https://media.discordapp.net/attachments/850445045937209365/852944234674913320/blight_1.png", 'https://media.discordapp.net/attachments/850445045937209365/852944263083589672/blight_2.png', "https://media.discordapp.net/attachments/850445045937209365/852944312379637830/blight_3.png", "https://media.discordapp.net/attachments/850445045937209365/852973375885279272/blight-5.png"]

API_KEY = os.environ['API_KEY']

channel_list = ["what-to-do", "applications", "verify", "portal", "invite-waiting-list", "rules-｡･", "announcements-｡･", "server-roles-｡･", "absences-｡･", "our-history-｡･", "progression-｡･", "pack-updates-｡･", "thought-of-the-day-｡･", "suggestions-｡･", "giveaways-｡･", "bot-reqs", "main-chat", "totd-discussion", "counting", "time-zones-counting", "face-reveals", "drip-check", "art", "pictures", "meme-shit", "bedwars-team", "skywars-team", "duels-team", "in-call-chat", "bot-commands", "sbs-commands", "mee6-level", "groovy-commands", "staff-chat", "project-exodus", "staff-bot-commands", "staff-announcements", "summaries", "rules", "invite-log", "kick-log", "mee6-logs", "staff-work", "mutes-and-warns", "infractions", "gexp-spreadsheets", "quack", "executive-discussion", "carl-logs", "demonical-discussion", "cute-gifs"]



class HypixelCommands(commands.Cog):
    """Hypixel Commands"""
    

    


    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None
   
    
    @commands.command(name="discord")
    async def discord(self, ctx, ign):
        r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}?').json()
        uuid = r['id']
        url_v2 = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
        print(url_v2)
        async with aiohttp.ClientSession() as session:
            baddata = await session.get(url_v2)
            data = await baddata.json()

        social = data["player"]["socialMedia"]["links"]["DISCORD"]
        await ctx.send(str(social))
    
    #Command for recruiters to toggle the "Accepted" role on members    
    @commands.command(name="accepted")
    @commands.has_any_role("Recruiter｡:+*", "Warden｡:+*", "Executive｡:+*", "Demonical｡:+*")
    async def accepted(self, ctx, member: Member):
    #Defining accepted role and stuff
      await ctx.message.delete()
      accepted = discord.utils.get(ctx.guild.roles, name="Accepted")
    #If they already have the accepted role
      if accepted in member.roles:
        await member.remove_roles(accepted)
        embed = discord.Embed(title="**Success!**", description=f"Removed Accepted role from {member.mention}", colour=0xd10a07)
        success = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await success.delete()
      #If they don't  
      else:
        await member.add_roles(accepted)
        embed = discord.Embed(title="**Success!**", description=f"Added Accepted role to {member.mention}", colour=0xd10a07)
        success = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await success.delete()
                
        


    @commands.command(name="void")
    async def void(self, ctx, message):
        """Shows the amount of void deaths of a user in bedwars."""
        
        ign = message

        r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}?').json()
        uuid = r['id']

        url_v2 = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
        print(url_v2)
        async with aiohttp.ClientSession() as session:
            baddata = await session.get(url_v2)
            data = await baddata.json()

        
        stat = data['player']['stats']['Bedwars']['void_deaths_bedwars']
        


        
        
        embed = discord.Embed(title="Not bad", description=f"You've only fallen off {stat} times! Good job!", colour=0xd10a07)
        embed.set_author(name=ign, icon_url="https://cdn.discordapp.com/emojis/821827657637167124.gif")
        await ctx.send(embed=embed)
    @commands.command(name="delete")
    @commands.has_role("Bloozing")
    async def delete(self, ctx):
      for channel in ctx.guild.channels:
        if str(channel.name) == "application-blozo":
          await channel.delete()




        
    @commands.command(name="apply")
    async def apply(self, ctx, username=None):
        """Creates a channel where you can fill out questions for applications"""
        await ctx.message.delete()
        application = discord.utils.get(ctx.guild.channels, name="applications")
        def check(msg):
            return msg.author == ctx.author and msg.channel == channel
        global color
        if username == None: 
            embed = discord.Embed(title="Failed", description="Please enter a valid IGN")
            problem = await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await problem.delete()
            return
        fulluuid = await get_uuid(username)
        if fulluuid.status != 200:
            embed = discord.Embed(title="Failed", description="Please enter a valid IGN")
            await ctx.send(embed=embed)
        else:
            uuid = await fulluuid.json()
            uuid = uuid["id"]
            try:
                global bedwars_star, bedwars_final_death, bedwars_final_kills, bigfkdr, fkdr, index, swkdr, swlevel 
                
                global pingdeny
                pingdeny = ctx.author 
                print(pingdeny)  
                    
                data = await get_data(uuid=uuid)    
                network_experience = data["player"]["networkExp"]
              #Not fixing the indentation from a removed if statement so changed it to something that will always force the else part
                if 1 == 2:
                  return
                else:
                    try:
                        async with aiohttp.ClientSession() as session:
                            bestprofnf = await session.get(f'https://hypixel-api.senither.com/v1/profiles/{uuid}/weight?key={API_KEY}')
                            bestprof = await bestprofnf.json()
                            badweight = bestprof["data"]["weight"]
                            weight = round(badweight, 2)
                    except:
                        weight = 0
                    bedwars_stats, duels_stats = await get_reqs(data=data)
                    # Star, FKDR, Index
                    # Star, KDR
                    # Wins, WLR
                    bedwars_star = bedwars_stats[0]
                    fkdr = bedwars_stats[1]
                    index = bedwars_stats[2]
                    duels_wins = duels_stats[0]
                    duels_wlr = duels_stats[1]

                
                

                    
                    print(fkdr)
                    print(bedwars_star)
                    checkreq = await check_reqs(bedwars_stats, duels_stats)
                    print('Starting gexp section')

                    url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
                    async with aiohttp.ClientSession() as session:
                      response = await session.get(url)
                      bresponse = await response.json()
                      uuid = bresponse['id']
                      print(uuid)
                      await session.close()
                      print('Finished finding uuid')
                    async with aiohttp.ClientSession() as session:
                      async with session.get(f'https://api.hypixel.net/guild?key={API_KEY}&player={uuid}') as req:
                        r = await req.json()
                        print('Found json of guild info')
                        await session.close()
                        if r['guild'] != None:
                          print('Guild was not None')
                          guild = r['guild']['name']
                          print('Finding members')
                          #expHistory = r['guild']['members'][uuid]['expHistory'].values()
                          for i in r['guild']['members']:
                            if i['uuid'] == uuid:
                              member = i
                          expHistory = member['expHistory'].values()
                          exp = sum(expHistory)
                          print(exp)
                          print('Defining "guildInfo"')
                          guildInfo = f'Guild: {guild}\nWeekly Gexp: {exp}'
                          guildresponse = ' Please leave your current guild.'
                        else:
                          print('No guild found')
                          guild = None
                          guildresponse = ''
                          print('Defining "guildInfo"')
                          guildInfo = 'This player is not currently in a guild'
                  
                    if 14 >= 13:
                      if checkreq is True:
                          if 1 == 2:
                              return
                          else:
                              print('bye')
                              #embed = discord.Embed(title="Accepted!", description="Congrats you have been accepted! You have been given the Accepted role and will be pinged when we have open slot.")
                              #await ctx.send(embed=embed)
                              
                              waitinglist = discord.utils.get(ctx.guild.channels, name="invite-waiting-list")
                              print(f"Found waitinglist channel: {waitinglist}")
                              
                              
                              
                              accepted = discord.utils.get(ctx.guild.roles, name="Accepted")               
                            
                              await ctx.author.add_roles(accepted)
                              await waitinglist.send(f"You have been accepted, {ctx.author.mention}.{guildresponse}\nIGN: {username.capitalize()}\nGuild: {guild}")
                          
                      else:
                          warden = discord.utils.get(ctx.guild.roles, name="Warden｡:+*")
                          executive = discord.utils.get(ctx.guild.roles, name="Executive｡:+*")
                          category = discord.utils.get(ctx.guild.categories)
                          application_channel = await ctx.guild.create_text_channel(f"application {username}")
                          await application_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)
                          await application_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
                          await application_channel.set_permissions(executive, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
                          await application_channel.set_permissions(warden, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
                      
                          channel_id = application_channel.id
                          channel = ctx.guild.get_channel(channel_id)
                          embed = discord.Embed(title="Guild application", description=f"As you do not meet requirements, we have made an application channel for you so that staff can confirm whether or not you can join the guild.\n\nUsername: {username}\n\nBedwars stats: {bedwars_star} stars, {fkdr} FKDR, {index} index\n\nDuels stats: {duels_wins} wins, {duels_wlr} WLR\n\n{guildInfo}")
                          await application_channel.send(ctx.author.mention)
                          await application_channel.send(embed=embed)
                    else:
                        warden = discord.utils.get(ctx.guild.roles, name="Warden｡:+*")
                        executive = discord.utils.get(ctx.guild.roles, name="Executive｡:+*")
                        category = discord.utils.get(ctx.guild.categories)
                        application_channel = await ctx.guild.create_text_channel(f"application {username}")
                        await application_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)
                        await application_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
                        await application_channel.set_permissions(executive, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
                        await application_channel.set_permissions(warden, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
                        channel_id = application_channel.id
                        channel = ctx.guild.get_channel(channel_id)
                        embed = discord.Embed(title="Guild Application", description=f"As you do not meet requirements, we have made an application channel for you so that staff can confirm whether or not you can join the guild.\n\nUsername: {username}\n\nBedwars stats: {bedwars_star} stars, {fkdr} FKDR, {index} index.\n\nDuels stats: {duels_wins} wins, {duels_wlr} WLR\n\n{guildInfo}")
                        await application_channel.send(ctx.author.mention)
                        await application_channel.send(embed=embed)
                        
                        


            except Exception as e:
                print(e)
                embed = discord.Embed(title="Failed", description="Something went wrong, make sure you inputted everything right!, try again or contact a staff")
                await ctx.send(embed=embed)
                #await asyncio.sleep(120)
                #await application_channel.delete()
        
            
        
            
        
            
        
    
        

        
    @commands.command(name="deny")
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")
    

    async def deny(self, ctx):
        """Only useable by staff, denies an application."""
        
        permcolor = discord.Colour.random()
        print(str(ctx.message.channel))
        
        
        if str(ctx.message.channel) not in channel_list:
            
            embed = discord.Embed(title="Denied!", description="Apologies, you have not been accepted.", colour=discord.Colour.random())
            await ctx.send(embed=embed)
            reply = await self.bot.wait_for('message')
            
            print(reply.content)
            print(reply.author)
            await asyncio.sleep(10)
            print('Deleting channel!')
            await ctx.channel.delete()
        
               
           

                
        
               
        else:
            staffchat = ctx.guild.get_channel(852971000346050594)  
            await staffchat.send(f"{ctx.author.mention} That is not a channel you can use the command 'deny' in.")  
    @commands.command(name="deletechannel", aliases=["dc", "channeldelete"])  
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")

    async def deletechannel(self, ctx):
        """Deleting a channel if its not a main channel."""

        if str(ctx.message.channel) not in channel_list:
            print('Deleting channel!')
            await ctx.channel.delete()
        else:
            staffchat = ctx.guild.get_channel(852971000346050594)  
            await staffchat.send(f"{ctx.author.mention} That is not a channel you can use the command 'deletechannel' in.") 

              
              
    @commands.command(name="accept")
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")

    async def accept(self, ctx, *, ign=None):
        """Accepts an application."""
        
        permcolor = discord.Colour.random()
        
        accepted = discord.utils.get(ctx.guild.roles, name="Accepted")
        
        channel_list = ["what-to-do", "applications", "verify", "portal", "invite-waiting-list", "rules-｡･", "announcements-｡･", "server-roles-｡･", "absences-｡･", "our-history-｡･", "progression-｡･", "pack-updates-｡･", "thought-of-the-day-｡･", "suggestions-｡･", "giveaways-｡･", "bot-reqs", "main-chat", "totd-discussion", "counting", "time-zones-counting", "face-reveals", "drip-check", "art", "pictures", "meme-shit", "bedwars-team", "skywars-team", "duels-team", "in-call-chat", "bot-commands", "sbs-commands", "mee6-level", "groovy-commands", "staff-chat", "project-exodus", "staff-bot-commands", "staff-announcements", "summaries", "rules", "invite-log", "kick-log", "mee6-logs", "staff-work", "mutes-and-warns", "infractions", "gexp-spreadsheets", "quack", "executive-discussion", "carl-logs", "demonical-discussion", "cute-gifs"]
        if ign is None:
            print('oi')
            if str(ctx.message.channel) not in channel_list:
                def check(message):
                    return message.content.lower() == "yes"
                print()
                logs = discord.utils.get(ctx.guild.channels, name="blight-bot-logs")
                await logs.send(f'{ctx.author.mention} Since you did not specify the IGN of the user you are accepting please make sure to manually add them, for future notice please specify them as it is more convienient and looks better.')
                embed = discord.Embed(title="Accepted!", description="Congrats you have been accepted! You have been given the Accepted role and will be pinged when we have open slots.", colour=permcolor)
                await ctx.send(embed=embed)

                #reply = await self.bot.wait_for('message', check=check)
                
                
                
                #x = reply.author
                #print(x)
                await pingdeny.add_roles(accepted)
                await asyncio.sleep(10)
                print('deleting!')
                await ctx.channel.delete()
            else: 
                staffchat = discord.utils.get(ctx.guild.channels, name="staff-chat")
                await staffchat.send(f"{ctx.author.mention} That is not a channel you can use the command 'accept' in.")
        else:
            try:
                if str(ctx.message.channel) not in channel_list:
                    print('bye')
                    embed = discord.Embed(title="Accepted!", description="Congrats you have been accepted! You have been given the Accepted role and will be pinged when we have open slots. **This Channel will be closed in 10 seconds!**", colour=permcolor)
                    await ctx.send(embed=embed)
                    #reply = await self.bot.wait_for('message')
                    waitinglist = discord.utils.get(ctx.guild.channels, name="invite-waiting-list")
                    url = f'https://api.mojang.com/users/profiles/minecraft/{ign}?'
                    async with aiohttp.ClientSession() as session:
                      response = await session.get(url)
                      bresponse = await response.json()
                      uuid = bresponse['id']
                      print(uuid)
                      await session.close()
                      print('Finished finding uuid')
                    async with aiohttp.ClientSession() as session:
                      async with session.get(f'https://api.hypixel.net/guild?key={API_KEY}&player={uuid}') as req:
                        r = await req.json()
                        print('Found json of guild info')
                        await session.close()
                        if r['guild'] != None:
                          guild = r['guild']['name']
                          guildmsg = ' Please leave your current guild.'
                        else:
                          guild = 'None'
                          guildmsg = ''
                          
                          
                    
                    await waitinglist.send(f"You have been accepted, {pingdeny.mention}.{guildmsg}\nIGN: {ign.capitalize()}\nGuild: {guild}")
                    
                    
                    #x = reply.author
                    #print(x)
                    await pingdeny.add_roles(accepted)
                    await asyncio.sleep(10)
                    print('deleting!')
                    await ctx.channel.delete()

                else: 
                    staffchat = discord.utils.get(ctx.guild.channels, name="staff-chat")
                    await staffchat.send(f"{ctx.author.mention} That is not a channel you can use the command 'accept' in.")
            except Exception as e:
                print(e)
                
            
                    
                    
            
                
            
                
            
                                                                                                         

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        
      
        if str(after.id) == "578672290510667786":
            trusted = discord.utils.get(after.guild.roles, name="Trusted")
            if trusted in after.roles:
                await asyncio.sleep(300)
                await after.remove_roles(trusted)
        
        
    @commands.command(name="verify")
    async def verify(self, ctx, *, IGN):
        """Verifies a user and gives them their guild roles."""
        
    
        try:
            url = f'https://api.mojang.com/users/profiles/minecraft/{IGN}?'
            async with aiohttp.ClientSession() as session:
                response = await session.get(url)
                bresponse = await response.json()
            uuid = bresponse['id']
            bettername = bresponse['name']
            
            url = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
            print(url)
            async with aiohttp.ClientSession() as session:
                baddata = await session.get(url)
                data = await baddata.json()
                stat = data["player"]["socialMedia"]["links"]["DISCORD"]
            
            name = str(ctx.author)

            
            
            

            
            
            statv2 = str(stat)
            aerial = discord.utils.get(ctx.guild.roles, name="Aerial")
            Unverified = discord.utils.get(ctx.guild.roles, name="Unverified")
            guest = discord.utils.get(ctx.guild.roles, name="Guest")
            warden = discord.utils.get(ctx.guild.roles, name="Warden｡:+*")
            mvp = discord.utils.get(ctx.guild.roles, name="MVP｡:+*")
            executive = discord.utils.get(ctx.guild.roles, name="Executive｡:+*")
            recruiter= discord.utils.get(ctx.guild.roles, name="Recruiter")

            if name==statv2:
                if statv2=="blozo#1918":
                    demonical = discord.utils.get(ctx.guild.roles, name="Demonical｡:+*")
                    await ctx.author.add_roles(demonical)
                else:
                    pass
                await ctx.author.edit(nick=bettername)
                
                async with aiohttp.ClientSession() as session:
                    baddata = await session.get(f"https://api.hypixel.net/guild?key={API_KEY}&player={uuid}")
                    data = await baddata.json()
                if data["guild"] is None or data["guild"]["name"]!='Blight':
                    await ctx.author.add_roles(guest)
                    
                    await ctx.author.remove_roles(Unverified)
                    embed = discord.Embed(title="Verified", description=f"You have been verified and given Guest because you are not in the guild.", colour=discord.Colour.random())
                    await ctx.send(embed=embed)
                    if aerial in ctx.author.roles:
                        await ctx.author.remove_roles(aerial)
                    if mvp in ctx.author.roles:
                        await ctx.author.remove_roles(aerial, mvp)
                    if warden in ctx.author.roles:
                        await ctx.author.remove_roles(aerial, mvp, warden)
                    if executive in ctx.author.roles:
                        await ctx.author.remove_roles(aerial, mvp, warden, executive)
                else:
                    for member in data["guild"]["members"]:
                        if member["uuid"] == uuid.replace("-",""):
                            rank = member["rank"]
                            formatted_rank = str(rank)
                            if formatted_rank == "Aerial":
                                await ctx.author.add_roles(aerial)
                                await ctx.author.remove_roles(Unverified)
                                embed = discord.Embed(title="Verified!", description=f"You have been verified and given the role {formatted_rank}.", colour=discord.Colour.random())
                                await ctx.send(embed=embed)
                            elif formatted_rank == "MVP":
                                await ctx.author.add_roles(mvp)
                                await ctx.author.add_roles(aerial)
                                await ctx.author.remove_roles(guest)
                                await ctx.author.remove_roles(Unverified)
                                embed = discord.Embed(title="Verified!", description=f"You have been verified and given the role {formatted_rank}.", colour=discord.Colour.random())
                                await ctx.send(embed=embed)
                            elif formatted_rank == "Warden":
                                await ctx.author.add_roles(warden)
                                await ctx.author.add_roles(aerial)
                                await ctx.author.remove_roles(guest)
                                await ctx.author.remove_roles(Unverified)
                                embed = discord.Embed(title="Verified!", description=f"You have been verified and given the role {formatted_rank}.", colour=discord.Colour.random())
                                await ctx.send(embed=embed)
                            elif formatted_rank == "Recruiter":
                                await ctx.author.add_roles(recruiter)
                                await ctx.author.add_roles(aerial)
                                await ctx.author.remove_roles(guest)
                                await ctx.author.remove_roles(Unverified)
                                embed = discord.Embed(title="Verified!", description=f"You have been verified and given the role {formatted_rank}.", colour=discord.Colour.random())
                                await ctx.send(embed=embed)
                            else:
                                return
            else:
                embed = discord.Embed(title="Failed!", description="Please verify your hypixel account with your discord account.", color = discord.Colour.random())
                await ctx.send(embed=embed)
        except(KeyError):
            embed = discord.Embed(title="Failed!", description="An error occured, make sure you inputted the right IGN.", colour=discord.Colour.random())
            await ctx.send(embed=embed)
            return
   
    @commands.command(name="inactive", aliases=["kicklist", "ia"])
    @commands.has_any_role("Warden｡:+*", "Executive｡:+*", "Bloozing", "Demonical｡:+*")

    async def inactive(self, ctx):
        """Shows a list and percentage of people who don't make blight reqs."""
        try:
            
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.hypixel.net/guild?key={API_KEY}&name=Blight') as req:
                    req = await req.json()
                    await session.close()
            array = {}
            exp = 0
            async with ctx.channel.typing():
                for i in range(len(req['guild']['members'])):
                    uuid = req['guild']['members'][i]['uuid']
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}') as names:
                            names = await names.json()
                    
                    
                    name = names['name'] + f" [{req['guild']['members'][i]['rank']}]"
                    expHistory = sum(req['guild']['members'][i]['expHistory'].values())
                    exp += expHistory
                    array[name] = exp
                    exp = 0


            
                sortedList = sorted(array.items(), key=lambda x: x[1], reverse=True)
                i = 0
                badkicklist = []
                bettertuple = sortedList[i]
                gexp = [bettertuple[1] for bettertuple in sortedList]
                members = [bettertuple[0] for bettertuple in sortedList]
                print(len(gexp))
                i = 0
                p = 0
                
                
                while i < len(gexp):
                    if gexp[i] < 100000:
                        badkicklist.append(f"**{members[i]}** ``{int(gexp[i])}``")
                        p = p + 1
                        i = i + 1
                    else:
                        i = i + 1
                
                iabaddecimal = p/len(gexp)
                iadecimal = round(iabaddecimal, 2)
                ia = "{:.0%}". format(iadecimal)
                ehkicklist = str(badkicklist)
                eeekicklist = ehkicklist.replace("'", "")
                betterlike = eeekicklist.replace(",", "\n")
                kicklist = betterlike[1:-1]
                

                
                embed = discord.Embed(title=f"{ia} Inactivite", description=f"{kicklist}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
                
         
        except Exception as e:
            print(e)
        
    @commands.command(name="gamereqs", aliases=["GameReqs", "Gamerequirements", "gamerequirements", "gq"])
    @commands.cooldown(rate=1, per=3600)
    async def gamereqs(self, ctx):
        def sw_xp_to_lvl(xp):
            xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
            if xp >= 15000:
                return (xp - 15000) / 10000. + 12
            else:
                for i in range(len(xps)):
                    if xp < xps[i]:
                        return i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])
        print('oi')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.hypixel.net/guild?key={API_KEY}&name=Blight') as req:
                req = await req.json()
                await session.close()
            array = {}
            exp = 0
            uuid = []
            rawgamereqs = []
            i = 0
            for count in range(len(req['guild']['members'])):
                uuid.append(req['guild']['members'][count]['uuid'])
            print(uuid)
            while i < len(uuid):
                    
                        
                    
                    async with aiohttp.ClientSession() as session:
                        baddata = await session.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid[i]}")
                        data = await baddata.json()
                    pp, ppp = await get_reqs(data)
                    
                    bedwars_star = pp[0]
                    fkdr = pp[1]
                    index = pp[2]
                    duelswins = ppp[0]
                    duelswlr = ppp[1]
                    if index >= 650 and int(bedwars_star) >= 150 and float(fkdr) >= float(1) and duelswins >= 1000 and duelswlr >= 1:
                        async with aiohttp.ClientSession() as session:
                            badname = await session.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid[i]}")
                            ewname = await badname.json()
                            name = ewname["name"]
                        i = i + 1
                        await asyncio.sleep(5)
                    elif index>= 1000 and int(bedwars_star) >= 150 and float(fkdr)>=float(1):
                        async with aiohttp.ClientSession() as session:
                            badname = await session.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid[i]}")
                            ewname = await badname.json()
                            name = ewname["name"]
                        i = i + 1
                        await asyncio.sleep(5)

                        
                    
                        
                        
                    else:
                        
                        
                        async with aiohttp.ClientSession() as session:
                            badname = await session.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid[i]}")
                            ewname = await badname.json()
                            name = ewname["name"]
                            await asyncio.sleep(5)
                        
                        rawgamereqs.append(f"**{name}**")
                        i = i + 1
                    
                    
                    
            ehgamereqs = str(rawgamereqs)
            eeegamereqs = ehgamereqs.replace("'", "")
            bettergamereqs = eeegamereqs.replace(",", "\n")
            gamereqs = bettergamereqs[1:-1]
            embed = discord.Embed(title="Gamereqs", description=f"{gamereqs}", colour = discord.Colour.random())
            await ctx.send(embed=embed)
            
    @commands.command(name="check", aliases=["ch", "chgq"])
    @commands.cooldown(rate=1, per=10)
    async def check(self, ctx, IGN = None):
        def sw_xp_to_lvl(xp):
            xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
            if xp >= 15000:
                return (xp - 15000) / 10000. + 12
            else:
                for i in range(len(xps)):
                    if xp < xps[i]:
                        return i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])
        if IGN is None:
            embed = discord.Embed(title="Checking Requirements!", description="There are multiple ways to do this (b!ch <IGN>, b!chgq <IGN>, b!check <IGN>) but for all of them you have to make sure to include the IGN parameter.")
            await ctx.send(embed=embed)
        else:
            url = f'https://api.mojang.com/users/profiles/minecraft/{IGN}?'
            async with aiohttp.ClientSession() as session:
                response = await session.get(url)
                bresponse = await response.json()
            uuid = bresponse['id']
            async with aiohttp.ClientSession() as session:
                baddata = await session.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}")
                data = await baddata.json()
            rqo, rqt = await get_reqs(data)
            chrq = await check_reqs(rqo, rqt)
            if chrq == True:
                await ctx.send("This player makes requirements!")
            else:
                await ctx.send("This player does not make requirements!")
              
            
            

    @commands.command(name="invited", aliases=["Log", "log", "invite", "Invited", "Invite"])
    @commands.has_any_role("Recruiter｡:+*", "Warden｡:+*", "Executive｡:+*", "Demonical｡:+*")
    async def invited(self, ctx, member):
        await ctx.message.delete()
      
        url = f'https://api.mojang.com/users/profiles/minecraft/{member}?'
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            bresponse = await response.json()
            uuid = bresponse['id']
            async with aiohttp.ClientSession() as session:
              baddata = await session.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}")
              data = await baddata.json()
              rqo, rqt = await get_reqs(data)
              chrq = await check_reqs(rqo, rqt)
              invited_channel = self.bot.get_channel(733166354764660767)
              if chrq == True:
                await invited_channel.send(f'`{member}` was invited by {ctx.author.mention} :white_check_mark:\n`Reminder:` This command is not automatic, please run `b!invited` to log your invites')
              else:
                await invited_channel.send(f'`{member}` was invited by {ctx.author.mention} :x:\n`Reminder:` This command is not automatic, please run `b!invited` to log your invites')




                

            
            
    @commands.command(name="requirements", aliases=["r", "reqs"])
    async def requirements(self, ctx):
        embed = discord.Embed(title="**Game Requirements**", description="**__Overall__**\n150+ Bedwars Stars and 1 FKDR + 1 of the following options\n\n__Option 1__\n1000+ Index\n\n__Option 2__\n650+ Index\n2000 Duels Wins\n1 Duels WLR\n\n\nINDEX = STARS x FKDR²", colour = discord.Colour.random())
        await ctx.send(embed=embed)
    

        

           
        
      
                    
                        
                    
                    
            
                

               
                        
        


        
        
            
    

        

            

       


        


   

        
        
    
        


         
        
        





        
        
        
        
        

        
        

        

def setup(bot: commands.Bot):
    bot.add_cog(HypixelCommands(bot))
        




