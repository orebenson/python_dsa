'''
Graphs are either directed or undirected
A connected graph menas there is a path between every pair of vertices
Graphs have subgraphs
Graphs can contain cycles or be acyclic (no cycles)

Represented in two ways:

Adjacency List:
- each node contains a list of children that it can access
- can be stored as nodes or in a hash table of lists of nodes


Adjacency Matrix:
- less space efficient
- matrix/table of N x N where a value at matrix[i][j] indicates an edge

#   0 1 2 3
   ________ 
0 | 1 1 0 1
1 | 0 0 0 1
2 | 0 1 1 0
3 | 0 1 0 1


'''

class GraphNode:
    def __init__(self) -> None:
        self.visited = False
        self.value = None
        self.children = [] # GraphNodes

class Graph:
    def __init__(self) -> None:
        self.nodes = [] # GraphNodes