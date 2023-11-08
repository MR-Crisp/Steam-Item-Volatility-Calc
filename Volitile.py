import requests
import numpy as np
from bs4 import BeautifulSoup
import simplejson
from soup2dict import convert
import json
import ast


# appid numbers

csgo = "730"
rust = "252490"
armello = "290340"

# url = 'https://steamcommunity.com/market/search?appid=' +csgo

login = 0


def get_data(securelogin):
    cookie = {"steamLoginSecure": securelogin}

    url = "http://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=Glove%20Case%20Key"

    response = requests.get(url, cookies=cookie)

    print(response)
    return response


def filter(response):
    index = response.text.find("[")

    data = response.text[index + 1: -2]

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

    variance = sum([((price - mean) ** 2)
                   for price in price_list]) / len(price_list)

    std = variance**0.5

    percent_change = (1 - ((mean - std) / mean)) * 100  # up or down

    return percent_change


def list_names():  # creates a list of names or updates it if it already exists
    url = "https://counterstrike.fandom.com/wiki/Skins/List"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    rows = soup.find_all(
        "span",
        class_=[
            "common",
            "uncommon",
            "rare",
            "mythical",
            "legendary",
            "ancient",
            "discontinued",
        ],
    )

    with open("output.txt", "w", encoding='utf8') as output_file:
        for i, row in enumerate(rows[0:-1], 0):
            if i % 2 == 0:
                output_file.write(row.text)
                output_file.write("|")
            else:
                output_file.write(row.text)
                output_file.write("\n")

    # one issue found with the write method, is that the website has formatted its data incorrectly, meaning that the grades sometimes come before, but sometimes after
    # so this next piece of code is to fix that

    with open("output.txt", "r+", encoding='utf8') as output_file:
        lines = output_file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split("|")
            GRADES = ["Industrial Grade", "Mil-Spec", "Classified",
          "Restricted", "Consumer Grade", "Covert"]
            for i in range(len(GRADES)):
                if line[0] == GRADES[i]:
                    # switches the two items
                    line[0], line[1] = line[1], line[0]
            output_file.write(line[0])
            output_file.write("|")
            output_file.write(line[1])
            output_file.write("\n")


def read_names():  # reads the names from output.txt
    with open("./output.txt", "r") as f:
        for line in f:
            line = line.split("|")
            line = line[0:-2]
            print(line)


def compare(response):
    data = filter(response)
    # ---------------------------------working on this


# response = get_data(login)
# data = filter(response)
# volatility = volatility_calc(data)
# print(volatility)


# print(volatility_calc(data))


test.txt