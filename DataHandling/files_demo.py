# How to open a file, using the best practice of a context manager.
with open('DataHandling/test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# If the file is very large, you will want to avoid loading all the contents into memory
with open('DataHandling/test.txt', 'r') as f:
    for line in f:
        print(line, end='')

# You can also read in files in batches of characters
with open('DataHandling/test.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)


# Write to a file
with open('DataHandling/test2.txt', 'w') as f:
    f.write('Test')
    f.write('Test')


# Using seek when writing a file
with open('DataHandling/test2.txt', 'w') as f:
    f.write('Testing')
    f.seek(0)
    f.write('Blah')


# Reading a writing to a file
with open('DataHandling/test.txt', 'r') as rf:
    with open('DataHandling/test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
