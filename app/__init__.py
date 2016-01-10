from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

#Initializing
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)                           # __name__ If you are using a single module, __name__ is always the correct value.
                                                    # If you however are using a package, it’s usually recommended to hardcode the name of your package there.
    app.config.from_object(config[config_name])     # Reading from config.py and uses the dictionary config, to determine which config to run based on config_name
    config[config_name].init_app(app)               #

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    return app