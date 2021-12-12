# ---------------------------------------------------------------------------------------------------------------------
# Binary Tree:
# ---------------------------------------------------------------------------------------------------------------------
# Each node must have at most two children
# Max number of nodes at level i is 2^i
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Binary Search Tree:
# ---------------------------------------------------------------------------------------------------------------------
# Special case of Binary Tree.
# Elements on the left of a node have values smaller than the node and those on right have values larger than the node
# Does not have duplicates
# Max number of nodes at level i is 2^i
# Uses:
#   1. Sort a list
#   2. Sets can be implemented using BST
# Big O Time Complexity:
#   1. Search: O(log(n))
#   2. Insertion: O(log(n))
# ---------------------------------------------------------------------------------------------------------------------
# BST Search:
# 1. Breadth-First Search
# 2. Depth-First Search
#    2a. In-order Traversal: Left Subtree -> Node -> Right Subtree          # Sorted in ascending order
#    2b. Pre-order Traversal: Node -> Left Subtree -> Right Subtree
#    2c. Post-order Traversal: Left Subtree -> Right Subtree -> Node
# ---------------------------------------------------------------------------------------------------------------------
# [15, 12, 7, 14, 27, 20, 23, 88]
#
#               15
#       12              27
#   7       14      20      88
#                       23
#
# BST In-order Traversal:   [7, 12, 14, 15, 20, 23, 27, 88]                 # Sorted in ascending order
# BST Pre-order Traversal:  [15, 12, 7, 14, 27, 20, 23, 88]
# BST Post-order Traversal: [7, 14, 12, 23, 20, 88, 27, 15]
# ---------------------------------------------------------------------------------------------------------------------

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return                                                      # Node already exists; no duplicates in BST

        if data < self.data:                                            # Add node in left subtree
            if self.left:                                               # If left subtree is present
                self.left.add_child(data=data)
            else:                                                       # If left subtree is empty
                self.left = BinarySearchTreeNode(data=data)

        if data > self.data:                                            # Add node in right subtree
            if self.right:                                              # If right subtree is present
                self.right.add_child(data=data)
            else:                                                       # If right subtree is empty
                self.right = BinarySearchTreeNode(data=data)

    def in_order_traversal(self):                                       # Left Subtree -> Node -> Right Subtree
        bst_elements = []

        if self.left:
            bst_elements += self.left.in_order_traversal()

        bst_elements.append(self.data)

        if self.right:
            bst_elements += self.right.in_order_traversal()

        return bst_elements

    def pre_order_traversal(self):                                      # Node -> Left Subtree -> Right Subtree
        bst_elements = [self.data]

        if self.left:
            bst_elements += self.left.pre_order_traversal()

        if self.right:
            bst_elements += self.right.pre_order_traversal()

        return bst_elements

    def post_order_traversal(self):                                     # Left Subtree -> Right Subtree -> Node
        bst_elements = []

        if self.left:
            bst_elements += self.left.post_order_traversal()

        if self.right:
            bst_elements += self.right.post_order_traversal()

        bst_elements.append(self.data)

        return bst_elements

    def bst_search(self, value):
        if value == self.data:
            return True

        if value < self.data:
            if self.left:                                                   # If left subtree exists
                return self.left.bst_search(value=value)                               # Search left subtree
            else:                                                           # If left subtree does not exist
                return False                                                    # Return 'not found'

        if value > self.data:
            if self.right:                                                  # If right subtree exists
                return self.right.bst_search(value=value)                              # Search right subtree
            else:                                                           # If right subtree does not exist
                return False                                                    # Return 'not found'

    def find_min(self):                                                     # Get leftmost leaf node
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):                                                     # Get rightmost leaf node
        if self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete_bst_node(self, value):
        # Case 1. Delete node with no child - Just delete
        # Case 2. Delete node with one child - Bring the child node (with its children) in deleted node's place
        # Case 3. Delete node with two children
        # Case 3a. Check right subtree, find min, copy min in deleted node's place, remove dup from right subtree
        # Case 3b. Check left subtree, find max, copy max in deleted node's place, remove dup from left subtree
        if value < self.data:
            if self.left:
                self.left = self.left.delete_bst_node(value=value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_bst_node(value=value)
        else:                                                       # Node to be deleted
            if self.left is None and self.right is None:            # Case 1: No more children
                return None
            if self.left is None:                                   # Case 2: Only right child
                return self.right                                   # Return right child, so current node is deleted
            if self.right is None:                                  # Case 2: Only left child
                return self.left                                    # Return left child, so current node is deleted

            # At this point, the node to be deleted has left and right subtree. Applying case 3a:
            min_val = self.right.find_min()                         # find min from right subtree
            self.data = min_val                                     # copy min value in deleted node's place
            # remove dup from right subtree and assign the new right subtree to current node's right
            self.right = self.right.delete_bst_node(value=min_val)

            # # At this point, the node to be deleted has left and right subtree. Applying case 3b:
            # max_val = self.left.find_max()                          # find max from left subtree
            # self.data = max_val                                     # copy max value in deleted node's place
            # self.left = self.left.delete(max_val)                   # remove dup from left subtree

        return self


def build_bst(elements):
    print('\nBuilding Binary Search Tree with elements: ', elements)
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    # numbers = [15, 12, 7, 14, 27, 20, 23, 88]
    numbers_bst = build_bst(numbers)

    print('BST In-order Traversal: ', numbers_bst.in_order_traversal())                 # [1, 4, 9, 17, 18, 20, 23, 34]
    print('BST Pre-order Traversal: ', numbers_bst.pre_order_traversal())               # [17, 4, 1, 9, 20, 18, 23, 34]
    print('BST Post-order Traversal: ', numbers_bst.post_order_traversal())             # [1, 9, 4, 18, 34, 23, 20, 17]

    print('4 is in list? ', numbers_bst.bst_search(value=4))

    print('Minimum number in BST: ', numbers_bst.find_min())
    print('Maximum number in BST: ', numbers_bst.find_max())
    print('Sum of numbers in BST: ', numbers_bst.calculate_sum())

    numbers_bst.delete_bst_node(20)
    print('BST In-order Traversal post deletion: ', numbers_bst.in_order_traversal())   # [1, 4, 9, 17, 18, 23, 34]

    countries = ['India', 'Japan', 'Germany', 'USA', 'China', 'India', 'UK', 'USA']
    country_bst = build_bst(countries)
    print('BST In-order Traversal: ', country_bst.in_order_traversal())
    print('UK is in the list? ', country_bst.bst_search('UK'))
    print('Sweden is in the list? ', country_bst.bst_search('Sweden'))
