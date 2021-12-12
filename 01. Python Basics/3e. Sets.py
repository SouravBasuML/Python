"""
-----------------------------------------------------------------------------------------------------------------------
Set: Unordered collection without duplicates
-----------------------------------------------------------------------------------------------------------------------
"""

programming_languages = {'Python', 'Java'}
print('\n', programming_languages)
print(type(programming_languages))      # set
print(dir(programming_languages))
# print(programming_languages[0])       # Not allowed as Set is unordered


# ---------------------------------------------------------------------------------------------------------------------
# Set Operations:
# ---------------------------------------------------------------------------------------------------------------------
# union()                   |
# intersection()            &
# difference()              -
# symmetric_difference()    ^
# issubset()                <
# issuperset()              >
# ---------------------------------------------------------------------------------------------------------------------
cs_courses = {'History', 'Math', 'Physics', 'Computers'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print()
print('CS:', cs_courses)
print('Art:', art_courses)

print('\nUnion: Elements in both sets:')
print(cs_courses.union(art_courses))
print(cs_courses | art_courses)

print('\nIntersection: Elements common to both sets:')
print(cs_courses.intersection(art_courses))
print(cs_courses & art_courses)

print('\nDifference: Elements in one set but not in other:')
print(cs_courses.difference(art_courses))
print(art_courses - cs_courses)
print(cs_courses.difference(cs_courses))                        # set()

print('\nSymmetric Difference: Elements in both sets but not common to both (excludes the intersection elements:')
print(cs_courses.symmetric_difference(art_courses))
print(cs_courses ^ art_courses)


# ---------------------------------------------------------------------------------------------------------------------
# Set Mutation Operations:
# ---------------------------------------------------------------------------------------------------------------------
# update()                          |=
# intersection_update()             &=
# difference_update()               -=
# symmetric_difference_update()     ^=
# ---------------------------------------------------------------------------------------------------------------------
cs_courses = {'History', 'Math', 'Physics', 'Computers'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print()
print('CS:', cs_courses)
print('Art:', art_courses)

print('\nupdate(): Updates a set with elements of other set:')
cs_courses.update(art_courses)
print('CS:', cs_courses)

print('\nintersection_update(): Updates a set by keeping only the elements found in it and another set:')
cs_courses.intersection_update(art_courses)
print(cs_courses)

print('\ndifference_update(): Updates a set by removing elements found in another set:')
cs_courses.difference_update(art_courses)
print(cs_courses)

print('\nsymmetric_difference_update(): Updates a set by only keeping elements found in either set, but not in both:')
cs_courses.symmetric_difference_update(art_courses)
print(cs_courses)


# ---------------------------------------------------------------------------------------------------------------------
# issubset(), issuperset(), isdisjoint():
# ---------------------------------------------------------------------------------------------------------------------
A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 6}
C = {1, 3, 5}

print(B.issubset(A))                # True (or B < A)
print(A.issuperset(C))              # True (or A > C)
print(B.isdisjoint(C))              # True. Null intersection


# ---------------------------------------------------------------------------------------------------------------------
# Empty Set:
# ---------------------------------------------------------------------------------------------------------------------
empty_set = set()
# empty_set = { }                   # This is a dict not a set

# ---------------------------------------------------------------------------------------------------------------------
# Type Conversion:
# ---------------------------------------------------------------------------------------------------------------------
print('\nType Conversion')

list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))

set1 = set(list1)
print(set1)
print(type(set1))


# ---------------------------------------------------------------------------------------------------------------------
# Frozen Sets: Immutable, Unordered Set. add() etc. not allowed
# ---------------------------------------------------------------------------------------------------------------------
v = ('a', 'e', 'i', 'o', 'u')
fset = frozenset(v)
print(fset)                             # frozenset({'a', 'i', 'o', 'e', 'u'})
print(type(fset))                       # <class 'frozenset'>
