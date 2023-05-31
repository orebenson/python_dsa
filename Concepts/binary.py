'''
Bit Manipulation

Python bit operators:
x << y
- returns x with bits shifted left by y places, adding zeros on end
- same as multiplying x by 2**y

x >> y
- returns x shifted right by y places, adding zeros at start
- same as flooring // x by 2**y

x & y
- bitwise AND
- each bit of output is 1 if corresponding bit of x and y is one else 0

x | y
- bitwise OR
- each bit of output is 0 of corr. in x AND y is 0 else 1

~ x
- complement of x
- switches 1s to 0s and vice versa

x ^ y
- bitwise XOR exvlusive or
- each output bit is same as corr. bit in x if is 0 in y
- complement of x if that bit in y is 1

'''