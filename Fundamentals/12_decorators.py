###################################
# Decorators
###################################

# See inner and outer functions
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function()


outer_function()


# Return a closed function
def outer_function_2(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function


hi_func = outer_function_2('Hi')
bye_func = outer_function_2('Bye')

hi_func()
bye_func()


#  A decorator is very similar, it takes a function as a function argument and modifies it.
# The decorator function is sort of waiting to be executed.
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)
decorated_display()


# Or using the decorator syntax makes it easier to read
# This reads as, i want my display function, now equal to my decorator_function with the display function passed in.
@decorator_function
def display_2():
    print('display function ran')


display_2()

###################################
# Decorator demo 2
###################################
# def another_function(func):
#     """
#     A function that accepts another function
#     """
#
#     def other_func():
#         val = "The result of %s is %s" % (func(),
#                                           eval(func())
#                                           )
#         return val
#     return other_func
#
#
# @another_function
# def a_function():
#     """A pretty useless function"""
#     return "1+1"
#
#
# if __name__ == "__main__":
#     value = a_function()
#     print(value)
