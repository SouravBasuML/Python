# ---------------------------------------------------------------------------------------------------------------------
# Selection Sort:
# ---------------------------------------------------------------------------------------------------------------------
# We create two segments of the list: one sorted and other unsorted. We continuously remove the smallest element from
# the unsorted segment of the list and append it to the sorted segment. We don’t swap intermediate elements.
# Hence this algorithm sorts the array in minimum number of swaps.
# Complexity: O(n^2)
# ---------------------------------------------------------------------------------------------------------------------

def selection_sort(a):
    for i in range(len(a)-1):
        min_index = i
        for j in range(min_index+1, len(a)):        # find the index of the minimum element in the unsorted array
            if a[j] < a[min_index]:
                min_index = j

        if i != min_index:
            a[i], a[min_index] = a[min_index], a[i]

    return a


if __name__ == '__main__':
    my_list = [3, 66, 32, 89, 4, 3, 0, 41]
    print(selection_sort(a=my_list))
