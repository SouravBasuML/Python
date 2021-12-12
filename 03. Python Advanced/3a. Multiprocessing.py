import time
import multiprocessing


# ---------------------------------------------------------------------------------------------------------------------
# Multiprocessing:
# ---------------------------------------------------------------------------------------------------------------------
# Multiprocessing is a good candidate for CPU bound tasks - tasks that do CPU processing intensive tasks
# Handling multiple processes simultaneously. Multiprocessing and Multithreading are ways to achieve multitasking
# ---------------------------------------------------------------------------------------------------------------------
# def calc_square(a):
#     for n in a:
#         time.sleep(5)
#         print('Square: ', n*n)
#
#
# def calc_cube(a):
#     for n in a:
#         time.sleep(5)
#         print('Cube: ', n*n*n)
#
#
# if __name__ == '__main__':
#     a = [1, 2, 3, 4]
#
#     p1 = multiprocessing.Process(target=calc_square, args=(a,))
#     p2 = multiprocessing.Process(target=calc_cube, args=(a,))
#
#     p1.start()                              # Check in Details tab of Windows Task Manager to see these processes
#     p2.start()
#
#     p1.join()                               # wait until process p1 is done
#     p2.join()


# ---------------------------------------------------------------------------------------------------------------------
# Each process has its own virtual memory or address space. Thus, program variables are not shared between processes
# You need to use Inter Process Communication (IPC) techniques to share data between two processes
# ---------------------------------------------------------------------------------------------------------------------
# square_result = []
#
#
# def calc_square(a):
#     global square_result
#     for n in a:
#         print('Square: ', n*n)
#         square_result.append(n*n)
#     print('Result inside p1 process: ', square_result)                  # [1, 4, 9, 16]
#
#
# if __name__ == '__main__':
#     a = [1, 2, 3, 4]
#     p1 = multiprocessing.Process(target=calc_square, args=(a,))         # p1 and main have their own address spaces
#     p1.start()                                                          # p1 has its own copy of the global variable
#     p1.join()
#     print('Result outside p1 process: ', square_result)                 # []


# ---------------------------------------------------------------------------------------------------------------------
# Sharing data between processes: Shared Memory (Array, Value)
# ---------------------------------------------------------------------------------------------------------------------
# Shared memory resides outside the processes, hence accessible by all processes
# Two methods to access shared memory:
# 1. Using Array
# 2. Using Value
# ---------------------------------------------------------------------------------------------------------------------
# def calc_square(a, result, count):
#     for idx, n in enumerate(a):
#         result[idx] = n*n
#         count.value += 1.0
#     print('Result inside p1 process: ', result[:])                              # [1, 4, 9, 16]
#     print('Value inside p1 process: ', count.value)                             # 4.0
#
#
# if __name__ == '__main__':
#     a = [1, 2, 3, 4]
#
#     # Create shared memory variable using Array (datatype, size)
#     result = multiprocessing.Array('i', 4)                                      # i = int
#
#     # Create shared memory variable using Value (datatype, value)
#     count = multiprocessing.Value('d', 0.0)                                     # d = double
#
#     # Pass the shared memory variable to the process
#     p1 = multiprocessing.Process(target=calc_square, args=(a, result, count))
#
#     p1.start()
#     p1.join()
#
#     print('Result outside p1 process: ', result[:])                             # [1, 4, 9, 16]
#     print('Value outside p1 process: ', count.value)                            # 4.0


# ---------------------------------------------------------------------------------------------------------------------
# Sharing data between processes: Shared Memory (Queue)
# ---------------------------------------------------------------------------------------------------------------------
# def calc_square(a, q):
#     for n in a:
#         q.put(n*n)
#
#
# if __name__ == '__main__':
#     a = [1, 2, 3, 4]
#
#     # Create shared memory variable using Queue and pass it to the process
#     q = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target=calc_square, args=(a, q))
#
#     p1.start()
#     p1.join()
#
#     print('Outside p1 process')
#     while not q.empty():
#         print(q.get())


# ---------------------------------------------------------------------------------------------------------------------
# Locks: Can be used in both multiprocessing and multithreading
# ---------------------------------------------------------------------------------------------------------------------
# def deposit(balance, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         balance.value += 1.0                                                # Lock your critical section
#         lock.release()
#
#
# def withdraw(balance, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         balance.value -= 1.0                                                # Lock your critical section
#         lock.release()
#
#
# if __name__ == '__main__':
#     balance = multiprocessing.Value('d', 200.0)                             # Shared memory variable
#     lock = multiprocessing.Lock()
#     d = multiprocessing.Process(target=deposit, args=(balance, lock))
#     w = multiprocessing.Process(target=withdraw, args=(balance, lock))
#
#     d.start()
#     w.start()
#
#     d.join()
#     w.join()
#
#     print('Final Balance: ',  balance.value)


# ---------------------------------------------------------------------------------------------------------------------
# Pool:
# ---------------------------------------------------------------------------------------------------------------------
# Map: Divide input processing load between multiple CPU cores
# Reduce: Aggregating results back from multiple CPU cores
# ---------------------------------------------------------------------------------------------------------------------

# def calc_square(n):
#     sum = 0
#     for x in range(1_000):
#         sum += x*x
#     return sum
#
#
# if __name__ == '__main__':
#     my_list = [1, 2, 3, 4, 5]
#     pool = multiprocessing.Pool(processes=4)                            # Internally create 4 processes
#
#     t1 = time.time()
#     result = pool.map(calc_square, range(100_000))
#     print('Multiprocessing using Pool took: ', time.time() - t1)
#     pool.close()
#     pool.join()                                                         # will wait for all cores to finish processing
#
#     result1 = []
#     t2 = time.time()
#     for i in range(100_000):
#         result1.append(calc_square(i))
#     print('Serial Processing took: ', time.time() - t2)
