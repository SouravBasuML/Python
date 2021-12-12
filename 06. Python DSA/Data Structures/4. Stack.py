from collections import deque

# ---------------------------------------------------------------------------------------------------------------------
# Stack: LIFO data structure
# ---------------------------------------------------------------------------------------------------------------------
# Uses:
# 1. Function calling in a programming language is managed by stack
# 2. Undo (ctrl + z) functionality in any editor
# ---------------------------------------------------------------------------------------------------------------------
# Push/Pop element -> O(1)
# Search element by value -> O(n)
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Stack implementation using List:
# Disadvantages: Same as of dynamic arrays
# ---------------------------------------------------------------------------------------------------------------------
# stk = []
# stk.append('https://www.cnn.com/')
# stk.append('https://www.cnn.com/world')
# stk.append('https://www.cnn.com/india')
# stk.append('https://www.cnn.com/china')
#
# print(stk)
# print(stk.pop())                                # returns and removes the last element
# print(stk)


# ---------------------------------------------------------------------------------------------------------------------
# Stack implementation using collections.deque:
# Deques are a generalization of stacks and queues. It is pronounced “deck” and is short for “double-ended queue”
# Supports appends & pops from either side of the deque with approx the same O(1) performance in either direction.
# ---------------------------------------------------------------------------------------------------------------------
# from collections import deque
# ---------------------------------------------------------------------------------------------------------------------

stack = deque()
print(stack)                                    # deque([])
print(type(stack))                              # <class 'collections.deque'>
print(dir(stack))

stack.append('https://www.cnn.com/')            # appendleft() -> appends to the left. Used in Queue implementation
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')
print(stack)
print(len(stack))

print()
print(stack.pop())                              # stack.popleft() -> pops from the left
print(stack)

stack.reverse()
print(stack)
