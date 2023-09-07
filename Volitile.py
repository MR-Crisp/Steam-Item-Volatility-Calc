import requests

#appid numbers

csgo = '730'
rust = '252490'
armello = '290340'

#url = 'https://steamcommunity.com/market/search?appid=' +csgo

cookie = {'steamLogin': '76561198058933558%7C%7C2553658936E891AAD'}

url = 'http://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=Glove%20Case%20Key'

response = requests.get(url, cookies=cookie)

print(response)


#https://stackoverflow.com/questions/31961868/how-to-retrieve-steam-market-price-history