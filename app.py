from flask import Flask, request, render_template,session
from VolatilityCalc import data_scrapper
app = Flask(__name__)

app.secret_key = '94c03d7e4a0af14133954975a141ad170cf648bc825b2ca6f0b170b405e4e393'
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
    input1 = request.form['input1']
    input2 = request.form['input2']
    # Process the inputs as needed
    return f'You entered: {input1} and {input2}'


if __name__ == '__main__':
    app.run(debug=True)
