from aiohttp import ClientSession
import discord
import requests
from discord.ext import commands
import random
import os
import asyncio
import json
import io
import contextlib
import datetime
import aiohttp




async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cat")
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat') # Make a request
            dogjson = await request.json() # Convert it to a JSON dictionary
        embed = discord.Embed(title="Cat!", color=discord.Color.purple()) # Create embed
        embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
        await ctx.send(embed=embed) # Send the embed
    
    @commands.command(name="rpanda")
    async def rpanda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/red_panda') # Make a request
            dogjson = await request.json() # Convert it to a JSON dictionary
        embed = discord.Embed(title="Red Panda!", color=discord.Color.purple()) # Create embed
        embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
        await ctx.send(embed=embed) # Send the embed
      
    @commands.command(name="panda")
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/panda') # Make a request
            dogjson = await request.json() # Convert it to a JSON dictionary
        embed = discord.Embed(title="Panda", color=discord.Color.purple()) # Create embed
        embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
        await ctx.send(embed=embed) # Send the embed
      
    @commands.command(name="bird")
    async def Bird(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/birb') # Make a request
            dogjson = await request.json() # Convert it to a JSON dictionary
        embed = discord.Embed(title="Bird", color=discord.Color.purple()) # Create embed
        embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
        await ctx.send(embed=embed) # Send the embed
    @commands.command(name="koala")
    async def koala(self, ctx): 
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/koala') # Make a request
            dogjson = await request.json() # Convert it to a JSON dictionary
        embed = discord.Embed(title="Koala", color=discord.Color.purple()) # Create embed
        embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
        await ctx.send(embed=embed) # Send the embed
    
    @commands.command(name="duck")
    async def duck(self, ctx):

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://random-d.uk/api/random') # Make a request
            dogjson = await request.json() # Convert it to a JSON dictionary
        embed = discord.Embed(title="Duck!", color=discord.Color.purple()) # Create embed
        embed.set_image(url=dogjson['url']) # Set the embed image to the value of the 'link' key
        await ctx.send(embed=embed) # Send the embed
    @commands.command(name="fart")
    async def fart(self, ctx):
      embed = discord.Embed(title="ewww", description=f"Ewwww {ctx.author.name} farted!")
      await ctx.send(embed=embed)

    @commands.command(name="penguin")
    @commands.cooldown(rate=1, per=2)
    async def penguin(self, ctx: commands.Context):
        variable = ["https://media.discordapp.net/attachments/862873875082379347/863840280968953856/adorable-baby-penguins.png?width=483&height=676",
        "https://media.discordapp.net/attachments/862873875082379347/863840230859341834/entertainment-2013-11-penguins-5-main.png?width=1014&height=676",
        "https://media.discordapp.net/attachments/862873875082379347/863840181924003860/6eaf86e60f5d9450d2372eaa65b5b3fc.png?width=712&height=676",
        "https://media.discordapp.net/attachments/862873875082379347/863840140237864990/gy6mkbk5ffk61.png?width=450&height=676",
        "https://cms.hostelbookers.com/hbblog/wp-content/uploads/sites/3/2011/11/Macaroni-penguin-e1321612212491.jpg",
        "http://www.awesomelycute.com/gallery/2015/05/cute-baby-penguin-8.jpg",
        "https://external-preview.redd.it/A9Kme6x7dAoHZZ2Y6mg7KIAFMyJaZ0_o2brmjfAdoTk.jpg?auto=webp&s=b19dc5b45613af90e6b5b319d5d3ad45fcb06cd1",
        "https://images.unsplash.com/photo-1602587365437-5d02d274b3cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8OHx8fGVufDB8fHx8&w=1000&q=80",
        "https://img.designswan.com/2013/04/penguin/4.jpg",
        "https://becausebirds.com/wp-content/uploads/2015/03/penguin-waddle.jpg",
        "https://us.123rf.com/450wm/antantarctic/antantarctic1508/antantarctic150800017/44230587-three-emperor-penguin-chicks-together.jpg?ver=6",
        "https://www.wildrepublic.com/wp-content/uploads/2018/11/Penguin-Walking-xl-600x404.jpg",
        "https://ichef.bbci.co.uk/news/976/cpsprodpb/146EC/production/_115229638_gettyimages-603118336-gentoo-antarcticpeninsula.jpg"]
        embed = discord.Embed(title="Here u go!", color=discord.Color.light_gray())
        embed.set_image(url=random.choice(variable))
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Fun(bot))