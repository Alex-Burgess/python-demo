###################################
# Iterators and iterables.
#
# An iterable is something that can be looped over, e.g. a list.
# An iterator is an object with a state so that it remembers where it is during iteration.
# An iterator can also be an iterable.
###################################

# Iterable
nums = [1, 2, 3]

print(dir(nums))    # __iter__() method exists, but no __next__() method.
# print(next(nums))   # TypeError: 'list' object is not an iterator

# Iterator
i_nums = iter(nums)
print(dir(i_nums))    # __iter__() method and __next__() method both exist.
print(next(i_nums))   # prints 1
print(next(i_nums))   # prints 2
print(next(i_nums))   # prints 3


# How to loop an iterator, without getting the StopIteration error
i_nums = iter(nums)
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


# An example of a class that is both an iterable and an iterator
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


my_nums = MyRange(1, 11)
for num in my_nums:
    print(num)

my_nums = MyRange(1, 11)
print(next(my_nums))


# Generator example - both an iterabe and an iterator
def square_numbers(nums):
    for i in nums:
        yield(i*i)


my_square_nums = square_numbers([1, 2, 3, 4, 5])

print(dir(my_square_nums))

# Convert an iterator to an iterable?
print(my_square_nums)   # prints generator object
print(list(my_square_nums))  # prints a list (which is an iterable)
