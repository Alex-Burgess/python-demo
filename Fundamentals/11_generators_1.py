###################################
# Generator basics
# Basic function example, which we'll later convert to a generator
###################################


def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)


# Generator equivalent

def square_numbers(nums):
    for i in nums:
        yield(i*i)


my_nums = square_numbers([1, 2, 3, 4, 5])


# print(my_nums)  # prints generator object
# print(next(my_nums))    # Demonstrates how yield runs one number at a time
# print(next(my_nums))
# print(next(my_nums))

for num in my_nums:
    print(num)


###################################
# Writing a generator as a list comprehension
###################################
# List comprehension
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums)

# Generator as a list comprehension
my_nums = (x*x for x in [1, 2, 3, 4, 5])
# print(my_nums)
# print(list(my_nums))  # This will print the values, but loses the performance benefits.
for num in my_nums:
    print(num)


###################################
# Example 1: Reading large files
# https://realpython.com/introduction-to-python-generators/
# If the file was very large, loading everying into memory could cause a MemoryError.
# By using a generator, you can open the file, iterate through it, and yield a row.
###################################
# def csv_reader(file_name):
#     for row in open(file_name, "r"):
#         yield row

# Or as a generator expression
# csv_gen = (row for row in open(file_name))


###################################
# Example 2: Generating an Infinite sequence
# range() is a finite sequence, using a generator you can create an infinite sequence.
###################################
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

# for i in infinite_sequence():
#     print(i, end=" ")
