from operator import attrgetter

'''
Sorting lists
'''
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# Create a new variable with sorted list
s_li = sorted(li)
# s_li = sorted(li, reverse=True)
print('Sorted Variable:\t', s_li)
print('Original Variable: \t', li)

# Sort the original list
li.sort()
# li.sort(reverse=True)
print('Original Variable: \t', li)

'''
Sorting tuples
'''
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('Tuple\t', s_tup)     # Note this is a list
print('Tuple\t', tuple(s_tup))     # Note this is a tuple

'''
Sorting dicts
'''
di = {'name': 'corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Sorted Dict keys: \t', s_di)


'''
Sorting objects with named attributes - version 1 - sorting function
'''


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


# We have a list of employees, that we want to sort
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
employees = [e1, e2, e3]


# Version 1 - sorting function
# def e_sort(emp):
#     return emp.age
#
#
# sorted_emps = sorted(employees, key=e_sort)
# print(sorted_emps)


# Version 2 - lambda function
# sorted_emps = sorted(employees, key=lambda emp: emp.salary)
# print(sorted_emps)

# Version 3 - attrgetter
sorted_emps = sorted(employees, key=attrgetter('age'))
print(sorted_emps)
