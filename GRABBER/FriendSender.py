from asyncio import sleep
import discum, time 
import discord

token = "mfa.ACtv8oIeZKVbfOXrbla5kc50Mya4-TLE5bHCWcu10oU3gmY5L7eLaobrRKl2ZFyfUM2cFw5rrPMT4p5sNlvc" #  Your account token

bot = discum.Client(token= token, log=True)
timer = 0


with open("id.txt") as infile:
    for line in infile:
        id = int(line)
        try:
            time.sleep(10)
            bot.requestFriend(f'{id}')
            time.sleep(10)
            newDM = bot.createDM([f"{id}"]).json()["id"]
            bot.sendMessage(newDM, """Hello,\nexcuse me for disturbing you.\nBut, I'm the founder of a modded mc server called "Last Dream", it's an MMORPG with an animation oriented on minecraft but a gameplay oriented on genshin impact.\nWe are in beta phase and are actively looking for beta testers.\nI would like to know if you would be interested in joining our team as a beta tester?\nKnowing that our beta testers are paid about 40€ / week\nthe remuneration varies according to the bugs you will find, and especially according to the impact of the bugs encountered\nor elements that according to him would allow to improve the experience of a player or to improve the gameplay\nThe website:\nhttps://lastdream.fun/#download \nThe discord:\nhttps://discord.gg/lastdream""")
            timer += 1
            if timer == 5:
                time.sleep(60)
                timer = 0
            else:
                continue
        except:
            continue