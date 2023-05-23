'''
Hash tables:
contain indexes, each with a list of keys and values

to add each key, compute its hash and map it to an index
store the key, value pair in the index
keys can have the same hash code, hash codes can have the same index

to find a value from key, hash key, find index, find value with key

can also use a balanced binary search tree

Worst case lookup time is O(n) with high collisions
minimum collisions O(1)
'''

from linked_list.singly_linked_list import Node, LinkedList
# Implementation of a dictionary with an array of linked lists
class HashTable:
    def __init__(self) -> None:
        self.table = []