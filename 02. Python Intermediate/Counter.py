"""
-----------------------------------------------------------------------------------------------------------------------
# Counter: Outputs a dictionary with the items in the list and and their occurrence, ordered descending
-----------------------------------------------------------------------------------------------------------------------
"""

from collections import Counter

c = Counter(['aaa', 'bbb', 'ccc', 'aaa', 'ddd'])
print(c)                            # Counter({'aaa': 2, 'bbb': 1, 'ccc': 1, 'ddd': 1})
print(type(c))                      # class 'collections.Counter'>

c.update(['aaa', 'ddd'])
print(c)                            # Counter({'aaa': 3, 'ddd': 2, 'bbb': 1, 'ccc': 1})

print((c.keys()))                   # dict_keys(['aaa', 'bbb', 'ccc', 'ddd'])
print((c.values()))                 # dict_values([3, 1, 1, 2])

print(c.most_common(1))             # [('aaa', 3)] -> most common
print(c.most_common(2))             # [('aaa', 3), ('ddd', 2)] -> top two

# Get the occurrence of the second most common element
print(c.most_common(2)[1])          # ('ddd', 2)
print(c.most_common(2)[1][0])       # ddd -> second most common element
print(c.most_common(2)[1][1])       # 2   -> occurrence of the second most common element

print(c['aaa'])                     # 3
print(c['zzz'])                     # 0

c['ccc'] = 5
print(list(c.elements()))           # ['aaa', 'aaa', 'aaa', 'bbb', 'ccc', 'ccc', 'ccc', 'ccc', 'ccc', 'ddd', 'ddd']
print(c)                            # Counter({'ccc': 5, 'aaa': 3, 'ddd': 2, 'bbb': 1})

c['ccc'] = 0
print(list(c.elements()))           # ['aaa', 'aaa', 'aaa', 'bbb', 'ddd', 'ddd']
print(c)                            # Counter({'aaa': 3, 'ddd': 2, 'bbb': 1, 'ccc': 0})

del c['ccc']
print(list(c.elements()))           # ['aaa', 'aaa', 'aaa', 'bbb', 'ddd', 'ddd']
print(c)                            # Counter({'aaa': 3, 'ddd': 2, 'bbb': 1})

c2 = Counter(['xxx', 'yyy', 'zzz', 'zzz', 'zzz', 'aaa', 'aaa', 'aaa'])
print(c2)                           # Counter({'zzz': 3, 'aaa': 3, 'xxx': 1, 'yyy': 1})
print(c + c2)                       # Counter({'aaa': 6, 'zzz': 3, 'ddd': 2, 'bbb': 1, 'xxx': 1, 'yyy': 1})

# After subtraction if the count negative, it is excluded
print(c - c2)                       # Counter({'ddd': 2, 'bbb': 1})
print(c2 - c)                       # Counter({'zzz': 3, 'xxx': 1, 'yyy': 1})
