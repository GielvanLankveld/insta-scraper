import requests
import json

class Instagram():
    def __init__(self, api_key):
        self.api_key = api_key
        self.GOOD_STRING = '\033[92m✔\033[0m'
        self.BAD_STRING = '\033[92m❌\033[0m'

    def scrape_profile(self, url, return_data):
        print(f'{self.GOOD_STRING} Crawling profile..')
        payload = {
            'fields': 'id,caption,media_url,timestamp',
            'access_token': self.api_key
            }
        r = requests.get(url, params=payload)
        json_data = r.json()

        return_data = return_data + json_data['data']
        if 'next' in json_data['paging']:
            return self.scrape_profile(json_data['paging']['next'], return_data)
        else:
            return return_data    
        