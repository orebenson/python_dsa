'''
Stack Data Structure

push/pop from the top of the stack
view the top element in the stack
'''

class Stack():
    def __init__(self) -> None:
        self.items = []

    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    

# s = Stack()
# s.push("A")
# s.push("D")
# print(s.get_stack())
# print(s.peek())
# s.pop()
# s.pop()
# print(s.is_empty())