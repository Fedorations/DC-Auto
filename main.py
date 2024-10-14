import requests
import time
import sys
from colorama import Fore, Style, init
import json

ascii = '''
 __  __     __  __     _____     ______     ______    
/\ \_\ \   /\ \_\ \   /\  __-.  /\  == \   /\  __ \   
\ \  __ \  \ \____ \  \ \ \/\ \ \ \  __<   \ \  __ \  
 \ \_\ \_\  \/\_____\  \ \____-  \ \_\ \_\  \ \_\ \_\ 
  \/_/\/_/   \/_____/   \/____/   \/_/ /_/   \/_/\/_/ 
                                                      
'''
print(f"{Fore.LIGHTBLUE_EX}{ascii}")

tokendc = "" # user token 4 discord
channel = input(f"{Fore.BLUE}Channel ID (>): ") 
message = {
    "content": '''
straight rizz though ngl


'''
}

headers = {
    "Authorization": tokendc,
    "Content-Type": "application/json"
}

for _ in range(999):
    start_send = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers=headers, data=json.dumps(message))
    time.sleep(7)
    req_send = start_send.json()
    content_sent = req_send['content']
    content_user = req_send['author']['username']
    print(f"{content_sent}")
    print(f"{content_user}")

