import random
import sys
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('ggplot')


# ---------------------------------------------------------------------------------------------------------------------
# Function to swap elements in a list:
# ---------------------------------------------------------------------------------------------------------------------
def swap_elements(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]


# ---------------------------------------------------------------------------------------------------------------------
# Bubble Sort:
# ---------------------------------------------------------------------------------------------------------------------
# In each iteration it compares elements in pairs and keeps swapping them such that the larger element
# is moved towards the end of the list.
# Non-recursive, Stable, In-place. Complexity O(n2)
# For 100 elements: If sorted: 99. If reverse sorted: 4950
# ---------------------------------------------------------------------------------------------------------------------
def bubble_sort(array):
    swapped = True
    for i in range(len(array)-1):
        if not swapped:
            break
        swapped = False
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                swap_elements(array, j, j+1)
                swapped = True
            yield array


# ---------------------------------------------------------------------------------------------------------------------
# Heap Sort:
# ---------------------------------------------------------------------------------------------------------------------
# We create two segments of the list: one sorted and one unsorted. We use heap data structure to efficiently get the
# max element from the unsorted segment of the list. Heapify method uses recursion to get the max element at the top.
# Non-recursive, unstable, In-place. Complexity O(nlogn)
# ---------------------------------------------------------------------------------------------------------------------
def heap_sort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        yield from heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        yield from heapify(array, i, 0)
    yield array


def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        yield from heapify(array, n, largest)
        yield array


# ---------------------------------------------------------------------------------------------------------------------
# Insertion Sort:
# ---------------------------------------------------------------------------------------------------------------------
# We segment the list into sorted and unsorted parts. Then we iterate over the unsorted segment, and insert
# the element from this segment into the correct position in the sorted list
# Non-recursive, Stable, In-place. Complexity O(n2)
# ---------------------------------------------------------------------------------------------------------------------
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap_elements(array, j, j - 1)
            j -= 1
            yield array


# ---------------------------------------------------------------------------------------------------------------------
# Merge Sort:
# ---------------------------------------------------------------------------------------------------------------------
# This is a divide and conquer algorithm. We split a list in half, and keep splitting the list by 2 until it only has
# a single element. Then we merge the sorted list. We keep doing this until we get a sorted list with all
# the elements of the unsorted input list.
# Recursive, Stable, Needs extra space. Complexity O(nlogn)
# ---------------------------------------------------------------------------------------------------------------------
def merge_sort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(A, start, mid)
    yield from merge_sort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A


def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A


# ---------------------------------------------------------------------------------------------------------------------
# Quick Sort:
# ---------------------------------------------------------------------------------------------------------------------
# We partition the list around a pivot element, sorting values around the pivot. Best performance is achieved when
# the pivot value splits the list in two almost equal halves.
# ---------------------------------------------------------------------------------------------------------------------
def quick_sort(A, start, end):
    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap_elements(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap_elements(A, end, pivotIdx)
    yield A

    yield from quick_sort(A, start, pivotIdx-1)
    yield from quick_sort(A, pivotIdx+1, end)


# ---------------------------------------------------------------------------------------------------------------------
# Selection Sort:
# ---------------------------------------------------------------------------------------------------------------------
# We create two segments of the list: one sorted and other unsorted. We continuously remove the smallest element from
# the unsorted segment of the list and append it to the sorted segment. We don’t swap intermediate elements.
# Hence this algorithm sorts the array in minimum number of swaps.
# Non-recursive, Unstable, In-place. Complexity O(n2)
# ---------------------------------------------------------------------------------------------------------------------
def selection_sort(array):
    for i in range(len(array)):
        # Find minimum unsorted value.
        minVal = array[i]
        minIdx = i
        for j in range(i, len(array)):
            if array[j] < minVal:
                minVal = array[j]
                minIdx = j
            yield array
        swap_elements(array, i, minIdx)
        yield array


# ---------------------------------------------------------------------------------------------------------------------
# Shell Sort:
# ---------------------------------------------------------------------------------------------------------------------
# Shell sort is an optimization over insertion sort. This is achieved by repeatedly doing insertion sort on all
# elements at fixed, decreasing intervals. Last iteration the interval is 1. Here it becomes a regular insertion sort
# and it guarantees that the array will be sorted. But to note one point is that by the time we do that array is
# almost sorted, hence the iteration is very fast.
# Non-recursive, Stable, In-place. Complexity O(n2)
# ---------------------------------------------------------------------------------------------------------------------
def shell_sort(array):
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                yield array
            array[j] = temp
        interval //= 2


# ---------------------------------------------------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":      # executed when invoked directly

    title = ''
    generator = []

    # number of elements in the list to sort
    num_of_elements = 100

    # Random list containing elements between 1 to 100 (with duplicates)
    list_to_sort = [random.randint(1, num_of_elements) for i in range(num_of_elements)]

    # Get the sorting method to execute from user
    print('\nSORTING METHODS:')
    print('1. Bubble Sort\n2. Heap Sort\n3. Insertion Sort\n4. Merge Sort\n'
          '5. Quick Sort\n6. Selection Sort\n7. Shell Sort\n')
    sort_method = int(input("Enter Sorting Method (Integer between 1 and 7): "))

    # Get appropriate generator to supply to matplotlib FuncAnimation method
    if sort_method == 1:
        title = 'Bubble Sort'
        generator = bubble_sort(list_to_sort)
    elif sort_method == 2:
        title = "Heap Sort"
        generator = heap_sort(list_to_sort)
    elif sort_method == 3:
        title = "Insertion Sort"
        generator = insertion_sort(list_to_sort)
    elif sort_method == 4:
        title = "Merge Sort"
        generator = merge_sort(list_to_sort, start=0, end=num_of_elements-1)
    elif sort_method == 5:
        title = "Quick Sort"
        generator = quick_sort(list_to_sort, start=0, end=num_of_elements-1)
    elif sort_method == 6:
        title = "Selection Sort"
        generator = selection_sort(list_to_sort)
    elif sort_method == 7:
        title = "Shell Sort"
        generator = shell_sort(list_to_sort)
    else:
        sys.exit('Invalid Input')

    print(f'{title} executing...')

    # Initialize figure and axis
    fig, ax = plt.subplots()
    ax.set_title(title)

    # Initialize a bar plot. matplotlib.pyplot.bar() returns a list of rectangles
    # (with each bar in the bar plot corresponding to one rectangle), which we store in bar_rects.
    bar_rects = ax.bar(range(len(list_to_sort)), list_to_sort, align="edge")

    # Set axis limits
    ax.set_xlim(0, num_of_elements)
    ax.set_ylim(0, int(1.1 * num_of_elements))

    # Place a text label in the upper-left corner of the plot to display number of operations performed by the
    # sorting algorithm (each "yield" is treated as 1 operation).
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
    # To track the number of operations, i.e., iterations through which the animation has gone, define a variable
    # "iteration". This variable will be passed to update_fig() to update the text label, and will also be incremented
    # in update_fig(). For this increment to be reflected outside the function, we make "iteration" a list of 1 element,
    # since lists (and other mutable objects) are passed by reference (but an integer would be passed by value).
    # NOTE: Alternatively, iteration could be re-declared within update_fig() with the
    # "global" keyword (or "nonlocal" keyword)
    iteration = [0]


    def update_fig(list_to_sort, rects, iteration):
        for rect, val in zip(rects, list_to_sort):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))


    anim = FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration),
                         frames=generator, interval=1, repeat=False)
    plt.show()
