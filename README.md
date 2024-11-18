
## Overview

This application displays key financial metrics, including Volatility and the Sharpe Ratio. It uses Flask for the web framework and dynamically updates the metrics on the web page.

## Features

- Display Volatility
- Display Sharpe Ratio
- Color-coded indicators for metric status (good or bad)

## Installation

First use the requirements.txt file to download all the dependancies:

`pip install -r requirements.txt`

Then Configure your machine to run flask locally.

Then create an file named `keys.json` and make a json object like so:

`{"app":"YOUR_FLASK_SECRET_KEY_HERE"}
`

replace the YOUR_FLASK_SECRET_KEY_HERE with a flask secret key which can be generated like so:

`python -c 'import secrets; print(secrets.token_hex())'`
## Usage

Run the app.py file and go to the local Host server

This webpage should show: 

![image](https://github.com/user-attachments/assets/220d5a51-5813-42a7-b16c-e071459f3523)

Click the login button to go to the login page:

![image](https://github.com/user-attachments/assets/72bc69d3-dc1c-4fa4-9173-4c2963bf4b1b)

Your Steam Secure Login and Sessoin ID, can be found once you have logged into steam and check your cookies in your browser (can be done by inspecting any page on steam).

Should look something like this:

![image](https://github.com/user-attachments/assets/0332ba2a-f8e4-45b9-8328-c25b621dc816)

And the session ID should look something like this:

`a7c9d2e34f5b6a1089e7c4f2
`
If sucessful this is the page that will come up:

![image](https://github.com/user-attachments/assets/23b32052-4936-498a-b099-3b3fa2132e12)

Then you need to enter the games appID that the item is from, for example CSGOs appID is 730. And the Item name itself.

- note that the program will take care of spaces in the name, but any special characters in items names will have to be manually URL encoded (this feature needs to be added).

![image](https://github.com/user-attachments/assets/90af53f5-9ef5-4bce-85e0-9d31438fd6ef)

If done correctly: 

![image](https://github.com/user-attachments/assets/abb8faec-9aae-453a-bb98-d5db6883ab97)

And finally the volatility and the Sharpe ratio are presented, as well as thier corresponsing colours:

![image](https://github.com/user-attachments/assets/f7b6e499-b9e2-496d-b584-f43a98981fa5)
## Contributing

Contributions are always welcome!

Some features that need improving are the:

- Url encoding that had to be done manually currently
- There isnt much Error handaling
- Login System need to be simplified
- A graph of the item in the past `n` amount of days
- Maybe adding a fuzzy finder to the item finder page
- Automatically detecting what game the item is from, so appID doesnt have to be searched


## Authors

- [@MR-Crisp](https://github.com/MR-Crisp)

