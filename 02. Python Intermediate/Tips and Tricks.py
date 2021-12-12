from getpass import getpass

# ---------------------------------------------------------------------------------------------------------------------
# Ternary Operators, Underscore Placeholders, Context Managers, Unpacking,
# Dynamic attributes for Classes and Functions, Entering Password, For-Else Loop, Yield
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Ternary Operators:
# ---------------------------------------------------------------------------------------------------------------------
# print('\nTernary Operator:')
# a = 5
# b = 3
# x = "large" if a > b else "small"
# print(x)


# ---------------------------------------------------------------------------------------------------------------------
# Underscore placeholders:
# ---------------------------------------------------------------------------------------------------------------------
# print('\nUnderscore placeholders:')
# num1 = 10_000_000_000
# num2 = 100_000_000
# total = num1 + num2
# print(f'{total:,}')


# ---------------------------------------------------------------------------------------------------------------------
# Context Managers - to manage resources - files, threads, locks, db connections
# No need to close file manually
# ---------------------------------------------------------------------------------------------------------------------
# with open('../Python Basics/Employees.txt', 'r') as f:
#     file_contents = f.read()


# ---------------------------------------------------------------------------------------------------------------------
# Unpacking
# ---------------------------------------------------------------------------------------------------------------------
# print('\nUnpacking:')
# a, b = (1, 2)
# c, _ = (1, 2)                   # if you are using only first value
# print(a)
# print(b)
# print(c)
#
# # a, b, c = (1, 2)              # ValueError
# # a, b, c = (1, 2, 3, 4, 5)     # ValueError
#
# print('\n')
# a, b, *c = (1, 2, 3, 4, 5)
# print(a)            # 1
# print(b)            # 2
# print(c)            # [3, 4, 5]
#
# print('\n')
# a, b, *_ = (1, 2, 3, 4, 5)    # ignores the rest
# print(a)            # 1
# print(b)            # 2
#
# print('\n')
# a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
# print(a)            # 1
# print(b)            # 2
# print(c)            # [3, 4, 5, 6]
# print(d)            # 7
#
# print('\n')
# a, b, *_, d = (1, 2, 3, 4, 5, 6, 7)
# print(a)            # 1
# print(b)            # 2
# print(d)            # 7


# ---------------------------------------------------------------------------------------------------------------------
# Add Dynamic Attributes to Classes:
# Get and Set Attributes on class objects
# ---------------------------------------------------------------------------------------------------------------------
# class Person:
#     pass
#
#
# person = Person()
#
# # we can dynamically add attributes and values to the objects
# person.firstname = 'Sourav'
# person.lastname = 'Basu'
#
# print('\nClass: setattr(), getattr()')
# print(person.firstname)
# print(person.lastname)
#
# # Attribute that we want to set is the value of another variable
# first_key = 'first'
# first_value = 'Sayani'
#
# setattr(person, first_key, first_value)
# print(person.first)         # Sayani
#
# first = getattr(person, first_key)
# print(first)                # Sayani

# ---------------------------------------------------------------------------------------------------------------------
# person.__setattr__('first', 'Sourav')
# person.__setattr__('last', 'Basu')
#
# print(person.__getattribute__('first'))
# print(person.__getattribute__('last'))
#
# print(dir(person))
# print(emp.__delattr__('first'))
# print(dir(person))


# ---------------------------------------------------------------------------------------------------------------------
# Setting Attributes to Functions:
# ---------------------------------------------------------------------------------------------------------------------
# def func(x):
#     intermediate_var = x**2 + x + 1
#
#     if intermediate_var % 2:
#         y = intermediate_var ** 3
#     else:
#         y = intermediate_var ** 3 + 1
#
#     # setting attributes here
#     func.optional_return = intermediate_var
#     func.is_awesome = 'Yes, my function is awesome.'
#
#     return y
#
#
# print('Final answer is', func(3))
# # # Accessing function attributes
# print('Show calculations -->', func.optional_return)
# print('Is my function awesome? -->', func.is_awesome)


# ---------------------------------------------------------------------------------------------------------------------
# Passwords:
# ---------------------------------------------------------------------------------------------------------------------
# print('\nInputting Passwords')
#
# username = input('Username: ')
# password = getpass('Password: ')        # from getpass import getpass
# print('Logging In...')


# ---------------------------------------------------------------------------------------------------------------------
# For-Else:
# ---------------------------------------------------------------------------------------------------------------------
# my_list = ['some', 'list', 'containing', 'five', 'elements']
# min_len = 3
#
# # 'Else' will execute only if no 'break' is encountered in the for loop
# for element in my_list:
#     if len(element) < min_len:
#         print(f'Caught an element shorter than {min_len} letters')
#         break
# else:
#     print(f'All elements at least {min_len} letters long')


# ---------------------------------------------------------------------------------------------------------------------
# Yield:
# The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state
# to enable function to resume where it is left off. When resumed, the function continues execution immediately after
# the last yield run. Unlike return, yield allows its code to produce a series of values over time, rather than
# computing them at once and sending them back like a list.
# ---------------------------------------------------------------------------------------------------------------------
# def next_square():
#     i = 1
#     # An Infinite loop to generate squares
#     while True:
#         yield i * i
#         i += 1  # Next execution resumes from this point
#
#
# # Driver code to test above generator function
# for num in next_square():
#     if num > 100:
#         break
#     print(num)

# ---------------------------------------------------------------------------------------------------------------------
# def print_even(my_list):
#     for i in my_list:
#         if i % 2 == 0:
#             yield i
#
# my_list = [1, 4, 5, 6, 7]
# print ('Even numbers :')
# for j in print_even(my_list):
#     print (j)


# ---------------------------------------------------------------------------------------------------------------------
# Misc:
# ---------------------------------------------------------------------------------------------------------------------
# z = {**x, **y}            # Merge 2 dictionaries
# a, b = b, a               # Swapping
# x, = y                    # Pattern matching
# not not x                 # It is is faster than bool(x)
# a, b = 1, 2               # Tuple assignment
# a = b = c = d = 1         # Multiple assignment
# a, b = a[:] = [[]], []    # Cyclic reference a = [[...], b = []]
# x < y < z                 # Chained comparison. True if y is between x and z. Same as x < y and y < z
