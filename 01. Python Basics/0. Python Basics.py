
"""
---------------------------------------------------------------------------------------------------------------------
Python is an compiled and interpreted language:
    Python code is compiled to byte code and stored in .pyc files
    This byte code is executed by the interpreter
Everything is an Object in Python
Python is Strongly-Typed: Variables have a type and type compatibility matters while performing operation
Python is Dynamically-Typed: Variable type is determined only at run time
---------------------------------------------------------------------------------------------------------------------

"""
import this             # Prints 'The Zen of Python', by Tim Peters


# ---------------------------------------------------------------------------------------------------------------------
# Help:
# ---------------------------------------------------------------------------------------------------------------------
type()                                          # tells what the object is
dir()                                           # lists all attributes and methods for that object
help()                                          # detailed documentation on the object


# ---------------------------------------------------------------------------------------------------------------------
# __name__
# ---------------------------------------------------------------------------------------------------------------------
# If the source file is being executed as the main program, the interpreter sets the __name__ variable to have a value
# “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.
print(__name__)                                 # __main__


# ---------------------------------------------------------------------------------------------------------------------
# Print:
# ---------------------------------------------------------------------------------------------------------------------
# print() by default adds a new line character \n at the end. The 'end' parameter adds a user-defined separator.
print('Python', end=' ')                        # Python Basics
print('Basics')
print('Python', end='\t\t')                     # Python		Basics
print('Basics')
print('Python', end='-')                        # Python-Basics
print('Basics')

# The 'sep' parameter adds a user-defined separator between different prints of the same print().
print('Python', 'Basics', sep=' --> ')          # Python --> Basics

print('''
Hi Sourav,
How are you?
Thanks
''')


# ---------------------------------------------------------------------------------------------------------------------
# Get input from user:
# ---------------------------------------------------------------------------------------------------------------------
# print(input("Enter name: "))
# print(input(int("Enter number: ")))


# ---------------------------------------------------------------------------------------------------------------------
# Comments
# ---------------------------------------------------------------------------------------------------------------------
# Docstring comments are added for every function and a help() on that function displays the docstring comments.
'''
Docstrings serve as 
multi-line comments
'''

"""
Docstrings serve as 
multi-line comments
"""


# ---------------------------------------------------------------------------------------------------------------------
# Variables: int, float, str, bool, None, complex
# ---------------------------------------------------------------------------------------------------------------------
a = 10
print(a)
print(type(a))                      # <class 'int'>
print(dir(a))                       # attributes and methods of Integer class
print(a.bit_length())               # 4 --> Number of bits necessary to represent self in binary.

a = a + 20.0
print(a)
print(type(a))                      # <class 'float'>
print(dir(a))                       # attributes and methods of Float class
print(0.625.as_integer_ratio())     # (5, 8)  -> (numerator, denominator)

s = 'sourav'
print(s)
print(type(s))                      # <class 'str'>
print(dir(s))                       # attributes and methods of String class

print(type(False))                  # <class 'bool'>
print(bool(1))                      # True -> all numbers are treated as true, except 0
print(bool(0))                      # False
print(bool("asf"))                  # True -> all strings are treated as true, except the empty string ""
print(bool(""))                     # False - > empty sequences (lists, tuples etc.) are False
print(int(True))                    # 1
print(int(False))                   # 0


a = None                            # None represents NULL in Python
print(a)                            # None
print(type(a))                      # <class 'NoneType'>

# complex data type stores complex numbers in the form A + Bj
x = 12
print(x.imag)                       # 0 --> 12 + 0j
y = 5 + 7j
print(y.imag)                       # 7.0


# ---------------------------------------------------------------------------------------------------------------------
# Operators:
# ---------------------------------------------------------------------------------------------------------------------
# Modulus (Remainder) Operator: %
# Logical Operators: and, or, not
# Other Operators: is, in (e.g. "a" is 'a')
# Comparison Operators: >, >=, <, <=, ==, !=
# Ternary Operators: e.g. big = x if x > y else y

print('*' * 10)                 # **********
print("+" + str(10))            # +10
print(34 % 12)                  # Remainder/Modulus operator
print(4**2)                     # Power operator
print(round((12/34), 2))        # Round up to 2 decimals
print(True or True and False)   # True. 'and' is evaluated before 'or'


# ---------------------------------------------------------------------------------------------------------------------
# If Statement:
# ---------------------------------------------------------------------------------------------------------------------
a = 4
b = 4
if a > b:
    print("Greater")
elif b > a:
    print("Lesser")
else:
    print("Equal")
