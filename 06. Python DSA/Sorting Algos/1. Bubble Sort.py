# ---------------------------------------------------------------------------------------------------------------------
# Bubble Sort:
# ---------------------------------------------------------------------------------------------------------------------
# In each iteration it compares elements in pairs and keeps swapping them such that the larger element
# is moved towards the end of the list. Non-recursive, Stable, In-place.
# Time complexity: O(n^2)
# Space Complexity: O(1) - No additional memory space is needed; just the array
# ---------------------------------------------------------------------------------------------------------------------

# def bubble_sort(a):
#     for i in range(len(a)-1):
#         swapped = False                             # if inner loop does not do a single swap, the array is sorted
#         for j in range(len(a)-1-i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#                 swapped = True
#         if not swapped:
#             break
#     return a
#
#
# if __name__ == '__main__':
#     my_list = [50, 9, 2, 1, 67, 34, 88, 34]
#     my_sorted_list = bubble_sort(a=my_list)
#     print(my_sorted_list)


# ---------------------------------------------------------------------------------------------------------------------
# Bubble Sort a dictionary based on key
# ---------------------------------------------------------------------------------------------------------------------

def bubble_sort_dict(a, key=None):
    for i in range(len(a)-1):
        swapped = False
        for j in range(len(a)-1-i):
            if a[j][key] > a[j+1][key]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a


if __name__ == '__main__':
    transactions = [
            {'name': 'eric', 'transaction_amount': 900, 'device': 'iphone-10'},
            {'name': 'dave', 'transaction_amount': 400, 'device': 'google pixel'},
            {'name': 'tran', 'transaction_amount': 200, 'device': 'one plus'},
            {'name': 'chet', 'transaction_amount': 800, 'device': 'iphone-8'},
        ]

    transactions = bubble_sort_dict(a=transactions, key='transaction_amount')
    # transactions = bubble_sort_dict(a=transactions, key='name')
    for item in transactions:
        print(item)
