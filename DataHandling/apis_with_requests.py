import requests
import json

'''
Request the content of a url, which can be used to demonstrate retrieving html.
'''
# r = requests.get('https://xkcd.com/353/')

# return all the properties and methods of the specified object.
# print(dir(r))

# Get more detailed information.
# print(help(r))

# Get the source of the html page
# print(r.text)


'''
Request an image url
'''
# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# Print the bytes content of the image
# print(r.content)

# Write the image to a file:
# with open('comic.png', 'wb') as f:
#     f.write(r.content)


'''
How to check the api request was successful
'''

# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# Get the specific status code
# print(r.status_code)

# Or more simply, for anything that is less than a 400 response (mostly 200).  So any type of client or server error will return false.
# print(r.ok)


'''
Adding url parameters
'''
payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)


'''
Retrieving the json response as a python dict
'''
# payload = {'username': 'alex', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)
# r_dict = r.json()
#
# print(r_dict['form'])


'''
Add a timeout
'''
# An exception will be thrown:
# r = requests.get('https://httpbin.org/delay/3', timeout=2)


'''
Food hygene ratings example
'''
uri = 'http://api.ratings.food.gov.uk/Establishments'
authority_id = 1
payload = {'localAuthorityId': authority_id}
resp = requests.get(uri, params=payload, headers={'x-api-version': '2'}, timeout=10)
establishments = resp.json()['establishments']

print(json.dumps(establishments[0], indent=4, sort_keys=True))
