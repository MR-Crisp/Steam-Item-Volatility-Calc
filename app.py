from flask import Flask, request, render_template,session
from VolatilityCalc import data_scrapper
import json
app = Flask(__name__)
with open('./keys.json', 'r') as file:
    data = json.load(file)
    key = data.get("app")
app.secret_key = key
@app.route('/')
def home():
    return render_template('HomePage.html')

@app.route('/login')
def login():
    return render_template('SteamLogin.html')


@app.route('/submit', methods=['POST']) #change this one to return the new page
def submit():
    steamLoginSecure = request.form['steam_secure_login']
    sessionid = request.form['session_id']
    session['sessionid'] = sessionid #saving this in a session so can be accesed across routes
    session['steamLoginSecure'] = steamLoginSecure

    return render_template('LoginSuccess.html')

@app.route('/GetData')
def get_data():
    return render_template('GetData.html')


@app.route('/process-input',methods = ['POST'])
def process_input():
    scrapper = data_scrapper()
    game = request.form['game']
    item = request.form['item']
    session['url'] = scrapper.url_builder(game,item)
    # Process the inputs as needed
    print(game,item)
    return render_template('GetDataSuccessful.html')

@app.route('/presentData')
def presentData():
    scraper = data_scrapper()
    steamLoginSecure = session['steamLoginSecure']
    sessionid = session['sessionid']
    url = session['url']
    response = scraper.get_data(steamLoginSecure, sessionid,url)
    response_text = response.text
    prices = scraper.json_filter(response_text)
    volatility1 = scraper.volatility_calc(prices)
    ratio1 = scraper.calculate_sharpe_ratio(prices,0.02/365)
    colour_volatility1 = scraper.eval_volatility(volatility1)
    colour_ratio1 = scraper.eval_sharpe_ratio(ratio1)
    return render_template('presentData.html',volatility = volatility1,ratio = ratio1,colour_volatility = colour_volatility1,colour_ratio = colour_ratio1)


if __name__ == '__main__':
    app.run(debug=True)
