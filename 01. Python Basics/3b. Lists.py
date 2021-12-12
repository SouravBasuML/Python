# ---------------------------------------------------------------------------------------------------------------------
# List: Are ordered and mutable. Can hold different data types. Can have duplicates
# ---------------------------------------------------------------------------------------------------------------------
# my_list = ['aaa', 123, 34.567, "aaa", (2, 5), [2, 'a']]
#
# names = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
# print(names)

# print(len(names))           # 5
# print(max(names))           # eee
# print(min(names))           # aaa
# print(type(names))          # <class 'list'>

# print(names[::-1])          # reverses the list
# print(names[0])             # aaa
# print(names[-1])            # eee
# print(names[3:])            # ['ddd', 'eee'] - returns a new list
# print(names[:3])            # ['aaa', 'bbb', 'ccc']
# print(names[:])             # ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
# print(names[1: -1])         # ['bbb', 'ccc', 'ddd']
# print(names[-1: 1])         # []
# print(names[3: 1])          # []


# ---------------------------------------------------------------------------------------------------------------------
# List Functions:
# ---------------------------------------------------------------------------------------------------------------------
# names.append('xxx')
# names.insert(1, 'zzz')
# print(names)
# names.insert(23, 'www')       # inserts at the end
# print(names)
# names.insert(22, 'vvv')       # inserts at the end
# print(names)
# print(names.pop())            # returns and removes the last item in the list
# print(names)
# print(names.pop(0))           # returns and removes the item at that index in the list
# print(names)
# names.remove('zzz')
# print(names)
# # names.remove('zzz')         # error - remove() takes only 1 argument
# # names.clear()               # empties the list
# print(names.index('ccc'))
# # print(names.index('ggg'))   # error
# print('ggg' in names)         # returns boolean value False, not error
# print(names.count('xxx'))
# names2 = names.copy()
# print(names2)
# print(names+names2)           # list concatenation
# print([*names, *names2])      # list concatenation by unpacking


# ---------------------------------------------------------------------------------------------------------------------
# List Sort:
# sort() : Sorts in place. Works only with lists
# sorted(): Returns a new sorted list from an iterable (list, strings, tuples)
# ---------------------------------------------------------------------------------------------------------------------
# names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
#
# print()
# print(names.sort())                 # sorts the list and returns none
# print(names)
# print(names.reverse())              # reverses the list and returns none
# print(names)
#
# print()
# names.sort()                        # sorts the list in ascending order
# print(names)
# names.reverse()                     # use with sort() to sort the list in descending order
# print(names)
#
# names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
# print()
# names.sort(reverse=False)           # sort ascending
# print(names)
# names.sort(reverse=True)            # sort descending
# print(names)
#
# # 'key' has the value of a function that will be called on each item in the list:
# names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
# print()
# names.sort(key=len, reverse=False)           # sort ascending in order of length of the items
# print(names)
# names.sort(key=len, reverse=True)            # sort descending in order of length of the items
# print(names)

# sorted():
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
print()
print(sorted(names))
print(sorted(names, reverse=True))
print(sorted(names, key=len))


# ---------------------------------------------------------------------------------------------------------------------
# Empty List:
# ---------------------------------------------------------------------------------------------------------------------
# empty_list = []
# empty_list = list()


# ---------------------------------------------------------------------------------------------------------------------
# 2D Lists:
# ---------------------------------------------------------------------------------------------------------------------
# print('\n2D List')
# print('-------')
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix)
# print('\n', matrix[0][2], '\n')
#
# for row in matrix:
#     for col in row:
#         print(col)
#
#
# game = [[0, 0, 0],      # list of list/ 2D list
#         [0, 0, 0],
#         [0, 0, 0]]
# print(game)             # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for row in game:
#     print(row)


# ---------------------------------------------------------------------------------------------------------------------
# Type Conversion:
# ---------------------------------------------------------------------------------------------------------------------
# print('\nType Conversion')
#
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)
# print(type(my_tuple))
#
# my_list = list(my_tuple)
# print(my_list)
# print(type(my_list))


# ---------------------------------------------------------------------------------------------------------------------
# Removing duplicates from list:
# ---------------------------------------------------------------------------------------------------------------------
# print('\nRemoving duplicates from list:')
#
# dup_list = [2, 3, 2, 2, 2, 3, 6, 1, 6, 1, 2, 2, 7, 7, 3, 2, 7]
# print('Dup List: ', dup_list)
#
# uniq_list = []
# for num in dup_list:
#     if num not in uniq_list:
#         uniq_list.append(num)
# print('Method 1: Unique List: ', uniq_list)
#
# print('Method 2: Unique List: ', list(set(dup_list)))       # Converting to set removes duplicates
