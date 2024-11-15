import json
import numpy as np
import requests

url ="https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=Danger%20Zone%20Case"

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
        volatility = round(volatility, 3)# Round the volatility to 3 decimal places

        return volatility

    def calculate_sharpe_ratio(self, data, risk_free_rate):
        daily_returns = np.diff(data) / data[:-1]# Calculate daily returns
        mean_returns = np.mean(daily_returns-risk_free_rate)
        std_returns = np.std(daily_returns-risk_free_rate)
        sharpe_ratio = (mean_returns/std_returns)# Calculate Sharpe Ratio
        sharpe_ratio = round(sharpe_ratio, 3)

        return sharpe_ratio

    def eval_sharpe_ratio(self,sharpe_ratio):
        MIN_SHARPE_RATIO = -1.0  #red
        MAX_SHARPE_RATIO = 2.0  #green
        normalised_sharpe = max(min(sharpe_ratio, MAX_SHARPE_RATIO), MIN_SHARPE_RATIO) # Clamp the Sharpe Ratio to the min/max boundaries
        normalised_sharpe = (normalised_sharpe - MIN_SHARPE_RATIO) / (MAX_SHARPE_RATIO - MIN_SHARPE_RATIO)
        red = int((1 - normalised_sharpe) * 255)  # More red for negative values
        green = int(normalised_sharpe * 255)  # More green for positive values
        hex_colour = f'#{red:02x}{green:02x}00'
        return hex_colour

    def eval_volatility(self,volatility):
        MAX_VALUE = 5
        normalized_value = min(max(volatility / MAX_VALUE, 0), 1)
        red = int(normalized_value * 255)
        green = int((1 - normalized_value) * 255)
        hex_colour = f"#{red:02X}{green:02X}00"
        return hex_colour

    def url_builder(self, appid,item):
        item = item.replace(r' ', '%20')
        url = f"https://steamcommunity.com/market/pricehistory/?{appid}=730&market_hash_name={item}"
        return url




if __name__ == "__main__":
    # scraper = data_scrapper()
    # steamLoginSecure = input("Please enter your SteamLoginSecure")
    # sessionid = input("Please enter your sessionid")
    # response = scraper.get_data(steamLoginSecure, sessionid,url)
    # response_text = response.text
    # prices = scraper.json_filter(response_text)
    # volatility = scraper.volatility_calc(prices)
    # print(volatility)
    # ratio = scraper.calculate_sharpe_ratio(prices,0.02/365)
    # col = scraper.eval_sharpe_ratio(ratio)
    # scraper.eval_volatility(volatility)
    scraper = data_scrapper()
    l = scraper.url_builder("730","Danger Zone Case")
    print(l)
test = url ="https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=Danger%20Zone%20Case"

