
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


'''
Level order traversal, known as Bread-First Traversal
Explore each level before moving to the next one
General algorithm:
    1. Compute height of the tree
    2. For each level until height, print that level
Algorithm is recursive 
'''
# Two functions - one to print all nodes at a given level, the other is to level order traversal

# Computes height of a tree - the number of nodes along the longest path from root to node at largest depth
def height(node: Node):
    if not node:
        return 0
    else:   #compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)

# print nodes at a given level
def printGivenLevel(root, level):
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

'''
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print('Level order traversal of binary tree is -")
printLevelOrder(root)

'''