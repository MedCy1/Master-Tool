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

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

words = (colorama.Fore.RED + '''
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

for line in words:
  time.sleep(0.000001)
  sys.stdout.write(line)
  sys.stdout.flush()

token = input("Enter Your Token : ")
message = input("le message que tu veux envoyer>>")

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
  
  usertotal = 0
  usercount = 0
  for user in dm.user.friends:
    usertotal += 1
  
  for user in dm.user.friends:
    try:
      await user.send(message)
      print(f"message envoyé à : {user.name}")
      usercount += 1
      kernel32.SetConsoleTitleW(f"title User DM: {usercount} Total DM: {usertotal}")
    except:
      print(f"erreur dans l'envoie du message pour : {user.name}")
  print(f"{dm.user.name} tous les utilisateurs ont été dm!")

dm.run(token, bot=False)