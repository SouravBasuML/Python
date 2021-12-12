import platform

print()
print(platform.platform())                      # Windows-10-10.0.19041-SP0
print(platform.system())                        # Windows
print(platform.release())                       # 10
print(platform.machine())                       # AMD64
print(platform.architecture())                  # ('32bit', 'WindowsPE')
print(platform.processor())                     # Intel64 Family 6 Model 94 Stepping 3, GenuineIntel

print()
print(platform.python_build())                  # ('tags/v3.8.1:1b293b6', 'Dec 18 2019 22:39:24')
print(platform.python_branch())                 # tags/v3.8.1
print(platform.python_version())                # 3.8.1
print(platform.python_version_tuple())          # ('3', '8', '1')
print(platform.python_revision())               # 1b293b6
print(platform.python_implementation())         # CPython
print(platform.python_compiler())               # MSC v.1916 32 bit (Intel)
