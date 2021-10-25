###################################
# Lists
###################################
# Empty list definition
empty_list = []
print(empty_list)

# lists are defined with square brackets
courses = ['History', 'Math', 'Physics', 'Science']
print(courses)

# Items can be accessed by their index
print(courses[2])
print(courses[-1])


# It is possible to access multiple items (aka slicing)
print(courses[0:2])     # All values from the beginning and up to, but not including the 2nd index
print(courses[1:3])     # All values from index 1 and up to, but no including the 3rd index
print(courses[0:-1])    # All values from the beginning and up to, but no including the last index (whatever that is)
print(courses[2:])      # All values from the 2nd index, up to and including the last index

# Append - add a new course to the end of the list
courses.append('Art')
print(courses)

# Insert - add a new course to a specified location in the list
courses.insert(0, 'P.E')
print(courses)

courses.insert(2, 'I.T')
print(courses)

# Extend
extra_courses = ['General Studies', 'Philosophy']
courses.extend(extra_courses)
print(courses)

# Remove - Remove a specific item
courses.remove('History')
print(courses)

# Pop - Remove the last item, useful if you want to use your list like a queue
popped = courses.pop()
print(popped)

# Reverse list
courses.reverse()
print(courses)

# Sort - will sort in alphabetical, or numberical order
letters = ['c', 'a', 'b', 'd']
letters.sort()
print(letters)

nums = [3, 4, 2, 1, 5]
nums.sort()
print(nums)

# Sort in reverse
nums = [3, 4, 2, 1, 5]
nums.sort(reverse=True)
print(nums)

# Sort without altering the list in place
letters = ['c', 'a', 'b', 'd']
sorted_letters = sorted(letters)
print(letters)
print(sorted_letters)

# min, max, sum
print(min(nums))
print(max(nums))
print(sum(nums))

# Check if a value is in the list
print('Art' in courses)

# How to iterate
for course in courses:
    print(course)

# How to iterate and display the index at the same time.
for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):   # Alter start index
    print(index, course)

# how to join a list, and split a list
course_str = ','.join(courses)
print(course_str)

new_list = course_str.split(',')
print(new_list)


###################################
# Tuples
###################################

# empty tuple definition
empty_tuple = ()
print(empty_tuple)


# Mutable vs immutable
list_1 = ['Math', 'Physics', 'History', 'Science']
list_2 = list_1     # List 1 and 2 are now both the same mutable object
list_1[0] = 'Art'
print('Art was added to both lists')
print(list_1)
print(list_2)


tuple_1 = ('Math', 'Physics', 'History', 'Science')
tuple_2 = tuple_1
# tuple_1[0] = 'Art'    # This will cause an error


###################################
# Sets
###################################

# empty set definition
# empty_set = {}    # No this is a dict
empty_set = set()
print(empty_set)

# Sets are very efficient at 'membership tests'
courses = {'History', 'Math', 'Physics', 'Science'}
print('Math' in courses)
print('P.E' in courses)

# Remove duplicates
courses.add('P.E')
courses.add('Math')
print(courses)

# Find differences
cs_courses = {'History', 'Math', 'Physics', 'Science'}
eng_courses = {'Design', 'Math', 'Physics', 'Science'}
print(cs_courses.difference(eng_courses))
print(cs_courses.intersection(eng_courses))
print(cs_courses.union(eng_courses))
