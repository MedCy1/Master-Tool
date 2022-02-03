import os
import requests
import colorama

def hypesquadchanger():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colorama.Fore.RED + '''
  ██████   █████   █    ██  ▄▄▄      ▓█████▄     ▄████▄   ██░ ██  ▄▄▄       ███▄    █   ▄████ ▓█████  ██▀███  
▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▒████▄    ▒██▀ ██▌   ▒██▀ ▀█  ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ░██   █▌   ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ░▓█▄   ▌   ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒░▒████▓    ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░ ▒▒▓  ▒    ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░ ░ ▒  ▒      ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
░  ░  ░     ░   ░  ░░░ ░ ░   ░   ▒    ░ ░  ░    ░         ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░    ░     ░░   ░ 
      ░      ░       ░           ░  ░   ░       ░ ░       ░  ░  ░      ░  ░         ░       ░    ░  ░   ░     
                                      ░         ░                                                             
'''
)
    print(f"""[01] Bravery\n""")
    print(f"""[02] Brilliance\n""")
    print(f"""[03] Balance\n\n\n""")
    print(f"""Enter your House choice""")
    house = str(input(f"""Choice: """))

    #f = open('tokens.txt', 'r')
    token = input("your token >>")#f.read()

    #for line in token:
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
            }
        if house == "1" or house == "01":
            payload = {'house_id': 1}
        elif house == "2" or house == "02":
            payload = {'house_id': 2}
        elif house == "3" or house == "03":
            payload = {'house_id': 3}
        else:
            print(f"""[#] Invalid Choice""")
            input(f"""\n[#] Press ENTER to exit""")
        r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
        if r.status_code == 204:
            print(f""" \n[!] Hypesquad House changed""")
            input(f"""\n[#] Press ENTER to exit""")
        else:
            print(f"""[#] Invalid token""")
            input(f"""\n[#] Press ENTER to exit""")
                
hypesquadchanger()