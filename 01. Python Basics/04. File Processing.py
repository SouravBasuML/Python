from pathlib import Path

# ---------------------------------------------------------------------------------------------------------------------
# File Processing:
# ---------------------------------------------------------------------------------------------------------------------
# r  -> Read (default)
#       File pointer is placed at the beginning of the file
#       Throws error if file does not exist
# w  -> Write.
#       Will create a new file if file does not exist
#       Will delete existing content and overwrite new content
# a  -> Append
#       The file pointer is at the end of the file if the file exists
#       If the file does not exist, it creates a new file for writing
# r+ -> Read and write
#       The file pointer will be at the beginning of the file
# w+ -> Write and read.
#       Will create a new file (for writing ands reading) if file does not exist
#       Will delete existing content and overwrite new content
# a+ -> Append and write
#       The file pointer is at the end of the file if the file exists
#       If the file does not exist, it creates a new file for reading and writing
# rb, wb, ab -> read, write, append in binary format
# ---------------------------------------------------------------------------------------------------------------------

# emp_file = open("Employees.txt", "r")
# print(emp_file.readable())          # True
# print(emp_file.readline())          # reads one line from the current position
# print(emp_file.read())              # reads entire file from the current position
# print(emp_file.readline())          # reads one line from the current position
# print(emp_file.readlines())         # reads all the lines from current position and puts them in a list
# # print(emp_file.readlines()[1])
# emp_file.close()
#
#
# # Read every line in file and calculate word count:
# print('\nWord Count:')
# emp_file = open("Employees.txt", "r")
# for employee in emp_file:
#     print(employee)
#     tokens = employee.split(' ')
#     print(tokens)
#     print(len(tokens))
# emp_file.close()
#
#
# # with: you don't have to explicitly close the file:
# print('with:')
# with open("Employees.txt", "r") as f:
#     print(f.read())
# print(f.closed)                     # to check if file is closed
#
#
# # Append
# emp_file = open("Employees.txt", "a")
# emp_file.write("\nFFF")
# emp_file.close()
#
#
# # Write
# emp_file = open("Employees1.txt", "w")
# emp_file.write("\nFFF")
# emp_file.close()


# ---------------------------------------------------------------------------------------------------------------------
# Directory, Path:
# ---------------------------------------------------------------------------------------------------------------------
# Absolute path: C:\Program Files\...
# Relative path

# Create a Path object to reference a file or directory in our computer
print("\nDirectory:")
print("----------")

path1 = Path("ecommerce")           # path1 is object of class Path
print(path1.exists())

path1 = Path("Emails")
path1.mkdir()                       # creates new directory Emails
path1.rmdir()                       # removes Emails directory

# Find all the files and directories in a given path:
path2 = Path()                      # changes path to current directory
print(path2)
print(path2.glob('*.*'))            # returns generator object

#   *       -> all files and directories in the current path
#   *.*     -> all files in the current path but not directories
#   *.xls   -> all excel files

print('\nPrinting all .py files in the current directory: ')
for file in path2.glob('*.py'):
    print(file)

print('\nPrinting all files and directories in the current directory: ')
for file in path2.glob('*'):
    print(file)
