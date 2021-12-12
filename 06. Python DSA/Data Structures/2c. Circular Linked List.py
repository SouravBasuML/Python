# ---------------------------------------------------------------------------------------------------------------------
# Circular Linked List:
# ---------------------------------------------------------------------------------------------------------------------
# Uses:
# 1. Time Sharing by OS
# 2. Round Robin processes
# ---------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class CircularLinkedList:
    def __init__(self):
        self.head = None                                # head variable points to the head of the LL

    def print_cll(self, loop_count):
        if self.head is None:                           # Blank LL
            print('Linked List is empty')
            return

        itr = self.head
        count = 0
        cll_str = ''
        while count < loop_count:
            cll_str += str(itr.data) + ' --> '
            itr = itr.next
            if itr is self.head:
                count += 1
        print(cll_str)

    def insert_values(self, data_list):
        if self.head is None:
            self.head = Node(data=data_list[0], next_node=None)

        itr = self.head
        for item in data_list[1: len(data_list)]:
            itr.next = Node(data=item, next_node=None)
            itr = itr.next
        itr.next = self.head


if __name__ == '__main__':
    my_cll = CircularLinkedList()

    # Create a new Circular Linked List with data in the given list:
    my_cll.insert_values(data_list=[1, 2, 3, 4, 5])
    my_cll.print_cll(loop_count=5)
