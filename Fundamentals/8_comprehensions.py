'''
List Comprehensions
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
Basics, traditional vs list comprehension
'''
# Traditional for loop
my_list = []
for n in nums:
    my_list.append(n)

print(my_list)

# list comprehension
# new_list = [expression for member in iterable]
my_list = [n for n in nums]
print(my_list)


'''
Second example - return the square for each 'n' in nums
'''
my_list = [n*n for n in nums]
print(my_list)

'''
Map and lambda example - a less readable way of doing the same as a list comprehension
'''
# object = map(function, iterable)
my_list = map(lambda n: n*n, nums)
print(list(my_list))


'''
I want 'n' for each 'n' in nums if 'n' is even
'''
my_list = [n for n in nums if n % 2 == 0]
print(my_list)


'''
Nested for loops with list comprehensions
I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
'''
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)


'''
Dictionary comprehensions
'''
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# my_list = zip(names, heros)
# print(list(my_list))

# traditional approach
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero

print(my_dict)

# dict comprehension
my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

'''
Set comprehensions
'''
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = {num for num in nums}
print(my_set)
