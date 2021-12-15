"""
-----------------------------------------------------------------------------------------------------------------------
Dictionary (Maps, Hash Tables, Associate Arrays)
Duplicate keys are allowed, but only the last value will be considered
-----------------------------------------------------------------------------------------------------------------------
"""

customer = {
    "name": "Sourav",
    "age": 30,
    "hobbies": ['aaa', 'bbb', 'ccc'],
    "is_verified": True
}

print(customer)
print(type(customer))                       # <class 'dict'>

print(customer.keys())                      # dict_keys(['name', 'age', 'hobbies', 'is_verified'])
print(customer.values())                    # dict_values(['Sourav', 30, ['aaa', 'bbb', 'ccc'], True])

print(customer["name"])                     # case sensitive
# print(customer["Name"])                   # error

print(customer.get("birth_date"))           # returns none, not error
print(customer.get("birth_date", "Jan 1"))  # adds a default value if key not present

customer["name"] = "Basu"                   # modify using a key
print(customer)

customer["birth_date"] = "Jan 2 1980"       # adds a new key
print(customer)

del customer["birth_date"]                  # deletes a key
print(customer)

print(customer.pop('age'))                  # returns and removes the item whose key is provided
print(customer)

print(customer.popitem())                   # returns and removes the last item
print(customer)

# customer.clear()                          # clears the dictionary


# ---------------------------------------------------------------------------------------------------------------------
# Loop over a dictionary:
# ---------------------------------------------------------------------------------------------------------------------
print('\n')
for key, value in customer.items():
    print(key, value)
for key in customer:
    print(key, customer[key])


# ---------------------------------------------------------------------------------------------------------------------
# Duplicate Keys (allowed):
# ---------------------------------------------------------------------------------------------------------------------
customer1 = {
    "name": "Sourav",
    "name": "Basu"
}
print(customer1)


# ---------------------------------------------------------------------------------------------------------------------
# Empty Dictionary:
# ---------------------------------------------------------------------------------------------------------------------
empty_dict = {}
empty_dict = dict()


# ---------------------------------------------------------------------------------------------------------------------
# Dictionaly within Dictionary:
# ---------------------------------------------------------------------------------------------------------------------
book_dict = {
    'tom': {
        'name': 'tom',
        'address': {
            'street1': '1 tom st',
            'street2': 'NY',
            'zip': 10001,
        },
        'phone': 2323333323
    },
    'bob': {
        'name': 'bob',
        'address': '1 bob st',
        'phone': 9898787987
    }
}

print(book_dict)
print(book_dict['tom'])
print(book_dict['tom']['name'])
print(book_dict['tom']['address'])
print(book_dict['tom']['address']['zip'])


# ---------------------------------------------------------------------------------------------------------------------
# Merge Dictionaries:
# ---------------------------------------------------------------------------------------------------------------------
x_dict = {'a': 10, 'b': 20, 'c': 30}
y_dict = {'m': 70, 'n': 80, 'o': 90}
z_dict = {'x': 40, 'y': 50, 'z': 60}
print('x_dict:', x_dict)
print('y_dict:', y_dict)
print('z_dict:', z_dict)

# Merge using update():
x_dict.update(y_dict)
x_dict.update(z_dict)
print('x_dict:', x_dict)

# Merge by unpacking (using **):
x_dict = {'a': 10, 'b': 20, 'c': 30}
y_dict = {'m': 70, 'n': 80, 'o': 90}
z_dict = {'x': 40, 'y': 50, 'z': 60}
merged_dict = {**x_dict, **y_dict, **z_dict}
print('merged_dict:', merged_dict)

# Merge using Union (|) operator: (Python 3.9 and above)
merged_dict = x_dict | y_dict | z_dict
print('merged_dict:', merged_dict)


# ---------------------------------------------------------------------------------------------------------------------
# Sort a Dictionary:
# ---------------------------------------------------------------------------------------------------------------------
my_dict = {
    'd': 54,
    'a': 38,
    'c': 24,
    'e': 11,
    'b': 67
}

for key, value in my_dict.items():
    print(key, value)

print('Sorted Dict by Key:')
for key in sorted(my_dict):
    print(key, my_dict[key])

print('Sorted Dict by Value:')
sorted_dict = {}
sorted_keys = sorted(my_dict, key=my_dict.get)
for key in sorted_keys:
    sorted_dict[key] = my_dict[key]
    print(key, my_dict[key])


# ---------------------------------------------------------------------------------------------------------------------
# Switch-Case using Dictionary:
# ---------------------------------------------------------------------------------------------------------------------
def week(day_of_week):
    switcher = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return switcher.get(day_of_week, "Invalid day of week")


print(week(day_of_week=8))
