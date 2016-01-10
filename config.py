import os
basedir = os.path.abspath(os.path.dirname(__file__))                    # Setting the basedir location to the file directory location

class Config:       #Configuring standard settings
    #SQLALCHEMY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'HARD_PASSWORD'        # Getting the SECRET_KEY variable from the os.
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True                                # To automatically commit changes using sqlalchemy when request is finished

    #MAIL
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'                             #
    FLASKY_MAIL_SENDER = 'Flasky Admin <asdper76@gmail.com>'            #
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')                       #

    @staticmethod  #A function decorated using @staticmethod will have no knowledge of what class it belongs to
    def __init__(app):
        pass

class DevelopmentConfig(Config):
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# Config for which setup to use
config = {
    'developent': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
