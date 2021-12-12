import datetime

# ---------------------------------------------------------------------------------------------------------------------
# OOP in Python:
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# Class:
# ---------------------------------------------------------------------------------------------------------------------
# Class: Blue print for real world objects
# Attributes: Data variables within a class
# Methods: functions of a class
# ---------------------------------------------------------------------------------------------------------------------

# class Point:                          # Pascal naming convention
#     def move(self):                   # self is a reference to the current object in memory
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
#
# print(point1.x)
# print(point1.y)
# point1.draw()
# point1.move()


# ---------------------------------------------------------------------------------------------------------------------
# __init__ (Constructor)
# ---------------------------------------------------------------------------------------------------------------------
# The __init__ method is called automatically when the object is first created
# 'self' is a reference to the current object in memory. You can use any other variable but 'self' in the convention
# ---------------------------------------------------------------------------------------------------------------------

# class Point:
#     def __init__(self, x=1, y=1):       # constructor. you can pass default values
#         self.x = x                      # current_object.attribute = argument passed
#         self.y = y                      # x and y are instance variables. Their data is unique to each instance
#         print('x: ', x)
#         print('y: ', y)
#
#     def print_point(self):
#         print(f'Point is at ({self.x}, {self.y})')
#
#
# print("\nConstructor:")
# point1 = Point()                        # x=1, y=1
# point1.print_point()                    # Point is at (1, 1)
#
#
# # No need to pass the instance argument in 'self' parameter for __init__; it is done automatically. Hence we must
# # code self in all the class methods, else there will be a TypeError
# point2 = Point(x=10, y=20)              # x=10, y=20.
# print(point2.x)                         # x is attribute of the point2 object
#
#
# # Both the below statements will do the same thing
# point2.print_point()                    # calling the method using the instance (self is automatically passed)
# Point.print_point(point2)               # calling the method using the Class and passing the instance as argument


# ---------------------------------------------------------------------------------------------------------------------
# Class Variables
# ---------------------------------------------------------------------------------------------------------------------
# Class variables are variables that are shared by all instances of a class. They must be accessed using:
# 1. the class itself or
# 2. through an instance of a class
# ---------------------------------------------------------------------------------------------------------------------
# class Employee:
#
#     # class variables
#     num_of_employees = 0
#     raise_pct = 1.04
#
#     def __init__(self, first, last, salary):
#         self.first = first
#         self.last = last
#         self.salary = salary
#         self.email = first + '.' + last + '@company.com'
#         Employee.num_of_employees += 1                          # accessing class variable using class
#
#     def apply_raise(self):
#         self.salary = self.salary * self.raise_pct              # accessing class variable using instance
#
#
# if __name__ == '__main__':
#
#     print(Employee.num_of_employees)    # 0
#
#     emp1 = Employee('f1', 'l1', 50000.0)
#     emp2 = Employee('f2', 'l2', 60000.0)
#
#     print(Employee.num_of_employees)    # 2
#     print(emp1.num_of_employees)        # 2
#     print(emp2.num_of_employees)        # 2
#
#     print(emp1.salary)                  # 50000.0
#     emp1.apply_raise()
#     print(emp1.salary)                  # 52000.0
#
#     # When we access an attribute on an instance, Python first checks if the instance contains the attribute.
#     # If it doesn't then it checks if its class or any class in its inheritance hierarchy has that arrtibute.
#     print(Employee.raise_pct)           # 1.04 (class variable accessed using the Class)
#     print(emp1.raise_pct)               # 1.04 (class variable accessed using the instance of the Class)
#     print(emp2.raise_pct)               # 1.04
#     print(emp1.__dict__)                # no class variables are present in the namespace
#     print(Employee.__dict__)            # class variables are present in the namespace
#
#     emp1.raise_pct = 1.05               # only changes the value for that instance
#     print(Employee.raise_pct)           # 1.04
#     print(emp1.raise_pct)               # 1.05 (raise_pct becomes an attribute of emp1)
#     print(emp2.raise_pct)               # 1.04 (returns the value of the class variable)
#     print(emp1.__dict__)                # raise_pct is now an attribute of this instance
#     print(emp2.__dict__)                # raise_pct is not available in this instance
#
#     Employee.raise_pct = 1.05           # changes the value for all instances
#     print(Employee.raise_pct)           # 1.05
#     print(emp1.raise_pct)               # 1.05
#     print(emp2.raise_pct)               # 1.05


# ---------------------------------------------------------------------------------------------------------------------
# Class Methods and Static Methods
# ---------------------------------------------------------------------------------------------------------------------
# Regular methods in a class automatically take the instance of the class as the first argument (self)
# Class methods take the class as the first argument (cls).
# Class methods are created by decorating the method with @classmethod
# ---------------------------------------------------------------------------------------------------------------------
# Static methods take neither self, nor cls as the first argument. They behave like regular functions. We include
# them in class because they have some logical connection with the class. e.g. a function that takes a date and
# returns if it is a workday or a weekend. This method is a good candidate for static method because it has a logical
# connection with Employee class but is not dependent on the class or any instances.
# Static methods are created by decorating the method with @staticmethod
# ---------------------------------------------------------------------------------------------------------------------
# class Employee:
#
#     # class variables
#     num_of_employees = 0
#     raise_pct = 1.04
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.num_of_employees += 1                      # accessing class variable using class
#
#     def apply_raise(self):
#         self.salary = self.salary * self.raise_pct          # accessing class variable using instance
#
#     @classmethod
#     def set_raise_amt(cls, new_hike):
#         # in this method we are working with the class and not an instance
#         cls.raise_pct = new_hike                            # updating class variable using cls instead of Employee
#
#     @classmethod
#     def from_string(cls, emp_str):
#         # if class methods are used as alternate constructors, convention is to begin the method name with 'from_'
#         name, salary = emp_str.split('-')
#         return cls(name=name, salary=salary)                # creates a new object using the cls variable
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:        # 5: Sat, 6: Sun
#             return False
#         return True
#
#
# if __name__ == '__main__':
#     emp1 = Employee('emp1', 50000.0)
#     emp2 = Employee('emp2', 60000.0)
#
#     print(Employee.raise_pct)                   # 1.04
#     print(emp1.raise_pct)                       # 1.04
#     print(emp2.raise_pct)                       # 1.04
#
#     # Using class method to update the class variable (this can also be done using Employee.raise_pct = 1.05)
#     Employee.set_raise_amt(new_hike=1.05)
#     print(Employee.raise_pct)                   # 1.05
#     print(emp1.raise_pct)                       # 1.05
#     print(emp2.raise_pct)                       # 1.05
#
#     # Class methods can be run from instances as well, but not a good practice.
#     # Doing this also changes the class variable and hence for all instances
#     emp1.set_raise_amt(new_hike=1.06)
#     print(Employee.raise_pct)                   # 1.06
#     print(emp1.raise_pct)                       # 1.06
#     print(emp2.raise_pct)                       # 1.06
#
#     # Class methods can be used as alternative constructors (a different way of creating objects)
#     # e.g. creating Employee objects from string objects
#     emp3_str = 'emp3-70000'
#     emp3 = Employee.from_string(emp_str=emp3_str)
#     print(emp3.salary)
#
#     # Static method:
#     my_date = datetime.date(year=2021, month=9, day=27)
#     print(Employee.is_workday(day=my_date))


# ---------------------------------------------------------------------------------------------------------------------
# Single Inheritance
# ---------------------------------------------------------------------------------------------------------------------
# class Employee:
#     # class variable
#     raise_pct = 1.04
#
#     def __init__(self, first, last, salary):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.salary = salary
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.salary = self.salary * self.raise_pct
#
#
# class Developer(Employee):
#     # class variable. Inherits this from base class, but overrides
#     raise_pct = 1.10
#
#     def __init__(self, first, last, salary, prog_lang):
#         # you can also use Employee.__init__(self, first, last, salary). Better to use super().__init__()
#         super().__init__(first=first, last=last, salary=salary)
#         self.prog_lang = prog_lang
#
#
# class Manager(Employee):
#     def __init__(self, first, last, salary, emp_list=[]):               # better to initialize emp_list using None
#         super().__init__(first=first, last=last, salary=salary)
#         self.emp_list = emp_list
#
#     def add_emp(self, emp):
#         if emp not in self.emp_list:
#             self.emp_list.append(emp)
#
#     def remove_emp(self, emp):
#         if emp in self.emp_list:
#             self.emp_list.remove(emp)
#
#     def print_emps(self):
#         for emp in self.emp_list:
#             print(self.first + ' supervises ' + emp.fullname() + ' -> ' + emp.email)
#
#
# if __name__ == '__main__':
#
#     emp_1 = Employee('Corey', 'Schafer', 50000.0)
#     dev_1 = Developer('Sourav', 'Basu', 60000.0, 'Python')
#     print(help(Developer))                          # To see the method resolution order and inherited items
#
#     print(emp_1.salary)                             # 50000.0
#     print(dev_1.salary)                             # 60000.0
#     emp_1.apply_raise()                             # Applies 4% raise
#     dev_1.apply_raise()                             # Applies 10% raise
#     print(emp_1.salary)                             # 52000.0
#     print(dev_1.salary)                             # 66000.0
#
#     # reading subclass attribute
#     print(dev_1.prog_lang)                          # Python
#
#     mgr_1 = Manager(first='Jane', last='Doe', salary=90000, emp_list=[emp_1])
#     mgr_1.add_emp(emp=dev_1)
#     mgr_1.print_emps()
#     mgr_1.remove_emp(emp=emp_1)
#     mgr_1.print_emps()
#
#     # isinstance()
#     print(isinstance(dev_1, Developer))             # True
#     print(isinstance(dev_1, Employee))              # True
#     print(isinstance(dev_1, Manager))               # False
#
#     # issubclass()
#     print(issubclass(Manager, Employee))            # True
#     print(issubclass(Developer, Employee))          # True
#     print(issubclass(Employee, Manager))            # False
#     print(issubclass(Manager, Manager))             # True
#     print(issubclass(Employee, Employee))           # True


# ---------------------------------------------------------------------------------------------------------------------
# Multiple Inheritance
# ---------------------------------------------------------------------------------------------------------------------
# class Father:
#     def hobby(self):
#         print('Father: I love gardening')
#
#
# class Mother:
#     def hobby(self):
#         print('Mother: I love cooking')
#
#
# class Child(Mother, Father):
#     def sports(self):
#         Father.hobby(self)
#         Mother.hobby(self)
#         print('Child: I love sports')
#
#
# if __name__ == '__main__':
#     f = Father()
#     f.hobby()           # Father: I love gardening
#
#     m = Mother()
#     m.hobby()           # Mother: I love cooking
#
#     c1 = Child()
#     c1.hobby()          # child class inherits method of same name from the first class of multiple inheritance
#     c1.sports()
