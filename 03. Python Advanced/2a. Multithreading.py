import time
import threading

# ---------------------------------------------------------------------------------------------------------------------
# Multithreading:
# ---------------------------------------------------------------------------------------------------------------------
# Runs tasks concurrently (asynchronously)
# Multithreading is a good candidate for I/O bound tasks i.e., I/O intensive tasks like waiting for user input,
# network operations, downloading/uploading, reading/writing to disks, file system etc.

# ---------------------------------------------------------------------------------------------------------------------
# Processes:
# ---------------------------------------------------------------------------------------------------------------------
# Processes are individual programs, each having its own virtual memory or address space.
# e.g. Chrome, Word, Calc, Explorer etc. are processes/programs running on a computer.
# Each process runs in its own address space and to communicate with each other processes, they may use
# files, shared memory, or message pipes.
# Global variables declared within a process will not be available to other processes.

# ---------------------------------------------------------------------------------------------------------------------
# Thread:
# ---------------------------------------------------------------------------------------------------------------------
# Each process may have multiple threads which will share the same address space of the process.
# Multiple threads allow the process to better utilize CPU idle time. When one thread is waiting (e.g. for I/O or
# message over a network) and the CPU is idle, the OS will schedule another thread.
# Each thread will do a specific task and will have its own instruction set, stack memory, instruction pointer etc.
# But they will share the same address space of the process and share the same heap memory. That means, threads can
# access global variables defined within the process. Threads are light-weight; processes are heavy-weight

# ---------------------------------------------------------------------------------------------------------------------
# Multitasking:
# ---------------------------------------------------------------------------------------------------------------------
# Multiple tasks/processes running in parallel, e.g. Multiple processes managed by an OS.
# Multiprocessing and Multithreading are ways to achieve multitasking
# ---------------------------------------------------------------------------------------------------------------------

def calc_square(a):
    for n in a:
        time.sleep(0.2)
        print('Square: ', n*n)


def calc_cube(a):
    for n in a:
        time.sleep(0.2)
        print('Cube: ', n*n*n)


if __name__ == '__main__':
    a = [1, 2, 3, 4]

    t = time.time()
    calc_square(a)
    calc_cube(a)
    print(f'Serial functions took: {round(time.time() - t, 2)} seconds')

    t = time.time()
    t1 = threading.Thread(target=calc_square, args=(a,))      # function will execute only when the thread starts
    t2 = threading.Thread(target=calc_cube, args=(a,))

    t1.start()
    t2.start()

    t1.join()                                                 # wait until thread t1 is done
    t2.join()

    print(f'Multithreading took: {round(time.time() - t, 2)} seconds')


# ---------------------------------------------------------------------------------------------------------------------
# Each thread shares the address space. Thus, program variables are shared between threads
# ---------------------------------------------------------------------------------------------------------------------
result = []


def calc_square(a):
    global result
    for n in a:
        time.sleep(0.2)
        print('Square: ', n*n)
        result.append(n*n)
    print('Result inside t1 thread: ', result)                          # [1, 1, 4, 8, 9, 27, 16, 64]


def calc_cube(a):
    global result
    for n in a:
        time.sleep(0.2)
        print('Cube: ', n*n*n)
        result.append(n*n*n)
    print('Result inside t2 thread: ', result)                          # [1, 1, 4, 8, 9, 27, 16, 64]


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    t1 = threading.Thread(target=calc_square, args=(a,))                # t1 and t2 share the same address space
    t2 = threading.Thread(target=calc_cube, args=(a,))
    t1.start()                                                          # t1 shares the global variable
    t2.start()                                                          # t2 shares the global variable
    t1.join()
    t2.join()
    print('Result outside threads: ', result)                           # [1, 1, 4, 8, 9, 27, 16, 64]
