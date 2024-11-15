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

@app.route('/get_data')
def get_data():
    game = request.form['input1']
    item = request.form['input2']
    session['url'] = data_scrapper.url_builder(game,item)
    # Process the inputs as needed
    return f'You entered: {input1} and {input2}'


if __name__ == '__main__':
    app.run(debug=True)
