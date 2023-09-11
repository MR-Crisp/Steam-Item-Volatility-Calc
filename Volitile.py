import requests

# appid numbers

csgo = "730"
rust = "252490"
armello = "290340"

# url = 'https://steamcommunity.com/market/search?appid=' +csgo

cookie = {
    "steamLoginSecure": "76561199003829124%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQxOV8yMzIyQUY3OV85MEFFNiIsICJzdWIiOiAiNzY1NjExOTkwMDM4MjkxMjQiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NDUxMzIwMCwgIm5iZiI6IDE2ODU3ODUxMTYsICJpYXQiOiAxNjk0NDI1MTE2LCAianRpIjogIjBEMjlfMjMyMkFGNzdfODVCOUEiLCAib2F0IjogMTY5NDQyNTA5MiwgInJ0X2V4cCI6IDE3MTI4MDA0NDAsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIzMS45NC41LjEzOSIsICJpcF9jb25maXJtZXIiOiAiMzEuOTQuNS4xMzkiIH0.LzchuQWdvqOswsn2tGi2gWEW1QrFueeBoUTe60VVeZbSxmMk9cXTMyamPZwoP6SHvpXhy6hpHf141lIKgrHiBQ",
    "sessionid": "102dd93f2ea34518d538e652",
}

url = "http://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=Glove%20Case%20Key"

response = requests.get(url, cookies=cookie)

print(response.text)


# https://stackoverflow.com/questions/31961868/how-to-retrieve-steam-market-price-history
