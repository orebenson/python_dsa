'''
Use stack to convert integer to binary

using divide by two method
'''
from stack import Stack

def int_to_bin(number):
    s = Stack()
    while number > 0:
        s.push(number % 2)
        number //= 2
    return s.get_stack()
            
# print(int_to_bin(13))
# print(int_to_bin(9))

