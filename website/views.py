# Blueprint here is used to define all the different routes that are going to be used with this specific route prefix
from flask import Blueprint, render_template

views = Blueprint('views', __name__) # Set up blueprint for flask application.

@views.route('/')
def home():
    return render_template('base.html')