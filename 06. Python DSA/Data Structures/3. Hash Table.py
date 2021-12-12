# ---------------------------------------------------------------------------------------------------------------------
# Hash Table / Hash Map
# ---------------------------------------------------------------------------------------------------------------------
# Dictionary is Python implementation of Hash Table. Underlying data structure of a dictionary is Hash Table
# The dictionary key is run through a hash function to find an index in an array in memory
# Collision Handling:
# 1. Chaining - values are stored as a new list
# 2. Linear probing - the next available empty memory location is used
# ---------------------------------------------------------------------------------------------------------------------
# Lookup by key -> Average O(1), Worst Case O(n)
# Insertion/Deletion -> Average O(1), Worst Case O(n)
# ---------------------------------------------------------------------------------------------------------------------
class HashTable:
    def __init__(self):
        self.MAX = 10                                       # assuming 100 is the size of the list
        # initialize each element to empty list as each element needs to hold key-value pairs to avoid collision
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):                                # Hash Function
        hash_value = 0
        for char in key:
            hash_value += ord(char)                         # ord() converts a character into its Unicode code value
        return hash_value % self.MAX                        # the remainder of h/100 is used as the hash value

    def __setitem__(self, key, value):                      # Add key, value pair to the Hash Table
        h = self.get_hash(key=key)

        # if key already exists, traverse the list and update the value else append the new (key, value) to the list
        found = False
        for item in self.arr[h]:
            if item[0] == key:                              # item[0] has the key
                item[1] = value                             # item[0] has the value
                found = True
        if not found:
            self.arr[h].append([key, value])

    def __getitem__(self, key):
        h = self.get_hash(key=key)
        for item in self.arr[h]:
            if item[0] == key:
                return item[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, item in enumerate(self.arr[h]):
            if item[0] == key:
                del self.arr[h][index]


t = HashTable()
t['march 6'] = 302
t['march 17'] = 300
t['march 20'] = 297
t['march 26'] = 999
t['march 31'] = 315

print('\nInsert:')
print(t.arr)

print('\nSearch:')
print('Value at march 26: ', t['march 26'])
print('Value at march 06: ', t['march 6'])
print('Value at march 17: ', t['march 17'])
print('Value at march 30: ', t['march 30'])

print('\nDelete:')
del t['march 6']
print(t.arr)
del t['march 17']
print(t.arr)
