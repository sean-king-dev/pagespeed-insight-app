from flask import Flask, render_template, request, jsonify
import requests
import json
from config import Config
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Run on host 0.0.0.0 to make it accessible externally
