
# ---------------------------------------------------------------------------------------------------------------------
# Property Decorator:
# ---------------------------------------------------------------------------------------------------------------------
# The property decorator allows us to define Class methods that we can access like attributes.
# This allows us to implement getter, setter, and deleter functionality for our class attributes.
# Using property decorators, we can change code in a class without breaking others' code.
# ---------------------------------------------------------------------------------------------------------------------
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


if __name__ == '__main__':
    emp_1 = Employee(first='John', last='Smith')
    print(emp_1.first)                      # John
    print(emp_1.email)                      # John.Smith@email.com
    print(emp_1.fullname())                 # John Smith

    # Without @property:
    # Changing first name, does not change email. It changes the fullname correctly because the fullname() always
    # reads the latest first and last names
    emp_1.first = 'Jim'
    print(emp_1.first)                      # Jim
    print(emp_1.email)                      # John.Smith@email.com -> does not change email
    print(emp_1.fullname())                 # Jim Smith

    # If we change email from an attribute to method, it will break others' code who are using this class.
    # They will have to change how they read email from an attribute to a method.
    # To correct this, we can use getter and setter methods as in Java. Python provides the @property

    # With @property:
    # We can call email method just like an attribute
    emp_1.first = 'Jim'
    print(emp_1.first)                      # Jim
    print(emp_1.email)                      # Jim.Smith@email.com
    print(emp_1.fullname())                 # Jim Smith


# ---------------------------------------------------------------------------------------------------------------------
# Setter, Getter, Deleter: Using property decorator
# ---------------------------------------------------------------------------------------------------------------------
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter                                        # setter property decorator
    def fullname(self, fullname):
        self.first, self.last = fullname.split(' ')

    @fullname.deleter                                       # deleter property decorator
    def fullname(self):
        print('Deleting full name')
        self.first = None
        self.last = None


if __name__ == '__main__':
    emp_1 = Employee(first='John', last='Smith')
    print(emp_1.first)                      # John
    print(emp_1.email)                      # John.Smith@email.com
    print(emp_1.fullname)                   # John Smith

    # Setter:
    # If you want to change full name and correspondingly change first name, last name and email,
    # With just the @property (but without the setter), it throws an AttributeError: can't set attribute
    emp_1.fullname = 'Sourav Basu'
    print(emp_1.first)                      # John
    print(emp_1.email)                      # John.Smith@email.com
    print(emp_1.fullname)                   # John Smith

    # Deleter:
    del emp_1.fullname
    print(emp_1.first)                      # None
    print(emp_1.email)                      # None.None@email.com
    print(emp_1.fullname)                   # None None
