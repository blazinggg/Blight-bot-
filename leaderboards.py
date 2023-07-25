from json.decoder import JSONDecodeError
from discord.ext import commands, tasks
import discord
import PIL
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import asyncio
import aiohttp
from pymongo import MongoClient
import pprint
import ssl
import random
import os
APIKEY = os.environ["API_KEY"]
mongo = os.environ["mongo"]



class Leaderboard(commands.Cog):
    """A cog for global error handling."""
    APIKEY = os.environ["API_KEY"]



    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.myloop.start()
        self.loop.start()
    i = 0
    
    @commands.command(name="lb")
    async def lb(self, ctx, arg=None, arg2=None, arg3=None):
        if arg is None:
            embed = discord.Embed(title="Please use the proper arguments", description="""**Bedwars:**
            b!lb bw star
            b!lb bw fkdr
            b!lb bw wins
            b!lb bw finals
            b!lb bw wlr
            b!lb bw index
            **Skywars:**
            b!lb sw kills
            b!lb sw kdr
            b!lb sw wins
            b!lb sw star
            **Duels:**
            b!lb duel kdr
            b!lb duel kill
            b!lb duel wlr
            b!lb duel win
            """)
            await ctx.send(embed=embed)
        elif str(arg.lower()) == "bw" or str(arg.lower()) =="b":
            if arg2 is None:
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Bedwars"]
                collection = db["Stars"]

                results = collection.find_one({"_id": 1})
                players = results["players"]
                stars = results["stars"]

                embed = discord.Embed(title="Bedwars Star Leaderboard", description=f"**{players[0]}**: {stars[0]}\n**{players[1]}**: {stars[1]}\n**{players[2]}**: {stars[2]}\n**{players[3]}**: {stars[3]}\n**{players[4]}**: {stars[4]}\n**{players[5]}**: {stars[5]}\n**{players[6]}**: {stars[6]}\n**{players[7]}**: {stars[7]}\n**{players[8]}**: {stars[8]}\n**{players[9]}**: {stars[9]}", colour = discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "star" or str(arg2.lower()) == "s":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Bedwars Leaderboard.png"))                
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Bedwars"]
                    collection = db["Stars"]

                    results = collection.find_one({"_id": 1})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Bedwars Star Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "fkdr" or str(arg2.lower()) == "fk" or str(arg2.lower()) == "fkd":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Bedwars FKDR Leaderboard.png"))                
                    
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Bedwars"]
                    collection = db["FKDR"]

                    results = collection.find_one({"_id": 2})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Bedwars FKDR Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "index" or str(arg2.lower()) == "i":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Bedwars Index Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Bedwars"]
                    collection = db["Index"]

                    results = collection.find_one({"_id": 3})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Bedwars Index Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "wins" or str(arg2.lower()) == "w" or str(arg2.lower()) == "win":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Bedwars Wins Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Bedwars"]
                    collection = db["Wins"]

                    results = collection.find_one({"_id": 5})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Bedwars Wins Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "finals" or str(arg2.lower()) == "final" or str(arg2.lower()) == "f":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Bedwars Finals Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Bedwars"]
                    collection = db["Finals"]

                    results = collection.find_one({"_id":4})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Bedwars Wins Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "wlr" or str(arg2.lower()) == "wl":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Bedwars WLR Leaderboard.png"))
                else:
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db = cluster["Bedwars"]
                    collection = db["WLR"]

                    results = collection.find_one({"_id":6})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Bedwars WLR Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)

            else:
                await ctx.send(file=discord.File("./Files/Bedwars Leaderboard.png"))                

        elif str(arg.lower()) == "sw" or str(arg.lower()) == "s":
            if str(arg2.lower()) == "star" or str(arg2.lower()) == "s":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Skywars Star Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Skywars"]
                    collection = db["Stars"]

                    results = collection.find_one({"_id":7})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Skywars Stars Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "kdr" or str(arg2.lower()) == "kd":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Skywars KDR Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Skywars"]
                    collection = db["KDR"]

                    results = collection.find_one({"_id":10})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Skywars KDR Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "kills" or str(arg2.lower()) == "kill" or str(arg2.lower()) == "k":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Skywars Kills Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Skywars"]
                    collection = db["Kills"]

                    results = collection.find_one({"_id":9})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Skywars Kill Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "wins" or str(arg2.lower()) == "win" or str(arg2.lower()) == "w":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Skywars Wins Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Skywars"]
                    collection = db["Wins"]

                    results = collection.find_one({"_id":8})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Skywars Kill Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
        elif str(arg.lower()) == "d" or str(arg.lower()) == "duels" or str(arg.lower()) == "duel":
            if str(arg2.lower()) == "kdr" or str(arg2.lower()) == "kd":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Duels KDR Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Duels"]
                    collection = db["KDR"]

                    results = collection.find_one({"_id":12})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Duels KDR Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "kills" or str(arg2.lower()) == "kill" or str(arg2.lower()) == "k":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Duels Kills Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Duels"]
                    collection = db["Kills"]

                    results = collection.find_one({"_id":11})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Duels Kills Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "wlr" or str(arg2.lower()) == "wl" or str(arg2.lower()) == "wlrs":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Duels WLR Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Duels"]
                    collection = db["WLR"]

                    results = collection.find_one({"_id":13})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Duels WLR Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) == "win" or str(arg2.lower()) == "wins" or str(arg2.lower()) == "w":
                if arg3 is None:
                    await ctx.send(file=discord.File("./Files/Duels Wins Leaderboard.png"))
                elif str(arg3.lower()) == "all" or str(arg3.lower()) == "a":
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Duels"]
                    collection = db["Wins"]

                    results = collection.find_one({"_id":14})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Duels Wins Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)
            elif str(arg2.lower()) =="bridge_win" or str(arg2.lower()) == "bridge_wins" or str(arg2.lower()) == "bw":
              if arg3 is None:
                await ctx.send(file=discord.File("./Files/Bridge Wins Leaderboard.png"))
              elif str(arg3.lower() == "all" or str(arg3.lower()) == "a"):
                    cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                    db= cluster["Duels"]
                    collection = db["Bridge Wins"]

                    results = collection.find_one({"_id":15})
                    both = str(results["both"])
                    both = both.replace("[", "")
                    both = both.replace("]", "")
                    both = both.replace("'", "")
                    both = both.replace(",", "")
                    both = both.replace(":", "\n")
                    embed = discord.Embed(title="Full Bridge Wins Leaderboard", description=both, colour = discord.Colour.random())
                    await ctx.send(embed=embed)






            
    @tasks.loop(minutes=5)  
    async def loop(self):
        cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
        db= cluster["Bedwars"]
        collection = db["Stars"]

        results = collection.find_one({"_id": 1})
        badplayers = results["players"]
        stars = results["stars"]
        colors = results["colors"]
        players = [s.replace("*", "") for s in badplayers]

        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Star Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Star Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{stars[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{stars[0]}", (colors[0][0], colors[0][1], colors[0][2]), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{stars[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{stars[1]}", (colors[1][0], colors[1][1], colors[1][2]), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{stars[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{stars[2]}", (colors[2][0], colors[2][1], colors[2][2]), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{stars[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{stars[3]}", (colors[3][0], colors[3][1], colors[3][2]), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{stars[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{stars[4]}", (colors[4][0], colors[4][1], colors[4][2]), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{stars[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{stars[5]}", (colors[5][0], colors[5][1], colors[5][2]), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{stars[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{stars[6]}", (colors[6][0], colors[6][1], colors[6][2]), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{stars[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{stars[7]}", (colors[7][0], colors[7][1], colors[7][2]), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{stars[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{stars[8]}", (colors[8][0], colors[8][1], colors[8][2]), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{stars[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{stars[9]}", (colors[9][0], colors[9][1], colors[9][2]), font=font)
        randmap.save("./Files/Bedwars Leaderboard.png")
        cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
        db= cluster["Bedwars"]
        collection = db["FKDR"]

        results = collection.find_one({"_id": 2})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        (139, 0 ,0)
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight FKDR Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight FKDR Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
        randmap.save("./Files/Bedwars FKDR Leaderboard.png")
        print("yes")
        db = cluster["Skywars"]
        collection = db["Stars"]
        results = collection.find_one({"_id": 7})
        badplayers = results["players"]
        players = [s.replace("*", "") for s in badplayers]
        colors = results["colors"]
        stars = results["stars"]

        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 48)
        draw.text((60, 100), "Blight Sw Star Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Sw Star Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{int(stars[0])}", (0,0,0), font=font)
        draw.text((650,230), f"{int(stars[0])}", (colors[0][0], colors[0][1], colors[0][2]), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{int(stars[1])}", (0,0,0), font=font)
        draw.text((650,295), f"{int(stars[1])}", (colors[1][0], colors[1][1], colors[1][2]), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{int(stars[2])}", (0,0,0), font=font)
        draw.text((650,360), f"{int(stars[2])}", (colors[2][0], colors[2][1], colors[2][2]), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{int(stars[3])}", (0,0,0), font=font)
        draw.text((650,425), f"{int(stars[3])}", (colors[3][0], colors[3][1], colors[3][2]), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{int(stars[4])}", (0,0,0), font=font)
        draw.text((650,490), f"{int(stars[4])}", (colors[4][0], colors[4][1], colors[4][2]), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{int(stars[5])}", (0,0,0), font=font)
        draw.text((650,555), f"{int(stars[5])}", (colors[5][0], colors[5][1], colors[5][2]), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{int(stars[6])}", (0,0,0), font=font)
        draw.text((650,620), f"{int(stars[6])}", (colors[6][0], colors[6][1], colors[6][2]), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{int(stars[7])}", (0,0,0), font=font)
        draw.text((650,685), f"{int(stars[7])}", (colors[7][0], colors[7][1], colors[7][2]), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{int(stars[8])}", (0,0,0), font=font)
        draw.text((650,750), f"{int(stars[8])}", (colors[8][0], colors[8][1], colors[8][2]), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{int(stars[9])}", (0,0,0), font=font)
        draw.text((650,820), f"{int(stars[9])}", (colors[9][0], colors[9][1], colors[9][2]), font=font)
        randmap.save("./Files/Skywars Star Leaderboard.png")
        db= cluster["Bedwars"]
        collection = db["Index"]

        results = collection.find_one({"_id": 3})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Index Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Index Leaderboard", (36, 157, 159), font=font)        
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{int(fkdrs[0])}", (0,0,0), font=font)
        draw.text((650,230), f"{int(fkdrs[0])}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{int(fkdrs[1])}", (0,0,0), font=font)
        draw.text((650,295), f"{int(fkdrs[1])}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{int(fkdrs[2])}", (0,0,0), font=font)
        draw.text((650,360), f"{int(fkdrs[2])}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{int(fkdrs[3])}", (0,0,0), font=font)
        draw.text((650,425), f"{int(fkdrs[3])}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{int(fkdrs[4])}", (0,0,0), font=font)
        draw.text((650,490), f"{int(fkdrs[4])}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{int(fkdrs[5])}", (0,0,0), font=font)
        draw.text((650,555), f"{int(fkdrs[5])}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{int(fkdrs[6])}", (0,0,0), font=font)
        draw.text((650,620), f"{int(fkdrs[6])}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{int(fkdrs[7])}", (0,0,0), font=font)
        draw.text((650,685), f"{int(fkdrs[7])}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{int(fkdrs[8])}", (0,0,0), font=font)
        draw.text((650,750), f"{int(fkdrs[8])}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{int(fkdrs[9])}", (0,0,0), font=font)
        draw.text((650,820), f"{int(fkdrs[9])}", (139, 0 ,0), font=font)
        randmap.save("./Files/Bedwars Index Leaderboard.png")
        db= cluster["Bedwars"]
        collection = db["Wins"]

        results = collection.find_one({"_id": 5})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Wins Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Wins Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Bedwars Wins Leaderboard.png")
        db= cluster["Bedwars"]
        collection = db["Finals"]

        results = collection.find_one({"_id": 4})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Finals Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Finals Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Bedwars Finals Leaderboard.png")
        db= cluster["Bedwars"]
        collection = db["WLR"]

        results = collection.find_one({"_id": 6})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight WLR Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight WLR Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Bedwars WLR Leaderboard.png")
        db= cluster["Skywars"]
        collection = db["KDR"]

        results = collection.find_one({"_id": 10})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Sw KDR Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Sw KDR Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Skywars KDR Leaderboard.png")
        db= cluster["Skywars"]
        collection = db["Kills"]

        results = collection.find_one({"_id": 9})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Sw Kills Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Sw Kills Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Skywars Kills Leaderboard.png")
        db= cluster["Skywars"]
        collection = db["Wins"]

        results = collection.find_one({"_id": 8})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Sw Wins Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Sw Wins Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Skywars Wins Leaderboard.png")
        db= cluster["Duels"]
        collection = db["Kills"]

        results = collection.find_one({"_id": 11})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Duels KDR Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Duels KDR Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Duels KDR Leaderboard.png")
        db= cluster["Duels"]
        collection = db["Kills"]

        results = collection.find_one({"_id": 11})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Duels Kills Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Duels Kills Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Duels Kills Leaderboard.png")
        db= cluster["Duels"]
        collection = db["WLR"]

        results = collection.find_one({"_id": 13})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Duels WLR Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Duels WLR Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Duels WLR Leaderboard.png")
        db= cluster["Duels"]
        collection = db["Wins"]

        results = collection.find_one({"_id": 14})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Duels Wins Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Duels Wins Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Duels Wins Leaderboard.png")
        db= cluster["Duels"]
        collection = db["Bridge Wins"]

        results = collection.find_one({"_id": 15})
        both = results["both"]
        fkdrs = [fkdrtuple[1] for fkdrtuple in both]
        badplayers = [fkdrtuple[0] for fkdrtuple in both]
        players = [s.replace("*", "") for s in badplayers]
        maps = ["./Files/Jurrasic.png","./Files/DreamGrove.png", "./Files/Lectus.png"]
        randmap = Image.open(random.choice(maps))
        draw = ImageDraw.Draw(randmap)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 50)
        draw.text((60, 100), "Blight Duels Wins Leaderboard", (0,0,0), font=font)
        draw.text((50, 100), "Blight Duels Wins Leaderboard", (36, 157, 159), font=font)
        font = ImageFont.truetype("./Files/Minecraft Regular.otf", 44)   
        draw.text((50,235), f"1. {players[0]}", (0,0,0), font=font)
        draw.text((50,230), f"1. {players[0]}", (255, 255, 255), font=font)
        draw.text((650,235), f"{fkdrs[0]}", (0,0,0), font=font)
        draw.text((650,230), f"{fkdrs[0]}", (139, 0 ,0), font=font)
        draw.text((50,300), f"2. {players[1]}", (0,0,0), font=font)
        draw.text((50,295), f"2. {players[1]}", (255, 255, 255), font=font)
        draw.text((650,300), f"{fkdrs[1]}", (0,0,0), font=font)
        draw.text((650,295), f"{fkdrs[1]}", (139, 0 ,0), font=font)
        draw.text((50,365), f"3. {players[2]}", (0,0,0), font=font)
        draw.text((50,360), f"3. {players[2]}", (255, 255, 255), font=font)
        draw.text((650,365), f"{fkdrs[2]}", (0,0,0), font=font)
        draw.text((650,360), f"{fkdrs[2]}",(139, 0 ,0), font=font)
        draw.text((50,430), f"4. {players[3]}", (0,0,0), font=font)
        draw.text((50,425), f"4. {players[3]}", (255,255,255), font=font)
        draw.text((650,430), f"{fkdrs[3]}", (0,0,0), font=font)
        draw.text((650,425), f"{fkdrs[3]}", (139, 0 ,0), font=font)
        draw.text((50,495), f"5. {players[4]}", (0,0,0), font=font)
        draw.text((50,490), f"5. {players[4]}", (255,255,255), font=font)
        draw.text((650,495), f"{fkdrs[4]}", (0,0,0), font=font)
        draw.text((650,490), f"{fkdrs[4]}", (139, 0 ,0), font=font)
        draw.text((50,560), f"6. {players[5]}", (0,0,0), font=font)
        draw.text((50,555), f"6. {players[5]}", (255,255,255), font=font)
        draw.text((650,560), f"{fkdrs[5]}", (0,0,0), font=font)
        draw.text((650,555), f"{fkdrs[5]}", (139, 0 ,0), font=font)
        draw.text((50,625), f"7. {players[6]}", (0,0,0), font=font)
        draw.text((50,620), f"7. {players[6]}", (255,255,255), font=font)
        draw.text((650,625), f"{fkdrs[6]}", (0,0,0), font=font)
        draw.text((650,620), f"{fkdrs[6]}", (139, 0 ,0), font=font)
        draw.text((50,690), f"8. {players[7]}", (0,0,0), font=font)
        draw.text((50,685), f"8. {players[7]}", (255,255,255), font=font)
        draw.text((650,690), f"{fkdrs[7]}", (0,0,0), font=font)
        draw.text((650,685), f"{fkdrs[7]}", (139, 0 ,0), font=font)
        draw.text((50,755), f"9. {players[8]}", (0,0,0), font=font)
        draw.text((50,750), f"9. {players[8]}", (255,255,255), font=font)
        draw.text((650,755), f"{fkdrs[8]}", (0,0,0), font=font)
        draw.text((650,750), f"{fkdrs[8]}", (139, 0 ,0), font=font)
        draw.text((50,820), f"10. {players[9]}", (0,0,0), font=font)
        draw.text((50,815), f"10. {players[9]}", (255,255,255), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (0,0,0), font=font)
        draw.text((650,820), f"{fkdrs[9]}", (139, 0 ,0), font=font)
        randmap.save("./Files/Bridge Wins Leaderboard.png")

            


    @tasks.loop(hours=2)
    async def myloop(self):
        print("started!")
        FirstIndexOption = []
        SecondIndexOption = []
        PlayerListStar = []
        StarListStar = []
        NewLine = []
        fkdrlist = []
        bwcolors = []
        swcolors = []
        IndexListIndex = []
        FinalsListFinals = []
        WinsListWins = []
        WLRListWLR = []
        SwStarListStar = []
        SwExpListExp = []
        SwKillsListKills = []
        SwWinsListWins = []
        SwKdrListKdr = []
        DuelsKdrListKdr = []
        DuelsWlrListWlr = []
        DuelsKillsListKills = []
        DuelsWinsListWins = []
        BridgeWinsListWins = []
        def sw_xp_to_lvl(xp):
            xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
            if xp >= 15000:
                return (xp - 15000) / 10000. + 12
            else:
                for i in range(len(xps)):
                    if xp < xps[i]:
                        return i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.hypixel.net/guild?key={APIKEY}&name=Blight') as req:
                req = await req.json()
                await session.close()
            array = {}
            exp = 0
            uuid = []
            rawgamereqs = []
            i = 0
            for count in range(len(req['guild']['members'])):
                uuid.append(req['guild']['members'][count]['uuid'])
            x = 0
            while i < len(uuid):
                
                
                    
                
                async with aiohttp.ClientSession() as session:
                    baddata = await session.get(f"https://api.hypixel.net/player?key={APIKEY}&uuid={uuid[i]}")
                    data = await baddata.json()
                try:
                    swexp = data["player"]["stats"]["SkyWars"]["skywars_experience"]
                except:
                    swexp = 0
                try:
                    swlevel = int(sw_xp_to_lvl(swexp))
                except:
                    swlevel = 0
                try:
                    duelswins = data["player"]["stats"]["Duels"]["wins"]
                except:
                    duelswins = 0
                try: 
                    duelslosses = data["player"]["stats"]["Duels"]["losses"]
                except:
                    duelslosses = 0
                try: 
                    duelsdeaths = data["player"]["stats"]["Duels"]["deaths"]
                except:
                    duelsdeaths = 0
                try:
                    duelskills = data["player"]["stats"]["Duels"]["kills"]
                except:
                    duelskills = 0



                    
                try:
                    bedwars_star = data["player"]["achievements"]["bedwars_level"]
                except:
                    bedwars_star = 0
                try:
                    bedwars_final_death = data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]
                except:
                    bedwars_final_death = 0
                try:
                    bedwars_final_kills = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
                except:
                    bedwars_final_kills = 0
                try:
                    bigfkdr = bedwars_final_kills/float(bedwars_final_death)
                except:
                    bigfkdr = 0
                
                
                try:
                    duelskdr = duelskills/float(duelsdeaths)
                except:
                    duelskdr = 0
                try:
                    duelswlr = duelswins/float(duelslosses)
                except:
                    duelswlr = 0
                
                try:
                    swwins = data["player"]["stats"]["SkyWars"]["wins"]
                except:
                    swwins = 0
                try:
                    swkills = data["player"]["stats"]["SkyWars"]["kills"]
                except:
                    swkills = 0
                try:
                    swdeaths = data["player"]["stats"]["SkyWars"]["deaths"]
                except:
                    swdeaths = 0
                try:
                    swkdr = swkills/float(swdeaths)
                except:
                    swkdr = 0

                try:
                    fkdr = round(bigfkdr, 2)
                except:
                    fkdr = 0
                try:
                    bedwars_losses = data["player"]["stats"]["Bedwars"]["losses_bedwars"]
                except:
                    bedwars_losses = 0
                try:
                    bedwars_wins = data["player"]["stats"]["Bedwars"]["wins_bedwars"]
                except:
                    bedwars_wins = 0
                try:
                    badbedwarswlr = bedwars_wins/float(bedwars_losses)
                except:
                    badbedwarswlr = 0
                try:
                    bedwarswlr = round(badbedwarswlr, 2)
                except:
                    bedwarswlr=0
                try:
                    bridgewins = data["player"]["stats"]["Duels"]["bridge_duel_wins"]
                except:
                    bridgewins = 0
                if int(bedwars_star) < 100:
                    bwcolors.append((128,128,128))
                elif int(bedwars_star) >=100 and int(bedwars_star) < 200:
                    bwcolors.append((255,255,255))
                elif int(bedwars_star) >= 200 and int(bedwars_star) < 300:
                    bwcolors.append((255,215,0))
                elif int(bedwars_star) >= 300 and int(bedwars_star) < 400:
                    bwcolors.append((0,255,255))
                elif int(bedwars_star) >= 400 and int(bedwars_star) < 500:
                    bwcolors.append((0,100,0))
                elif int(bedwars_star) >= 500 and int(bedwars_star) < 600:
                    bwcolors.append((0,153,153))
                elif int(bedwars_star) >= 600 and int(bedwars_star) < 650:
                    bwcolors.append((139,0,0))
                elif int(bedwars_star) >= 650 and int(bedwars_star) < 800:
                    bwcolors.append((255,102,255))
                elif int(bedwars_star) >= 800 and int(bedwars_star) < 900:
                    bwcolors.append((0,0,139))
                elif int(bedwars_star) >= 900 and int(bedwars_star) < 1000:
                    bwcolors.append((48,25,52))
                elif int(bedwars_star) >= 1000:
                    bwcolors.append((139,0,0))
                else:
                    bwcolors.append((128,128,128))
                if int(swlevel) < 5:
                    swcolors.append((128,128,128))
                elif int(swlevel) >= 5 and int(swlevel) < 10:
                    swcolors.append((255,255,255))
                elif int(swlevel) >= 10 and int(swlevel) < 15:
                    swcolors.append((249, 166, 2))
                elif int(swlevel) >= 15 and int(swlevel) < 20:
                    swcolors.append((80, 231, 237))
                elif int(swlevel) >= 20 and int(swlevel) < 25:
                    swcolors.append((0, 161, 0))
                elif int(swlevel) >= 25 and int(swlevel) < 30:
                    swcolors.append((0, 161, 161))
                elif int(swlevel) >= 30 and int(swlevel) < 35:
                    swcolors.append((152, 4, 4))
                elif int(swlevel) >= 35 and int(swlevel) < 40:
                    swcolors.append((255, 85, 255))
                elif int(swlevel) >= 40 and int(swlevel) < 45:
                    swcolors.append((85, 85, 255))
                elif int(swlevel) >= 45 and int(swlevel) < 50:
                    swcolors.append((166, 0, 166))
                else:
                    swcolors.append((152, 4, 4))
        





                
                
                async with aiohttp.ClientSession() as session:
                    badname = await session.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid[i]}")
                    ewname = await badname.json()
                    name = ewname["name"]
                
                
                try:
                    index = bedwars_star*float(fkdr)
                except:
                    index = 0
                FirstIndexOption.append
                BridgeWinsListWins.append(bridgewins)
                index = int(index)
                fkdrlist.append(fkdr)
                DuelsKdrListKdr.append(duelskdr)
                DuelsWlrListWlr.append(duelswlr)
                DuelsWinsListWins.append(duelswins)
                DuelsKillsListKills.append(duelskills)
                SwWinsListWins.append(swwins)
                IndexListIndex.append(index)
                SwKillsListKills.append(swkills)
                PlayerListStar.append(f"**{str(name)}**")
                StarListStar.append(int(bedwars_star))
                NewLine.append(":")
                FinalsListFinals.append(bedwars_final_kills)
                SwStarListStar.append(swlevel)
                WLRListWLR.append(badbedwarswlr)
                WinsListWins.append(bedwars_wins)
                SwExpListExp.append(swexp)
                SwKdrListKdr.append(swkdr)
                FullBridgeWinsList = list(zip(PlayerListStar, BridgeWinsListWins, NewLine))
                FullDuelsWinsList = list(zip(PlayerListStar, DuelsWinsListWins, NewLine))
                FullDuelsKillsList = list(zip(PlayerListStar, DuelsKillsListKills, NewLine))
                FullDuelsWlrList = list(zip(PlayerListStar, DuelsWlrListWlr, NewLine))
                FullDuelsKdrList = list(zip(PlayerListStar, DuelsKdrListKdr, NewLine))
                FullSwKdrList = list(zip(PlayerListStar, SwKdrListKdr, NewLine))
                FullSwKillsList = list(zip(PlayerListStar, SwKillsListKills, NewLine))
                FullSwWinsList = list(zip(PlayerListStar, SwWinsListWins, NewLine))
                FullSwStarList = list(zip(PlayerListStar, SwExpListExp, NewLine))
                FullWLRList = list(zip(PlayerListStar, WLRListWLR, NewLine))
                FullWinsList = list(zip(PlayerListStar, WinsListWins, NewLine))
                FullFinalList = list(zip(PlayerListStar, FinalsListFinals, NewLine))
                FullIndexList = list(zip(PlayerListStar, IndexListIndex, NewLine))
                FullFKDRList = list(zip(PlayerListStar, fkdrlist, NewLine))
                FullStarList = list(zip(PlayerListStar , StarListStar, NewLine))
                Starlistcolor = list(zip(PlayerListStar, StarListStar, bwcolors))
                SwStarlistcolor = list(zip(PlayerListStar, SwExpListExp, swcolors))
                i = i + 1
                x = x + 1
                print(f"Looped {x} times!")
                await asyncio.sleep(60)
            BridgeWinsOrderedList = sorted(FullBridgeWinsList, key=lambda x: x[1], reverse=True)
            DuelsKillsOrderedList = sorted(FullDuelsKillsList, key=lambda x: x[1], reverse=True)
            DuelsWlrOrderedList = sorted(FullDuelsWlrList, key=lambda x: x[1], reverse=True)
            DuelsWinsOrderedList = sorted(FullDuelsWinsList, key=lambda x: x[1], reverse=True)
            DuelsKdrOrderedList = sorted(FullDuelsKdrList, key=lambda x: x[1], reverse=True)
            SwKdrOrderedList = sorted(FullSwKdrList, key=lambda x: x[1], reverse=True)
            SwKillsOrderedList = sorted(FullSwKillsList, key=lambda x: x[1], reverse=True)
            SwWinsOrderedList = sorted(FullSwWinsList, key=lambda x: x[1], reverse=True)
            SwStarOrderedList = sorted(FullSwStarList, key=lambda x: x[1], reverse=True)
            WLROrderedList = sorted(FullWLRList, key=lambda x: x[1], reverse=True)
            WinsOrderedList = sorted(FullWinsList, key=lambda x: x[1], reverse=True)
            IndexOrderedList = sorted(FullIndexList, key=lambda x: x[1], reverse=True)
            FKDROrderedList = sorted(FullFKDRList, key=lambda x: x[1], reverse=True)
            StarOrderedList = sorted(FullStarList, key=lambda x: x[1], reverse=True)
            BwColourOrderedList = sorted(Starlistcolor, key=lambda x: x[1], reverse=True)
            SwColourOrderedList = sorted(SwStarlistcolor, key=lambda x: x[1], reverse=True)
            FinalsOrderedList = sorted(FullFinalList, key=lambda x: x[1], reverse=True)
            i = 0
            bridgewins = [bridgewinstuple[1] for bridgewinstuple in BridgeWinsOrderedList]
            bridgewinsplayers = [bridgewinstuple[0] for bridgewinstuple in BridgeWinsOrderedList]
            duelskdr = [duelskdrtuple[1] for duelskdrtuple in DuelsKdrOrderedList]
            duelswlr = [duelswlrtuple[1] for duelswlrtuple in DuelsWlrOrderedList]
            duelskills = [duelskillstuple[1] for duelskillstuple in DuelsKillsOrderedList]
            duelswins = [duelswinstuple[1] for duelswinstuple in DuelsWinsOrderedList]
            duelskillsplayers = [duelstuple[0] for duelstuple in DuelsKillsOrderedList]
            duelskdrplayers = [duelstuple[0] for duelstuple in DuelsKdrOrderedList]
            duelswlrplayers = [duelstuple[0] for duelstuple in DuelsWlrOrderedList]
            duelswinsplayers = [duelstuple[0] for duelstuple in DuelsWinsOrderedList]
            swkdr = [swkdrtuple[1] for swkdrtuple in SwKdrOrderedList]
            swkdrplayers = [swkdrplayer[0] for swkdrplayer in SwKdrOrderedList]
            swkills = [swkilltuple[1] for swkilltuple in SwKillsOrderedList]
            swwins = [swwinstuple[1] for swwinstuple in SwWinsOrderedList]
            swexp = [swstartuple[1] for swstartuple in SwStarOrderedList]
            wlr = [wlrtuple[1] for wlrtuple in WLROrderedList]
            Wins = [winstuple[1] for winstuple in WinsOrderedList]
            finals = [finaltuple[1] for finaltuple in FinalsOrderedList]
            Index = [indextuple[1] for indextuple in IndexOrderedList]
            swcolors = [swcolortuple[2] for swcolortuple in SwColourOrderedList]
            colors = [colortuple[2] for colortuple in BwColourOrderedList]
            stars = [startuple[1] for startuple in StarOrderedList]
            fkdrs = [fkdrtuple[1] for fkdrtuple in FKDROrderedList]
            players = [startuple[0] for startuple in StarOrderedList]
            IndexPlayers = [indextuple[0] for indextuple in IndexOrderedList]
            FinalsPlayers = [finaltuple[0] for finaltuple in FinalsOrderedList]
            SwKillsPlayers = [swkilltuple[0] for swkilltuple in SwKillsOrderedList]
            WinsPlayers = [winstuple[0] for winstuple in WinsOrderedList]
            WLRPlayers = [wlrtuple[0] for wlrtuple in WLROrderedList]
            SwStarPlayers = [swleveltuple[0] for swleveltuple in SwStarOrderedList]
            SwStarList = []
            SwWinsPlayers = [swplayerstuple[0] for swplayerstuple in SwWinsOrderedList]
            while i < len(swexp):
                swstar = sw_xp_to_lvl(swexp[i])
                SwStarList.append(swstar)
                i = i + 1
            BestSwStarList = list(zip(SwStarPlayers, SwStarList, swcolors, NewLine))
            SwStars = [swstartuple[1] for swstartuple in BestSwStarList]
            GoodSwStarPlayers = [swstartuple[0] for swstartuple in BestSwStarList]

            
            
            
            from pymongo import MongoClient
            from pprint import pprint
            import ssl
            cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
            db= cluster["Bedwars"]
            swdb = cluster["Skywars"]
            ddb = cluster["Duels"]
            BridgeWinsCollection = ddb["Bridge Wins"]
            SwStarCollection = swdb["Stars"]
            SwKillCollection = swdb["Kills"]
            StarCollection = db["Stars"]
            FKDRCollection = db["FKDR"]
            IndexCollection = db["Index"]
            FinalsCollection = db["Finals"]
            WinsCollection = db["Wins"]
            WLRCollection = db["WLR"]
            SwWinsCollection = swdb["Wins"]
            SwKdrCollection = swdb["KDR"]
            DuelsKillsCollection = ddb["Kills"]
            DuelsKDRCollection = ddb["KDR"]
            DuelsWLRCollection = ddb["WLR"]
            DuelsWinsCollection = ddb["Wins"]
            print(int(sum(Wins)))
            avgduelskdr = sum(duelskdr)//float(len(duelskdr))
            avgduelswlr = sum(duelswlr)//float(len(duelswlr))
            avgduelskills = sum(duelskills)//len(duelskills)
            avgbridgewins = sum(bridgewins)//len(bridgewins)
            avgduelswins = sum(duelswins)//len(duelswins)
            avgswkills = int(sum(swkills))//len(swkills)
            avgswwins = int(sum(swwins))//len(swwins)
            avgwins = int(sum(Wins))//len(Wins)
            notroundedavgfkdr = (sum(fkdrs))//float(len(fkdrs))
            avgfkdr = round(notroundedavgfkdr, 2)
            print(f"AVGFKDR is {avgfkdr}")
            avgswstar = int(sum(swexp))//len(swexp)
            avgstar = int(sum(stars))//len(stars)
            avgindex = int(sum(Index))//len(Index)
            avgfinals = int(sum(finals))//len(finals)
            notroundedavgwlr = (sum(wlr))//float(len(wlr))
            avgwlr = round(notroundedavgwlr, 2)
            avgswkdr = sum(swkdr)//float(len(swkdr))

            print(f"WLR is {avgwlr}")
            star_results = StarCollection.update_one({"_id":1}, {"$set":{"players": players, "stars": stars, "colors": colors, "avgstar": avgstar, "both": StarOrderedList}})
            fkdr_results = FKDRCollection.update_one({"_id": 2},{"$set":{"players": players, "FKDR": fkdrs, "avgsfkdr": avgfkdr, "both": FKDROrderedList}})
            index_results = IndexCollection.update_one({"_id": 3}, {"$set":{"players": IndexPlayers, "index": Index, "avgindex": avgindex, "both": IndexOrderedList}})
            finals_results = FinalsCollection.update_one({"_id": 4}, {"$set":{"players": FinalsPlayers, "finals": finals, "avgfinals": avgfinals, "both": FinalsOrderedList}})
            wins_results = WinsCollection.update_one({"_id": 5}, {"$set":{"players": WinsPlayers, "wins": Wins, "avgwins": avgwins, "both": WinsOrderedList }})
            wlr_results = WLRCollection.update_one({"_id": 6}, {"$set":{"players": WLRPlayers, "wlr": wlr, "avgwlr": avgwlr, "both": WLROrderedList}})
            swstar_results = SwStarCollection.update_one({"_id": 7}, {"$set":{"players": GoodSwStarPlayers, "stars": SwStars, "colors": swcolors, "avgstar": avgswstar, "both":BestSwStarList}})
            swwins_results = SwWinsCollection.update_one({"_id": 8}, {"$set":{"players": SwWinsPlayers, "wins": swwins, "avgwins": avgswwins, "both": SwWinsOrderedList}})
            swkills_results = SwKillCollection.update_one({"_id": 9}, {"$set":{"players": SwKillsPlayers, "kills": swkills, "avgkills": avgswkills, "both": SwKillsOrderedList}})
            swkdr_results = SwKdrCollection.update_one({"_id":10}, {"$set":{"players": swkdrplayers, "kdr": swkdr, "avgkdr": avgswkdr, "both": SwKdrOrderedList}})
            duelskills_results = DuelsKillsCollection.update_one({"_id": 11}, {"$set":{"players": duelskillsplayers, "kills": duelskills, "avgkills": avgduelskills, "both": DuelsKillsOrderedList}})
            duelskdr_results = DuelsKDRCollection.update_one({"_id": 12}, {"$set":{"players": duelskdrplayers, "kdr": duelskdr, "avgkdr": avgduelskdr, "both": DuelsKdrOrderedList}})
            duelswlr_results = DuelsWLRCollection.update_one({"_id": 13}, {"$set":{"players": duelswlrplayers, "wlr": duelswlr, "avgwlr": avgduelswlr, "both": DuelsWlrOrderedList}})
            duelswins_results = DuelsWinsCollection.update_one({"_id": 14}, {"$set":{"players": duelswinsplayers, "wins": duelswins, "avgwins": avgduelswins, "both": DuelsWinsOrderedList}})
            bridgewins_results = BridgeWinsCollection.update_one({"_id": 15}, {"$set":{"players": bridgewinsplayers, "wins": bridgewins, "avgwins": avgbridgewins, "both": BridgeWinsOrderedList}})
            print("Results Updated!")
    @commands.command(name="avg", aliases=["a", "average"])
    async def avg(self, ctx, arg=None, arg2=None):
        if arg is None:
            embed = discord.Embed(title="How to use average",description="Our average command lets us see some of our average stats in our main game modes! Its very easy to use and their are a lot of shortcuts.")
            await ctx.send(embed=embed)
        elif str(arg.lower()) == "bw" or str(arg.lower()) == "b":
            if str(arg2.lower()) == "fkdr" or str(arg2.lower()) == "fk" or str(arg2.lower()) == "fkd":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Bedwars"]
                collection = db["FKDR"]

                results = collection.find_one({"_id": 2})
                badfkdr = results["FKDR"]
                x = sum(badfkdr)
                y = len(badfkdr)
                badavgfkdr = float(x/y)
                avgfkdr = round(badavgfkdr, 2)
                
                embed = discord.Embed(title="Blights Average FKDR", description=f"Blights average FKDR is {avgfkdr}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "star" or str(arg2.lower()) == "stars" or str(arg2.lower()) == "s":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Bedwars"]
                collection = db["Stars"]

                results = collection.find_one({"_id": 1})
                badstar = results["stars"]
                x = sum(badstar)
                y = len(badstar)
                badavgstar = float(x/y)
                avgstar = round(badavgstar, 2)

                
                embed = discord.Embed(title="Blights Average Star", description=f"Blights average Star is {int(avgstar)}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "index" or str(arg2.lower()) == "i":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Bedwars"]
                collection = db["Index"]
                bresults = collection.find_one({"_id": 3})
                results = bresults["avgindex"]
                embed = discord.Embed(title="Blights Average Index", description=f"Blights average Index is {results}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "finals" or str(arg2.lower()) == "final" or str(arg2.lower()) == "f":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Bedwars"]
                collection = db["Finals"]
                
                bresults = collection.find_one({"_id": 4})
                results = bresults["avgfinals"]
                embed = discord.Embed(title="Blights average Finals ", description=f"Blights average Finals is {results}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "wlr" or str(arg2.lower()) == "wl":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Bedwars"]
                collection = db["WLR"]
                bresults = collection.find_one({"_id": 6})
                results = bresults["wlr"]
                x = sum(results)
                y = len(results)
                badwlr = float(x/y)
                avgwlr = round(badwlr,2)
                embed = discord.Embed(title="Blights average WLR", description=f"Blights average WLR is {avgwlr}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "wins" or str(arg2.lower()) == "win" or str(arg2.lower()) =="w":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Bedwars"]
                collection = db["Wins"]
                bresults = collection.find_one({"_id": 5})
                results = bresults["avgwins"]
                embed = discord.Embed(title="Blights average Wins", description=f"Blights average Wins is {results}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            else:
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Bedwars"]
                collection = db["Stars"]

                results = collection.find_one({"_id": 1})
                badstar = results["stars"]
                x = sum(badstar)
                y = len(badstar)
                badavgstar = float(x/y)
                avgstar = round(badavgstar, 2)
                embed = discord.Embed(title="Blights Average Star", description=f"Blights average Star is {int(avgstar)}", colour=discord.Colour.random())
                await ctx.send(embed=embed)

        elif str(arg.lower()) == "sw" or str(arg.lower()) == "s":
            if str(arg2.lower()) == "kdr" or str(arg2.lower()) == "kd":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Skywars"]
                collection = db["KDR"]
                bresults = collection.find_one({"_id": 10})
                results = bresults["kdr"]
                x = sum(results)
                y = len(results)
                badwlr = float(x/y)
                avgwlr = round(badwlr,2)
                embed = discord.Embed(title="Blights average Skywars KDR", description=f"Blights average KDR is {avgwlr}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "kills" or str(arg2.lower()) == "kill" or str(arg2.lower()) == "k":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Skywars"]
                collection = db["Kills"]
                bresults = collection.find_one({"_id": 9})
                results = bresults["avgkills"]
                
                embed = discord.Embed(title="Blights average Skywars kills", description=f"Blights average kills is {results}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "stars" or str(arg2.lower()) == "star" or str(arg2.lower()) == "s":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Skywars"]
                collection = db["Stars"]

                results = collection.find_one({"_id": 7})
                stars = results["stars"]
                x = (sum(stars))
                y = len(stars)
                resultss = int(x/y)
                embed = discord.Embed(title="Blights average Skywars stars", description=f"Blights average star is {resultss}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "wins" or str(arg2.lower()) == "win" or str(arg2.lower()) == "w":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Skywars"]
                collection = db["Wins"]

                results = collection.find_one({"_id": 8})
                stars = results["wins"]
                x = (sum(stars))
                y = len(stars)
                resultss = int(x/y)
                embed = discord.Embed(title="Blights average Skywars wins", description=f"Blights average wins is {resultss}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            else:
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Skywars"]
                collection = db["Stars"]

                results = collection.find_one({"_id": 7})
                stars = results["stars"]
                x = (sum(stars))
                y = len(stars)
                resultss = int(x/y)
                embed = discord.Embed(title="Blights average Skywars stars", description=f"Blights average star is {resultss}", colour=discord.Colour.random())
                await ctx.send(embed=embed)

        elif str(arg.lower()) == "duels" or str(arg.lower()) == "d":
            if str(arg2.lower()) == "wins" or str(arg2.lower()) == "win" or str(arg2.lower()) == "w":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Duels"]
                collection = db["Wins"]

                results = collection.find_one({"_id": 14})
                stars = results["avgwins"]
                
                embed = discord.Embed(title="Blights average Duels wins", description=f"Blights average wins is {stars}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "kills" or str(arg2.lower()) == "kill" or str(arg2.lower()) == "k":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Duels"]
                collection = db["Kills"]

                results = collection.find_one({"_id": 11})
                stars = results["avgkills"]
                
                embed = discord.Embed(title="Blights average Duels kills", description=f"Blights average kills is {stars}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "wlr" or str(arg2.lower()) == "wl":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Duels"]
                collection = db["WLR"]

                results = collection.find_one({"_id": 13})
                stars = results["wlr"]
                x = (sum(stars))
                y = len(stars)
                resultss = float(x/y)
                result = round(resultss, 2)
                embed = discord.Embed(title="Blights average Duels WLR", description=f"Blights average WLR is {result}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "kd" or str(arg2.lower()) == "kdr":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Duels"]
                collection = db["WLR"]

                results = collection.find_one({"_id": 12})
                stars = results["kdr"]
                x = (sum(stars))
                y = len(stars)
                resultss = float(x/y)
                result = round(resultss, 2)
                embed = discord.Embed(title="Blights Duels KDR", description=f"Blights average KDR is {result}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            elif str(arg2.lower()) == "bridge_wins" or str(arg2.lower()) == "bw":
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Duels"]
                collection = db["Bridge Wins"]

                results = collection.find_one({"_id": 15})
                stars = results["avgwins"]
                
                embed = discord.Embed(title="Blights Duels KDR", description=f"Blights average Bridge Wins is {result}", colour=discord.Colour.random())
                await ctx.send(embed=embed)
            else:
                cluster= MongoClient(mongo, ssl_cert_reqs=ssl.CERT_NONE)
                db= cluster["Duels"]
                collection = db["Wins"]

                results = collection.find_one({"_id": 14})
                stars = results["avgwins"]
                
                embed = discord.Embed(title="Blights average Duels wins", description=f"Blights average wins is {stars}", colour=discord.Colour.random())
                await ctx.send(embed=embed)




            
        else:
                await ctx.send("Invalid")

    
            
        

            
        

            

async def setup(bot: commands.Bot):
    await bot.add_cog(Leaderboard(bot))

