from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.restful import Api

db = SQLAlchemy()


def add_cors_headers(response):
    """
    Setup response headers for api requests
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = (
        'Origin, '
        'X-Requested-With, Content-Type, Accept')
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


def create_app(config_name):
    """
    Flask app factory
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    api = Api()
    db.init_app(app)

    from .resources import MonsterResource

    api.add_resource(MonsterResource, '/<int:id>', endpoint='monster')
    api.init_app(app)
    app.after_request(add_cors_headers)

    return app
