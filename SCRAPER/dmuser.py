import discord
client = discord.Client()

token = input("Enter Your Token or gay ")
userid = input("Enter the ID ")

@client.event(name="msg", pass_context=True)
async def msg(context, userid, message):
    user = client.get_user(userid)
    await user.send(message)

client.run(token, bot=False)