# Quick Tip 1: Docstrings
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")

# print(say_hello.__doc__)
# print(help(say_hello))


# Quick Tip 2: F Strings
def f_string_demo(first_name, last_name):
    """Prints out a quick message with someones name"""

    # format example
    sentence = 'My name is {} {}.'.format(first_name, last_name)
    print(sentence)

    # f-string example
    sentence = f'My name is {first_name} {last_name}.'
    print(sentence)


f_string_demo('Alex', 'Burgess')
