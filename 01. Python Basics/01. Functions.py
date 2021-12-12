import math
import random
import statistics
import datetime
import calendar

# ---------------------------------------------------------------------------------------------------------------------
# Functions: Parameters, Arguments, Math, Scope, Random, Statistics, Recursion, Calendar and Datetime,
#            Higher Order Functions
# ---------------------------------------------------------------------------------------------------------------------


def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome to Python')


# parameters are the placeholders we define in the function, e.g. name
# arguments are the values passed to the parameter, e.g. Sourav
# function call cannot be above the function definition
# calling a function without () just points to the function, doesn't run the function

greet_user(input('Enter name: '))


# Parameters
def greet(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome to Python')


greet("Sourav", "Basu")                         # positional arguments
greet(last_name="Basu", first_name="Sourav")    # keyword argument
greet("Sourav", last_name="Basu")               # keyword argument must always be after positional arguments


# Return Values
def square(number):
    return number * number


# print(square(int(input('Enter number: '))))


# ---------------------------------------------------------------------------------------------------------------------
# Global vs. Local variable
# ---------------------------------------------------------------------------------------------------------------------
total = 1


def addition():
    total = 5
    print(total)                # 5 (Local)


addition()
print(total)                    # 1 (Global)


# ---------------------------------------------------------------------------------------------------------------------
# Math Functions
# ---------------------------------------------------------------------------------------------------------------------
print(20 / 3)   # Returns floating point division answer
print(20 // 3)  # Floor Division - Returns whole number
print(31 % 4)   # Modulus operator - Returns reminder
print(3 ** 4)   # 3^4

x = 10
x += 3  # Augmented assignment operator

# Operator Precedence PEMDAS
# 1. Parenthesis
# 2. Exponentiation
# 3. Multiplication or Division
# 4. Addition or Subtraction
print(2 + 3 * 5 ** 3)

print()
print(round(2.51))                      # 3
print(round(2.49))                      # 2
print(round(123.456, ndigits=2))        # 123.46
print(round(123.456, ndigits=1))        # 123.5
print(round(123.456, ndigits=0))        # 123.0
print(round(123.456, ndigits=-1))       # 120.0
print(round(123.456, ndigits=-2))       # 100.0


print(abs(-3.1))            # 3.1
print(divmod(13, 4))        # (3, 1) -> (quotient, remainder) tuple

print()
print(bin(100))             # 0b1100100 - Binary
print(hex(100))             # 0x64 - Hexadecimal
print(oct(100))             # 0o144 - Octal
print(ord('a'))             # 97 - Unicode value

print()
print(dir(math))            # shows all functions in math module
print(math.ceil(2.01))      # 3
print(math.floor(2.99))     # 2
print(math.factorial(8))
print(math.pow(3, 4))       # 81.0
print(math.sqrt(36.0001))
print(math.log10(1000))     # 3
print(math.pi)
print(math.e)


# ---------------------------------------------------------------------------------------------------------------------
# Random: import random
# ---------------------------------------------------------------------------------------------------------------------
print(random.random())                  # Random number between 0 and 1
print(random.randint(3, 100))           # random number between 3 and 100, both inclusive

members = ['aaa', 'bbb', 'ccc', 'ddd']
print(random.choice(members))

random.shuffle(members)                        # from random import shuffle
print(members)


# Dice Roll:
class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)   # no need to include () for tuple in return statement


dice1 = Dice()
print(dice1.roll())


# ---------------------------------------------------------------------------------------------------------------------
# Statistics: import statistics
# ---------------------------------------------------------------------------------------------------------------------
# Average
print(statistics.mean([1, 4, 2, 3, 4, 2, 2, 3, 4, 4, 3, 2, 5, 2]))

# Middle value or the average of the two middle values in a sorted list
print(statistics.median([1, 4, 2, 3, 4, 2, 2, 3, 4, 4, 3, 2, 5, 2]))

# Most repeated item
print(statistics.mode([1, 4, 2, 3, 4, 2, 2, 3, 4, 4, 3, 2, 5, 2]))

print(statistics.variance([1, 4, 2, 3, 4, 2, 2, 3, 4, 4, 3, 2, 5, 2]))


# ---------------------------------------------------------------------------------------------------------------------
# Recursion:
# ---------------------------------------------------------------------------------------------------------------------
# Print 1 to 100 without using loops
def print_number(i):
    if i < 101:
        print(i)
        print_number(i+1)


i = 1
print_number(i)


# ---------------------------------------------------------------------------------------------------------------------
# Calendar, Datetime
# ---------------------------------------------------------------------------------------------------------------------
# import datetime
# import calendar
# ---------------------------------------------------------------------------------------------------------------------
# print(datetime.datetime(2020, 11, 25, 13, 33, 45))        # 2020-11-25 13:33:45

# print(calendar.weekheader(2))                               # Mo Tu We Th Fr Sa Su
# print(calendar.weekheader(3))                               # Mon Tue Wed Thu Fri Sat Sun
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.weekheader(3))                               # Sun Mon Tue Wed Thu Fri Sat
#
# print(f'There are {calendar.leapdays(y1=2022, y2=2030)} leap days between 2022 and 2030.')
# print(calendar.isleap(2021))                                # False
#
# # Weekdays: 0: Mon, 1: Tue, 2: Wed, 3: Thu, 4: Fri, 5: Sat, 6: Sun
# print(calendar.firstweekday())                              # 0 (for default first week day - Monday)
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.firstweekday())                              # 6 (for first week day - Sunday)
# print(calendar.weekday(year=2021, month=9, day=28))         # 1 (Tuesday)
#
# print(calendar.monthrange(year=2021, month=9))              # (2, 30) -> (first day of month, number of days in month)
#
# print(calendar.month(theyear=2021, themonth=9))
# print(calendar.month(theyear=2021, themonth=9, w=4, l=2))   # w = width, l = length
#
# print(calendar.calendar(theyear=2021))
# print(calendar.calendar(theyear=2021, c=2, m=6))            # c = rows, m = cols
# print(calendar.calendar(theyear=2021, w=2, l=1))            # w = width, l = length


# ---------------------------------------------------------------------------------------------------------------------
# Higher Order Functions:
# ---------------------------------------------------------------------------------------------------------------------
print('\nHigher Order Functions:')
# Functions that operate on other functions are called "higher-order functions."

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n',
)


# By default, max returns the largest of its arguments. But if we pass in a function using the optional key argument,
# it returns the argument x that maximizes key(x) (aka the 'argmax').
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    '\nWhich number is biggest?', max(100, 51, 14),
    'Which number is the biggest modulo 5?', max(100, 51, 14, key=mod_5),
    sep='\n',
)
