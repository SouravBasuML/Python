import itertools

# ---------------------------------------------------------------------------------------------------------------------
# Iterable: A thing we can iterate over e.g. lists, tuples, dicts, sets etc.
# Iterator: A special object with next_node method
# Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.
# ---------------------------------------------------------------------------------------------------------------------

print('Iterable')
x = [1, 2, 3, 4]            # iterable, not an iterator
# print(next_node(x))       # not allowed. 'list' object is not an iterator
for i in x:
    print(i)                # allowed. Iterable


print('\nIterator')
x = [1, 2, 3, 4]
n = itertools.cycle(x)
for i in range(10):
    print(next(n))      # iterator

# for i in n:            # infinite loop over the list. Iterable
#     print(i)


# Make an Iterable object Iterator
print('\niter() function')
x = [1, 2, 3, 4]
y = iter(x)             # iterator and iterable
for i in y:
    print(i)            # 1, 2, 3, 4

for i in y:
    print(i)            # will iterate only once (which it did above), here it will not print anything


x = [1, 2, 3, 4]
y = iter(x)             # iterator and iterable
next(y)
next(y)
for i in y:             # will print 3, 4
    print(i)


# ---------------------------------------------------------------------------------------------------------------------

line = ['this', 'is', 'a', 'sentence']

print(dir(line))        # has the iter method as list is iterable

itr = iter(line)        # itr is a list_iterator object
print(type(itr))        # <class 'list_iterator'>
print(dir(itr))         # has the next_node method as it is an iterator

print(next(itr))        # this
print(next(itr))        # is
print(next(itr))        # a
print(next(itr))        # sentence
# print(next_node(itr))      # Error. StopIteration exception

for item in line:
    print(item)         # for-loop internally calls the next_node method on the iterator. It takes care of StopIteration


# Reversed Iterator:
itr = reversed(line)    # has the reversed method as list is iterable
print(next(itr))        # sentence
print(next(itr))        # a
print(next(itr))        # is
print(next(itr))        # this
# print(next_node(itr))      # Error. StopIteration exception


# ---------------------------------------------------------------------------------------------------------------------
# Iter example using Remote Control
# ---------------------------------------------------------------------------------------------------------------------

class RemoteControl:
    def __init__(self):
        self.channels = ['hbo', 'cnn', 'espn', 'bbc']
        print(self.channels)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

    def __reversed__(self):
        self.index -= 1
        if self.index == -1:
            raise StopIteration
        return self.channels[self.index]


r = RemoteControl()
print('\nRemote Control:')
itr = iter(r)
channel_seq = ['+', '+', '+', '-', '-', '+', '+', '+', '-', '-', '-']

for seq in channel_seq:
    if seq == '+':
        print(seq, ': ', next(itr))
    if seq == '-':
        print(seq, ': ', reversed(itr))
