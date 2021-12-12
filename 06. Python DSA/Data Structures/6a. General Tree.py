# ---------------------------------------------------------------------------------------------------------------------
# Tree: Hierarchical data structure
# General Tree: Can have any number of child nodes
# ---------------------------------------------------------------------------------------------------------------------
# Uses:
# 1. Folder structure in file system
# 2. Implement Organizational Hierarchy
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Product Tree:
# ---------------------------------------------------------------------------------------------------------------------
# --> Electronics
#     --> Laptop
#         --> Dell
#         --> Lenovo
#         --> MacBook
#     --> Cell Phone
#         --> Samsung
#         --> OnePlus
#         --> Huawei
#     --> TV
#         --> Sony
#         --> LG
#         --> Panasonic
# ---------------------------------------------------------------------------------------------------------------------

# class TreeNode:
#     def __init__(self, data):
#         self.parent = None
#         self.data = data
#         self.children = []
#
#     def add_child(self, child):                         # self here is the node to which a child needs to be added
#         child.parent = self                             # self becomes the parent of the new child node
#         self.children.append(child)                     # child node gets appended to the existing list of children
#
#     def get_level(self):
#         level = 0
#         node = self
#         while node.parent:
#             level += 1
#             node = node.parent
#
#         return level
#
#     def print_tree(self):
#         print('    ' * self.get_level() + '--> ' + self.data)
#
#         for each_child in self.children:
#             each_child.print_tree()
#
#
# def build_product_tree():
#     root = TreeNode('Electronics')
#
#     laptop = TreeNode(data='Laptop')
#     cellphone = TreeNode(data='Cell Phone')
#     tv = TreeNode(data='TV')
#
#     root.add_child(child=laptop)
#     root.add_child(child=cellphone)
#     root.add_child(child=tv)
#
#     laptop.add_child(child=TreeNode(data='Dell'))
#     laptop.add_child(child=TreeNode(data='Lenovo'))
#     laptop.add_child(child=TreeNode(data='MacBook'))
#
#     cellphone.add_child(child=TreeNode(data='Samsung'))
#     cellphone.add_child(child=TreeNode(data='OnePlus'))
#     cellphone.add_child(child=TreeNode(data='Huawei'))
#
#     tv.add_child(child=TreeNode(data='Sony'))
#     tv.add_child(child=TreeNode(data='LG'))
#     tv.add_child(child=TreeNode(data='Panasonic'))
#
#     return root
#
#
# if __name__ == '__main__':
#     tree = build_product_tree()
#     print('Product Tree:')
#     tree.print_tree()


# ---------------------------------------------------------------------------------------------------------------------
# Organizational Hierarchy Tree:
# ---------------------------------------------------------------------------------------------------------------------
# --> Adam (CEO)                                        --> l0
#     --> Bob (COO)                                         --> l11
#         --> Chet (Operations Head)                            --> l111
#         --> Charles (Operations Manager)                      --> l112
#     --> Bill (CTO)                                        --> l12
#         --> Dick (Infrastructure Head)                        --> l121
#             --> Eric (Cloud Manager)                              --> l1211
#             --> Eaton (Network Manager)                           --> l1212
#             --> Enio (Security Manager)                           --> l1213
#         --> Dun (Application Head)                            --> l122
#     --> Bud (HR)                                          --> l13
#         --> Rick (Recruitment Manager)                        --> l131
#         --> Rod (Policy Manager)                              --> l132
# ---------------------------------------------------------------------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child):                         # self here is the node to which a child needs to be added
        child.parent = self                             # self becomes the parent of the new child node
        self.children.append(child)                     # child node gets appended to the existing list of children

    def get_level(self):
        level = 0
        node = self
        while node.parent:
            level += 1
            node = node.parent

        return level

    def print_tree(self, hierarchy_type):
        indentation = '    ' * self.get_level() + '--> '

        for key, value in self.data.items():
            if hierarchy_type == 'name':
                print(indentation + value)
            elif hierarchy_type == 'designation':
                print(indentation + key)
            elif hierarchy_type == 'both':
                print(indentation + value + ' (' + key + ')')

        for each_child in self.children:
            each_child.print_tree(hierarchy_type=hierarchy_type)

    def print_tree_levels(self, level):
        if self.get_level() > level:
            return

        indentation = '    ' * self.get_level() + '--> '
        for key, value in self.data.items():
            print(indentation + value + ' (' + key + ')')

        for each_child in self.children:
            each_child.print_tree_levels(level=level)


def build_management_tree():
    root = TreeNode({'CEO': 'Adam'})

    l11 = TreeNode(data={'COO': 'Bob'})
    l12 = TreeNode(data={'CTO': 'Bill'})
    l13 = TreeNode(data={'HR': 'Bud'})

    l111 = TreeNode(data={'Operations Head': 'Chet'})
    l112 = TreeNode(data={'Operations Manager': 'Charles'})

    l121 = TreeNode(data={'Infrastructure Head': 'Dick'})
    l122 = TreeNode(data={'Application Head': 'Dun'})

    l1211 = TreeNode(data={'Cloud Manager': 'Eric'})
    l1212 = TreeNode(data={'Network Manager': 'Eaton'})
    l1213 = TreeNode(data={'Security Manager': 'Enio'})

    l131 = TreeNode(data={'Recruitment Manager': 'Rick'})
    l132 = TreeNode(data={'Policy Manager': 'Rod'})

    root.add_child(l11)
    root.add_child(l12)
    root.add_child(l13)

    l11.add_child(l111)
    l11.add_child(l112)

    l12.add_child(l121)
    l12.add_child(l122)

    l13.add_child(l131)
    l13.add_child(l132)

    l121.add_child(l1211)
    l121.add_child(l1212)
    l121.add_child(l1213)

    return root


if __name__ == '__main__':
    root_node = build_management_tree()

    print('\nOrganizational Hierarchy: Names:')
    root_node.print_tree(hierarchy_type='name')
    print('\nOrganizational Hierarchy: Designation:')
    root_node.print_tree(hierarchy_type='designation')
    print('\nOrganizational Hierarchy: Name + Designation:')
    root_node.print_tree(hierarchy_type='both')

    print('\nOrganizational Hierarchy: Level 0:')
    root_node.print_tree_levels(level=0)
    print('\nOrganizational Hierarchy: Level 1:')
    root_node.print_tree_levels(level=1)
    print('\nOrganizational Hierarchy: Level 2:')
    root_node.print_tree_levels(level=2)
    print('\nOrganizational Hierarchy: Level 3:')
    root_node.print_tree_levels(level=3)
