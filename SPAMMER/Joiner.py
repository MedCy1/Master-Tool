import requests
 
def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v9/invites/{}".format(server_invite), headers=header)

join("OTMwODk2NjMzMTU0MTE3NzM0.Yfme2w.4092UlCtRN7NpopYv1OkxiAFp3Y", "U8gAUEQ3<")