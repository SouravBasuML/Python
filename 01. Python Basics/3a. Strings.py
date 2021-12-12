# ---------------------------------------------------------------------------------------------------------------------
# Strings: Immutable Objects
# ---------------------------------------------------------------------------------------------------------------------
# print('\nPython for "Beginners"')
# print("Beginner's Python course")
#
# print('''
# Hi Sourav,
# How are you?
# Thanks
# ''')


# ---------------------------------------------------------------------------------------------------------------------
# Strings Operations
# ---------------------------------------------------------------------------------------------------------------------
# name = "Sourav"     # or 'Sourav'
# print(name[0])      # S
# print(name[-1])     # v
# print(name[0:4])    # Sour - will not return the character at index 4
# print(name[2:])     # urav
# print(name[:3])     # Sou
# print(name[1:-1])   # oura - will not return the last character at index -1
# print(name[:])      # Sourav
# print(name[::])     # Sourav
# print(name[::1])    # Sourav
# print(name[::2])    # Sua - In steps of 2
# print(name[::-1])   # varuoS - reversed string
# print(name[::-2])   # vro - reversed string in steps of 2


# ---------------------------------------------------------------------------------------------------------------------
# Formatted Strings
# ---------------------------------------------------------------------------------------------------------------------
first_name = 'Sourav'
last_name = 'Basu'
print(f'{first_name} [{last_name}]')            # Sourav [Basu]

print('I am {} {}.'.format(first_name, last_name))

planet = 'Pluto'
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))


s = """\nPluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)


# ---------------------------------------------------------------------------------------------------------------------
# Strings Functions
# ---------------------------------------------------------------------------------------------------------------------
# name = 'Sourav Basu'
# print('\n')
# print(len(name))                    # len is general purpose function, not restricted to strings
# print(name.upper())                 # upper etc. are methods of string class
# print(name.lower())
# print(name.find('u'))               # 2
# print(name.find('z'))               # -1 (not found)
# print(name.find('Basu'))            # 7
# print(name.replace('Basu', 'ZZZ'))
# print('Basu' in name)               # True
# print(name.title())                 # returns every word with first letter capitalized
# print(name.startswith('So'))        # True
# print(name.endswith('su'))          # True


# print('123'.isdigit())              # True (True if all characters in the string are digit)
# print('123.9'.isdigit())            # False

# print('123'.isnumeric())            # True (True if all characters in the string are numeric or Unicode characters)
# print('123.9'.isnumeric())          # False

# print('123'.isdecimal())            # True (True if all characters in the string are decimals)
# print('123.9'.isdecimal())          # False

# ---------------------------------------------------------------------------------------------------------------------
# Multiline String:
# ---------------------------------------------------------------------------------------------------------------------
# address = '''123 Main St.
# NY
# 12345
# '''
# print(address)


# ---------------------------------------------------------------------------------------------------------------------
# String Split:
# ---------------------------------------------------------------------------------------------------------------------
# message = 'How are you doing?'
# print(message)
# print(message.split(' '))                         # ['How', 'are', 'you', 'doing?']


# ---------------------------------------------------------------------------------------------------------------------
# String Join:
# ---------------------------------------------------------------------------------------------------------------------
# my_list = ['How', 'are', 'you', 'doing?']
# print(' '.join(my_list))                           # 'How are you doing?' join with space
#
# my_list = ['S', 'o', 'u', 'r', 'a', 'v']
# print(''.join(my_list))                            # 'Sourav' join without space
#
# my_list = ['1', '2', '3', '4', '5']
# separator = ' --> '
# print(separator.join(my_list))                     # 1 --> 2 --> 3 --> 4 --> 5 join with other strings


# ---------------------------------------------------------------------------------------------------------------------
# String Strip:
# ---------------------------------------------------------------------------------------------------------------------
# my_string = '    Sourav     '
# print(my_string)                            # '    Sourav     '
# print(my_string.strip())                    # 'Sourav'
#
# my_string = 'malayalam'
# print(my_string)                            # 'malayalam'
# print(my_string.strip('ma'))                # 'layal' - removes all occurrences of 'm' and 'a' at both ends
# print(my_string.strip('mal'))               # 'y' - removes all occurrences of 'm', 'a', and 'l at both ends


# ---------------------------------------------------------------------------------------------------------------------
# String Sort:
# ---------------------------------------------------------------------------------------------------------------------
# my_sentence = 'Jessica found a dollar on the ground'
# print()
# print(my_sentence)
# print(sorted(my_sentence.split()))
# print(sorted(my_sentence.split(), key=len))
# print(sorted(my_sentence.split(), key=len, reverse=True))
