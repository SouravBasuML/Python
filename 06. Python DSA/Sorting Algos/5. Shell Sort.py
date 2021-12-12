# ---------------------------------------------------------------------------------------------------------------------
# Shell Sort:
# ---------------------------------------------------------------------------------------------------------------------
# Shell sort is an optimization over insertion sort.
# In insertion sort, if the smaller elements are towards the end, it will take a lot of comparisons and swaps
# to insert them in the right position.
# 1. Start with an interval of n/2 and sort the elements that are present at a gap of n/2
# 2. Keep reducing the interval by n/2 and keep sorting the sub arrays
# 3. Last iteration should have an interval of 1, at which point it becomes insertion sort
# ---------------------------------------------------------------------------------------------------------------------
# Complexity:
# Worst Case: O(n^2)
# Best Case: O(nlogn)
# ---------------------------------------------------------------------------------------------------------------------

def shell_sort(a):
    length = len(a)
    interval = length // 2

    while interval > 0:
        for i in range(interval, length):
            anchor = a[i]
            j = i
            while j >= interval and a[j - interval] > anchor:
                a[j] = a[j-interval]
                j -= interval
            a[j] = anchor
        interval //= 2

    return a


if __name__ == '__main__':
    my_list = [30, 21, 9, 0, 14, 67, 3, 9, 99]
    print(shell_sort(a=my_list))
