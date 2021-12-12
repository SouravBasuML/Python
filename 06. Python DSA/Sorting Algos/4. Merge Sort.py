# ---------------------------------------------------------------------------------------------------------------------
# Merge Sort:
# ---------------------------------------------------------------------------------------------------------------------
# Divide and Conquer Algorithm.
# Keep dividing the array in half recursively till you have only one element in each array.
# Then you merge 2 arrays at a time, so that the merged array is sorted.
# ---------------------------------------------------------------------------------------------------------------------
# Complexity:
# Time Complexity: Worst/Average: O(nlogn), Best: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------------------------------------------------------------------
def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left_arr = a[:mid]
    right_arr = a[mid:]

    left_arr = merge_sort(a=left_arr)
    right_arr = merge_sort(a=right_arr)

    return merge(a=left_arr, b=right_arr)


def merge(a, b):
    merged_array = []
    len_a = len(a)
    len_b = len(b)
    idx_a = idx_b = 0
    while idx_a < len_a and idx_b < len_b:
        if a[idx_a] < b[idx_b]:
            merged_array.append(a[idx_a])
            idx_a += 1
        else:
            merged_array.append(b[idx_b])
            idx_b += 1

    while idx_a < len_a:
        merged_array.append(a[idx_a])                   # append remaining elements of a
        idx_a += 1

    while idx_b < len_b:
        merged_array.append(b[idx_b])                   # append remaining elements of b
        idx_b += 1

    return merged_array


if __name__ == '__main__':
    my_list = [90, 4, 22, 54, 3, 99, 4, 23, 40, 22]
    print(merge_sort(a=my_list))
