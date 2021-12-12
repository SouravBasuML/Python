# ---------------------------------------------------------------------------------------------------------------------
# Quick Sort:
# ---------------------------------------------------------------------------------------------------------------------
# Divide and Conquer Algorithm.
# Average Time Complexity: O(nlogn)
# Worst Case Time Complexity: O(n^2) - If list is already sorted you create an imbalanced partition everytime
# ---------------------------------------------------------------------------------------------------------------------
# We partition the list around a pivot element, sorting values around the pivot. Best performance is achieved when
# the pivot value splits the list in two almost equal halves.
# We consider an element (first, last, median, random) as the pivot and put it in its right position in the array.
# That means, elements to the left of the pivot will be smaller than the pivot and vice versa on the right.
# Then we take the left and right partitions and apply the above step recursively.
# Putting the pivot in its right place is called 'Partitioning'. There are two Partitioning Schemes:
# 1. Hoare Partition - Difficult to implement, Superior performance
# 2: Lomuto Partition - Easy to implement, Inferior performance
# ---------------------------------------------------------------------------------------------------------------------

def hoare_partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]      # pivot is the first element of the list

    while start < end:
        # keep shifting start pointer to the right till you find an element larger than pivot
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        # keep shifting end pointer to the left till you find an element smaller than pivot
        while elements[end] > pivot:
            end -= 1

        # swap elements at start and end pointers:
        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    # swap pivot with element at end pointer to get pivot in its right place in the array
    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]

    # end index is returned so that partition can be recursively called
    return end


def lomuto_partition(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            elements[i], elements[p_index] = elements[p_index], elements [i]
            p_index += 1

    elements[p_index], elements[end] = elements[end], elements[p_index]

    return p_index


def quick_sort(a, start, end):
    if start < end:
        # partition_index = hoare_partition(elements=a, start=start, end=end)
        partition_index = lomuto_partition(elements=a, start=start, end=end)
        quick_sort(elements, start=start, end=partition_index - 1)              # Left Partition
        quick_sort(elements, start=partition_index + 1, end=end)                # Right Partition


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(a=elements, start=0, end=len(elements) - 1)
    print(elements)
