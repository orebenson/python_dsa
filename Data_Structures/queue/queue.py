'''
Queue data structure

first in first out
'''

from linked_list.singly_linked_list import Node

class Queue:   
    def __init__(self) -> None:
        self.first = None
        self.last = None 
    
    def add(self, item):
        if self.last == None:
            self.last = Node(item)
        else:
            self.last.next = Node(item)
        if self.first == None: self.first = self.last

    def remove(self):
        if self.first != None:
            res = self.first.data
            self.first = self.first.next
            return res
        else:
            return None
        
    def peek(self):
        if self.first != None:
            return self.first.data
        else:
            return None
        
    def isEmpty(self):
        return self.first == None