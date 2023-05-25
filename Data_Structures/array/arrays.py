'''
When arrays resize for increased input, the size may multiply by 2 each time
this sizing factor depends on the language 
- pythons is 112%
- java arraylist multiplies by 2

insertion n elements is O(n)
O(1) on average
'''

class ArrayList:
    def __init__(self) -> None:
        self.array = []

    # def append
    # def delete
    # def get