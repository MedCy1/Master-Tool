from lib2to3.pgen2 import token
import discord
import os
import colorama
import time
import ctypes
from os import system
import sys

colorama.init()
dm = discord.Client()


kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
os.system("cls")
kernel32.SetConsoleTitleW(f"DM ALL Tool | by Med x Onexy")

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

print(colorama.Fore.RED + '''
▓█████▄  ███▄ ▄███▓    ▄▄▄       ██▓     ██▓    
▒██▀ ██▌▓██▒▀█▀ ██▒   ▒████▄    ▓██▒    ▓██▒    
░██   █▌▓██    ▓██░   ▒██  ▀█▄  ▒██░    ▒██░    
░▓█▄   ▌▒██    ▒██    ░██▄▄▄▄██ ▒██░    ▒██░    
░▒████▓ ▒██▒   ░██▒    ▓█   ▓██▒░██████▒░██████▒
 ▒▒▓  ▒ ░ ▒░   ░  ░    ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░
 ░ ▒  ▒ ░  ░      ░     ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░
 ░ ░  ░ ░      ░        ░   ▒     ░ ░     ░ ░   
   ░           ░            ░  ░    ░  ░    ░  ░
 ░                                              
  '''
)

entrtoken = ("Enter Your Token\n")
for char in entrtoken:
  time.sleep(0.06)
  sys.stdout.write(char)
  sys.stdout.flush()
token = input(">>")
print("\n")

message = ("Enter The Server ID\n")
for char in message:
  time.sleep(0.06)
  sys.stdout.write(char)
  sys.stdout.flush()
gildid = input(">>")
guild = dm.get_guild(gildid)
print("\n")

message = ("Enter Your Message\n")
for char in message:
  time.sleep(0.06)
  sys.stdout.write(char)
  sys.stdout.flush()
token = input(">>")


@dm.event
async def on_connect():
  print("Connecté en tant que :")
  print(dm.user.name)
  print(dm.user.id)
  time.sleep(2)
  clear()

  print("LOADING...")
  time.sleep(0.5)
  clear()
  print(".")
  time.sleep(0.4)
  clear()
  print("..")
  time.sleep(0.4)
  clear()
  print("...")
  time.sleep(0.4)
  clear()
  
  membertotal = 0
  usercount = 0
  for user in dm.user.friends:
    membertotal += 1
  
  for user in guild.member_count:
    try:
      await user.send(message)
      print(f"message envoyé à : {user.name}")
      usercount += 1
      kernel32.SetConsoleTitleW(f"title User DM: {usercount} Total DM: {membertotal}")
    except:
      print(f"erreur dans l'envoie du message pour : {user.name}")
  print(f"{dm.user.name} tous les utilisateurs ont été dm!")

dm.run(token, bot=False)