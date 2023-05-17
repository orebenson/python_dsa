'''
Singly linked list implementation

search: O(n)
insert at element: O(1)
delete element: O(1)
insert at end: O(n) 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        llist = []
        cur_node = self.head
        while cur_node:
            llist.append(cur_node.data)
            cur_node = cur_node.next
        print(llist)
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node not in the list")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p



llist1 = LinkedList()
llist2 = LinkedList()
for i in range(10):
    if i%2 == 0: llist1.append(i)
    else: llist2.append(i)

llist1.merge_sorted(llist2)

print(llist1.print_list())


# print(llist1.print_list())
# print(llist2.print_list())

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# # llist.append("C")
# llist.append("D")

# llist.insert_after_node(llist.head.next, "C")
# llist.print_list()