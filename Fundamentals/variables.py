"""
Strings
"""

# Strings can be single of double quotes
mystring = 'Hello, World!'
print(mystring)

mystring = "Hello, World!"
print(mystring)

# Double quotes allow apostrophes
mystring = "A famous philosopher one wrote, 'blah...'"
print(mystring)

# Strings can be joined
statement = 'My name is: '
name = 'Alex'
print(statement + name)


"""
Numbers
"""

# Integers and floats can be defined without declaring their types
myint = 7
print(myint)

myfloat = 13.0
print(myfloat)

# You can change number type using int and float
print(int(myfloat))
print(float(myint))

# It is possible to assign multiple variables "simultaneously"
a, b = 3, 4
print(a, b)
