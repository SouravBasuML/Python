# ---------------------------------------------------------------------------------------------------------------------
# Generator: 'yield' keyword makes a generator.
# Doesn't hold the entire result in memory; it yields one result at a time
# ---------------------------------------------------------------------------------------------------------------------
# A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with
# the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a
# generator function.
# A generator function returns a generator object that is iterable, i.e., can be used as an Iterators .
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# List: Holds the entire result in memory
# ---------------------------------------------------------------------------------------------------------------------
def square_num(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = square_num([1, 2, 3, 4, 5])
print('\nList:')
print(my_nums)                              # [1, 4, 9, 16, 25]
print(type(my_nums))                        # <class 'list'>


# ---------------------------------------------------------------------------------------------------------------------
# Generator: 'yield' keyword makes a generator.
# Doesn't hold the entire result in memory; it yields one result at a time
# ---------------------------------------------------------------------------------------------------------------------
def square_num(nums):
    for i in nums:
        yield i*i


print('\nGenerator:')
my_nums = square_num([1, 2, 3, 4, 5])
print(my_nums)                              # <generator object square_num at 0x012AC1B0>
print(type(my_nums))                        # <class 'generator'>

print(next(my_nums))                        # 1
print(next(my_nums))                        # 4
print(next(my_nums))                        # 9
print(next(my_nums))                        # 16
print(next(my_nums))                        # 25
# print(next_node(my_nums))                 # StopIteration exception


# ---------------------------------------------------------------------------------------------------------------------
# Use for-loop on Generators. No need to worry about StopIteration exception. For-loop knows when to stop
# ---------------------------------------------------------------------------------------------------------------------
def square_num(nums):
    for i in nums:
        yield i*i


my_nums = square_num([1, 2, 3, 4, 5])
print('\nFor-Loop on Generator:')
print(my_nums)                                  # <generator object square_num at 0x01B5C258>
print(type(my_nums))                            # <class 'generator'>

for num in my_nums:
    print(num)


# ---------------------------------------------------------------------------------------------------------------------
# List Comprehension
# ---------------------------------------------------------------------------------------------------------------------
print('\nList Comprehension:')
my_nums = [x*x for x in [1, 2, 3, 4, 5]]        # [] makes it a list
print(my_nums)                                  # [1, 4, 9, 16, 25] - List
print(type(my_nums))                            # <class 'list'>

for num in my_nums:
    print(num)


# ---------------------------------------------------------------------------------------------------------------------
# Generator Expression: Generators using List Comprehension
# ---------------------------------------------------------------------------------------------------------------------
print('\nGenerators using List Comprehension:')
my_nums = (x*x for x in [1, 2, 3, 4, 5])        # () makes it a generator
print(my_nums)                                  # <generator object <genexpr> at 0x0169C258>
print(type(my_nums))                            # <class 'generator'>

for num in my_nums:
    print(num)


# ---------------------------------------------------------------------------------------------------------------------
# Convert Generator to List (Print all the values from the Generator itself).
# Advantages of Generators are lost
# ---------------------------------------------------------------------------------------------------------------------
print('\nConvert Generator to List:')
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)                                  # <generator object <genexpr> at 0x0169C258>
print(type(my_nums))                            # <class 'generator'>
print(list(my_nums))                            # List - [1, 4, 9, 16, 25]


# ---------------------------------------------------------------------------------------------------------------------
# Fibonacci Series Generator:
# ---------------------------------------------------------------------------------------------------------------------
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


print('\nFibonacci Series Generator:')
for f in fib():
    if f > 100:
        break
    print(f)
