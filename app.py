from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Read API key from config.json
with open('config.json') as config_file:
    config_data = json.load(config_file)
    api_key = config_data.get('apiKey', '')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pagespeed', methods=['GET'])
def get_pagespeed_data():
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'Please provide a URL'}), 400

    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'

    params = {
        'url': url,
        'key': api_key,
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
