'''
Red-Black tree implementation
-if a node has no child, points to a nil node
-self-balancing binary search tree
-approx. balanced tree height is O(logn)
-worst case O(logn)
-O(n) storage

CLRS version - 5 key properties:
- Every node is red or black
- Root node is black
- Every left (nil) node is black
- If a node is red, both children are black
- Any node path > leaf, same no. of black nodes

'''