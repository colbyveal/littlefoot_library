from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from library_data_collection import *
from urllib.parse import parse_qs
import json2table

app = Flask(__name__)
api = Api(app)
records_file = './Records/web_records.json'
RECORDS = {}
headers = {'Content-Type': 'text/html'}


class Index(Resource):
    def get(self):
        return make_response(render_template('index.html'),200,headers)


class Records(Resource):
    def get(self):
        RECORDS = load_data(records_file)

        headers = {'Content-Type': 'application/json'}
        return make_response(json.dumps(RECORDS, indent=4),200,headers)


class Report(Resource):
    def get(self):

        RECORDS = load_data(records_file)
        report = process_report(RECORDS)
        report_category = report['Books Per Category: ']
        category_json = json.loads(report_category)
        json2html_catgory = json2table.convert(category_json,table_attributes={"id": "category_table"})
        report.pop('Books Per Category: ')
        report['Books Per Category : '] = json2html_catgory
        json2html_report = json2table.convert(report, table_attributes={'id': 'report_table'})
        
        return make_response(render_template('report.html',report=json2html_report),200,headers)


class Submit(Resource):
    def get(self):
        result = request.args
        return make_response(render_template('records.html',result=result),200,headers)

    def post(self):
        result = request.form.to_dict()

        if not result.get('Pages'):
            return '400: Please include Number of Pages when submitting', 400

        elif not validate_ddc(result.get('DDC')):
            return '400: DDC not valid', 400

        update_web_records(result,records_file)
        return make_response(render_template('records.html',result=result),200,headers)


api.add_resource(Index, '/')
api.add_resource(Records, '/records')
api.add_resource(Report, '/report')
api.add_resource(Submit, '/submit_action')

if __name__ == '__main__':
    app.run()
