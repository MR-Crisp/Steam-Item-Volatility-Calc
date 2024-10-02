# This file makes the 'website' folder essentially a python package
# can import this
from flask import Flask

# creates the flask application
def create_app():
    app = Flask(__name__)
    return app

