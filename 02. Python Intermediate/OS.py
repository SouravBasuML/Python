import os
from datetime import datetime

# ---------------------------------------------------------------------------------------------------------------------
# OS Module:
# ---------------------------------------------------------------------------------------------------------------------
# Allows us to interact with the underlying OS, e.g. navigate the file system, get file information, create directories,
# move files, lookup and change the environment variables etc.
# ---------------------------------------------------------------------------------------------------------------------

# print(dir(os))

# print(os.getcwd())                                      # Current working Directory
# os.chdir('C:\\Users\DELL\PycharmProjects\py_env')       # Change Directory
# print(os.getcwd())

# print(os.listdir())                                     # List the contents of the current working directory
# print(os.listdir('C:\\Users\DELL\PycharmProjects'))     # List the contents of the speified directory


# os.mkdir('Demo Folder')                                 # Creates a directory/folder
# os.makedirs('Dir1\SubDir1\SubDir2')                     # Creates a hierarchy of directories/folders

# os.rmdir('Demo Folder')                                 # Removes a directory. Safer to use
# os.removedirs('Dir1')                                   # Error: Directory is not empty
# os.removedirs('Dir1\SubDir1\SubDir2')                   # Removes the entire directory hierarchy

# os.rename('old file name', 'new file name')


# ---------------------------------------------------------------------------------------------------------------------
# # File Statistics:
# ---------------------------------------------------------------------------------------------------------------------
# print(os.stat('Address Book.txt'))
# print(os.stat('Address Book.txt').st_size)                              # File size in bytes
# print(datetime.fromtimestamp(os.stat('Address Book.txt').st_mtime))     # Last modification time

# ---------------------------------------------------------------------------------------------------------------------
# Traverse Directory Tree and print all sub-directories and files within:
# ---------------------------------------------------------------------------------------------------------------------
# # os.walk() yields a generator tuple of three values (dir-path, directories, files)
# for dirpath, dirnames, filenames in os.walk('C:\\Users\DELL\PycharmProjects\py_env'):
#     print('Dir Path: ', dirpath)
#     print('Dir Names: ', dirnames)
#     print('Dir Path: ', filenames)
#     print()

# ---------------------------------------------------------------------------------------------------------------------
# Environment Variables:
# ---------------------------------------------------------------------------------------------------------------------
print(os.environ)
print(os.environ.get('HOMEDRIVE'))                                      # C:
print(os.environ.get('HOMEPATH'))                                       # \Users\DELL


# ---------------------------------------------------------------------------------------------------------------------
# os.path():
# ---------------------------------------------------------------------------------------------------------------------
print(dir(os.path))

print(os.path.exists('/user/tmp/.text.txt'))                            # True if path exists
print(os.path.basename('/user/tmp/.text.txt'))                          # .text.txt
print(os.path.dirname('/user/tmp/.text.txt'))                           # /user/tmp
print(os.path.split('/user/tmp/.text.txt'))                             # ('/user/tmp', '.text.txt')
print(os.path.isdir('/user/tmp/.text.txt'))                             # True if directory
print(os.path.isfile('/user/tmp/.text.txt'))                            # True if file
print(os.path.splitext('/user/tmp/.text.txt'))                          # ('/user/tmp/.text', '.txt')

# Joining file paths:
file_path = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
print(file_path)                                                        # \Users\DELL\test.txt

# Create a file in the HOMEPATH:
with open(file_path, 'w') as f:
    f.write('aaa')
