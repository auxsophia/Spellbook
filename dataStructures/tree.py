'''
Terminology used in trees
Root
The top node in a tree.
Child
A node directly connected to another node when moving away from the root.
Parent
The converse notion of a child.
Siblings
A group of nodes with the same parent.
Descendant
A node reachable by repeated proceeding from parent to child. Also known as subchild.
Ancestor
A node reachable by repeated proceeding from child to parent.
Leaf
External node (not common)
A node with no children.
Branch node
Internal node
A node with at least one child.
Degree
For a given node, its number of children. A leaf is necessarily degree zero.
Edge
The connection between one node and another.
Path
A sequence of nodes and edges connecting a node with a descendant.
Level
The level of a node is defined as: 1 + the number of edges between the node and the root.
Height of node
The height of a node is the number of edges on the longest path between that node and a leaf.
Height of tree
The height of a tree is the height of its root node.
Depth
The depth of a node is the number of edges from the tree's root node to the node.
Forest
A forest is a set of n ≥ 0 disjoint trees.
'''

class Node(object):
    def __init__(self, data, num_children = 2):
        self.data = data
        self.num_children = num_children
        self.children = []
        return self

class Tree(object):
    def __init__(self, data, num_children = 2, notation = "prefix"):
        self.root = Node(data, num_children)
        self.notation = notation

# Common operations:
# Incomplete: insert with queue.
    def insert(data, node = self.root):
        if len(node.children) < node.num_children:
            node.children.append(Node(data, node.num_children))
        else:
            for child in node.children:
                if len(child.children) < child.num_children:
                    Tree.insert(data, node = child)
                    return


# Searching for an item
# Adding a new item at a certain position on the tree
# Deleting an item
# Pruning: Removing a whole section of a tree
# Grafting: Adding a whole section to a tree
# Finding the root for any node
# Finding the lowest common ancestor of two nodes
# Enumerating all the items
# Enumerating a section of a tree
