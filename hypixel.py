import os
import aiohttp
import requests
API_KEY = os.environ['API_KEY']


async def get_data(uuid):
    async with aiohttp.ClientSession() as session:
        baddata = await session.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}")
        print(f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}")
        data = await baddata.json()
    return data
async def get_uuid(name):
    url = f'https://api.mojang.com/users/profiles/minecraft/{name}'
    async with aiohttp.ClientSession() as session:
        print(url)
        response = await session.get(url)
        bresponse = await response.json()
    return response

bad_uuid = "9418e3b5-6def-41d4-855d-47ff56c73af1"
uuid = "af81dba9-96af-4d07-8a8b-aa542b085b98"
EXP_NEEDED = [100000, 150000, 250000, 500000, 750000, 1000000, 1250000, 1500000, 2000000, 2500000, 2500000, 2500000, 2500000, 2500000, 3000000]
# A list of amount of XP required for leveling up in each of the beginning levels (1-15).

def get_level(exp):
    level = 0

    for i in range(1000):
    # Increment by one from zero to the level cap.
        need = 0
        if  i >= len(EXP_NEEDED):
            need = EXP_NEEDED[len(EXP_NEEDED) - 1]
        else:
            need = EXP_NEEDED[i]
        # Determine the current amount of XP required to level up,
        # in regards to the "i" variable.
  
        if (exp - need) < 0:
            return ((level + (exp / need)) * 100) / 100
        # If the remaining exp < the total amount of XP required for the next level,
        # return their level using this formula.

        level += 1
        exp -= need
        # Otherwise, increase their level by one,
        # and subtract the required amount of XP to level up,
        # from the total amount of XP that the guild had.

    return 1000
    # This should never happen...
async def get_reqs(data):
    def sw_xp_to_lvl(xp):
            xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
            if xp >= 15000:
                return (xp - 15000) / 10000. + 12
            else:
                for i in range(len(xps)):
                    if xp < xps[i]:
                        return i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])

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
        duelswins = data["player"]["stats"]["Duels"]["wins"]
    except:
        duelswins = 0
    try: 
        duelslosses = data["player"]["stats"]["Duels"]["losses"]
    except:
        duelslosses = 0
    try:
        notroundedduelswlr = duelswins/float(duelslosses)
    except:
        notroundedduelswlr = 0
    try:
        duelswlr = round(notroundedduelswlr, 2)
    except:
        duelswlr = 0
    try:
        bigfkdr = bedwars_final_kills/float(bedwars_final_death)
    except:
        bigfkdr = 0
    try:
        fkdr = round(bigfkdr, 2)
    except:
        fkdr = 0
    try:
        indexnotint = (fkdr**2)*bedwars_star
    except: 
        indexnotint = 0
    try:
        index = int(indexnotint)
    except:
        index = 0
    bedwars_stats = [bedwars_star, fkdr, index]

    duels_stats = [duelswins, duelswlr]
    return bedwars_stats, duels_stats


async def check_reqs(bedwars_stats, duels_stats):
    print("check reqs")
    bedwars_star = bedwars_stats[0]
    fkdr = bedwars_stats[1]
    index = bedwars_stats[2]
    duels_wins = duels_stats[0]
    duels_wlr = duels_stats[1]
  
    if int(index) >= 650 and int(bedwars_star) >= 150 and float(fkdr) >= float(1) and int(duels_wins) >= 1000 and float(duels_wlr) >= float(1):
        return True

    elif int(bedwars_star) >= 150 and float(fkdr) >= float(1) and int(index) >= 1000:
        return True
    else:
        return False
    


