import requests
import json

# Read the configuration from the JSON file
try:
    with open('config.json') as config_file:
        config_data = json.load(config_file)
except FileNotFoundError:
    print("Error: Configuration file 'config.json' not found.")
    exit(1)

# Access the API key in your Python code
api_key = config_data.get('apiKey')
if not api_key:
    print("Error: API key not found in the configuration file.")
    exit(1)

def get_pagespeed_data(url):
    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'

    params = {
        'url': url,
        'key': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    website_url = 'https://example.com'
    pagespeed_data = get_pagespeed_data(website_url)

    if pagespeed_data:
        # Example: Print the overall score
        print(f"Overall Score: {pagespeed_data['lighthouseResult']['categories']['performance']['score']}")
