import requests
import json


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''

    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


def get_api_method(response):
    '''Returns the API method, e.g. GET, POST, PUT, DELETE'''

    return response['httpMethod']


def error_function(raise_error: bool):
    if raise_error:
        raise Exception('An error occurred!')

    return True


def get_establishment_ratings(authority_id: int):
    uri = 'http://api.ratings.food.gov.uk/Establishments'
    payload = {'localAuthorityId': authority_id}
    resp = requests.get(uri, params=payload, headers={'x-api-version': '2'}, timeout=20)
    establishments = resp.json()['establishments']

    # print(json.dumps(resp.json(), indent=4, sort_keys=True))
    # print(json.dumps(establishments[0], indent=4, sort_keys=True))

    return establishments


get_establishment_ratings(1)
