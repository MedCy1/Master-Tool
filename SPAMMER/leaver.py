import discord

client = discord.Client()
token = input("your-client-token : ")

whitelist = [
    # discord guild ids you don't want to leave
]


@client.event
async def on_ready():
    for guild in client.guilds:
        try:
            if guild.id not in whitelist:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(e)


client.run(token, bot=False)