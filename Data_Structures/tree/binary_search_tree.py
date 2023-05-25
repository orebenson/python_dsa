'''
Binary search tree implementation

form of linked list

not every tree is a binary search tree

complete binary tree:
- each level is full besides possibly the last one 

full binary tree:
- every node has 0 or 2 children

perfect binary tree:
- all nodes have 2 children
- all leaf nodes on same level

balanced trees:
- red black trees and avl trees are types of balanced trees

avg case: search, insert, delete: O(logn)
worst case: O(n)
search, insert, delete: O(h) - bst height

each node has parent and two children
- left subtree nodes are less than node
- right subtree nodes are more than node

'''

class TreeNode():
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

# Inserts new node containing key, only if key not in tree already
# O(h)
def insert(root, key):
    if not root:
        root = TreeNode(key)
        return root
    if key < root.key:
        left = insert(root.left, key)
        root.left = left
        left.parent = root
    else:
        right = insert(root.right, key)
        root.right = right
        right.parent = root
    return root

# Takes in tree, old node to be replaced, and node to replace it
def shift_nodes(bst, old, new):
    if not old.parent:
        bst.root = new
    elif old == old.parent.left:
        old.parent.left = new
    else:
        old.parent.right = new
    if new:
        new.parent = old.parent

# Deleted node from tree, will update tree
# O(h)
def delete(root, node):
    if not node.right:
        shift_nodes(root, node, node.right)
    elif not node.left:
        shift_nodes(root, node, node.left)
    else: # node has two children
        node_successor = min(node.right)
        if node_successor != node.right: # Re-Assign right child
            shift_nodes(root, node_successor, node_successor.right)
            node_successor.right = node.right
            node_successor.right.parent = node_successor
        shift_nodes(root, node, node_successor)
        node_successor.left = node.left
        node_successor.left.parent = node_successor

'''
Tree traversals - depth first search
complexity of O(n) as algo is called twice on each node
Inorder: processes each node inbetween left and right subtree 
Preorder: process each node before left and right subtrees
Postorder: process each node after left and right subtrees
'''

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

# Preorder traversal
def preorder(root):
    if root:
        print(root.key)
        preorder(root.left)
        preorder(root.right)

# Preorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key)

'''
Search tree queries
complexity O(h) h = height
min/max, search, predecessor
'''

def min(root):
    while root.left:
        root = root.left
    return root

def max(root):
    while root.right:
        root = root.right
    return root

def search(root, key):
    while root and key != root.key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
    return root

# Find element before node in inorder ordering
# O(h) complexity
def predecessor(node):
    if node.left:
        return max(node.left)
    else:
        # Move up tree until parent is to the left and not right and return
        par = node.parent
        while par and node != par.right:
            node = par
            par = par.parent
        return par
    
# Find element after node in postorder ordering
# O(h) complexity
def successor(node):
    if node.right:
        return min(node.right)
    else:
        # Move up tree until parent is to the right
        par = node.parent
        while par and node != par.left:
            node = par
            par = par.parent
        return par

# Invert tree
def invertTree(root):
    if root is not None:
        invertTree(root.right)
        invertTree(root.left)
        root.left, root.right = root.right, root.left
    return root

if __name__ == '__main__':
    root = None
    root = insert(root, 5)
    insert(root, 3)
    insert(root, 2)
    insert(root, 4)
    insert(root, 7)
    insert(root, 6)
    insert(root, 8)

    inorder(root)
    print("--------")
    delete(root, root)
    inorder(root)