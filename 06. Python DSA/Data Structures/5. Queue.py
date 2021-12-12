from collections import deque

# ---------------------------------------------------------------------------------------------------------------------
# Queue: FIFO data structure
# ---------------------------------------------------------------------------------------------------------------------
# Uses:
# 1. Pub-Sub messaging models
# ---------------------------------------------------------------------------------------------------------------------
# Push/Pop element -> O(1)
# Search element by value -> O(n)
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# Queue implementation using List:
# Disadvantages: Same as of dynamic arrays
# ---------------------------------------------------------------------------------------------------------------------
stock_price = []
stock_price.insert(0, 10.2)                     # Insert at 0th position to simulate queue
stock_price.insert(0, 13.5)
stock_price.insert(0, 11.9)
print(stock_price)

print(stock_price.pop())                        # FIFO
print(stock_price)


# ---------------------------------------------------------------------------------------------------------------------
# Queue implementation using collections.deque:
# Deques are a generalization of stacks and queues. It is pronounced “deck” and is short for “double-ended queue”
# Supports appends & pops from either side of the deque with approx the same O(1) performance in either direction.
# ---------------------------------------------------------------------------------------------------------------------
# from collections import deque
# ---------------------------------------------------------------------------------------------------------------------

q = deque()
q.appendleft(10.2)              # Always use appendleft() to implement queue
q.appendleft(13.5)
q.appendleft(11.9)

print(q)                        # deque([11.9, 13.5, 10.2])
print(len(q))                   # 3

print(q.pop())                  # 10.2
print(q)                        # deque([11.9, 13.5])
