from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from library_data_collection import *
from urllib.parse import parse_qs

app = Flask(__name__)
api = Api(app)
records_file = './Records/web_records.json'
RECORDS = {'poop'}

class Index(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)

class Records(Resource):
    def get(self):
        RECORDS = load_data(records_file)

        headers = {'Content-Type': 'application/json'}
        return make_response(json.dumps(RECORDS, indent=4),200,headers)

    def post(self, records):
        return 'test'

    def delete(self,record_count):
        return 'test'

class Submit(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        result = request.args
        return make_response(render_template('records.html',result=result),200,headers)

    def post(self):
        headers = {'Content-Type': 'text/html'}
        result = request.form.to_dict()

        if not result.get('Pages'):
            return '400: Please include Number of Pages when submitting'

        elif not validate_ddc(result.get('DDC')):
            return '400: DDC not valid'

        update_web_records(result,records_file)
        return make_response(render_template('records.html',result=result),200,headers)

api.add_resource(Index, '/')
api.add_resource(Records, '/records')
api.add_resource(Submit, '/submit_action')

if __name__ == '__main__':
    app.run()
