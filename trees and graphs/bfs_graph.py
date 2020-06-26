# Breadth First Search for a graph

import collections

class Node(object):
    def __init__(self, name):
        self.children = []
        self.name = []
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    # takes an empty array, traverses the tree using BFS, and stores in the array
    def breadthFirstSearch(self, array):
        nodes = collections.deque()     # this queue will hold children at each level
        nodes.append(self)

        while nodes:
            current_node = nodes.popleft()  
            array.append(current_node.name)

            for child in current_node.children:
                nodes.append(child)

        return array

# Time is O(V+E) | space is O(V) 