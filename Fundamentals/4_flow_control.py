"""
For Loops
"""


# simple loop
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# break
for num in nums:
    if num == 3:
        print('Found the number 3!')
        break
    print(num)

# continue
for num in nums:
    if num == 3:
        print('Found the number 3!')
        continue
    print(num)

# Loops within a loop
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Run through a loop x times  (0-9)
for i in range(10):
    print(i)

# Run through a loop x times  (1-10)
for i in range(1, 11):
    print(i)

# While loop
x = 0

while x < 10:
    print(x)
    x += 1

# Break a loop
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# A more simple loop
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1

"""
Conditionals and Booleans

Equal: ==
Not Equal: !=
Greater than: >
Less than: <
Greater or Equal: >=
Less or Equal: <=
Object identity: is
"""

# A string comparison
language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Bash':
    print('Language is Bash')
else:
    print('Language was not matched')

# A number comparison
number = 5

if number == 4:
    print('Number conditional was True')
else:
    print('Number conditional was Not True')


# Structural Pattern Matching - python version 3.10 (released 4th October)
# status = 404
#
# match status:
#     case 400:
#         return "Bad request"
#     case 404:
#         return "Not found"
#     case 418:
#         return "I'm a teapot"
#     case _:
#         return "Something's wrong with the internet"

# Booleans
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin user is logged in')
else:
    print('Admin user is not logged in')

if not logged_in:
    print("Please log in")
else:
    print("Welcome")


# Object identity - Two objects can be equal but not be the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a), id(b))
print(a is b)

b = a
print(id(a), id(b))
print(a is b)


# False values:

# condition = False
# condition = None
# condition = 0
condition = ''  # Or any empty sequence, e.g. '', (), []
# condition = {} # Empty mapping

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
