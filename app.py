#Dependencies
import os
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS


def create_app():

    app = Flask(__name__)
    app.config.from_object('config.Dev')
        
    '''Configurações'''

    JWTManager(app)
    CORS(app)

    from src.services import mongodb
    mongodb.configure(app)

    '''Extensions'''
    
    '''Declared routes'''


    # Route default
    @app.route('/')
    def default_route():
        return jsonify(message='Hello World')

    return app
