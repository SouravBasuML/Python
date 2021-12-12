import platform
import sys
import ctypes

# ---------------------------------------------------------------------------------------------------------------------
# Memory, id(), ==, is, Singleton Objects, Interning, Garbage Collection, del()
# https://rushter.com/blog/python-garbage-collector/
# ---------------------------------------------------------------------------------------------------------------------
# Note: Output values in comments may not match when this module is executed
# ---------------------------------------------------------------------------------------------------------------------
# Everything in Python is an object:
# Every string, number, list, dictionary, class, function, the boolean objects True and False, and the None object.
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# id(): Returns memory address of an object as an integer.
# ---------------------------------------------------------------------------------------------------------------------
print('Address of 10: ', id(10), hex(id(10)))
print('Address of function str: ', id(str), hex(id(str)))
print('Address of True: ', id(True), hex(id(True)))


stock_price = [298, 305, 320, 301, 292]
print('\nAddress of List: ', id(stock_price), hex(id(stock_price)))

print()
for (i, price) in enumerate(stock_price):
    print('Address of stock_price[', i, ']', id(price), hex(id(price)))


# a and b refer to the same location in memory
print()
a = [1, 2, 3]
b = a
print(id(a), hex(id(a)))
print(id(b), hex(id(b)))

# a and b refer to different locations in memory
print()
a = [1, 2, 3]
b = a.copy()
print(id(a), hex(id(a)))
print(id(b), hex(id(b)))


# ---------------------------------------------------------------------------------------------------------------------
# The "==" can be used to compare two objects and see if they’re equal (i.e. they have the same content)
# The "is" operator will test whether they are the same object, which means they are at the same memory address:
# ---------------------------------------------------------------------------------------------------------------------
a = [1, 2, 3]
b = a
c = a.copy()
print()

# a and b have the same contents, and are the same object
print(a == b)                       # True
print(a is b)                       # True

# a and c have the same contents, but are two different objects at different memory addresses
print(a == c)                       # True
print(a is c)                       # False

# If we add another object to c, it's now got diff contents to a, and it's a diff object at a diff memory address
c.append(5)                         # c = [1, 2, 3, 4, 5], a = [1, 2, 3, 4]
print(a == c)                       # False
print(a is c)                       # False


# ---------------------------------------------------------------------------------------------------------------------
# Singleton Objects: exist only once and at one point in memory for the entire existence of your program.
# ---------------------------------------------------------------------------------------------------------------------
# True, False, None are Singleton Objects
# Every time your function returns True, it’s returning the very same object that pops up every other time you see True.
# You can’t initialise a second, different True object anywhere else in your program.
# ---------------------------------------------------------------------------------------------------------------------
print()
print(True is True)                 # True
print(False is False)               # True
print(None is None)                 # True


# ---------------------------------------------------------------------------------------------------------------------
# Interning: Optimization technique (when Python initialises) for caching or pre-loading a list of objects at start up.
# ---------------------------------------------------------------------------------------------------------------------
# If a value is interned, Python will instantiate one and only one object of its kind, so that it always looks to the
# same object at the same memory address whenever that object is referenced.
# Among other things, Python will instantiate and intern the range of numbers -5 to 256 inclusive (in CPython)
# all of which will be singleton objects. But numbers outside of this range will be instantiated as new integer objects
# as needed, and will be separate objects with different memory addresses.
# In Python optimization, integer interning is the method of caching or pre-loading a list of integers at start up.
# ---------------------------------------------------------------------------------------------------------------------
print('\nInterning:')
print('Python Implementation: ', platform.python_implementation())         # CPython (import platform)

a = 256
b = 256
print(id(a), id(b))
print(a == b)                       # True
print(a is b)                       # True

a = 257
b = 257
print()
print(id(a), id(b))
print(a == b)                       # True
print(a is b)                       # False


# No matter how you create the int obj, if it is the same integer and within the range (-5 to 256) it will be interned
a = 100                             # Direct integer assignment
b = int(100)                        # Using int() built-in function
c = int('100')                      # Converting a string to an integer
d = int('1100100', 2)               # From binary to integer, 2 indicates base for number system

print()
print(a == b == c == d)             # True
print(a is b is c is d)             # True

a = 257                             # Direct integer assignment
b = int(257)                        # Using int() built-in function
c = int('257')                      # Converting a string to an integer

print()
print(a == b == c)                  # True
print(a is b is c)                  # False


# What could you possibly input as x to make this function return True?
def check(x):
    if x+1 is 1+x:
        return False
    if x+2 is not 2+x:
        return False
    return True


print()
print(check(-7))                    # True. Only x = -7 will return True
print(check(-5))                    # False. Any other number will return False


# ---------------------------------------------------------------------------------------------------------------------
# Interning String objects: Any string that contains only letters, digits and underscores will generally be interned.
# ---------------------------------------------------------------------------------------------------------------------
# Advantages:
# 1. Python can do comparisons much, much faster.
# 2. If you’re working with a dataset that includes an extended body of text in separate strings (such as NLP),
# you can dramatically reduce the memory used if all those repeated words (the, and, a etc.) are only instantiated once.
# ---------------------------------------------------------------------------------------------------------------------
print('\nString Interning:')
a = 'Here is a string'
b = 'Here is a string'
print(a == b)                       # True
print(a is b)                       # False

c = 'here_is_a_string'
d = 'here_is_a_string'
print(c == d)                       # True
print(c is d)                       # True


# Force Python to Intern Strings:
s = sys.intern('This is my new string!')                # import sys
t = sys.intern('This is my new string!')
print(s == t)                                           # True
print(s is t)                                           # True


# ---------------------------------------------------------------------------------------------------------------------
# Garbage Collection, del():
# del() will delete the reference to the object
# ---------------------------------------------------------------------------------------------------------------------
print('\nGarbage Collection:')
x = 'A string I just created'
y = x
print(id(x) == id(y))                                   # True
del x                                                   # variable x is deleted, not the object itself
print(y)                                                # 'a string I just created'. y is still pointing to the string


# Find how many variables are referencing a particular object. import ctypes
# Python will free up the memory when number of references become 0
print()
x1 = 'My new string'
y1 = x1
i = id(x1)
print(ctypes.c_long.from_address(i).value)              # 2
del x1                                                  # reference variable x1 is deleted, not the object itself
print(ctypes.c_long.from_address(i).value)              # 1
del y1                                                  # reference variable y1 is deleted, not the object itself
print(ctypes.c_long.from_address(i).value)              # 0


# ---------------------------------------------------------------------------------------------------------------------
# Circular Reference:
# Even when you delete l1 and l2, reference count is 1 because of the circular reference
# Python's inbuilt garbage collector module (called gc) will take care of freeing up such memory
# ---------------------------------------------------------------------------------------------------------------------

print('\nCircular Reference:')
l1 = []
l2 = []

i = id(l1)
j = id(l2)
print(ctypes.c_long.from_address(i).value)              # 1
print(ctypes.c_long.from_address(j).value)              # 1

l1.append(l2)
l2.append(l1)
print(ctypes.c_long.from_address(i).value)              # 2
print(ctypes.c_long.from_address(j).value)              # 2

del l1
print(ctypes.c_long.from_address(i).value)              # 1
print(ctypes.c_long.from_address(j).value)              # 2

del l2
print(ctypes.c_long.from_address(i).value)              # 1
print(ctypes.c_long.from_address(j).value)              # 1
