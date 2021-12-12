import time

# ---------------------------------------------------------------------------------------------------------------------
# Searching Techniques:
# ---------------------------------------------------------------------------------------------------------------------
# Linear Search: O(n)
# Binary Search: O(log n) - List needs to be sorted
# ---------------------------------------------------------------------------------------------------------------------


def time_it(func):                              # Decorator function 'time_it' taking function as an argument
    def wrapper_function(*args, **kwargs):      # *args: positional args, **kwargs: Keyword args
        start = time.time()
        result = func(*args, **kwargs)          # call the function that was passed to time_it() as an argument
        end = time.time()
        print()
        print(func.__name__ + " took " + str((end - start) * 1000) + " milli secs.")
        return result
    return wrapper_function                     # returns func without (), that means it returns an un-executed func


@time_it
def linear_search(num_list, num_to_find):
    for index, element in enumerate(num_list):
        if element == num_to_find:
            return index
    return -1


def binary_search_recursive(num_list, left, right, num_to_find):
    if right < left:
        return -1

    mid = (left + right) // 2

    if num_to_find == num_list[mid]:
        return mid

    if num_to_find > num_list[mid]:
        return binary_search_recursive(num_list=num_list, left=mid+1, right=right, num_to_find=num_to_find)

    if num_to_find < num_list[mid]:
        return binary_search_recursive(num_list=num_list, left=left, right=mid-1, num_to_find=num_to_find)


@time_it
def binary_search_iterative(num_list, num_to_find):
    left = 0
    right = len(num_list) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if num_to_find == num_list[mid]:
            return mid

        if num_to_find > num_list[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_duplicates(num_list, num_to_find):

    index = binary_search_iterative(num_list, num_to_find)
    idx_list = [index]

    i = index - 1
    while i >= 0:
        if num_to_find == num_list[i]:
            idx_list.append(i)
        else:
            break
        i -= 1

    i = index + 1
    while i < len(num_list):
        if num_to_find == num_list[i]:
            idx_list.append(i)
        else:
            break
        i += 1

    return sorted(idx_list)


if __name__ == '__main__':
    number_list = [5, 7, 8, 13, 22, 37, 45, 88, 91]
    number_to_find = 13

    # number_list = [i for i in range(100_000_001)]
    # number_to_find = 100_000_000

    idx = linear_search(num_list=number_list, num_to_find=number_to_find)
    print(f'Number found at index {idx} using Linear Search')

    idx = binary_search_recursive(num_list=number_list, left=0, right=len(number_list) - 1, num_to_find=number_to_find)
    print(f'Number found at index {idx} using Binary Search (Recursive)')

    idx = binary_search_iterative(num_list=number_list, num_to_find=number_to_find)
    print(f'Number found at index {idx} using Binary Search (Iterative)')

    # number_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    # number_to_find = 15
    #
    # idx = binary_search_duplicates(num_list=number_list, num_to_find=number_to_find)
    # print(number_list)
    # print(f'{number_to_find} is found at indices: ', idx)
