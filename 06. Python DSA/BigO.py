# ---------------------------------------------------------------------------------------------------------------------
# Big O notation is the way to measure how a software program's running time or space requirements
# grow as the input size grows. We can't measure this using absolute terms such as time in seconds because different
# computers have different hardware hence we need a mathematical way to measure time complexity of a program and
# Big O is that mathematical way. The basic idea is to come up with mathematical function for a running time and
# consider only the  fastest growing term and discard other terms as well as constants.
# Big O is used to measure space complexity as well.
# ---------------------------------------------------------------------------------------------------------------------
# https://www.bigocheatsheet.com/
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# O(n)
# ---------------------------------------------------------------------------------------------------------------------
def calc_square(num_list):
    result = []
    for num in num_list:
        result.append(num * num)
    return result


# ---------------------------------------------------------------------------------------------------------------------
# O(1) - Constant Time Operation
# ---------------------------------------------------------------------------------------------------------------------
def find_pe(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe


# ---------------------------------------------------------------------------------------------------------------------
# O(n2)
# ---------------------------------------------------------------------------------------------------------------------
def find_dup(num_list):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] == num_list[j]:
                print(num_list[i] + ' is duplicate')
                break


# ---------------------------------------------------------------------------------------------------------------------
# O(n2 + n) -> O(n2)
# ---------------------------------------------------------------------------------------------------------------------
def find_dup(num_list):
    # O(n2)
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] == num_list[j]:
                dup = num_list[i]
                break

    # O(n)
    for i in range(len(num_list)):
        if num_list[i] == dup:
            print(i)


# ---------------------------------------------------------------------------------------------------------------------
# O(n) - Linear Search
# ---------------------------------------------------------------------------------------------------------------------
def binary_search(num_list, num):
    for i in range(len(num_list)):
        if num_list[i] == num:
            print('Found')


# ---------------------------------------------------------------------------------------------------------------------
# O(log n) - Binary Search
# ---------------------------------------------------------------------------------------------------------------------
def binary_search(num_list, num):
    pass

# Iteration 1: n/(2^1) -> n/2
# Iteration 2: n/(2^2) -> n/4
# Iteration 3: n/(2^3) -> n/8
# ...
# Iteration k: n/(2^k)
#
# n = 2^k
# log(n) = log(2^k) = k log(2)
# k = log(n)
# O(log n)
