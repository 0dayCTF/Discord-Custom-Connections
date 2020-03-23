import requests
 
url = "https://discordapp.com/api/v6/users/@me/connections/battlenet/RANDOMNUMBER"
 
payload = "{\"name\": \"NAME OF CONNECTION\",\n\"visibility\": 1\n}".encode('utf-8').decode('latin-1')
headers = {
    'authorization': "YOUR TOKEN HERE",
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
