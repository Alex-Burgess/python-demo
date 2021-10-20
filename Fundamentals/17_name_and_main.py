# my_test_module has an example of using __main__.
# This shows that the __name__ of the test module is set to the name of the module.

# Note that name python modules with numbers is not such a good idea, but it can be worked around.
# import my_test_module

__import__('17_test_module')


print("Main execution module's name: {}".format(__name__))  # This shows that the __name__ is set to __main__.
