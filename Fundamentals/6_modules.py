"""
modules
"""
import random
import sys

# Basic import
# import my_module
#
# courses = ['History', 'Math', 'Physics', 'CompSci']
#
# index = my_module.find_index(courses, 'Math')
# print(index)


# Import as
# import my_module as mm
#
# courses = ['History', 'Math', 'Physics', 'CompSci']
#
# index = mm.find_index(courses, 'Math')
# print(index)


# import from
# from my_module import find_index
# courses = ['History', 'Math', 'Physics', 'CompSci']
#
# index = find_index(courses, 'Math')
# print(index)


# import from with as
from my_module import find_index as fi
courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')
print(index)


# sys path
print(sys.path)


# Importing a module from the standard python library
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)
