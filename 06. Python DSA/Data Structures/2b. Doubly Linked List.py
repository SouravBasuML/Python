# ---------------------------------------------------------------------------------------------------------------------
# Doubly Linked List:
# ---------------------------------------------------------------------------------------------------------------------
# Uses:
# 1. Navigating back and forth between browser visited web pages
# 2. Browsing a photo album
# 3. Browsing a music playlist
# ---------------------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_dll_len(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next
        return length

    def print_dll_forward(self):
        if self.head is None:
            print('Doubly Linked List is Empty')
            return

        itr = self.head
        dll_fwd_str = ''
        while itr:
            dll_fwd_str += str(itr.data) + ' --> '
            itr = itr.next
        print('Doubly Linked List: ', dll_fwd_str)

    def print_dll_backward(self):
        if self.head is None:
            print('Doubly Linked List is Empty')
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        dll_bwd_str = ''
        while itr:
            dll_bwd_str += str(itr.data) + ' --> '
            itr = itr.prev
        print('Doubly Linked List in Reverse: ', dll_bwd_str)

    def insert_at_beginning(self, data):
        node = Node(data=data, next_node=self.head, prev_node=None)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data=data, next_node=None, prev_node=itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data=data)

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_dll_len():
            print('Invalid index to Insert')
            return

        if index == 0:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        for i in range(index-1):
            itr = itr.next
        node = Node(data=data, next_node=itr.next, prev_node=itr)
        node.next.prev = node
        itr.next = node

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_dll_len():
            print('Invalid index to remove')
            return

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        for i in range(index - 1):
            itr = itr.next
        itr.next = itr.next.next
        if itr.next:
            itr.next.prev = itr


if __name__ == '__main__':
    my_dll = DoublyLinkedList()

    # print()
    # my_dll.insert_at_beginning(data=10)
    # my_dll.insert_at_beginning(data=5)
    # my_dll.insert_at_beginning(data=1)
    # my_dll.insert_at_beginning(data=0)
    # my_dll.print_dll_forward()
    # my_dll.print_dll_backward()
    # print('Length of Doubly Linked List: ', my_dll.get_dll_len())

    # print()
    # my_dll.insert_at_end(data=20)
    # my_dll.insert_at_end(data=30)
    # my_dll.insert_at_end(data=40)
    # my_dll.print_dll_forward()
    # my_dll.print_dll_backward()
    # print('Length of Doubly Linked List: ', my_dll.get_dll_len())

    print()
    my_dll.insert_values(data_list=['A', 'B', 'C', 'D', 'E'])
    my_dll.print_dll_forward()
    my_dll.print_dll_backward()
    print('Length of Doubly Linked List: ', my_dll.get_dll_len())

    # print()
    # my_dll.insert_at_index(index=2, data='Z')
    # my_dll.print_dll_forward()
    # my_dll.print_dll_backward()
    # print('Length of Doubly Linked List: ', my_dll.get_dll_len())

    print()
    my_dll.remove_at_index(index=3)
    my_dll.print_dll_forward()
    my_dll.print_dll_backward()
    print('Length of Doubly Linked List: ', my_dll.get_dll_len())
