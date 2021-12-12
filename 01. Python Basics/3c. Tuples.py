# ---------------------------------------------------------------------------------------------------------------------
# Tuples (immutable - cannot append, insert, remove, clear, pop)
# Ordered. Can have different data types. Can have duplicates
# ---------------------------------------------------------------------------------------------------------------------

programming_languages = "Python", "Java", "Go", "C++", "C#"   # or ("Python", "Java") or 'Python', 'Java'
print(programming_languages)
print(type(programming_languages))                      # <class 'tuple'>
for i in programming_languages:
    print(i)

numbers = (1, 2, 3, 2, 3, 2, 2, 2)
print(numbers[1])
print(numbers.count(2))
print(numbers.index(3))

coordinates = (
    (0, 0),
    (3, 2),
    (5, 9),
    (2, 7)
)
print(coordinates)
print(coordinates[2][1])


# ---------------------------------------------------------------------------------------------------------------------
# Sort:
# ---------------------------------------------------------------------------------------------------------------------
print()
print('Sorted Asc: ', sorted(programming_languages))
print('Sorted Desc: ', sorted(programming_languages, reverse=True))
print('Sorted key=len: ', sorted(programming_languages, key=len))

band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]
print()
print('Band Students: ', band_students)
print('Band Students sorted by name asc: ', sorted(band_students))
print('Band Students sorted by name desc: ', sorted(band_students, reverse=True))
print('Band Students sorted by age: ', sorted(band_students, key=lambda student: student[1]))
print('Band Students sorted by instrument: ', sorted(band_students, key=lambda student: student[2]))


# ---------------------------------------------------------------------------------------------------------------------
# Unpacking:
# ---------------------------------------------------------------------------------------------------------------------
coordinates2 = (1, 2, 3)    # can be done for lists too
x, y, z = coordinates2
print()
print(x, y, z)


# ---------------------------------------------------------------------------------------------------------------------
# Empty Tuple:
# ---------------------------------------------------------------------------------------------------------------------
empty_tuple = ()
empty_tuple = tuple()


# ---------------------------------------------------------------------------------------------------------------------
# Type Conversion:
# ---------------------------------------------------------------------------------------------------------------------
print('\nType Conversion')

list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))

tuple1 = tuple(list1)
print(tuple1)
print(type(tuple1))
