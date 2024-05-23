from flask import Flask, render_template, request, jsonify, Response
import requests
import json
from config import Config
from flask_cors import CORS
import csv
import os

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

    # Save the CSV data to a file
    filename = f'{url}_pagespeed_data.csv'
    filepath = os.path.join(app.root_path, 'downloads', filename)

    # Ensure the 'downloads' directory exists
    os.makedirs(os.path.join(app.root_path, 'downloads'), exist_ok=True)

    with open(filepath, 'w', newline='') as csvfile:
        csvfile.write(csv_data)

    # Create a response with the CSV data
    response = Response(
        csv_data,
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )

    return response

def convert_to_csv(data):
    # Modify this function based on the structure of your PageSpeed API response
    lighthouse_result = data.get('lighthouseResult', {})
    audits = lighthouse_result.get('audits', {})

    # Extract relevant metrics from the audits
    metrics = {
        'Bootup Time': audits.get('bootup-time', {}).get('numericValue', 'N/A'),
        'Critical Request Chains': audits.get('critical-request-chains', {}).get('numericValue', 'N/A'),
        'Cumulative Layout Shift': audits.get('cumulative-layout-shift', {}).get('numericValue', 'N/A'),
        'Diagnostics': audits.get('diagnostics', {}).get('numericValue', 'N/A'),
        'DOM Size': audits.get('dom-size', {}).get('numericValue', 'N/A'),
        'Duplicated Javascript': audits.get('duplicated-javascript', {}).get('numericValue', 'N/A'),
        'Efficient Animated Content': audits.get('efficient-animated-content', {}).get('numericValue', 'N/A'),
        'Final Screenshot': audits.get('final-screenshot', {}).get('numericValue', 'N/A'),
        # Add more metrics as needed
    }

    # Convert metrics to CSV format
    csv_data = ','.join(metrics.keys()) + '\n'
    csv_data += ','.join(map(str, metrics.values())) + '\n'

    return csv_data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
