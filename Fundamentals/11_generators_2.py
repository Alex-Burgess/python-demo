'''
Example of performance difference
'''
import memory_profiler as mem_profile
import random
import time


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)

    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        yield person


# t1 = time.process_time()
# people = people_list(1000000)
# t2 = time.process_time()

'''
Result:
Memory (Before): [37.80078125]Mb
Memory (After): [304.546875]Mb
Took 1.7925419999999999 Seconds
[Finished in 2.851s]
'''


t1 = time.process_time()
people = people_generator(1000000)
t2 = time.process_time()

'''
Result:
Memory (Before): [37.8671875]Mb
Memory (After): [37.87890625]Mb
Took 1.0000000000010001e-05 Seconds
[Finished in 1.232s]

Note: No memory has been assigned and no time was taken, because with the generator, it didn't actually do anything (yet)
'''

print('Memory (After): {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))
