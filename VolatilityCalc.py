import json
import numpy as np
import requests

url ="https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=Glove%20Case%20Key"


class data_scrapper:

    def __init__(self):
        return


    def json_filter(self,response_text):
        try:
            response_data = json.loads(response_text)# Convert the JSON text to a Python dictionary
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

        general_list = response_data.get('prices')# Get the 'prices' list from the parsed JSON dictionary
        prices_list = [item[1] for item in general_list]# Extract the second element (price) from each sub-list in 'prices'

        return prices_list


    def get_data(self, securelogin, id,url):
        cookie = {"steamLoginSecure": securelogin, "sessionid": id}
        response = requests.get(url, cookies=cookie)

        return response


    def volatility_calc(self,data):
        return_calc = (np.diff(data)/data[:-1])
        volatility = np.std(return_calc)*100
        # Round the volatility to 3 decimal places
        volatility = round(volatility, 3)

        return volatility


def main():
    scraper = data_scrapper()
    steamLoginSecure = input("Please enter your SteamLoginSecure")
    sessionid = input("Please enter your sessionid")
    response = scraper.get_data(steamLoginSecure, sessionid,url)
    response_text = response.text
    prices = scraper.json_filter(response_text)
    if prices == None:
        return
    volatility = scraper.volatility_calc(prices)
    print(volatility)
    return


if __name__ == "__main__":
    main()

