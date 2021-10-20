'''
Create a Sentence object that has an iterator that allows the words of the sentence to be looped over.

my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)

Expected output:
This
is
test

Create a class with an iterator to solve this problem.
Then create a generator to solve this problem.

Remember an iterator is an object with state so that it remembers where it is during iteration.
'''


'''
Class Solution
'''


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0      # We will return an iterator, so index will remember the state
        self.words = self.sentence.split()  # Splits on whitespace by default.

    def __iter__(self):
        return self

    def __next__(self):
        # Option 1
        # try:
        #     word = self.words[self.index]
        #     self.index += 1
        #     return word
        # except:
        #     raise StopIteration

        # Option 2
        if self.index >= len(self.words):
            raise StopIteration
        else:
            word = self.words[self.index]
            self.index += 1
            return word


my_sentence = Sentence('This is a test')

# Words as an iterable
# for word in my_sentence:
#     print(word)

# Also works as an iterator
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
# print(next(my_sentence))   # Will raise stop iteration exception


'''
Generator Solution

This is a lot simpler because it takes care of the iter and next methods
'''


def g_sentence(sentence):
    for word in sentence.split():
        yield(word)


my_sentence = g_sentence('This is a test')

# for word in my_sentence:
#     print(word)

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
# print(next(my_sentence))   # Will raise stop iteration exception
