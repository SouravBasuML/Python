import numpy as np

# ---------------------------------------------------------------------------------------------------------------------
# Numpy is implemented in C and Fortran
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Numpy arrays:
# ---------------------------------------------------------------------------------------------------------------------
# # Initializing a numpy array:
# a = np.array([1.0, 2.0, 3.0])
# b = np.array([[1, 2, 3], [4, 5, 6]])
#
# print('\nNumpy Array:')
# print(a)
# print(b)
# print(type(a))                                               # <class 'numpy.ndarray'>

# # Dimension:
# print('\nDimension:')
# print(a.ndim)                                               # 1
# print(b.ndim)                                               # 2

# # Shape:
# print('\nShape:')
# print(a.shape)                                              # (3,)
# print(b.shape)                                              # (2, 3)

# # Data Type:
# print('\nData Type:')
# c = np.array([[2, 3, 4], [5, 6, 7]], dtype='int8')
# print(a.dtype)                                              # float64
# print(b.dtype)                                              # int32
# print(c.dtype)                                              # int8

# # Size
# print('\nSize:')
# print(a.itemsize)                                           # 8 bytes (float64)
# print(b.itemsize)                                           # 4 bytes (int32)
# print(c.itemsize)                                           # 1 bytes (int8)

# # Number of elements
# print('\nNumber of elements:')
# print(a.size)                                               # 3 bytes (float64)
# print(b.size)                                               # 6 bytes (int32)
# print(c.size)                                               # 6 bytes (int8)

# # Total Size
# print('\nTotal Size:')
# print(a.nbytes)                                             # 24 bytes (float64)
# print(b.nbytes)                                             # 24 bytes (int32)
# print(c.nbytes)                                             # 6 bytes (int8)

# # If number of elements don't match in each dimension, numpy considers each dimension as a list
# A = np.array([[1, 2, 3], [4, 5]])
# print(A)                                                    # [list([1, 2, 3]) list([4, 5])]

# # arange()
# print('\narange():')
# print(np.arange(10))                                        # [0 1 2 3 4 5 6 7 8 9]
# print(np.arange(3, 10))                                     # [3 4 5 6 7 8 9]
# print(np.arange(0, 100, 5))                                 # (start, end, step)

# # linspace()
# print('\nlinspace():')
# print(np.linspace(start=1, stop=100, num=5))                # Generates linearly spaced 5 numbers between 1 and 100


# ---------------------------------------------------------------------------------------------------------------------
# Read/Modify/Slice Numpy Arrays:
# ---------------------------------------------------------------------------------------------------------------------
# A = np.array([[1, 2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8, 9]])
# print(A)

# # Get specific element:
# print('\nSpecific element:')
# print(A[1, 5])                                              # 8 [row, col]
# print(A[1, -2])                                             # 8 [row, col]

# # Get specific row:
# print('\nSpecific row:')
# print(A[0])                                                 # [1 2 3 4 5 6 7] - first row
# print(A[0, :])                                              # [1 2 3 4 5 6 7]
# print(A[-1])                                                # [3 4 5 6 7 8 9] - last row
# print(A[-1, 2:6])                                           # [5 6 7 8]

# # Get specific column:
# print('\nSpecific column:')
# print(A[:, 2])                                              # [3 5]

# # Get specific elements [start_index:end_index:step_size]:
# print(A[0, 1:-1:2])                                         # [2 4 6]

# # Change specific element:
# print('\nChange specific element:')
# A[1, 4] = 100
# print(A)

# # Change entire column:
# print('\nChange entire column:')
# A[:, 2] = 50
# print(A)
# A[:, 3] = [60, 70]
# print(A)

# # Change entire row:
# print('\nChange entire row:')
# A[0, :] = 1
# print(A)
# A[0, :] = [5, 6, 5, 6, 5, 6, 5]                             # same shape list needs to be specified
# print(A)


# ---------------------------------------------------------------------------------------------------------------------
# Iterate through Arrays: nditer
# ---------------------------------------------------------------------------------------------------------------------
# a = np.arange(12).reshape(3, 4)
# print(a)

# for row in a:
#     print(row)

# for row in a:
#     for item in row:
#         print(item)

# for item in a.flatten():
#     print(item)

# for item in np.nditer(a, order='C'):                # C order -> row-wise
#     print(item)

# for item in np.nditer(a, order='F'):                # Fortran order -> col-wise
#     print(item)


# ---------------------------------------------------------------------------------------------------------------------
# Iterate through Two Arrays: Shape should be compatible
# ---------------------------------------------------------------------------------------------------------------------
# a = np.arange(12).reshape(3, 4)
# b = np.arange(100, 112).reshape(3, 4)
# print(a)
# print(b)

# for x, y in np.nditer([a, b]):
#     print(x, y)

# a = np.arange(12).reshape(3, 4)
# b = np.array([100, 200, 300]).reshape(3, 1)
# print(a)
# print(b)

# for x, y in np.nditer([a, b]):
#     print(x, y)


# ---------------------------------------------------------------------------------------------------------------------
# 3D Arrays:
# ---------------------------------------------------------------------------------------------------------------------
# A = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print('\n3D Arrays:')
# print(A)
# print(A.ndim)                                               # 3
# print(A[0, 1, 1])                                           # 4 (work outside in)
# print(A[1, 0, 1])                                           # 6 (work outside in)
# print(A[:, 1:, :])
# A[:, 1, :] = [[9, 9], [9, 9]]                               # replace - provide list of same shape
# print(A)


# ---------------------------------------------------------------------------------------------------------------------
# Initializing Numpy Arrays:
# ---------------------------------------------------------------------------------------------------------------------
# # Initializing 0s:
# print(np.zeros(5))                                          # 0's matrix - 1D
# print(np.zeros((2, 3, 3, 3)))                               # 0's matrix - 4D

# # Initializing 1s:
# print(np.ones((4, 3, 3), dtype='int16'))                    # 1's matrix - 3D

# # Initializing any number:
# print(np.full((2, 2), 99))                                  # 2D matrix initialized with 99. full((shape), init_val)

# # Initializing a matrix of previously defined shape:
# A = np.array([[1, 2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8, 9]])
# print(A)
# print(np.full(A.shape, 4))
# print(np.full_like(A, 4))

# # Random initialization:
# A = np.array([[1, 2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8, 9]])
# print(np.random.rand(4, 2))                                 # np.random.rand(shape)
# print(np.random.random_sample(A.shape))
# print(np.random.randint(-2, 9, size=(3, 4)))                 # randint(start (inclusive), end (exclusive), shape)

# # Identity Matrix:
# print(np.identity(5))

# # Repeating matrix:
# A = np.array([[1, 2, 3]])
# print(A)
# print(np.repeat(A, 3, axis=0))
# print(np.repeat(A, 3))                                      # axis=1 is the default
# print(np.repeat(A, 3, axis=1))

# # Practice:
# OP = np.ones((5, 5))
# Z = np.zeros((3, 3))
# Z[1, 1] = 9
# OP[1: 4, 1: 4] = Z                                          # OP[1: -1, 1: -1] = Z
# print(OP)

# # Copying arrays:
# a = np.array([1, 2, 3])
# b = a                                                       # Copying reference
# b[1] = 100
# print(b)
# print(a)                                                    # a changes

# a = np.array([1, 2, 3])
# b = a.copy()                                                # Copying value
# b[1] = 100
# print(b)
# print(a)                                                    # a does not change


# ---------------------------------------------------------------------------------------------------------------------
# Element wise operations: https://docs.scipy.org/doc/numpy/reference/routines.math.html
# ---------------------------------------------------------------------------------------------------------------------
# A = np.array([1, 2, 3, 4])
# print(A)

# print(A + 2)                                                # unlike lists
# print(A - 2)
# print(A * 2)
# print(A / 2)
# print(A ** 2)
# print(A ** 5)

# print(np.sin(A))
# print(np.cos(A))
# print(np.tan(A))

# B = np.array([1, 0, 1, 0])
# print(A + B)
# print(A - B)
# print(A * B)


# ---------------------------------------------------------------------------------------------------------------------
# Linear Algebra: https://numpy.org/doc/stable/reference/routines.linalg.html
# ---------------------------------------------------------------------------------------------------------------------
# A = np.ones((2, 3))
# B = np.full((3, 2), 2)
# print(A)
# print(B)
#
# # Matrix multiplication:
# print(np.matmul(A, B))
#
# # Find Determinant:
# C = np.identity(3)
# print(np.linalg.det(C))
#
# np.dot(A, B)                                        # Dot product of two matrices
# np.vdot(A, B)                                       # Dot product of two vectors
# np.inner(A, B)                                      # Inner product of two matrices
# np.outer(A, B)                                      # Outer product of two vectors
# np.linalg.matrix_power(A, n)                        # Raise a square matrix to the (integer) power n
# np.linalg.inv(A)                                    # Inverse of matrix
# np.linalg.pinv(A)                                   # Pseudo-inverse of a matrix


# ---------------------------------------------------------------------------------------------------------------------
# Statistics: https://numpy.org/doc/stable/reference/routines.statistics.html
# ---------------------------------------------------------------------------------------------------------------------
# A = np.array([[4, 1, 5, 9, 1], [6, 2, 4, 0, 1], [3, 0, 9, 9, 1], [9, 0, 2, 5, 3]])
# print(A)

# # Sort:
# print(np.sort(A, axis=1))
# print(np.sort(A, axis=0))

# print(np.min(A))                                    # min of entire matrix
# print(np.min(A, axis=1))                            # min along x axis
# print(np.min(A, axis=0))                            # min along y axis
# print(np.max(A))                                    # max of entire matrix
# print(np.max(A, axis=1))                            # max along x axis
# print(np.max(A, axis=0))                            # max along y axis
# print(np.sqrt(A))

# print(np.count_nonzero(A))                          # count non-zero elements
# print(np.sum(A, axis=0))                            # sum
# print(np.average(A, axis=0))                        # average
# print(np.median(A, axis=0))                         # median
# print(np.mean(A, axis=0))                           # mean
# print(np.std(A, axis=0))                            # std
# print(np.var(A, axis=0))                            # variance

# # Statistics ignoring NaN
# print(np.nanmin(A, axis=0))
# print(np.nanmax(A, axis=0))
# print(np.nanmedian(A, axis=0))
# print(np.nanmean(A, axis=0))
# print(np.nanstd(A, axis=0))
# print(np.nanvar(A, axis=0))


# ---------------------------------------------------------------------------------------------------------------------
# Reorganizing Arrays: reshape, ravel, stack, split
# ---------------------------------------------------------------------------------------------------------------------

# # Reshaping Arrays (does not alter the original array):
# A = np.array([[4, 1, 5, 9, 1], [6, 2, 4, 0, 1], [3, 0, 9, 9, 1], [9, 0, 2, 5, 3]])
# print(A)
# print(A.reshape(1, 20))                                     # 1 row, 20 cols
# print(A.reshape(20, 1))                                     # 20 rows, 1 col
# print(A.reshape(5, 4))                                      # 5x4 matrix
# print(A.reshape(2, 2, 5))
# print(A.ravel())                                            # Flattens an n-dim array to 1-dim

# # Vertically stacking vectors:
# v1 = np.array([1, 2, 3, 4])
# v2 = np.array([5, 6, 7, 8])
# print(v1)
# print(v2)
# print(np.vstack([v1, v2]))
# print(np.vstack([v1, v1, v2, v2, v2]))

# # Horizontal Stack:
# h1 = np.ones((2, 4))
# h2 = np.zeros((2, 2))
# print(h1)
# print(h2)
# print(np.hstack([h1, h2]))

# # Horizontal Split:
# a = np.arange(30).reshape(2, 15)
# b = np.hsplit(a, 3)
# print(a)
# print(b)
# for arr in b:
#     print(arr)

# c = np.vsplit(a, 2)
# print(c)
# for arr in c:
#     print(arr)


# ---------------------------------------------------------------------------------------------------------------------
# Load Data from File:
# ---------------------------------------------------------------------------------------------------------------------
# file_data = np.genfromtxt('NumpyData.txt', delimiter=',')
# print(file_data)
#
# file_data = file_data.astype('int32')
# print(file_data)
#
# # Boolean Masking and Advanced Indexing:
# print(file_data > 50)
# print(file_data[file_data > 50])
# print(np.any(file_data > 50, axis=0))
# print(np.all(file_data > 50, axis=0))
# print((file_data > 50) & (file_data < 100))
# print(~((file_data > 50) & (file_data < 100)))


# ---------------------------------------------------------------------------------------------------------------------
# Indexing with Boolean Array:
# ---------------------------------------------------------------------------------------------------------------------
# a = np.arange(12).reshape(3, 4)
# b = a > 4
# print(a)
# print(b)
# print(a[b])                                 # only those elements of a that are > 4
# a[b] = -1                                   # replace all elements > 4 with -1
# print(a)
