from flask import Flask
from flask_restful import Api, Resource

from app.routes.dataframe.kmeans import KMeansRoute
from app.routes.dataframe.elbow import ElbowRoute


from app.config import Config

def create_app(config=Config):
    from flask_cors import CORS, cross_origin

    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Setup all the routes of the app
    api.add_resource(KMeansRoute, '/kmeans')
    api.add_resource(ElbowRoute, '/elbow')


    app.config.from_object(config)

    return app