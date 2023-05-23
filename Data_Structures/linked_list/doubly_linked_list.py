'''
Doubly linked list
'''

from linked_list.singly_linked_list import Node

class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        # self.data = data
        # self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    # def append
    # def delete
    # def insert befpre node
    # def insert after node
    # def print