# This file makes the 'website' folder essentially a python package
# can import this
from flask import Flask

# creates the flask application
def create_app():
    app = Flask(__name__)

    # import said blueprints into the init file
    from .views import views # 'views' is the blueprint, which therefore includes all the associated routes
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

