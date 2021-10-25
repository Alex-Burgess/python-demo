###################################
# LEGB - Local, Enclosing, Global, Built-in
###################################

###################################
# Basic example of global and local
# result:
# local y
# global x
###################################
# x = 'global x'
#
#
# def test():
#     y = 'local y'
#     print(y)    # Prints the variable local to the function
#     print(x)    # Prints the global variable x
#
#
# test()
# print(x)    # Prints the global variable x
# #print(y)    # This will give a name 'y' is not defined error.


###################################
# Demonstrating local is a high order than global.
# result:
# local x
# global x
###################################
# x = 'global x'
#
#
# def test():
#     x = 'local x'   # Creates a local x variable that exists only inside this function
#     print(x)    # Prints the global variable x
#
#
# test()
# print(x)    # Prints the global variable x

###################################
# Demonstrating global keyword.
# result:
# local x
# local x
###################################
# x = 'global x'
#
#
# def test():
#     global x
#     x = 'local x'   # Creates a local x variable that exists only inside this function
#     print(x)    # Prints the global variable x
#
#
# test()
# print(x)    # Prints the global variable x


###################################
# Print out some Built-in names
###################################
# import builtins
# print(dir(builtins))


###################################
# An example of overriding a built in name.  The min function is a built function for finding the min value.
# If we override it, our function will use the global function, before the built-in function and we get an error.
###################################
# def min():
#     pass
#
#
# m = min([5, 1, 4, 8, 3])
# print(m)


###################################
# Enclosing variables
###################################
# def outer():
#     x = 'outer x'
#
#     def inner():
#         print(x)    # This is set at the enclosing function
#
#     inner()
#     print(x)
#
#
# outer()


###################################
nonlocal example
###################################


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)    # This is set at the enclosing function

    inner()
    print(x)


outer()
