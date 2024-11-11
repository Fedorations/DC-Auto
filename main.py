import requests, time, json, os
from pystyle import Colors, Colorate

banner = r'''
 __  __     __  __     _____     ______     ______    
/\ \_\ \   /\ \_\ \   /\  __-.  /\  == \   /\  __ \   
\ \  __ \  \ \____ \  \ \ \/\ \ \ \  __<   \ \  __ \  
 \ \_\ \_\  \/\_____\  \ \____-  \ \_\ \_\  \ \_\ \_\ 
  \/_/\/_/   \/_____/   \/____/   \/_/ /_/   \/_/\/_/ 
'''

# Define the path to config.json relative to the script's location
config_path = os.path.join(os.path.dirname(__file__), "config.json")

# Attempt to load the configuration file
try:
    with open(config_path, 'r') as config_file:
        configuration = json.load(config_file)
except FileNotFoundError:
    print(f"Configuration file not found. Ensure it exists at: {config_path}")
    exit(1)

# Extract configuration
Token = configuration.get("discordToken") 
chid = configuration.get("channelId") 
Seconds = configuration.get("Time_Per_Message") 
msgs = configuration.get("Messages") 

message = {
    "content": '''Hello!
How Are You?'''
}

print(Colorate.Horizontal(Colors.blue_to_white, banner, 1))

headers = {
    "Authorization": Token,
    "Content-Type": "application/json"
}

# Send messages in loop
for _ in range(msgs):
    response = requests.post(
        f"https://discord.com/api/v9/channels/{chid}/messages", 
        headers=headers, 
        json=message
    )
    if response.status_code == 200:
        print(f"{message['content']} || MSG Sent!")
    else:
        print("Failed to send message:", response.json())
    time.sleep(Seconds)
