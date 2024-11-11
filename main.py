import requests, time, sys, os, json
from pystyle import Colors, Colorate, Write

banner = r'''
 __  __     __  __     _____     ______     ______    
/\ \_\ \   /\ \_\ \   /\  __-.  /\  == \   /\  __ \   
\ \  __ \  \ \____ \  \ \ \/\ \ \ \  __<   \ \  __ \  
 \ \_\ \_\  \/\_____\  \ \____-  \ \_\ \_\  \ \_\ \_\ 
  \/_/\/_/   \/_____/   \/____/   \/_/ /_/   \/_/\/_/ 
                                                      
'''
with open(f"C:/Users/{os.getlogin()}/Desktop/DcSender-main/DcMain/config.json") as config_file:
    configuration = json.load(config_file)

Token = configuration["discordToken"] 
chid = configuration["channelId"] 
Seconds = configuration["Time_Per_Message"] 
msgs = configuration["Messages"] 
#---------------------
message = {
    "content": '''Hello!
How Are You?'''
}
#-----------------------
print(Colorate.Horizontal(Colors.blue_to_white, f"{banner}", 1))

headers = {
    "Authorization": Token,
    "Content-Type": "application/json"
}

for _ in range(msgs):
    start_send = requests.post(f"https://discord.com/api/v9/channels/{chid}/messages", headers=headers, data=json.dumps(message))
    time.sleep(Seconds)
    req_send = start_send.json()
    content_sent = req_send['content']
    print(content_sent + " || MSG Sent!")
