import requests
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear') 

randomNumber = random.randint(100000, 999999) # 100000 - 999999

cls()

print("What game do you want? (Enter number)")
print("1. Skype")
print("2. League Of Legends")
print("3. Battle Net")
game = input("> ")

cls()

print("What is the name of the connection?")
name = input("> ")

cls()

print("What is your token?")
token = input("> ")

if (game == "1"):
    game = "skype"
elif (game == "2"):
    game = "leagueoflegends"
else:
    game = "battlenet"

url = "https://discordapp.com/api/v6/users/@me/connections/" + game +"/" + str(randomNumber)

payload = "{\"name\": \"" + name + "\",\n\"visibility\": 1\n}".encode('utf-8').decode('latin-1')
headers = {
    'authorization': token,
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
    'accept': "*/*",
    'authority': "discordapp.com",
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Host': "discordapp.com",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
 
response = requests.request("PUT", url, data=payload, headers=headers)
 
print(response.text)
