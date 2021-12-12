import datetime
from functools import reduce
from timeit import timeit
import numpy as np

# ---------------------------------------------------------------------------------------------------------------------
# all, any, bool, enumerate, eval and exec, filter, format, hash, map, reduce, repr, timeit, zip
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# Calling a function with () executes the function and returns the value to the caller.
# Calling a function without () returns the reference of the callable function to the caller. It is up to the caller
# to decide what to do with the returned function reference.
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# all():
# ---------------------------------------------------------------------------------------------------------------------
# The all() function is an inbuilt function which returns true if all the elements of a given iterable (List, Dict,
# Tuple, Set, String etc.) are True else it returns False. It also returns True if the iterable object is empty.
# ---------------------------------------------------------------------------------------------------------------------
# print(all([]))                                  # True
# print(all([1 == 1, 'A' == 'A']))                # True
# print(all([1 == 1, 'A' == 'a']))                # False
# print(all([1 == 1, False]))                     # False
# print(all([True, True, False]))                 # False
# print(all([1, 2, 3, -4]))                       # True
# print(all([1, 2, 0, -4]))                       # False

# # Determine if an array of integers is monotonic (increasing or decreasing)
# a = [9, 8, 8, 7, 7, 2, 1, 2]
# print(all(a[i+1] >= a[i] for i in range(len(a) - 1)) or all(a[i+1] <= a[i] for i in range(len(a) - 1)))


# ---------------------------------------------------------------------------------------------------------------------
# any():
# ---------------------------------------------------------------------------------------------------------------------
# The any() function is an inbuilt function in Python which returns true if any element of a given iterable
# (List, Dict, Tuple, set, etc) is True else it returns False.
# It returns False if all the elements are False. It also returns False if the iterable object is empty.
# ---------------------------------------------------------------------------------------------------------------------
# print(any([]))                                  # False
# print(any([1 == 1, 'A' == 'A']))                # True
# print(any([1 == 1, 'A' == 'a']))                # True
# print(any([1 == 1, False]))                     # True
# print(any([1 == 2, False]))                     # False
# print(any([True, True, False]))                 # True
# print(any([1, 2, 3, -4]))                       # True
# print(any([1, 2, 0, -4]))                       # True


# ---------------------------------------------------------------------------------------------------------------------
# bool():
# ---------------------------------------------------------------------------------------------------------------------
# The bool() method is used to return or convert a value to a Boolean value i.e., True or False,
# using the standard truth testing procedure.
# ---------------------------------------------------------------------------------------------------------------------
# print()bool(False)          # False
# print(bool(True))           # True
# print(bool(None))           # False
# print(bool(0.0))            # False
# print(bool(1))              # True
# print(bool([]))             # False. Empty list
# print(bool(()))             # False. Empty tuple
# print(bool({}))             # False. Empty set
# print(bool(''))             # False. Empty string
# print(bool('a'))            # True
# print(bool(8 % 2 == 0))     # True


# ---------------------------------------------------------------------------------------------------------------------
# enumerate():
# ---------------------------------------------------------------------------------------------------------------------
# Working with list index. Returns index and value of the iteration as a tuple
# You can enumerate lists, tuples, dictionaries, and sets
# ---------------------------------------------------------------------------------------------------------------------

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))                     # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# print(list(enumerate(seasons, start=1)))            # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
#
# for index, season in enumerate(seasons, start=1):
#     print(index, season)                            # tuple returned is unpacked into 2 variables index and season
#
# season_dict = dict(enumerate(seasons, start=1))
# print(season_dict)                                  # {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}


# ---------------------------------------------------------------------------------------------------------------------
# eval() and exec():
# ---------------------------------------------------------------------------------------------------------------------
# a = 3
# b = eval('a + 2')           # Evaluates expressions
# print('b =', b)             # 5
#
# exec('c = a ** 2')          # Executing Statements
# print('c is', c)            # 9


# ---------------------------------------------------------------------------------------------------------------------
# filter():
# ---------------------------------------------------------------------------------------------------------------------
# filter(function, iterable object)
# 'Function' (user defined or lambda) is a boolean condition, that rejects all the items in the iterable object that
# are not true. Iterable object can be List, Dict, Tuple, Set, String etc.
# Filters a sequence via a function, which checks each element in the iterator is true or not and returns a filtered
# sequence. The sequence can be sets, lists, tuples, or containers of any iterators
# ---------------------------------------------------------------------------------------------------------------------
# def vowel_func(letter):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return True if letter in vowels else False            # function has to return a boolean for filter to be applied
#
#
# letter_sequence = ['g', 'e', 'e', 'j', 'i', 's', 'a', 'u', 'r', 'o', 'a']
# filtered_seq = filter(vowel_func, letter_sequence)
# print(list(filtered_seq))


# ---------------------------------------------------------------------------------------------------------------------
# format():
# ---------------------------------------------------------------------------------------------------------------------
# The format method can be used to return a formatted representation of an object that is controlled by a
# format specifier. These methods call the internal __format__() function of an object. It takes two arguments,
# the value we would like to format and the format specifications.
# https://pyformat.info/
# ---------------------------------------------------------------------------------------------------------------------
# print(format(1392391237, "b"))                  # 1010010111111100011010001000101
#
# print('{} {}'.format(1, 2))                     # 1 2
# print('{:>10}'.format('test'))                  # Align Right: '       test'
# print('{:10}'.format('test'))                   # Align Left : 'test      '
# print('{:_<10}'.format('test'))                 # Align right with padding: 'test______'
# print('{:^10}'.format('test'))                  # Align center: '   test   '
# print('{:.5}'.format('xylophone'))              # Truncate: 'xylop'
#
# print('{:d}'.format(42))                        # 42
# print('{:f}'.format(3.141592653589793))         # 3.141593
# print('{:4d}'.format(42))                       # '  42'
# print('{:06.2f}'.format(3.141592653589793))     # 003.14
# print('{:04d}'.format(42))                      # 0042
# print('{:+d}'.format(42))                       # +42
# print('{:=5d}'.format((- 23)))                  # -  23
# print('{:=+5d}'.format(23))                     # +  23
#
# print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))           # 2001-02-03 04:05


# ---------------------------------------------------------------------------------------------------------------------
# hash():
# ---------------------------------------------------------------------------------------------------------------------
# The hash() function is used to return the hash value of an object in Python. A hash will be a signed integer that is
# used to express that given value. The function takes an object as an argument
# ---------------------------------------------------------------------------------------------------------------------
# print(hash(10.0))               # 10 (Interning - remains unchanged)
# print(hash(10.1))               # 230584300921368586 (keeps changing)
#
# print(hash('Hello'))            # -9091121333054745971 (keeps changing)
#
# print(hash(True))               # 1 (Interning - remains unchanged)
# print(hash(None))               # -9223363242553030195 (Interning - remains unchanged)
# print(hash(False))              # 0 (Interning - remains unchanged)
#
# print(hash(__name__))           # 6561575834942770975 (keeps changing)


# ---------------------------------------------------------------------------------------------------------------------
# map():
# ---------------------------------------------------------------------------------------------------------------------
# map(function, iterable object)
# The map function applies a given function (user defined or lambda) evenly to each element of an iterable.
# Iterable object can be List, Dict, Tuple, Set, String etc.
# ---------------------------------------------------------------------------------------------------------------------
# def add_one(item):
#     return item+1
#
#
# my_list = [10, 20, 30, 40]
#
# new_list = map(add_one, my_list)
# print(new_list)                             # <map object at 0x000001CD6876ED90>
# print(type(new_list))                       # <class 'map'>
#
# new_list = list(map(add_one, my_list))
# print(new_list)                             # [11, 21, 31, 41]


# ---------------------------------------------------------------------------------------------------------------------
# reduce():
# ---------------------------------------------------------------------------------------------------------------------
# from functools import reduce
# reduce (function, iterable object)
# reduce() takes an existing function, applies it cumulatively to all the items in an iterable, and generates a single
# final value, without the use of for loops. It implements a mathematical technique known as folding or reduction.
# ---------------------------------------------------------------------------------------------------------------------
# def my_add(a, b):
#     result = a + b
#     print(f"{a} + {b} = {result}")
#     return result
#
#
# my_list = [1, 2, 3, 4, 5]
# reduce(my_add, my_list)
#
# print('\nThe sum of the list elements is: ', end='')
# print(reduce(lambda a, b: a+b, my_list))
#
# print('\nMax element of the list is: ', end='')
# print(reduce(lambda a, b: max(a, b), my_list))


# ---------------------------------------------------------------------------------------------------------------------
# repr()
# ---------------------------------------------------------------------------------------------------------------------
# Goal of __repr__ is to be unambiguous
# Goal of __str__ is to be readable
# ---------------------------------------------------------------------------------------------------------------------
# a = [1, 2, 3, 4]
# b = 'this is a string'
# c = datetime.datetime.utcnow()
# d = str(c)
#
# print('\nstr() - Readable:')
# print(str(a))
# print(str(b))
# print(str(c))
# print(str(d))
#
#
# print('\nrepr() - Unambiguous:')
# print(repr(a))
# print(repr(b))
# print(repr(c))
# print(repr(d))


# ---------------------------------------------------------------------------------------------------------------------
# timeit():
# ---------------------------------------------------------------------------------------------------------------------
# from timeit import timeit
# To measure execution time of Python code. It returns the number of seconds it took to execute the code snippet
# a certain number of times.
# ---------------------------------------------------------------------------------------------------------------------
# def while_loop(n=100_000_000):          # Add 1 to 100_000_000 using while loop
#     i = 0
#     s = 0
#     while i < n:                        # iteration happens in Python
#         s += i                          # summation happens in Python
#         i += 1
#     return s
#
#
# def for_loop(n=100_000_000):            # Add 1 to 100_000_000 using for loop
#     s = 0
#     for i in range(n):                  # iteration happens in C
#         s += i                          # summation happens in Python
#     return s
#
#
# def sum_range(n=100_000_000):           # Add 1 to 100_000_000 using built-in functions instead of loops
#     return sum(range(n))
#
#
# def sum_numpy(n=100_000_000):           # Add 1 to 100_000_000 using Numpy Array. Numpy  is written in C and Fortran
#     return np.sum(np.arange(n))         # arange creates an array of size 100 million in memory; not memory efficient
#
#
# def sum_math(n=100_000_000):            # Add 1 to 100_000_000 using math
#     return n * (n - 1) // 2
#
#
# print('While Loop:\t\t', timeit(while_loop, number=1))          # 8.15 secs
# print('For Loop:\t\t', timeit(for_loop, number=1))              # 4.84 secs
# print('Sum Range:\t\t', timeit(sum_range, number=1))            # 3.19 secs
# print('Numpy Sum:\t\t', timeit(sum_numpy, number=1))            # 0.27 secs
# print('Math Sum:\t\t', timeit(sum_math, number=1))              # 3.1 e-06 secs


# ---------------------------------------------------------------------------------------------------------------------
# code snippet to be executed only once
# mysetup = "from math import sqrt"
#
# # code snippet whose execution time is to be measured
# mycode = '''
# def example():
#     mylist = []
#     for x in range(100):
#         mylist.append(sqrt(x))
# '''
#
# no_of_exec = 1_000_000
#
# # timeit statement (returns number of seconds to execute)
# # from timeit import timeit
# exec_time = timeit(setup=mysetup, stmt=mycode, number=no_of_exec)
# print(f'Time taken for {no_of_exec:,} executions: {exec_time} seconds.')
# print(f'Time taken for 1 executions: {exec_time / no_of_exec} seconds.')


# ---------------------------------------------------------------------------------------------------------------------
# zip():
# ---------------------------------------------------------------------------------------------------------------------
# To iterate over multiple lists simultaneously
# The zip function creates a new iterator out of multiple iterables and allows one to iterate over multiple elements
# of different lists at the same time in the same cycle.
# Will iterate till the shortest list is exhausted
# To continue till end of longest list, use ziplongest function from the itertools library
# ---------------------------------------------------------------------------------------------------------------------
# print('\nZip:')
# A = ['A1', 'A2', 'A3', 'A4']
# B = ['B1', 'B2', 'B3', 'B4']
# C = ['C1', 'C2', 'C3', 'C4']
#
# for a, b, c in zip(A, B, C):
#     print(a, b, c)      # tuple returned by zip is unpacked in 3 variables
#
# for values in zip(A, B, C):
#     print(values)       # prints a tuple

# A = [23, 28, 43, 23, 23, 94, 32]
# B = [34, 58, 109, 72, 33, 2, 90]
# C = []
#
# for a, b in zip(A, B):
#     C.append((a+b)/2)
# for values in zip(A, B, C):
#     print(values)
# ---------------------------------------------------------------------------------------------------------------------
