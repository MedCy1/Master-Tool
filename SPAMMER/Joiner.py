from lib2to3.pgen2 import token
import requests
 
def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v9/invites/{}".format(server_invite), headers=header)

f = open('tokens.txt', 'r')
tokens = f.read()
server_invite = input("Enter Invitation : ")

for line in tokens:
    join(tokens, server_invite)
tokens.close()