import json

# Example multi-line string that is valid json
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-7532",
            "emails": null,
            "has_license": true
        }
    ]
}
'''


# How to load json from a string, use load-s, which stands for load string.
data = json.loads(people_string)
print(data)

# print out a specific element of the json object
for person in data['people']:
    print(person['name'])


# Convert the python dictionary back into a json string.
# This is typically use to print the json output in a readable way, using indent, etc
print(json.dumps(data, indent=4, sort_keys=True))

# Load json from file
with open('DataHandling/establishments.json') as f:
    establishments = json.load(f)

print(establishments[0]['LocalAuthorityName'])

# Write the data to a file
with open('DataHandling/establishments_output.json', 'w') as f:
    json.dump(data, f, indent=4)
