###################################
# Dictionaries
###################################

# Define a dictionary
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

# Access a single key:value pair
print(student['name'])

# Checking if keys exist
# print(student['phone'])     # This will return a KeyError
print(student.get('name'))     # This will return John
print(student.get('phone'))     # This will return None
print(student.get('phone', 'Not Found'))        # This sets a default value to be returned if key does not exist


# Adding new keys
student['phone'] = '07900123456'
print(student)

# Updating a value
student['phone'] = '07900987654'
print(student)

# Update method - this is useful when we want to update multiple values
student.update({'name': 'Jane', 'age': 26})
print(student)

# Delete a key using the del keyword
del student['age']
print(student)

# Delete a key using the pop method
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
age = student.pop('age')
print(student)
print(age)

# Determine the number of keys
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(len(student))

# Print the keys
print(student.keys())

# Print the values
print(student.values())

# Print keys and values
print(student.items())

# Iterate a dict
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
