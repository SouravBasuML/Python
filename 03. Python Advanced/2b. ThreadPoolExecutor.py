import time
import concurrent.futures


# ---------------------------------------------------------------------------------------------------------------------
# Thread Pool Executor:
# ---------------------------------------------------------------------------------------------------------------------
# import concurrent.futures
# No need to code thread.start() or thread.join()
# ---------------------------------------------------------------------------------------------------------------------
def calc_square(a):
    time.sleep(1)
    return a*a


# ---------------------------------------------------------------------------------------------------------------------
# submit():
# ---------------------------------------------------------------------------------------------------------------------
# To execute the function once at a time, use the submit() method of ThreadPoolExecutor():
# The submit method schedules a function to be executed and returns a 'Future' object
# The 'Future' object encapsulates the execution of our function and allows us to check in on it after it has been
# scheduled, e.g. we can check if the function is executing/done, and also print the return value of the function
# using the result()
# Threads are automatically joined once the concurrent.futures.ThreadPoolExecutor() context manager ends.
# ---------------------------------------------------------------------------------------------------------------------

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(calc_square, 10)                        # <class 'concurrent.futures._base.Future'>
    f2 = executor.submit(calc_square, 15)                        # <class 'concurrent.futures._base.Future'>
    print(f1.result())
    print(f2.result())

end = time.perf_counter()

print(f'Execution done in {round(end - start, 2)} seconds')


# ---------------------------------------------------------------------------------------------------------------------
# as_completed():
# ---------------------------------------------------------------------------------------------------------------------
# as_completed() gives us an iterator that we can loop over to yield the results of our threads as they are completed,
# not in the order in which the threads are started
# ---------------------------------------------------------------------------------------------------------------------

# start = time.perf_counter()
#
# # Calling submit() in loop
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(calc_square, i) for i in range(10)]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())                                                   # will print as the threads complete
#
# end = time.perf_counter()
#
# print(f'Execution done in {round(end - start, 2)} seconds')


# ---------------------------------------------------------------------------------------------------------------------
# map():
# ---------------------------------------------------------------------------------------------------------------------
# Execute the function over an iterable (list of values), without using submit() in loop.
# map() does not return a 'Future' object, instead it returns the result
# map() will return the results in the order that the threads were started (and not as and when completed, like above)
# If our function raises an exception, it won't be raised while executing the thread; the exception will be raised
# when its value is retrieved from the results iterator. Hence exception needs to be handled while looping through
# the results iterator.
# ---------------------------------------------------------------------------------------------------------------------

# start = time.perf_counter()
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     results = executor.map(calc_square, my_list)
#     for result in results:
#         print(result)                                           # map() returns the result, not a 'Future' object
#
# end = time.perf_counter()
#
# print(f'Execution done in {round(end - start, 2)} seconds')
