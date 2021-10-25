###################################
# Functions
###################################


# An empty function
def empty_func():
    pass


empty_func()


# Return a value
def hello_func():
    return 'Hello Function.'


print(hello_func())


# Wrapping and Chaining functions
print(len(hello_func()))
print(hello_func().upper())


# Input parameters (with default values):
def hello_func(greeting, name='You'):
    return '{}, {}.'.format(greeting, name)


print(hello_func('Hello!'))
print(hello_func('Hi', 'Alex'))


# *args, **kwargs - (Note, tuple and dictionary)
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

# Passing in a list (or tuple) and a dictionary and unpacking the values
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)


# Docstrings
def hello_func(greeting, name='You'):
    """Returns a greeting message."""

    return '{}, {}.'.format(greeting, name)
