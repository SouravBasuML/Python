# ---------------------------------------------------------------------------------------------------------------------
# Scope
# ---------------------------------------------------------------------------------------------------------------------

x = 1
print('\n1.')
print(id(x))


def test():
    x = 2
    print(id(x))


test()
print(id(x))
print(x)    # 1

# ---------------------------------------------------------------------------------------------------------------------
y = 1
print('\n2.')
print(id(y))


def test():
    global y
    y = 2
    print(id(y))


test()
print(id(y))
print(y)    # 2

# ---------------------------------------------------------------------------------------------------------------------
global z
z = 1
print('\n3.')
print(id(z))


def test():
    z = 2
    print(id(z))


test()
print(id(z))
print(z)    # 1

# ---------------------------------------------------------------------------------------------------------------------
a = [1]
print('\n4.')
print(id(a))


def test():
    a = [2]
    print(id(a))


test()
print(id(a))
print(a)    # [1]

# ---------------------------------------------------------------------------------------------------------------------
b = [1]
print('\n5.')
print(id(b))


def test():
    global b
    b = [2]
    print(id(b))


test()
print(id(b))
print(b)    # [2]

# ---------------------------------------------------------------------------------------------------------------------
c = [1]
print('\n6.')
print(id(c))


def test():
    c[0] = 2
    print(id(c))


test()
print(id(c))
print(c)    # [2]
# ---------------------------------------------------------------------------------------------------------------------
