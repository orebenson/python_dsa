'''
Binary heaps

min/max heaps

min/max tree is a complete binary tree
each node is smaller/larger than its children
smallest/largest node is at the root

Insert into a heap: O(log n)
- insert new node at end (bottom rightmost leaf)
- swap new node with parent until the right spot is found

Extract minimum/maximum from heap: O(log n)
- swap root with bottom rightmost leaf
- swap root down with min/max node till heap is satisfied

'''

from tree.binary_search_tree import TreeNode


class MinHeap:
    def __init__(self) -> None:
        
    # def getMin()
    # def extractMin()
    # def insert(item)

