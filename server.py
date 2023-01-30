import os
from flask import Flask
from extensions import db_connect


basedir = os.path.abspath(os.path.dirname(__file__))

def create_app() -> Flask:
    
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    register_extension(app)
    
    return app

def register_extension(app):
    db_connect.init_app(app)
