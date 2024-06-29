import requests
from bs4 import BeautifulSoup
import json
url = 'https://stocktwits.com/'
header = {
   "accept":"application/json",
   "accept-language":"en-US,en;q=0.9",
   "if-none-match":"W/^\^",
   "origin":"https://stocktwits.com",
   "priority":"u=1, i",
   "referer":"https://stocktwits.com/",
   "sec-ch-ua":"^\^",
   "sec-ch-ua-mobile":"?0",
   "sec-ch-ua-platform":"^\^",
   "sec-fetch-dest":"empty",
   "sec-fetch-mode":"cors",
   "sec-fetch-site":"same-site",
   "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}
response = requests.get(url, headers=header)
data_json = response.json()
print(data_json)