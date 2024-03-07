import requests
import json

import json

# Read the configuration from the JSON file
with open('config.json') as config_file:
    config_data = json.load(config_file)

# Access the API key in your Python code
api_key = config_data['apiKey']
print(f"API Key: {api_key}")

def get_pagespeed_data(url):
    api_key = 'api_key'
    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'

    params = {
        'url': url,
        'key': api_key,
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    return data

if __name__ == "__main__":
    website_url = 'https://example.com'
    pagespeed_data = get_pagespeed_data(website_url)

    # Example: Print the overall score
    print(f"Overall Score: {pagespeed_data['lighthouseResult']['categories']['performance']['score']}")
