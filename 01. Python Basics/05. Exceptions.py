# ---------------------------------------------------------------------------------------------------------------------
# Exception Handling
# ---------------------------------------------------------------------------------------------------------------------
# ZeroDivisionError: Raised when division or modulo by zero takes place for all numeric types
# OverflowError: Raised when a calculation exceeds maximum limit for a numeric type
# FloatingPointError: Raised when a floating point calculation fails
# ValueError: Raised when the built-in function for a data type has the valid type of arguments, but the arguments have
#             invalid values specified. e.g. inputting string in place of integer
# TypeError: Raised when an operation or function is attempted that is invalid for the specified data type
#            e.g. adding string and integer
# FileNotFoundError: Raised when file not found
# NameError: variable not defined
# Memory Error
# ImportError: Raised when an import statement fails
# IndexError: Raised when an index is not found in a sequence
# KeyError: Raised when the specified key is not found in the dictionary
# SyntaxError: Raised when there is an error in Python syntax.
# IndentationError: Raised when indentation is not specified properly.
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Catching Exception
# ---------------------------------------------------------------------------------------------------------------------

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid Value. Enter numeric")
except ZeroDivisionError:
    print("Age cannot be 0")
except Exception as e:                  # will catch all remaining exceptions. Hence put at the end
    print('Exception: ', e)
    print('Exception Type: ', type(e).__name__)
else:
    print('No exception occurred')
finally:
    print('Finally block. Print this no matter what')


# ---------------------------------------------------------------------------------------------------------------------
# Throwing Exception
# ---------------------------------------------------------------------------------------------------------------------

# Throwing System Exception
try:
    raise MemoryError('Memory Error in execution')
except MemoryError as e:
    print(e)


# Throwing User-Defined Exception
class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def handle(self):
        print('User-defined exception: ', self.msg)


try:
    raise Accident("Crash Ahead. Take Detour")
except Accident as e:
    e.handle()
