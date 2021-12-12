# ---------------------------------------------------------------------------------------------------------------------
# Linked List:
# ---------------------------------------------------------------------------------------------------------------------
# Stores values at random memory location, linked by pointers. Unlike arrays, does not pre-allocate memory
# ---------------------------------------------------------------------------------------------------------------------
# Uses:
# 1. Using the back button on browser
# 2. Breaking down a large file in to smaller files for transmitting and assembling them in order at the destination
# ---------------------------------------------------------------------------------------------------------------------
# Insert/Delete element at the beginning: O(1)
# Insert/Delete element at the end: O(n) - as you will have to traverse the linked-list
# Linked list traversal: O(n)
# Accessing element by value: O(n)
# ---------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None                                # head variable points to the head of the LL

    def get_ll_len(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next
        return length

    def print_ll(self):
        if self.head is None:                           # Blank LL
            print('Linked List is empty')
            return

        itr = self.head
        llstr = ''
        while itr:                                      # while itr is not None:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def insert_at_beginning(self, data):
        node = Node(data=data, next_node=self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data, next_node=None)
            return

        itr = self.head
        while itr.next:                                 # # while itr.next is not None:
            itr = itr.next
        itr.next = Node(data=data, next_node=None)

    def insert_values(self, data_list):
        self.head = None
        for item in data_list:
            self.insert_at_end(data=item)

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_ll_len():
            print('Invalid index to Insert')
            return

        if index == 0:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        for i in range(index-1):
            itr = itr.next
        node = Node(data=data, next_node=itr.next)
        itr.next = node

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_ll_len():
            print('Invalid index to remove')
            return

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        for i in range(index-1):
            itr = itr.next
        itr.next = itr.next.next

    def insert_after_by_value(self, data_after, data_to_insert):
        if self.head is None:
            print('Empty Linked List.')
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data=data_to_insert, next_node=itr.next)
                break
            itr = itr.next
        else:
            print('Node with data "' + str(data_after) + '" not found. New node not inserted.')

    def remove_by_value(self, data_to_remove):
        if self.head is None:
            print('Empty Linked List.')
            return

        if self.head.data == data_to_remove:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data_to_remove:
                itr.next = itr.next.next
                break
            itr = itr.next
        else:
            print('Node with data "' + str(data_to_remove) + '" not found. New node not deleted.')

    def reverse_ll(self):
        if self.head is None:
            print('Empty Linked List.')
            return

        itr = self.head
        temp_list = []
        while itr:
            temp_list.append(itr.data)
            itr = itr.next
        for i in range(len(temp_list)):
            self.insert_values(data_list=temp_list[::-1])


if __name__ == '__main__':
    my_linked_list = LinkedList()

    # my_linked_list.insert_at_beginning(data=10)
    # my_linked_list.print_ll()

    # my_linked_list.insert_at_end(data=20)
    # my_linked_list.print_ll()

    # # Create a new Linked List with data in the given list:
    my_linked_list.insert_values(data_list=[1, 2, 3, 4, 5, 10, 20, 30, 40, 50])
    my_linked_list.print_ll()
    print('Length of my Linked List: ', my_linked_list.get_ll_len())

    # # Remove node at a given index:
    # my_linked_list.remove_at_index(index=8)
    # my_linked_list.print_ll()
    # print('Length of my Linked List: ', my_linked_list.get_ll_len())

    # # Insert a node at a given index:
    # my_linked_list.insert_at_index(index=5, data=99)
    # my_linked_list.print_ll()
    # print('Length of my Linked List: ', my_linked_list.get_ll_len())

    # # Insert a node with value 99 after the first occurrence of the node with value 30
    # my_linked_list.insert_after_by_value(data_after=30, data_to_insert=99)
    # my_linked_list.print_ll()
    # print('Length of my Linked List: ', my_linked_list.get_ll_len())

    # # Remove the first occurrence of the node with value "20"
    # my_linked_list.remove_by_value(data_to_remove=99)
    # my_linked_list.print_ll()
    # print('Length of my Linked List: ', my_linked_list.get_ll_len())

    # # Reverse a Linked List
    my_linked_list.reverse_ll()
    my_linked_list.print_ll()
    print('Length of my Linked List: ', my_linked_list.get_ll_len())
