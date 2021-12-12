# ---------------------------------------------------------------------------------------------------------------------
# List Comprehension: Easier and more readable way to create a list
# ---------------------------------------------------------------------------------------------------------------------
print('\nList Comprehension:')
num = [1, 3, 4, 6, 4, 3, 7, 9, 5, 3, 4]

even = [i for i in num if i % 2 == 0]
print('Even: ', even)

square = [i*i for i in num]
print('Square: ', square)

# print [('a', 0), ('a', 1), ('a', 2), ('b', 0), ('b', 1), ... ]
my_list = [(i, j) for i in "abcd" for j in range(3)]
print(my_list)


# ---------------------------------------------------------------------------------------------------------------------
# Dictionary Comprehension
# ---------------------------------------------------------------------------------------------------------------------
print('\nDictionary Comprehension:')

cities = ['Mumbai', 'New York', 'Paris']
countries = ['India', 'USA', 'France']

city_dict = {city: country for city, country in zip(cities, countries)}
print(city_dict)
print(type(city_dict))

city_dict = {city: country for city, country in zip(cities, countries) if city != 'Paris'}
print(city_dict)

# ---------------------------------------------------------------------------------------------------------------------
print()
z = zip(cities, countries)
print(z)                            # <zip object at 0x01A73EA8>
print(type(z))                      # <class 'zip'>

for a in z:
    print(a)                        # tuple: ('Mumbai', 'India') etc.

for values in zip(cities, countries):
    print(values)                   # tuple: ('Mumbai', 'India') etc.

print()
for c1, c2 in zip(cities, countries):
    print(c1, c2)                   # Mumbai India etc. Tuple returned by zip is unpacked in 2 variables c1 and c2


# ---------------------------------------------------------------------------------------------------------------------
# Set Comprehension
# ---------------------------------------------------------------------------------------------------------------------
print('\nSet Comprehension:')

num = [1, 3, 4, 6, 4, 3, 3, 4, 7, 9, 5, 3, 4, 9, 7, 9]
my_set = {i for i in num}
print(my_set)
