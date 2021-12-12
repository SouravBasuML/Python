import json

# ----------------------------------------------------------------------------------------------------------------------
# JSON (Java Script Object Notation) is a language-independent, data exchange format
# ----------------------------------------------------------------------------------------------------------------------

# Create an Address Book dictionary
book_dict = {
    'tom': {
        'name': 'tom',
        'address': '1 tom st',
        'phone': 2323333323
    },
    'bob': {
        'name': 'bob',
        'address': '1 bob st',
        'phone': 9898787987
    }
}
print('\nDictionary: ', book_dict)
print(type(book_dict))

# ----------------------------------------------------------------------------------------------------------------------
# json.dump()
# ----------------------------------------------------------------------------------------------------------------------
# Take the dict and dump it into a .json file:
with open('Address Book.json', 'w') as f:
    json.dump(book_dict, f, indent=4)

# ----------------------------------------------------------------------------------------------------------------------
# json.dumps()
# ----------------------------------------------------------------------------------------------------------------------
# Take the dict and dump it as a string in JSON format
json_string = json.dumps(book_dict, indent=4)
print('\nJSON String: ', json_string)
print(type(json_string))

# Write the JSON string to a file:
with open('Address Book.txt', 'w') as f:
    f.write(json_string)
f.close()


# ----------------------------------------------------------------------------------------------------------------------
# json.load()
# ----------------------------------------------------------------------------------------------------------------------
# Load the .json file parse it into a JSON object
with open('Address Book.json', 'r') as f:
    print('\nReading from .json file: ')
    print(json.load(f))


# Once data is written to a file in JSON format, you can now read this JSON data using any language
# that supports JSON such as JS, C++ etc.
f = open('Address Book.txt', 'r')
book_string = f.read()
f.close()

print('\nString read from file: ', book_string)
print(type(book_string))


# ----------------------------------------------------------------------------------------------------------------------
# json.loads()
# ----------------------------------------------------------------------------------------------------------------------
# Load the string as a dictionary and parse it into a JSON object
add_dict = json.loads(book_string)
print('\nDictionary: ', add_dict)
print(type(add_dict))

# Read the data in dictionary
print(add_dict['bob'])
print(add_dict['bob']['phone'])

for person in add_dict:
    print(person)
    print(add_dict[person])
