###################################
# A basic string concatenation.  The drawbacks are:
# Hard to read
# Easy to get the spaces wrong
###################################
import datetime
person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

###################################
# String format example
###################################
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)

###################################
# String formating with numbering
###################################
tag = 'h1'
text = 'This is a headline'
html = '<{0}>{1}</{0}>'.format(tag, text)
print(html)

###################################
# Numbered Placeholders with dict keys
###################################
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)


###################################
# Using a list
###################################
my_list = ['Jenn', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(my_list)
print(sentence)


###################################
# Using a class
###################################
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)


###################################
# Named placeholders
###################################
sentence = 'My name is {name} and I am {age} years old.'.format(name='Alex', age=23)
print(sentence)

# Or using ** to unpack the dictionary
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)


###################################
# Formating numbers
###################################
# Colon can be used to zero pad the number
for i in range(1, 11):
    sentence = 'The vale is {:02}'.format(i)
    print(sentence)

# Or decimals
for i in range(1, 11):
    sentence = 'The vale is {:.2f}'.format(i)
    print(sentence)


###################################
# Formating Dates
###################################
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence = 'The year is {0:%Y} and the month is {0:%B}'.format(my_date)
print(sentence)


###################################
# F Strings
###################################
person = {'name': 'Jenn', 'age': 23}

# format
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

# f-string

sentence = f"My name is {person['name']} and I am {person['age']} years old."
print(sentence)
