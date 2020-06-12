
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Inorder traversal:
# Left, Root, Right
def printInorder(root):
    if root:
        printInorder(root.left)     # visit left, recur

        print(root.data)            # print node's value

        printInorder(root.right)    # visit right, recur

# Preorder traversal:
# Root, Left, Right
def printPreorder(root):
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)

# Postorder traversal:
# Left, Right, Root
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

'''
Test tree below
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Preorder traversal of binary tree')
printPreorder(root)

print('Inorder traversal of a binary tree')
printInorder(root)

print('Postorder traversa of a binary tree')
printPostorder(root)