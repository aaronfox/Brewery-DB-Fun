import os
import requests
import json

class Breweries:
    def __init__(self, key):
        self.key = key

    def print_test(self):
        print('Craft beers are the best!')

    def get_random_brewery(self):
        response = requests.get('https://sandbox-api.brewerydb.com/v2/brewery/random/?key=' + self.key)
        # Make sure response is correct
        if response.status_code != 200:
            return 'ERROR: Could not retrieve random brewery'

        random_brewery_json = json.loads(response.content)
        brewery_id = random_brewery_json['data']['id'].strip()
        brewery_name = random_brewery_json['data']['name']

        # Get location of brewery (or at least first one returned by API)
        response = requests.get('https://sandbox-api.brewerydb.com/v2/brewery/' + brewery_id.strip() + '/locations/?key=' + self.key)
        if response.status_code != 200:
            return 'ERROR: Could not retrieve random brewery location'

        random_brewery_location_json = json.loads(response.content)
        # Retrieve either state or country
        random_brewery_state_or_region = random_brewery_location_json['data'][0]['region']

        print(f'You\'re headed to {random_brewery_state_or_region}! Have fun at {brewery_name}!')


