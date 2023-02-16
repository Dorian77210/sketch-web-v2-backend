import sys
sys.path.append('../')

from flask_restful import Resource
from flask import request, jsonify
from flask_cors import cross_origin

from app.services.dataframe import DataFrameService

class ElbowRoute(Resource):

    @cross_origin()
    def post(self):
        json = request.get_json()
        data = json['data']['dataframe']
        maxClusters = int(json['data']['maxClusters'])

        result = DataFrameService.elbow(data, maxClusters)

        return jsonify({
            'success': True,
            'result': result
        })