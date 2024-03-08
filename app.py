from flask import Flask, render_template, request, jsonify, Response
import requests
import json
from config import Config
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)
config = Config()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pagespeed', methods=['GET'])
def get_pagespeed_data():
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'Please provide a URL'}), 400

    api_key = config.API_KEY
    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'

    params = {
        'url': url,
        'key': api_key,
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    return jsonify(data)

@app.route('/api/download-pagespeed', methods=['GET'])
def download_pagespeed_data():
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'Please provide a URL'}), 400

    api_key = config.API_KEY
    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'

    params = {
        'url': url,
        'key': api_key,
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    # Convert the data to CSV format
    csv_data = convert_to_csv(data)

    # Create a response with the CSV data
    response = Response(
        csv_data,
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename={url}_pagespeed_data.csv'}
    )

    return response

def convert_to_csv(data):
    # Extract relevant data from the JSON response and convert to CSV format
    # Modify this function based on the structure of your PageSpeed API response
    # For demonstration purposes, let's assume the data is a dictionary with 'field1' and 'field2'
    csv_data = 'field1,field2\n'
    csv_data += f'{data["field1"]},{data["field2"]}\n'
    return csv_data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
