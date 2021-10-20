'''
Exception handling
'''

# Basic try, except block
try:
    f = open('testfile.txt')
except Exception:
    print('Sorry. This file does not exist!')


# Catch more specific or expected exceptions
try:
    f = open('Fundamentals/test_file.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist!')

# Chain exceptions
try:
    f = open('Fundamentals/test_file.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist!')
except Exception:
    print('Sorry. Something went wrong!')

# Print the exception error message
try:
    f = open('testfile.txt')
except Exception as e:
    print(e)


# Using Else statements.
try:
    f = open('Fundamentals/test_file.txt')
except FileNotFoundError:
    print('Sorry. This file does not exist!')
else:
    print(f.read())
    f.close()

# With the code above, we can be really specific about what we are catching.
# We could write it as follows but then it's not quite as clear
try:
    f = open('Fundamentals/testfile.txt')
    print(f.read())
    f.close()
except FileNotFoundError:
    print('Sorry. This file does not exist!')


# using finally
try:
    f = open('Fundamentals/testfile.txt')
except FileNotFoundError:
    print('Sorry. This file does not exist!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally....")


# Raising exceptions
try:
    f = open('Fundamentals/test_file.txt')
    if f.name == 'Fundamentals/test_file.txt':
        raise Exception
except FileNotFoundError:
    print('Sorry. This file does not exist!')
except Exception:
    print('Sorry. Something went wrong!')
