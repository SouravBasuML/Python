# ---------------------------------------------------------------------------------------------------------------------
# Dunder or Magic Methods:
# ---------------------------------------------------------------------------------------------------------------------
# See also: OOP.py
# ---------------------------------------------------------------------------------------------------------------------
# Dunder methods are double underscored methods that are used to emulate the behavior of built-in types.
# Commonly used for operator overloading e.g. __init__, __add__, __len__, __str__, __repr__ etc.
# ---------------------------------------------------------------------------------------------------------------------

a = 'Hello'
b = ' Sourav'
print(a.__add__(b))                 # Hello Sourav -> same as a + b
print(int.__add__(1, 2))            # 3
print(str.__add__('a', 'b'))        # ab
print(a.__contains__('H'))          # True -> same as 'H' in a
print(a.__eq__('Hello'))            # True -> same as a == 'Hello'
print(a.__len__())                  # 5 -> Same as len(a)
print(a.__str__())                  # Hello -> same as print(str(a))
print(a.__repr__())                 # 'Hello' -> same as print((repr(a))
print(a.__getitem__(2))             # l -> same as a[2]

c = {1: 'a', 2: 'b', 3: 'c'}
c.__setitem__(3, 'p')               # same as c[3] = 'p'
print(c)                            # {1: 'a', 2: 'b', 3: 'p'}


# ---------------------------------------------------------------------------------------------------------------------
# Implementation of __add__, __repr__ in a class
# ---------------------------------------------------------------------------------------------------------------------

# class String:
#     def __init__(self, string):
#         self.string = string
#
#     def __repr__(self):
#         return 'Printing Object: {}'.format(self.string)
#
#     def __add__(self, other):
#         return self.string + other
#
#
# if __name__ == '__main__':
#     string1 = String("Hello")
#
#     # Without __repr__ or __str__: prints memory address of the string object
#     # With __repr__ or __str__: Printing Object: Hello
#     print(string1)
#
#     # Without __add__ TypeError: unsupported operand type(s) for +: 'String' and 'str'
#     # with __add__: 'Hello Sourav'
#     print(string1 + ' Sourav')


# ---------------------------------------------------------------------------------------------------------------------
# __setitem__ and __getitem__
# ---------------------------------------------------------------------------------------------------------------------
# __setitem__ and __getitem__ are methods used for assigning value to and accessing value of an item.
# They are implicitly invoked when we set a value to an item or access an item of a list, tuple dictionary, etc.
# We can overload their operations by explicitly defining them.
# ---------------------------------------------------------------------------------------------------------------------
# class CustomList(object):
#     def __init__(self, elements=0):
#         self.my_custom_list = [0] * elements
#
#     def __setitem__(self, index, value):
#         self.my_custom_list[index] = value
#
#     def __getitem__(self, index):
#         return 'You are accessing element {} whose value is: {}'.format(index, self.my_custom_list[index])
#
#     def __str__(self):
#         return 'My List is: ' + str(self.my_custom_list)
#
#     def get_len(self):
#         return 'Length of my list is: ', self.my_custom_list.__len__()
#
#
# if __name__ == '__main__':
#     my_list = CustomList(12)
#     print(my_list)                      # you can directly print the object my_list because of __str__
#
#     my_list[0] = 99                     # you can assign a value using the object because of __setitem__
#     print(my_list[0])                   # you can retrieve a value using the object because of __getitem__
#     print(my_list)
#
#     print(my_list.get_len())


# ---------------------------------------------------------------------------------------------------------------------
# Dunder or Magic Methods in Class
# ---------------------------------------------------------------------------------------------------------------------
# Emulates built in methods in Python. Used for operator overloading
# ---------------------------------------------------------------------------------------------------------------------
# class Employee:
#
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):                   # is implicitly called whenever we create an object
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#     # __repr__ is for unambiguous representation of the object (primarily used by developers)
#     # Output of __repr__ should be such that it can be used in Python code to recreate the object
#     # if __str__ is not coded, it defaults to __repr__. (but not the other way round).
#     # __repr__ should be coded at the minimal
#     def __repr__(self):
#         return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
#
#     # __str__ is for readable representation of the object (primarily used by end users)
#     def __str__(self):
#         return '{} - {}'.format(self.fullname(), self.email)
#
#     # overriding '+' to add salaries of employees
#     def __add__(self, other):
#         return self.pay + other.pay
#
#     # overriding len() to get the length of employee's fullname
#     def __len__(self):
#         return len(self.fullname())
#
#
# if __name__ == '__main__':
#
#     emp_1 = Employee('Corey', 'Schafer', 50000.0)
#     emp_2 = Employee('Sourav', 'Basu', 60000.0)
#
#     print(emp_1.__repr__())
#     print(repr(emp_1))                  # this is actually calling emp_1.__repr__() in the background
#     print(emp_1.__str__())
#     print(str(emp_1))                   # this is actually calling emp_1.__str__() in the background
#     print(emp_1)                        # uses __str__. If it is not coded will fall back to __repr__
#
#     print(emp_1 + emp_2)                # 110000.0
#     print(len(emp_2))                   # 11

