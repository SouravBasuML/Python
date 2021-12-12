import time

# ---------------------------------------------------------------------------------------------------------------------
# Decorators:
# ---------------------------------------------------------------------------------------------------------------------
# Decorator is a function that takes another function as an argument, adds some functionality,
# and returns another function, without altering the source code of the original function.
# It wraps your existing functions with other functions. This helps keep the functionality separate
# e.g. add a timer or logger decorator to your existing functions
# Multiple decorators can be applied to existing functions.
# We can use a Decorator Class instead of Decorator Function
# ---------------------------------------------------------------------------------------------------------------------
# Functions are first class objects in Python. That means, they can be treated just like any other variable.
# You can pass them as argument to another function or return them as a return value
# ---------------------------------------------------------------------------------------------------------------------
# wrapper_function() takes *args, **kwargs as parameters, so that any number of positional and keyword arguments
# can be passed to it. That means, we can decorate functions that don't pass any arguments or
# that pass any number of positional and keyword arguments.
# ---------------------------------------------------------------------------------------------------------------------


def time_it(func):                              # Decorator function 'time_it' taking function as an argument
    def wrapper_function(*args, **kwargs):      # *args: positional args, **kwargs: Keyword args
        start = time.time()
        result = func(*args, **kwargs)          # call the function that was passed to time_it() as an argument
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " milli secs.")
        return result
    return wrapper_function                     # returns func without (), that means it returns an un-executed func


@time_it
def calc_square(num_list):
    result = []
    for num in num_list:
        result.append(num * num)
    return result


@time_it
def calc_cube(num_list):
    result = []
    for num in num_list:
        result.append(num * num * num)
    return result


array = range(1, 1_000_000)

# At run time, when the below function is called, control goes into the decorator first passing the function
# (square_array) as an argument. From within the wrapper function, the square_array function is called
square_array = calc_square(array)
cube_array = calc_cube(array)
