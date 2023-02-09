import os

from flask import Flask
from flask_cors import CORS
from rest.routes.poke_routes import pokemon_bp
from app.extensions import db_connect

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app() -> Flask:

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
        basedir, 'data.sqlite',
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_extension(app)

    CORS(app)

    @app.route('/')
    def index():
        return '<h1> Hello There </h1>'

    return app


def register_extension(app):
    db_connect.init_app(app)

def regiter_blueprints(app):
    app.regiter_blueprint(pokemon_bp)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
