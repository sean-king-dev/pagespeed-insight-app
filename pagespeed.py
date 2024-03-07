import requests
import json

def get_pagespeed_data(url):
    api_key = 'YOUR_APAIzaSyD3_W1VvDbcrfxfQCxEfoSZYUz-SxAEfVoI_KEY'
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
