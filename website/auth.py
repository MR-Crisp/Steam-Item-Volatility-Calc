# Blueprint here is used to define all the different routes that are going to be used with this specific route prefix
from flask import Blueprint

auth = Blueprint('auth', __name__) # Set up blueprint for flask application.

# setup the different routes
@auth.route('/login')
def login():
    return "LOGIN"