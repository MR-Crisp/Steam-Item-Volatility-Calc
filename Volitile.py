import requests
import numpy as np


# appid numbers

csgo = "730"
rust = "252490"
armello = "290340"

# url = 'https://steamcommunity.com/market/search?appid=' +csgo


def get_data():
    cookie = {
        "steamLoginSecure": "76561199003829124%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQxOV8yMzIyQUY3OV85MEFFNiIsICJzdWIiOiAiNzY1NjExOTkwMDM4MjkxMjQiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5NDYwNDE0NywgIm5iZiI6IDE2ODU4NzYwMjksICJpYXQiOiAxNjk0NTE2MDI5LCAianRpIjogIjBEMjlfMjMyMkFGQUFfNEQ3MjUiLCAib2F0IjogMTY5NDQyNTA5MiwgInJ0X2V4cCI6IDE3MTI4MDA0NDAsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIzMS45NC41LjEzOSIsICJpcF9jb25maXJtZXIiOiAiMzEuOTQuNS4xMzkiIH0.Fk-9Fz5aBQ34GiEU5rDdlORWIp7hVhd8oQPL0bhEAdVZQyFZqlvmL_2GhxtllJUPns8nojB469kAHwj_ks7lDw",
    }

    url = "http://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=Glove%20Case%20Key"

    response = requests.get(url, cookies=cookie)

    print(response)
    return response


def filter(response):
    index = response.text.find("[")

    data = response.text[index + 1 : -2]

    data = data.split("],[")
    data[-1] = data[-1][0:-1]

    for i in range(len(data)):
        data[i] = data[i].split(",")

    return data


def volatility_calc(data):
    price_list = []

    for i in range(len(data)):
        price_list.append(float(data[i][1]))

    mean = sum(price_list) / len(price_list)

    variance = sum([((price - mean) ** 2) for price in price_list]) / len(price_list)

    std = variance**0.5

    percent_change = (1 - ((mean - std) / mean)) * 100  # up or down

    return percent_change


def compare():
    pass


response = get_data()
data = filter(response)
volatility = volatility_calc(data)
print(volatility)


# print(volatility_calc(data))
