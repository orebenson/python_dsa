'''
Two algorithms for searching graphs
DFS(depth first) and BFS(breadth first)

DFS:
- recursive
- fully explore a branch before moving to next node
- better if we want to visit every node
- preorder and some other tree traversals are DFS

BFS:
- iterative using a queue
- explore all neighbors before moving to next node
- better for finding shortest path

Bidirectional Search:
- Finding shortest path between two nodes
- Performs BFS from each node, finding collisions
- Combines the path

'''

from Data_Structures.graph.graphs import GraphNode, Graph
from Data_Structures.queue.queue import Queue

def createGraph():
    # create a graph
    return None

def DFS(node): # recursive
    if node == None: return
    # visit(node) # perform whatever visit process
    node.visited = True
    for n in node.children:
        if n.visited == False:
            DFS(n)
    return None

def BFS(node):
    queue = Queue()
    node.visited = True
    queue.add(node)

    while not queue.isEmpty():
        r = queue.remove()
        # visit(node) # perform whatever visit process
        for n in r.nodes:
            if n.visited == False:
                n.visited = True
                queue.add(n)
    return None

