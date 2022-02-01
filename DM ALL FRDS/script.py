from email import message
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

print(colorama.Fore.CYAN + '''
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
messageinput = ("Enter Your Message\n")
for char in messageinput:
  time.sleep(0.06)
  sys.stdout.write(char)
  sys.stdout.flush()
message = input(">>")

@dm.event
async def on_connect():
  print("Connected at :")
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
      print(f"\033[0;32m [+] Message Send To : {user.name}")
      usercount += 1
      kernel32.SetConsoleTitleW(f"title User DM: {usercount} Total DM: {usertotal}")
    except:
      print(f"\033[0;31m [+] error for sending message to : {user.name}")
  print(f"\033[0;36m {dm.user.name} [+] All Users As Been DM successfully")

dm.run(token, bot=False)