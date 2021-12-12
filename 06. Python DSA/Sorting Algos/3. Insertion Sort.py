# ---------------------------------------------------------------------------------------------------------------------
# Insertion Sort:
# ---------------------------------------------------------------------------------------------------------------------
# We segment the list into sorted and unsorted parts. Then we iterate over the unsorted segment, and insert
# the element from this segment into the correct position in the sorted segment.
# Non-recursive, Stable, In-place.
# ---------------------------------------------------------------------------------------------------------------------
# Complexity:
# Worst Case: O(n^2) comparisons, O(n^2) Swaps - Array is reverse sorted
# Best Case: O(n) comparisons, O(1) Swaps - Array is sorted
# Average Case: O(n^2) comparisons, O(n^2) Swaps
# Worst Case Space Complexity: O(n) total, O(1) auxiliary (for the temp variable)
# ---------------------------------------------------------------------------------------------------------------------

def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return a


if __name__ == '__main__':
    my_list = [11, 9, 29, 7, 2, 15, 28]
    print(insertion_sort(a=my_list))
