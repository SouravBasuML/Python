from functools import reduce

# ---------------------------------------------------------------------------------------------------------------------
# Lambdas: Anonymous Functions
# ---------------------------------------------------------------------------------------------------------------------
f = lambda a: a*a
result = f(5)
print(result)

f = lambda a, b: a + b
result = f(5, 6)
print(result)


# filter even numbers from a list
nums = [3, 4, 6, 5, 4, 7, 8, 8, 7, 6, 4, 5, 6, 7, 7]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

# double a list using map()
doubles = list(map(lambda n: n*2, evens))
print(doubles)

# sum up the list using reduce()
sum_up = reduce(lambda a, b: a + b, doubles)            # from functools import reduce
print(sum_up)
