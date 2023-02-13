from flask import Flask
from flask_restful import Api

def create_app():
    from flask_cors import CORS, cross_origin

    app = Flask(__name__)
    api = Api(app)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app