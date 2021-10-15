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
"""
